"""Gamification Client to send payload data."""
import json
import socket
import logging
import importlib

from django.conf import settings

from gamification_event_tracker.storage import GammaStorage
from gamification_event_tracker import exceptions


if (
    hasattr(settings, 'RG_GAMIFICATION') and
    settings.RG_GAMIFICATION.get('ENABLED') == True and
    settings.RG_GAMIFICATION.get('RG_GAMIFICATION_ENDPOINT')):

    G_CONFIG = settings.RG_GAMIFICATION

    params = {
        'enabled': True,
        'endpoint': G_CONFIG.get('RG_GAMIFICATION_ENDPOINT'),
        'secret': G_CONFIG.get('KEY'),
        'key': G_CONFIG.get('SECRET')
    }


logger = logging.getLogger(__name__)
g_storage = GammaStorage(**params)


class GamificationPublisher(object):
    """
    Publishing wrapper around tincan.remote_lrs.RemoteLRS.
    Raise custom error types when LRS publishing activity not successful.
    """
    def publish_event(self, event):
        """
        params:
        event gamification event
        """
        try:
            g_resp = g_storage.save(event)
        except (socket.gaierror, ) as e:  # can't connect at all, no response
            raise exceptions.GammaConnectionError(queue=event)

        try:
            json_response = g_resp.json()
        except TypeError as e:
            logger.info("Error while publishing event statement {}".format(g_resp))
        else:
            if g_resp.status_code == 200:
                logger.info("Succeeded sending statement {}".format(json_response))
            elif g_storage.response_has_errors(json_response):
                    logger.info("Error while publishing event statement {}: {}".format(event, json_response))


publisher = GamificationPublisher()

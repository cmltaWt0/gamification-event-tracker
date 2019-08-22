import logging

from track.backends import BaseBackend

from gamification_event_tracker import client, converter


LOGGER = logging.getLogger(__name__)
TRACKING_LOGGER = logging.getLogger('tracking')


class GamificationProcessor(BaseBackend):
    """
    Is responsible for capturing, transforming and sending all the event tracking logs
    generated by Open edX platform.

    This transformer is used in the commong.djangoapps.track django app as a replacement
    for the default tracking backend.

    It is also used as an addition to the event tracking pipeline in the event_tracking app
    by Open edX
    """

    def __call__(self, event):
        """
        Handles the transformation and delivery of an event.
        
        Delivers the event to the caliper log file as well as delivers it to
        an external API if configured to do so.

        @params:
        event: raw event from edX event tracking pipeline
        """
        try:
            g_statement = converter.to_gamma(event)

            if g_statement is not None:
                client.publisher.publish_event(g_statement.data)
            return event

        except KeyError:
            TRACKING_LOGGER.exception("Missing transformer method implementation for {}".format(
                event.get('event_type')))

        except Exception as ex:
            TRACKING_LOGGER.exception(ex.args)

    def send(self, event):
        """
        Implements the abstract send method in track.backends.BaseBackend

        @params:
        event: (dict) raw event from edX event tracking pipeline:
        """
        if not event['event_type'].startswith('/'):
            TRACKING_LOGGER.info(self.__call__(event))
        else:
            TRACKING_LOGGER.info(json.dumps(event))
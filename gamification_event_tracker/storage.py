"""H2Labs LearningLocker xAPI backend."""

import json
import re
import requests

from gamification_event_tracker import exceptions, settings


class GammaStorage(object):
    """
    RG Gamification default backend knows as GAMMA.
    """
    def __init__(self, enabled=False, endpoint=None, key=None, secret=None):
        self.is_enabled = all((enabled, endpoint, key, secret))
        self.endpoint = endpoint
        self.key = key
        self.secret = secret

    def save(self, event):
        headers = {
            'App-key': self.key,
            'App-secret': self.secret
        }
        if self.is_enabled:
            return requests.put(
                self.endpoint+settings.GAMMA_API_SUFFIX,
                data=event,
                headers=headers,
                verify=False
            )

    def response_has_errors(self, response_data):
        return json.loads(response_data).has_key('Error')

    def request_unauthorised(self, response_data):
        return json.loads(response_data).get('message', '') == 'Unauthorised'

    def response_has_storage_errors(self, response_data):
        return json.loads(response_data).has_key('warnings')

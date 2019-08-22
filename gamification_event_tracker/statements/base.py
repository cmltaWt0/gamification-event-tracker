"""Statements base for Gamma Event Log."""
from abc import ABCMeta, abstractmethod
import json


class BaseGammaEvent(object):
    """
    Base class for Gamification Event Logs.
    """
    __metaclass__ = ABCMeta

    def __init__(self, event, *args, **kwargs):
        """
        Initialize an xAPI Statement from a tracking log event.
        """
        self.event_type = self.get_type(event)
        self.username = self.get_username(event)
        self.course_id = self.get_course_id(event)
        self.org = self.get_org(event)
        self.uid = self.get_uid(event)
    
    def get_type(self, event):
        return event['event_type']

    def get_username(self, event):
        return event['username']

    def get_course_id(self, event):
        return event.get('context', {}).get('course_id', '')
    
    def get_org(self, event):
        return event.get('context', {}).get('org_id', '')

    @property
    def data(self):
        return dict(
            username=self.username,
            course_id=self.course_id,
            org=self.org,
            event_type=self.event_type,
            uid=self.uid
        )

    @abstractmethod
    def get_uid(self, event):
        pass

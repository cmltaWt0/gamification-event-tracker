"""
Add GamificationProcessor to event tracking backends' list.
"""
__version__ = "0.0.1"

from django.conf import settings as django_settings

from gamification_event_tracker.settings import RG_GAMIFICATION_TRACKING_BACKENDS, RG_GAMIFICATION_TRACKING_PROCESSOR


default_app_config = 'gamification_event_tracker.apps.GamificationTrackingConfig'


if (
    hasattr(django_settings, 'RG_GAMIFICATION') and
    django_settings.RG_GAMIFICATION.get('ENABLED') == True and
    django_settings.RG_GAMIFICATION.get('RG_GAMIFICATION_ENDPOINT')):

    if hasattr(django_settings, 'EVENT_TRACKING_BACKENDS'):
        django_settings.EVENT_TRACKING_BACKENDS['tracking_logs']['OPTIONS']['processors'] += [
            {'ENGINE': RG_GAMIFICATION_TRACKING_PROCESSOR}
        ]

    if hasattr(django_settings, 'TRACKING_BACKENDS'):
        django_settings.TRACKING_BACKENDS = RG_GAMIFICATION_TRACKING_BACKENDS

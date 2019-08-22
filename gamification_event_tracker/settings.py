"""
Settings for xApi tracking app.
"""


RG_GAMIFICATION_TRACKING_PROCESSOR = 'gamification_event_tracker.processor.GamificationProcessor'

RG_GAMIFICATION_TRACKING_BACKENDS = {
    'logger': {
        'ENGINE': RG_GAMIFICATION_TRACKING_PROCESSOR,
        'OPTIONS': {
            'name': 'tracking'
        }
    }
}


GAMMA_API_SUFFIX = 'api/v0/gamma-profile/'
OPENEDX_PLATFORM_URI = '/'
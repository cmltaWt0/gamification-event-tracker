"""Convert tracking log entries to xAPI statements."""

import logging

from django.conf import settings

from gamification_event_tracker import exceptions
from gamification_event_tracker.statements import course, video, problem


logger = logging.getLogger(__name__)


TRACKING_EVENTS_TO_GAMMA_STATEMENT_MAP = {

    # course enrollment
    'edx.course.enrollment.activated': course.CourseEnrollmentStatement,
    'edx.course.enrollment.deactivated': course.CourseUnenrollmentStatement,

    # course completion
    'edx.certificate.created': course.CourseCompletionStatement,

    # problems
    'problem_check': problem.ProblemCheckStatement,
    'edx.grades.problem.submitted': problem.ProblemSubmittedStatement,
    'problem_graded': problem.ProblemGradedStatement,
    'reset_problem': problem.ProblemResetStatement,



    # video
    'ready_video': video.VideoStatement,
    'load_video': video.VideoStatement,
    'edx.video.loaded': video.VideoStatement,

    'play_video': video.VideoPlayStatement,
    'edx.video.played': video.VideoPlayStatement,

    'pause_video': video.VideoPauseStatement,
    'edx.video.paused': video.VideoPauseStatement,

    'stop_video': video.VideoCompleteStatement,
    'edx.video.stopped': video.VideoCompleteStatement,

    'seek_video': video.VideoSeekStatement,
    'edx.video.position.changed': video.VideoSeekStatement,

    'show_transcript': video.VideoTranscriptStatement,
    'hide_transcript': video.VideoTranscriptStatement,
    'edx.video.transcript.shown': video.VideoTranscriptStatement,
    'edx.video.transcript.hidden': video.VideoTranscriptStatement,
    'edx.video.closed_captions.shown': video.VideoTranscriptStatement,
    'edx.video.closed_captions.hidden': video.VideoTranscriptStatement,
}



def to_gamma(event):
    """Return tuple of Gamification statements or None if ignored or unhandled event type."""

    # strip Video XBlock prefixes for checking
    event_type = event['event_type'].replace("xblock-video.", "")

    if event_type in settings.IGNORED_EVENT_TYPES:
        return  # deliberately ignored event

    try:
        statement_class = TRACKING_EVENTS_TO_GAMMA_STATEMENT_MAP[event_type]
    except KeyError:  # untracked event
        return
    
    return statement_class(event)

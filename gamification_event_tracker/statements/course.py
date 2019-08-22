from . base import BaseGammaEvent


class BaseCourse(BaseGammaEvent):
    def get_uid(self, event):
        event_dict =  event.get('event', {})
        if event_dict:
            uid = '{}:{}:{}'.format(
                event_dict.get('course_id', ''),
                event_dict.get('user_id', ''),
                event_dict.get('mode', '')
            )
        return uid or ''


class CourseEnrollmentStatement(BaseCourse):
    pass


class CourseUnenrollmentStatement(BaseCourse):
    pass


class CourseCompletionStatement(BaseCourse):
    pass

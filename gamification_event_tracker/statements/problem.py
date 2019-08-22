from . base import BaseGammaEvent


class BaseProblem(BaseGammaEvent):
    def get_uid(self, event):
        event_dict =  event.get('event', {})
        if event_dict:
            uid = '{}:{}:{}'.format(
                event_dict.get('problem_id', ''),
                self.get_course_id(event),
                self.get_username(event)
            )
        return uid or ''

class ProblemCheckStatement(BaseProblem):
    pass


class ProblemSubmittedStatement(BaseProblem):
    pass


class ProblemResetStatement(BaseProblem):
    pass


class ProblemGradedStatement(BaseProblem):
    pass

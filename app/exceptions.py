class QuizException(Exception):
    pass


class QuizFinishedException(QuizException):
    pass

class AnswerPositionOverflow(QuizException):
    pass

class SemesterNotFound(QuizException):
    pass


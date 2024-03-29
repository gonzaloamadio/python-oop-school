"""
Define entities or members.
A Student has a name, last name, id, classes he attend, quizzes he takes.
A Teacher has a name, last name, id, classes he teaches, quizzes he makes.

ASSUMPTIONS:
    Both teacher and students has two names. Could be more complet / better.

    By design, students can enroll to "running courses", and only running
    courses are courses given by teachers.
    There is no restriction in which course can a student enroll.
    Could be improved by having a hierarchy of courses, or another
    implementation of which courses can students enroll, but I think is out of
    scope of this exercise.

    I assumed that the grade of the students is the sum of the grades of the
    quizzes they have completed.
"""
from classroom.app.exceptions import QuizFinishedException, SemesterNotFound
from classroom.app.utils import get_semester_id
from typing import List, Dict, NoReturn, Union, TYPE_CHECKING
from classroom.app.quizzes import Quiz
if TYPE_CHECKING: # pragma: no cover
    from classroom.app.quizzes import Quiz
    from classroom.app.courses import CourseRunning
    QuizInfo = Dict[str, Quiz]
    Quizzes = Dict[str, QuizInfo]
    Classes = List[str]


class Person(object):
    """
    Returns a ```Person``` object with given name.

    """

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def get_names(self) -> str:
        "Returns a string containing hole name of the person"
        return "{} {}".format(self.first_name, self.last_name)


class Student(Person):
    """
    Returns a ```Student``` object.

    Atribute
    --------
    first_name : str
        first name of the student
    last_name : str
        last name or surname of the student
    student_id : str
        unique identifier of a student
    classes : list[str]
        list of running courses codes that a student is enroled in.
    quizzes : list[Quiz]
        list of quizzes this student has answered to.
    """

    def __init__(
        self, first_name: str, last_name: str, student_id: str, *args, **kwargs
    ) -> None:
        """
        Parameters
        ----------
        first_name : str
            first name of the student
        last_name : str
            last name or surname of the student
        student_id : str
            unique identifier of a student
        """
        Person.__init__(self, first_name, last_name)
        self.student_id = student_id
        self.classes: 'Classes' = []
        # Will have the following shape : {'<semester_id>':{'<quiz_id>': Quiz}}
        self.quizzes: 'Quizzes' = {}

    def get_enroled_courses(self) -> 'Classes':
        """Get courses this student is enroled to."""
        return self.classes

    def enrol(self, course_running: 'CourseRunning') -> None:
        """Add course to courses that the student is enroled in."""
        self.classes.append(course_running.running_course_code)
        course_running.add_student(self)

    def subscribe_to_quiz(self, quiz: 'Quiz') -> None:
        """Given a quiz, subscribe this user to it."""
        # quiz.add_student(self)
        semester = get_semester_id()
        # If semester's key is not created, do it, and add quiz.
        self.quizzes.setdefault(semester, {})[quiz.quiz_id] = quiz

    # def _get_semester_quizzes(self, semester_id: str) -> Union[QuizInfo, NoReturn]:
    def _get_semester_quizzes(self, semester_id: str) -> 'QuizInfo':
        """Given a semester id, return an object:  {quiz_id : Quiz}.

        Raises
        ------
        SemesterNotFound:
            If semester_id is not found.

        Return
        ------
        Quizzes Info: {'<quiz_id>' : Quiz, ... }
            Information about quizzes belonging to the semester.
        """
        current_semester_quiz_info = self.quizzes.get(semester_id, None)
        if not current_semester_quiz_info:
            raise SemesterNotFound('The semester was not found.')
        return current_semester_quiz_info

    def answer_quiz(self, quiz_id: str, answer: int) -> str:
        """Answer a quiz for this semester."""
        try:
            current_quizzes = self._get_semester_quizzes(get_semester_id())
        except SemesterNotFound:
            return "You are not subscribed to this quiz in current semester"
        quiz = current_quizzes.get(quiz_id) # type: ignore
        if not quiz:
            return "Quiz not defined"
        try:
            quiz.answer_next_question(answer)
        except QuizFinishedException as err:
            return "Quiz already finished"
        return "Ok"

    def get_score_for_semester(self, semester_id: str = None) ->  Union[str, float]:
        """Given a semester_id, get score for that semester.

        Raises
        ------
        SemesterNotFound:
            If semester_id is not found.

        Return
        ------
        score : int
            Score calculation for all quizzes of the semester.
        """
        if not semester_id:
            semester_id = get_semester_id()
        try:
            current_quizzes = self._get_semester_quizzes(semester_id) # type: ignore
        except SemesterNotFound:
            return "You have not subscribed to any quiz in this semester"
        score = 0.0
        for qid in current_quizzes:
            score += current_quizzes[qid].get_score()
        return score


class Teacher(Person):
    """
    Returns a ```Teacher``` object.

    Atribute
    --------
    first_name : str
        first name of the teacher
    last_name : str
        last name or surname of the teacher
    teacher_id : str
        unique identifier of a teacher
    classes : list[str]
        list of running courses codes that the teacher is teaching in.
    """

    def __init__(self, first_name: str, last_name: str, teacher_id: str) -> None:
        """
        Parameters
        ----------
        first_name : str
            first name of the teacher
        last_name : str
            last name or surname of the teacher
        teacher_id : str
            unique identifier of a teacher
        """
        Person.__init__(self, first_name, last_name)
        self.teacher_id = teacher_id
        self.classes: 'Classes' = []

    def add_course_to_teach(self, course_code):
        """Add running course to courses that the teacher is teaching in."""
        self.classes.append(course_code)

    def get_teaching_courses(self):
        """Return a list of running courses the teacher is teaching in."""
        return self.classes

    def create_quiz(self, qid: str, name: str) -> 'Quiz':
        return Quiz(qid, self, name)

    @staticmethod
    def assign_quiz_to_student(student: Student, quiz: 'Quiz') -> None:
        student.subscribe_to_quiz(quiz)

    @staticmethod
    def calc_student_grade_for_semester(student: Student, semester_id: str = None) -> Union[str,float]:
        return student.get_score_for_semester(semester_id)

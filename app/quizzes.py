"""Define classes related to quizzes.


ASSUMPTIONS:
    Names of quizes are unique.
    Quizzes are created by one teacher.
    There are always 4 choices in the questions, and 1 correct answer.
    When take a quiz, student can answer questions in order. Can not take a quizz
    again if it is finished.
    Question is the set of question and possible answers. Could be more granular.
"""
from collections import namedtuple
from app.exceptions import QuizFinishedException, AnswerPositionOverflow

class Question:
    """Question. A question belong to a quiz.
    I consider a question as the set of question, and multiple choice answer.

    Atributes
    --------
    text : str
        question
    _correct_answer : int
        Which of the answer is the correct one.
    possible_answers : [string]
        List of possible answers.
    is_answered : bool
        is this question already answered?
    is_answered_correct : bool
        is this question answered and correct?
    """

    def __init__(self, text):
        """
        Parameters
        ----------
        text : str
            question
        """
        self.text = text
        self._correct_answer = 1
        self.possible_answers = [None] * 4
        self.is_answered = False
        self.is_answered_correct = False

    @property
    def correct_answer(self):
        return self._correct_answer

    @correct_answer.setter
    def correct_answer(self, num):
        if not (0 < num <= 4):
            raise AnswerPositionOverflow("Choices can be between 1 and 4")
        self._correct_answer = num

    def foofoo(self, papa):
        pass

    def add_possible_answer(self, answer, position, is_correct):
        """Add a possible answer in a position (1, 2, 3, 4)."""
        if not (0 < position <= 4):
            raise AnswerPositionOverflow("Position must be between 1 and 4")
        else:
            self.possible_answers[position] = answer
            self.correct_answer =  position
            return True

class Quiz:
    """Represents a quiz.
    A quiz is composed of questions. It is done by a teacher.
    It can be finished, i.e. all the questions are ansered, or be
    partially finished.

    Atribute
    --------
    test : str
        answer of a question
    question : Question
        questions that make this quiz
    is_finished : bool
        is the quizz finished?
    """
    def __init__(self, quiz_id, teacher, name):
        self.quiz_id = quiz_id
        self.teacher = teacher
        self.name = name
        self.questions = []
        # TODO: Make read only
        self.is_finished = False

    def add_question(self, q: Question) -> None:
        self.questions.append(q)
        self.is_finished = False

    def _is_quiz_finished(self) -> bool:
        # Check if there is a question that is not answered
        question = next((q for q in self.questions if q.is_answered == False), None)
        return question != None

    def answer_next_question(self, answer: int) -> None:
        # Get first question not answered, we can continue an unifinished quizz
        question = next((q for q in self.questions if q.is_answered == False), None)
        if question is None or self.is_finished:
            raise QuizFinishedException('Quiz is already finished')
        # If answer matches the correct option, mark as answered ok.
        # TODO: Change for function with exception
        if answer == question.correct_answer:
            question.is_answered_correct = True
        # Mark question as answered
        question.is_answered = True
        # If there is no more unanswered questions
        if not self._is_quiz_finished():
            self.is_finished = True

    def get_score(self):
        if not self.questions:
            return 0
        total_questions = len(self.questions)
        correct_answers = len([x for x in self.questions if x.is_answered_correct])
        score = round((correct_answers / total_questions) * 100.0, 2)
        return score

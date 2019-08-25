"""Test related with quizzes."""

import factory
from tests.utils import BaseTestCase

from app.entities import Teacher
from app.exceptions import AnswerPositionOverflow, QuizFinishedException
from tests.factories import TeacherFactory, StudentFactory
from tests.factories import DepartmentFactory, CourseFactory, CourseRunningFactory
from tests.factories import QuizFactory, QuestionFactory, RandomQuestionFactory


class QuizTests(BaseTestCase):

    def setUp(self):
        self.quiz = QuizFactory()

    def test_quiz_has_attrs(self):
        '''Test: quiz has basic attributes.'''
        self.assertHasAttr(self.quiz, 'quiz_id')
        self.assertHasAttr(self.quiz, 'teacher')
        self.assertHasAttr(self.quiz, 'name')
        self.assertHasAttr(self.quiz, 'questions')
        self.assertHasAttr(self.quiz, 'is_finished')

    def test_quiz_params_on_creation(self):
        '''Test: quiz does not modify params on creation.'''
        self.assertEqual(self.quiz.quiz_id, 'quiz_01')
        self.assertEqual(self.quiz.name, 'Mathematics Quiz Number 1')
        self.assertIsInstance(self.quiz.teacher, Teacher)
        self.assertEqual(self.quiz.questions, [])
        self.assertEqual(self.quiz.is_finished, False)

    def test_quiz_can_add_question(self):
        '''Test: Can we add a question to a quiz?.'''
        quiz = self.quiz
        q1 = RandomQuestionFactory()
        q2 = RandomQuestionFactory()
        quiz.add_question(q1)
        quiz.add_question(q2)
        self.assertEqual(len(quiz.questions), 2)
        self.assertEqual(quiz.is_finished, False)

    def test_quiz_can_answer_next_question(self):
        '''Test if there is a function to answer next question.'''
        quiz = self.quiz
        q1 = RandomQuestionFactory()
        quiz.add_question(q1)
        quiz.answer_next_question(1)

    def test_quiz_is_marked_as_finished_when_last_question_i1s_answered(self):
        '''Test if a quiz is flagged as finished when there are no more questions to answer.'''
        quiz = self.quiz
        q1 = RandomQuestionFactory()
        # q1.correct_answer = 1
        quiz.add_question(q1)
        quiz.answer_next_question(1)
        self.assertEqual(quiz.is_finished, True)

    def test_quiz_cannot_be_answered_if_finished_or_empty(self):
        '''If a quiz is finished, we cannot answer it again.'''
        quiz = self.quiz
        with self.assertRaises(QuizFinishedException) as e:
            quiz.answer_next_question(2)
        self.assertEqual(str(e.exception), 'Quiz is already finished')

    def test_quiz_get_score(self):
        '''Test get score, should be a ratio between total questions and correct.'''
        quiz = self.quiz
        self.assertEqual(quiz.get_score(), 0)
        q1 = RandomQuestionFactory()
        q1.add_possible_answer('2',1, True)
        quiz.add_question(q1)
        quiz.answer_next_question(1)
        self.assertEqual(quiz.get_score(), 100)
        q2 = RandomQuestionFactory()
        q2.add_possible_answer('2',1, True)
        quiz.add_question(q2)
        quiz.answer_next_question(2)
        self.assertEqual(quiz.get_score(), 50)

class QuestionTests(BaseTestCase):

    def setUp(self):
        self.question = QuestionFactory()

    def test_question_has_attrs(self):
        '''Test: question has basic attributes.'''
        self.assertHasAttr(self.question, 'text')
        self.assertHasAttr(self.question, '_correct_answer')
        self.assertHasAttr(self.question, 'possible_answers')
        self.assertHasAttr(self.question, 'is_answered')
        self.assertHasAttr(self.question, 'is_answered_correct')

    def test_question_params_on_creation(self):
        '''Test: question does not modify params on creation.'''
        self.assertEqual(self.question.text, 'How much is 1 + 1?')
        self.assertEqual(self.question._correct_answer, 1)
        self.assertEqual(len(self.question.possible_answers), 4)
        self.assertEqual(self.question.is_answered, False)
        self.assertEqual(self.question.is_answered_correct, False)

    def test_question_can_add_a_possible_answer(self):
        '''Add an answer to the multiple choice of this question.'''
        question = self.question
        # Add answer, in a position, is it correct?
        question.add_possible_answer('2', 1, True)
        # We assume to have only 4 choices.
        with self.assertRaises(AnswerPositionOverflow) as e:
            question.add_possible_answer('3', 5, True)
        self.assertEqual(str(e.exception), 'Position must be between 1 and 4')

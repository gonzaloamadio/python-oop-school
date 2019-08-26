from classroom.tests.factories import (
    CourseRunningFactory,
    StudentFactory,
    TeacherFactory,
    QuizFactory,
    QuestionFactory,
)
from classroom.tests.utils import BaseTestCase
from classroom.app.quizzes import Quiz


class StudentTests(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        cls.student = StudentFactory()

    def test_student_has_attrs(self):
        '''Test: student has basic attributes.'''
        self.assertHasAttr(self.student, 'first_name')
        self.assertHasAttr(self.student, 'last_name')
        self.assertHasAttr(self.student, 'student_id')
        self.assertHasAttr(self.student, 'classes')
        self.assertHasAttr(self.student, 'quizzes')

    def test_student_basic_info(self):
        '''Test: student does not modify params on creation.'''
        student = self.student
        self.assertEqual(student.first_name, 'Gonzalo')
        self.assertEqual(student.last_name, 'Amadio')
        self.assertEqual(student.student_id, 'GA1988')
        names = student.get_names()
        self.assertEqual(names, 'Gonzalo Amadio')
        self.assertEqual(student.classes, [])
        self.assertEqual(student.quizzes, {})

    def test_student_has_courses(self):
        '''Test if can get enroled courses of a student.'''
        student = self.student
        courses = student.get_enroled_courses()
        self.assertIsNotNone(courses)

    def test_student_can_enrol_to_course_running(self):
        '''Test if a student can enrol to a running course.'''
        student = self.student
        course = CourseRunningFactory()
        # Check if we can enrol to course
        student.enrol(course)
        # Check if after enrol, student was added to the course
        students_in_course = course.get_students()
        self.assertIn(student, students_in_course)
        # Check if after enrol, course was added to student list of courses
        self.assertIn(course.running_course_code, student.get_enroled_courses())

    def test_student_can_subscribe_to_quizz(self):
        quiz = QuizFactory()
        self.student.subscribe_to_quizz(quiz)

    def test_student_can_answer_quizz(self):
        student = self.student
        res = student.answer_quizz('non_existent', 1)
        assert res == "You are not subscribed to this quiz in current semester"
        quiz = QuizFactory()
        question = QuestionFactory()
        question.add_possible_answer('2', 1, True)
        quiz.add_question(question)
        student.subscribe_to_quizz(quiz)
        res = student.answer_quizz(quiz.quiz_id, 1)
        assert res == "Ok"
        res = student.answer_quizz('not_existent', 1)
        assert res == "Quiz not defined"
        res = student.answer_quizz(quiz.quiz_id, 1)
        assert res == "Quiz already finished"

    def test_student_can_get_score_for_semester(self):
        student = self.student
        res = student.get_score_for_semester('not_existent')
        assert res == 'You have not subscribed to any quiz in this semester'
        quiz = QuizFactory()
        question = QuestionFactory()
        question.add_possible_answer('2', 1, True)
        quiz.add_question(question)
        student.subscribe_to_quizz(quiz)
        student.answer_quizz(quiz.quiz_id, 1)
        res = student.get_score_for_semester()
        assert res == 100.00



class TeacherTests(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        cls.teacher = TeacherFactory()

    def test_department_has_attrs(self):
        """Test: department has basic attributes."""
        self.assertHasAttr(self.teacher, 'first_name')
        self.assertHasAttr(self.teacher, 'last_name')
        self.assertHasAttr(self.teacher, 'teacher_id')
        self.assertHasAttr(self.teacher, 'classes')

    def test_teacher_basic_info(self):
        teacher = self.teacher
        self.assertEqual(teacher.first_name, 'John')
        self.assertEqual(teacher.last_name, 'Doe')
        names = teacher.get_names()
        self.assertEqual(names, 'John Doe')
        self.assertEqual(teacher.classes, [])

    def test_teacher_has_courses(self):
        '''Test if can get courses which the teacher is teaching.'''
        teacher = self.teacher
        courses = teacher.get_teaching_courses()
        self.assertIsNotNone(courses)

    def test_teacher_teaches_running_course(self):
        '''Test if teacher can add a running course to teach.'''
        teacher = self.teacher
        course = CourseRunningFactory()
        teacher.add_course_to_teach(course.get_code())
        self.assertIn(course.get_code(), teacher.get_teaching_courses())

    def test_teacher_can_create_quiz(self):
        q = self.teacher.create_quiz('myid', 'Math quiz')
        self.assertIsInstance(q, Quiz)


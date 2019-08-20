import factory
from tests.utils import BaseTestCase

from app.entities import Student, Teacher
from tests.courses_test import (CourseFactory,
                                RunningCourseFactory,
                                DepartmentFactory)


class StudentFactory(factory.Factory):
    '''Factory to create students.'''
    class Meta:
        model = Student

    first_name = 'Gonzalo'
    last_name = 'Amadio'
    student_id = 'GA1988'

class RandomStudentFactory(factory.Factory):
    class Meta:
        model = Student

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    student_id = factory.Faker('student_id')

class TeacherFactory(factory.Factory):
    '''Factory to create students.'''
    class Meta:
        model = Teacher

    first_name = 'John'
    last_name = 'Doe'
    teacher_id = 'JD1966'


#class StudentTests(unittest.TestCase):
class StudentTests(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        cls.student = StudentFactory()

    def test_student_has_attrs(self):
        self.assertHasAttr(self.student, 'first_name')
        self.assertHasAttr(self.student, 'last_name')
        self.assertHasAttr(self.student, 'student_id')

    def test_student_basic_info(self):
        student = self.student
        self.assertEqual(student.first_name, 'Gonzalo')
        self.assertEqual(student.last_name, 'Amadio')
        self.assertEqual(student.student_id, 'GA1988')
        names = student.get_names()
        self.assertEqual(names, 'Gonzalo Amadio')

    def test_student_has_courses(self):
        student = self.student
        courses = student.get_enroled_courses()
        self.assertIsNotNone(courses)

    def test_student_can_enrol_to_course_running(self):
        student = self.student
        course = RunningCourseFactory()
        # Check if we can enrol to course
        student.enrol(course.get_code())
        # Check if after enrol, student was added to the course
        students_in_course = course.get_students()
        self.assertIn(student, students_in_course)

class TeacherTests(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        cls.teacher = TeacherFactory()

    def test_teacher_basic_info(self):
        teacher = self.teacher
        self.assertEqual(teacher.first_name, 'John')
        self.assertEqual(teacher.last_name, 'Doe')
        names = teacher.get_names()
        self.assertEqual(names, 'John Doe')

    def test_teacher_has_courses(self):
        teacher = self.teacher
        courses = teacher.get_teaching_courses()
        self.assertIsNotNone(courses)

    def test_teacher_teaches_running_course(self):
        teacher = self.teacher
        course = RunningCourseFactory()
        res = teacher.add_course_to_teach(course.get_code())
        self.assertIsNotNone(res)

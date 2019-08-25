import factory
from tests.utils import BaseTestCase

#from app.entities import Student, Teacher
#from tests.courses_test import (CourseFactory,
#                                CourseRunningFactory,
#                                DepartmentFactory)


from tests.factories import TeacherFactory, StudentFactory
from tests.factories import DepartmentFactory, CourseFactory, CourseRunningFactory

#class StudentTests(unittest.TestCase):
class StudentTests(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        cls.student = StudentFactory()

    def test_student_has_attrs(self):
        self.assertHasAttr(self.student, 'first_name')
        self.assertHasAttr(self.student, 'last_name')
        self.assertHasAttr(self.student, 'student_id')
        self.assertHasAttr(self.student, 'classes')
        self.assertHasAttr(self.student, 'quizzes')

    def test_student_basic_info(self):
        student = self.student
        self.assertEqual(student.first_name, 'Gonzalo')
        self.assertEqual(student.last_name, 'Amadio')
        self.assertEqual(student.student_id, 'GA1988')
        names = student.get_names()
        self.assertEqual(names, 'Gonzalo Amadio')
        self.assertEqual(student.classes, [])
        self.assertEqual(student.quizzes, {})

    def test_student_has_courses(self):
        student = self.student
        courses = student.get_enroled_courses()
        self.assertIsNotNone(courses)

    def test_student_can_enrol_to_course_running(self):
        student = self.student
        course = CourseRunningFactory()
        # Check if we can enrol to course
        student.enrol(course)
        # Check if after enrol, student was added to the course
        students_in_course = course.get_students()
        self.assertIn(student, students_in_course)
        # Check if after enrol, course was added to student list of courses
        self.assertIn(course.running_course_code, student.get_enroled_courses())

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
        teacher = self.teacher
        courses = teacher.get_teaching_courses()
        self.assertIsNotNone(courses)

    def test_teacher_teaches_running_course(self):
        teacher = self.teacher
        course = CourseRunningFactory()
        teacher.add_course_to_teach(course.get_code())
        self.assertIn(course.get_code(), teacher.get_teaching_courses())

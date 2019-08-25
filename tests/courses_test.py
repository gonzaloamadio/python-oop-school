"""Tests related with entities belonging to a school."""

import factory
from tests.utils import BaseTestCase

#from app.courses import Course, Department, CourseRunning

# from tests.entities_test import TeacherFactory, StudentFactory
from tests.factories import TeacherFactory, StudentFactory
from tests.factories import DepartmentFactory, CourseFactory, CourseRunningFactory

class DepartmentTests(BaseTestCase):

    def setUp(self):
        self.department = DepartmentFactory()

    def test_department_has_attrs(self):
        """Test: department has basic attributes."""
        self.assertHasAttr(self.department, 'name')
        self.assertHasAttr(self.department, 'department_code')
        self.assertHasAttr(self.department, 'courses')

    def test_department_params_on_creation(self):
        """Test: department does not modify params on creation."""
        code = self.department.department_code
        name = self.department.name
        courses = self.department.courses
        self.assertEqual(code, 'DEPOM')
        self.assertEqual(name, 'Department of Mathematics')
        self.assertEqual(courses, {})

    def test_department_get_courses(self):
        """Test: Get the courses belonging to this department."""
        department = self.department
        courses = department.get_courses()
        self.assertIsNotNone(courses)

    def test_department_create_course(self):
        """Test: Create and add a course to this department."""
        department = self.department
        # Check if we can create a course
        res = department.add_course("Mathematics", "MAT")
        # Check if the created course belong to this department
        self.assertIn(res.course_code, department.get_courses())

    def test_department_can_mark_course_as_running(self):
        """Test: Mark a course as running.
        A course can be a course as an idea, and also be teached some year.
        """
        from app.courses import CourseRunning
        department = self.department
        course = CourseFactory()
        year = 2019
        crunning = department.mark_course_as_running(course, year)
        self.assertIsInstance(crunning, CourseRunning)
        self.assertIn(crunning, course.get_runnings())

    def test_department_can_add_teacher_to_running_course(self):
        """Test: Assign a teacher to a running course."""
        department = self.department
        crunning = CourseRunningFactory()
        teacher = TeacherFactory()
        department.assign_teacher_to_course(teacher, crunning)
        self.assertEqual(crunning.teacher, teacher)
        self.assertIn(crunning.running_course_code, teacher.get_teaching_courses())

    def test_department_can_add_student_to_running_course(self):
        """Test: Add a student to a running course."""
        department = self.department
        crunning = CourseRunningFactory()
        student = StudentFactory()
        department.add_student_to_course(student, crunning)
        self.assertIn(student, crunning.students)


class CourseRunningTests(BaseTestCase):

    def setUp(self):
        self.running_course = CourseRunningFactory()

    def test_running_course_has_attrs(self):
        """Test: running_course has basic attributes."""
        self.assertHasAttr(self.running_course, 'course')
        self.assertHasAttr(self.running_course, 'year')
        self.assertHasAttr(self.running_course, 'students')
        self.assertHasAttr(self.running_course, 'teacher')
        self.assertHasAttr(self.running_course, 'running_course_code')

    def test_running_course_params_on_creation(self):
        """Test: running_course does not modify params on creation."""
        rc = self.running_course
        self.assertEqual(rc.year, '2019')
        # They point to different places. Should make a comparison attr by attr.
        # self.assertEqual(rc.course, CourseFactory())
        # Check that students is created and empty
        self.assertFalse(rc.students)
        # Check that students is created and empty or None
        self.assertFalse(rc.teacher)
        c = CourseFactory()
        self.assertEqual(rc.running_course_code, "{}_{}".format(c.course_code, '2019'))

    def test_running_course_year_is_number_in_string(self):
        """Test: the year passed as string is actually a number."""
        self.assertTrue(int(self.running_course.year))

    def test_running_course_can_add_students(self):
        rc = self.running_course
        s = StudentFactory()
        rc.add_student(s)
        self.assertIn(s, rc.students)

    def test_running_course_can_add_teacher(self):
        rc = self.running_course
        t = TeacherFactory()
        rc.assign_teacher(t)
        self.assertEqual(t, rc.teacher)


class CourseTests(BaseTestCase):

    def setUp(self):
        self.course = CourseFactory()

    def test_course_has_attrs(self):
        """Test: course has basic attributes."""
        self.assertHasAttr(self.course, 'description')
        self.assertHasAttr(self.course, 'course_code')
        self.assertHasAttr(self.course, 'department')
        self.assertHasAttr(self.course, 'runnings')

    def test_course_params_on_creation(self):
        """Test: course does not modify params on creation."""
        c = self.course
        self.assertEqual(c.description, "Mathematics")
        self.assertEqual(c.course_code, "MAT")
        # Point to different objects. Should compare differently.
        # self.assertEqual(c.department, DepartmentFactory())
        # Check that runnings is created and empty
        self.assertFalse(c.runnings)

    def test_course_can_add_course_running(self):
        crunning = self.course.add_running('2019')
        # Point to different objects. Should compare differently.
        # self.assertEqual(crunning, CourseRunningFactory())
        self.assertIn(crunning, self.course.get_runnings())


if __name__ == '__main__':
    unittest.main()

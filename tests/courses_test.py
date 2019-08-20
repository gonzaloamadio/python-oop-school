import factory
from tests.utils import BaseTestCase

from app.courses import Course, Department, CourseRunning

from tests.entities_test import TeacherFactory, StudentFactory

class DepartmentFactory(factory.Factory):
    '''Factory to create departments.'''
    class Meta:
        model = Department

    name = "Department of Mathematics"
    department_code = "DEPOM"

class CourseFactory(factory.Factory):
    '''Factory to create courses.'''
    class Meta:
        model = Course

    description = "Mathematics"
    course_code = "MAT"
    # department = factory.SubFactory(DepartmentFactory)
    department = DepartmentFactory()

class RunningCourseFactory(factory.Factory):
    '''Factory to create courses that are running in a particular year.'''
    class Meta:
        model = RunningCourse

    # course = factory.SubFactory(CourseFactory)
    course = CourseFactory()
    year = '2019'
    running_course_code = "MAT_2019"

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
        course = CourseFactory()
        self.assertEqual(course,res)
        # Check if the created course belong to this department
        self.assertIn(res, department.get_courses())

    def test_department_can_mark_course_as_running(self):
        """Test: Mark a course as running.
        A course can be a course as an idea, and also be teached some year.
        """
        department = self.department
        course = CourseFactory()
        year = 2019
        crunning = department.mark_course_as_running(course, year)
        self.assertIsInstance(crunning, CourseRunning)

    def test_department_can_add_teacher_to_running_course(self):
        """Test: Assign a teacher to a running course."""
        department = self.department
        crunning = RunningCourseFactory()
        teacher = TeacherFactory()
        department.asign_teacher_to_course(teacher, crunning)
        self.assertEqual(crunning.teacher, teacher)

    def test_department_can_add_student_to_running_course(self):
        """Test: Add a student to a running course."""
        department = self.department
        crunning = RunningCourseFactory()
        student = StudentFactory()
        department.add_student_to_course(student, crunning)
        self.assertIn(student, crunning.students)


class RunningCourseTests(BaseTestCase):

    def setUp(self):
        self.running_course = RunningCourseFactory()

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
        self.assertEqual(rc.course, CourseFactory())
        # Check that students is created and empty
        self.assertFalse(rc.students)
        # Check that students is created and empty or None
        self.assertFalse(rc.teacher)
        self.assertEqual(rc.running_course_code, "{}_{}".format(course_code, year))

    def test_running_course_year_is_number_in_string(self):
        """Test: the year passed as string is actually a number."""
        self.assertTrue(int(self.running.year))

    def test_running_course_can_add_students(self):
        rc = cls.running_course
        s = StudentFactory()
        rc.add_student(s)
        self.assertIn(s, rc.students)

    def test_running_course_can_add_teacher(self):
        rc = cls.running_course
        t = TeacherFactory()
        rc.add_teacher(t)
        self.assertEqual(t, rc.teacher)


class CourseTests(BaseTestCase):

    def setUp(cls):
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
        self.assertEqual(c.department, DepartmentFactory())
        # Check that runnings is created and empty
        self.assertFalse(c.runnings)

    def test_course_can_add_course_running(self):
        crunning = self.course.add_running('2019')
        self.assertEqual(crunning, RunningCourseFactory())


if __name__ == '__main__':
    unittest.main()

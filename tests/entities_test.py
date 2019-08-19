import unittest
import factory

from app.entities import Student, Teacher


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


class StudentTests(unittest.TestCase):

    def test_student_basic_info(self):
        student = StudentFactory()
        self.assertEqual(student.first_name, 'Gonzalo')
        self.assertEqual(student.last_name, 'Amadio')
        names = student.get_names()
        self.assertEqual(names, 'Gonzalo Amadio')


class TeacherTests(unittest.TestCase):

    def test_teacher_basic_info(self):
        teacher = TeacherFactory()
        self.assertEqual(teacher.first_name, 'John')
        self.assertEqual(teacher.last_name, 'Doe')
        names = teacher.get_names()
        self.assertEqual(names, 'John Doe')


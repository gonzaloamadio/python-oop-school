import unittest

from app.entities import Student

import factory
#from pytest_factoryboy import register

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

#register(StudentFactory)


class StudentTests(unittest.TestCase):

    def test_student_basic_info(self):
        student = StudentFactory()
        self.assertEqual(student.first_name, 'Gonzalo')
        self.assertEqual(student.last_name, 'Amadio')
        names = student.get_names()
        self.assertEqual(names, 'Gonzalo Amadio')


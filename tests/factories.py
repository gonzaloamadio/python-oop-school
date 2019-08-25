import factory
from app.entities import Student, Teacher
from app.courses import Course, Department, CourseRunning
from app.quizzes import Quiz, Question

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

class StudentFactory(factory.Factory):
    '''Factory to create students.'''
    class Meta:
        model = Student
    first_name = 'Gonzalo'
    last_name = 'Amadio'
    student_id = 'GA1988'
    classes = []
    quizzes = {}

class RandomStudentFactory(factory.Factory):
    class Meta:
        model = Student
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    student_id = factory.Faker('student_id')
    classes = []
    quizzes = {}

class TeacherFactory(factory.Factory):
    '''Factory to create students.'''
    class Meta:
        model = Teacher
    first_name = 'John'
    last_name = 'Doe'
    teacher_id = 'JD1966'

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
    department = DepartmentFactory()

class CourseRunningFactory(factory.Factory):
    '''Factory to create courses that are running in a particular year.'''
    class Meta:
        model = CourseRunning
    course = CourseFactory()
    year = '2019'

class QuizFactory(factory.Factory):
    '''Factory to create a Quiz.'''
    class Meta:
        model = Quiz
    teacher = TeacherFactory()
    quiz_id = 'quiz_01'
    name = 'Mathematics Quiz Number 1'

class QuestionFactory(factory.Factory):
    '''Factory to create a Question.'''
    class Meta:
        model = Question
    text = "How much is 1 + 1?"

class RandomQuestionFactory(factory.Factory):
    '''Factory to create a Question.'''
    class Meta:
        model = Question
    text = factory.Faker('text')

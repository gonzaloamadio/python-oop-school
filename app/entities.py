"""
Define entities or members.
A Student has a name, last name, id, classes he attend, quizzes he takes.
A Teacher has a name, last name, id, classes he teaches, quizzes he makes.

ASSUMPTIONS:
    Both teacher and students has two names. Could be more complet / better.
"""
class Person(object):
    """
    Returns a ```Person``` object with given name.

    """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_names(self):
        "Returns a string containing hole name of the person"
        return "{} {}".format(self.first_name, self.last_name)


class Student(Person):
    """
    Returns a ```Student``` object.

    Atribute
    --------
    name : str
        name of the student
    last_name : str
        last name or surname of the student
    student_id : str
        unique identifier of a student

    """
    def __init__(self, first_name, last_name, student_id):
        Person.__init__(self, first_name, last_name)
        self.student_id = student_id
        self.classes = []

#    def get_details(self):
#        "Returns a string containing student's details."
#        return "%s studies %s and is in %s year." % (self.name, self.branch, self.year)


class Teacher(Person):
    """
    Returns a ```Teacher``` object, takes a list of strings (list of papers) as
    argument.
    """
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "%s teaches %s" % (self.name, ','.join(self.papers))



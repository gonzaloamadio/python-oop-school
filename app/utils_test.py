from unittest import TestCase
from datetime import datetime

from classroom.app.utils import get_semester_id

class UtilsTest(TestCase):

    def test_get_semester_id(self):
        year = datetime.now().year
        first_semester = "{}_{}".format(year, 1)
        second_semester = "{}_{}".format(year, 2)
        res = get_semester_id()
        assert (res == first_semester or res == second_semester)


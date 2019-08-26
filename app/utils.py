import datetime

def get_semester_id():
    semester = 1 if datetime.datetime.now().month <= 6 else 2
    return "{}_{}".format(datetime.datetime.now().year, semester)

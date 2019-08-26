
# Exercise

Create object oriented design and use test driven development to
implement classes and methods with appropriate data structure
and test the code for the following scenario.
Please add comments describing any assumptions you make:

There are Teachers
There are Students
Students are in classes that teachers teach
Teachers can create multiple quizzes with many questions (each question is multiple choice)
Teachers can assign quizzes to students
Students solve/answer questions to complete the quiz, but they don't have to complete it at
once. (Partial submissions can be made).
Quizzes need to get graded
For each teacher, they can calculate each student's total grade accumulated over a semester
for their classes

# Usage

### requirements

`Python 3.5+`

### Create virtual env 

```
$ sudo apt-get install python3.6
$ sudo pip install virtualenvwrapper
$ export WORKON_HOME=$HOME/.virtualenvs
$ export PROJECT_HOME=$HOME/
$ source /usr/local/bin/virtualenvwrapper.sh
$ source ~/.bashrc
$ mkvirtualenv --python=python3.6 classroom
```

### Clone project and configure


```
$ git clone https://github.com/gonzaloamadio/python-oop-school.git classroom
$ pip install -r requirements.txt
```

Test that pytest is installed:

```
$ pytest --version
This is pytest version 5.1.0, imported from /home/gonzalo/.virtualenvs/classroom/lib/python3.6/site-packages/pytest.py
```

### Run tests and coverage

```
$ cd classroom
$ pytest --cov=classroom --cov-report term-missing
```

Output:

```
app/utils_test.py .                                        
tests/courses_test.py ..............                       
tests/entities_test.py ...........                         
tests/quizzes_test.py ..........                           

----------- coverage: platform linux, python 3.6.6-final-0 
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
__init__.py                  0      0   100%
app/__init__.py              0      0   100%
app/courses.py              48      0   100%
app/entities.py             61      0   100%
app/exceptions.py            8      0   100%
app/quizzes.py              51      0   100%
app/utils.py                 4      0   100%
app/utils_test.py           10      0   100%
tests/__init__.py            0      0   100%
tests/courses_test.py       84      0   100%
tests/entities_test.py      85      0   100%
tests/factories.py          56      0   100%
tests/quizzes_test.py       77      0   100%
tests/utils.py               2      0   100%
------------------------------------------------------
TOTAL                      486      0   100%

```

### Run type check

```
$ mypy app/
```


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

### Create virtual env and install packages

```
$ sudo apt-get install python3.6
$ sudo pip install virtualenvwrapper
$ export WORKON_HOME=$HOME/.virtualenvs
$ export PROJECT_HOME=$HOME/
$ source /usr/local/bin/virtualenvwrapper.sh
$ source ~/.bashrc
$ mkvirtualenv --python=python3.6 classroom
```

```
pip install -r requirements.txt
```

Test that pytest is installed:

```
pytest --version
This is pytest version 5.1.0, imported from /home/gonzalo/.virtualenvs/classroom/lib/python3.6/site-packages/pytest.py
```

"""
Create classes to track homeworks.

1. Homework - accepts howework text and deadline (datetime.timedelta)
Homework has a method, that tells if deadline has passed.

2. Student - can solve homework with `do_homework` method.
Raises DeadlineError with "You are late" message if deadline has passed

3. Teacher - can create homework with `create_homework`; check homework with `check_homework`.
Any teacher can create or check any homework (even if it was created by one of colleagues).

Homework are cached in dict-like structure named `homework_done`. Key is homework, values are 
solutions. Each student can only have one homework solution.

Teacher can `reset_results` - with argument it will reset results for specific homework, without - 
it clears the cache.

Homework is solved if solution has more than 5 symbols.

-------------------
Check file with tests to see how all these classes are used. You can create any additional classes 
you want.
"""
from datetime import datetime, timedelta


class DeadlineError(Exception):
    pass


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = timedelta(days=deadline)
        self.created_at = datetime.now()

    def is_active(self):
        return datetime.now() <= (self.created_at + self.deadline)


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def do_homework(self, homework, solution):
        if not homework.is_active():
            raise DeadlineError("You are late")
        result = HomeworkResult(self, homework, solution)
        return result


class HomeworkResult:
    def __init__(self, author, homework, solution):
        self.author = author
        self.homework = homework
        self.solution = solution


class Teacher:
    homework_done = {}

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @classmethod
    def create_homework(cls, text, deadline):
        hw = Homework(text, deadline)
        cls.homework_done[hw] = set()
        return hw

    @classmethod
    def check_homework(cls, homework_result):
        result_set = cls.homework_done[homework_result.homework]
        if len(homework_result.solution) > 5:
            result_set.add(homework_result)
            cls.homework_done[homework_result.homework] = result_set
            return True

    @classmethod
    def reset_results(cls, homework=None):
        if homework:
            if homework in cls.homework_done:
                del cls.homework_done[homework]
        else:
            cls.homework_done.clear()

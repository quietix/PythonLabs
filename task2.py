import uuid
from enum import Enum
from typing import Optional


class TaskStatuses(Enum):
    ToDo = 1
    InProgress = 2
    Completed = 3



class Task:
    def __init__(self, description=None, status=None, completing_term=None):
        self._id = uuid.uuid4()
        self._description: Optional[str] = description
        self._status: Optional[TaskStatuses] = status
        self._completing_term: Optional[int] = completing_term

    # id
    def get_id(self):
        return self._id

    # description
    def get_description(self):
        return self._description

    def set_description(self, description: str):
        self._description = description

    # status
    def get_status(self):
        return self._status

    def set_status(self, status: TaskStatuses):
        self._status = status

    # completing_term
    def get_completing_term(self):
        return self._completing_term

    def set_completing_term(self, completing_term):
        self._completing_term = completing_term

    # str
    def __str__(self):
        return f"{self.get_id()}, {self.get_description()}, {self.get_status()}, {self.get_completing_term()}"


if __name__ == "__main__":
    description = input("Enter task description: ")

    status_num = int(input("Enter 1 for ToDo, 2 for InProgress, 3 for Completed: "))
    status = TaskStatuses(status_num)

    completing_term = int(input("Enter completing term: "))

    my_task = Task(description, status, completing_term)

    print(my_task)

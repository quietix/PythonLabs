from abc import ABC, abstractmethod


class Student(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def complete_thesis(self):
        pass

    @abstractmethod
    def attend_lectures(self):
        pass

    def process_student(self):
        self.study()
        self.attend_lectures()
        self.complete_thesis()


class BachelorStudent(Student):
    def study(self):
        print(f"{self.name} is studying for the bachelor's degree.")

    def complete_thesis(self):
        print(f"{self.name} is working on a bachelor's thesis.")

    def attend_lectures(self):
        print(f"{self.name} is attending bachelor level lectures.")


class MasterStudent(Student):
    def study(self):
        print(f"{self.name} is studying for the master's degree.")

    def complete_thesis(self):
        print(f"{self.name} is working on a master's thesis.")

    def attend_lectures(self):
        print(f"{self.name} is attending master level lectures.")


class PhDStudent(Student):
    def study(self):
        print(f"{self.name} is studying for the PhD degree.")

    def complete_thesis(self):
        print(f"{self.name} is working on a PhD dissertation.")

    def attend_lectures(self):
        print(f"{self.name} is attending PhD level lectures.")

    def conduct_research(self):
        print(f"{self.name} is conducting research for the PhD dissertation.")

    def process_student(self):
        super().process_student()
        self.conduct_research()


if __name__ == "__main__":
    bachelor = BachelorStudent("Ivan", 20)
    master = MasterStudent("Mstyslav", 27)
    phd = PhDStudent("Maria", 23)

    print("Bachelor Student Process:")
    bachelor.process_student()

    print("\nMaster Student Process:")
    master.process_student()

    print("\nPhD Student Process:")
    phd.process_student()
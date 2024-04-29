def task7(students: list[dict]):
    surnames_to_print = []
    for student in students:
        if student["Avarage mark"] > 80:
            surnames_to_print.append(student["Surname"])
    return surnames_to_print


if __name__ == "__main__":
    student1 = {"Name": "Ivan",
                "Surname": "Zashchyk",
                "Avarage mark": 99.9}
    student2 = {"Name": "Artem",
                "Surname": "Lunev",
                "Avarage mark": 89}
    student3 = {"Name": "No name",
                "Surname": "No surname",
                "Avarage mark": 65}
    student4 = {"Name": "No name 2",
                "Surname": "No surname 2",
                "Avarage mark": 70}

    print(task7([student1, student2, student3, student4]))
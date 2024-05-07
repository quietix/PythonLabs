import json


def task4_2():
    with open("task4.json", "r+") as f:
        my_tuple = tuple(json.load(f))
        min_number = min(my_tuple)
        f.write(f"\n{min_number}")
        print(f"\nmin number: {min_number}")


def task4():
    numbers = input("Enter numbers separated by commas: ")
    my_tuple = tuple([int(x) for x in numbers.replace(" ", "").split(',')])
    print(f"Your tuple:\n{my_tuple}")
    with open("task4.json", "w") as f:
        json.dump(my_tuple, f)
    task4_2()


if __name__ == "__main__":
    task4()
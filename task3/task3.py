import json
from random import randint
from numbers import Number

def list_elems_sum(lst: list[Number]):
    new_list = [elem for elem in lst if elem in range(0, 11)]
    return sum(new_list)


def task3():
    # part 1
    generated_data = [randint(0, 20) for i in range(5)]
    with open("task3.json", "w") as f:
        json.dump(generated_data, f)
    print(f"generated_data:\n{generated_data}\n")

    # part 2
    with open("task3.json", "r+") as f:
        read_data = json.load(f)
        print(f"read_data:\n{read_data}\n")
        lst_sum = list_elems_sum(read_data)
        print(f"sum:\n{lst_sum}\n")
        f.write(f"\n{lst_sum}")


if __name__ == "__main__":
    task3()
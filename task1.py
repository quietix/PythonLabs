from random import random

def task1(num: int) -> list[float]:
    arr = [random() for i in range(num)]
    return arr


if __name__ == "__main__":
    list_len = input("Enter list length: ")
    res = task1(int(list_len))
    print(res)

from random import random

def task1(num: int):
    arr = (random() for i in range(num))
    return arr


if __name__ == "__main__":
    list_len = input("Enter list length: ")
    res = task1(int(list_len))
    for val in res:
        print(val)

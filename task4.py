def task4(input_range: int):
    return [i for i in range(input_range) if i % 2 == 1]


if __name__ == "__main__":
    print(task4(10))
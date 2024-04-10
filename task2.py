def task2(line: str):
    counter = 0
    for char in line:
        counter += 1
    return counter

if __name__ == "__main__":
    print(task2("12345"))
def task6(numbers: list[str]):
    sum = 0
    for num in numbers:
        sum += float(num)
    return sum

if __name__ == "__main__":
    print(task6(["1", "2", "3.5", "4.3"]))
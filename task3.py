def task3(arr: list[int]):
    print(arr)
    while len(arr) > 2:
        del arr[2::3]
        print(arr)


if __name__ == "__main__":
    arr: list[int] = [1,2,3,4,5,6,7,8,9,10]
    task3(arr)
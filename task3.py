def task3(arr: list, a: int, b: int):
    arr_len = len(arr)
    assert a < b and a < arr_len and b < arr_len and a >= 0
    return [arr[i] for i in range(arr_len) if a <= i <= b]


if __name__ == "__main__":
    init_list = ["Apple", "World", "Darkness", "Glory", "Power", "Dignity"]
    print(init_list)

    print(task3(init_list, 1, 4))

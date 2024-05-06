def task2(init_list: list[int]):
    return (elem for elem in init_list if elem % 2 == 0)


if __name__ == "__main__":
    init_list = [i for i in range(11)]
    print(f"Init list:\n{init_list}")

    new_list_generator = task2(init_list)
    print(f"New list:")
    for val in new_list_generator:
        print(val, end=', ')

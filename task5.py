def task5(numbers: list):
    """
    Finds avarage of the numbers in list
    """
    sum = 0

    for num in numbers:
        sum += num

    return sum / len(numbers)



if __name__ == "__main__":
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]

    print(f'List1:\n{list1}')
    print(f'List2:\n{list2}')

    new_list = [task5(list1), task5(list2)]

    print(f'New list:\n{new_list}')
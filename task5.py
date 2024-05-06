def task5(lst: list[int], tries: int) -> str:
    lst_len = len(lst)
    return "".join(str(f"{lst[i % lst_len]}, ") for i in range(tries))


if __name__ == "__main__":
    lst = [i for i in range(2)]
    tries = 5

    print(f"init list:\n{lst}")
    print(task5(lst, tries))
def task2():
    with open("li.py", "w+") as f:
        f.write("li_1 = [1,2]\n")
        f.write("li_2 = ['red', 'green']")

        f.seek(0)

        for line in f.readlines():
            print(line.strip())


if __name__ == "__main__":
    task2()
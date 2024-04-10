def task1(line1: str, line2: str) -> int:
    if len(line1) < 2 or len(line2) < 2:
        return -1

    counter = 0

    for i in range(len(line1) - 1):
        bigram = line1[i] + line1[i+1]
        if line2.find(bigram) != -1:
            counter += 1
            letter_to_remove = bigram[0]
            line1.replace(letter_to_remove, "")
            line2.replace(letter_to_remove, "")

    return counter


if __name__ == "__main__":
    line1 = input("Line1: ")
    line2 = input("Line2: ")
    print(task1(line1, line2))

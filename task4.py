def task4(items_num: int, edit_len: int, replace_symb: str, words: list[str]):
    print(words)

    for i, word in enumerate(words):
        if len(word) == edit_len:
            word = word[:-3] + replace_symb
            words[i] = word

    print(words)



if __name__ == "__main__":
    items_num = int(input("Number of list items: "))
    edit_len = int(input("Length of words that will be edited: "))
    replace_symb = input("Symbol to replace last 3 symbols with: ")

    words = []
    for i in range(items_num):
        word = input(f"Word{i+1}: ")
        words.append(word)

    task4(items_num, edit_len, replace_symb, words)
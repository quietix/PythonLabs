import json
from pprint import pprint

def task1(path_to_json: str = "data1.json"):
    with open(path_to_json, 'r') as f:
        extracted_data: dict = json.load(f)

        print("Init data:")
        pprint(extracted_data)

        values_lst = [str(val) for val in extracted_data.values()]
        print(f"\nValues:\n{values_lst}\n")

        longest_word = max(values_lst, key=lambda word: len(word))
        print(longest_word)


if __name__ == "__main__":
    task1()
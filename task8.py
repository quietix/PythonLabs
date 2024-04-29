from pprint import pprint

def task8(dicts: list[dict]):
    names = []

    for item in dicts:
        if item["status"]:
            names.append(item["name"])

    return names


if __name__ == "__main__":
    dict1 = {"status": True,
             "name": "Ivan"}
    dict2 = {"status": False,
             "name": "Artem"}
    dict3 = {"status": True,
             "name": "No name 1"}
    dict4 = {"status": False,
             "name": "No name 2"}

    dicts = [dict1, dict2, dict3, dict4]

    print("Dicts:")
    pprint(dicts)

    names = task8(dicts)

    print(f"\nNames:\n{names}")

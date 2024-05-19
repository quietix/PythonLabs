from numbers import Number

class Account:
    def __init__(self, owner_name, owner_surname="", balance: Number=0):
        self.owner_name = owner_name
        self.owner_surname = owner_surname
        self._balance = balance

    def get_balance(self):
        return self._balance

    def __str__(self):
        return f"Account properties: {self.owner_name} {self.owner_surname}"


if __name__ == "__main__":
    acc = Account("Ivan", balance=500.5)
    print(acc)
    print(acc.get_balance())
class Good:
    def __init__(self, amount: int, limit: int):
        self.amount = amount
        self.limit = limit

    def check_amount(self):
        if self.amount < self.limit:
            print(f"Need to deliver more {self.__class__.__name__}")
        else:
            print(f"{self.__class__.__name__} is all good. No need in more amount.")

    def deliver_items(self, items_num: int):
        self.amount += items_num
        return f"Successfully delivered {items_num} items. Total is {self.amount}"

    def sell_items(self, amount: int):
        if self.amount >= amount:
            self.amount -= amount
            print(f"{self.__class__.__name__} amount is successfully reduced. Current amount is {self.amount}")
            self.check_amount()
        else:
            print(f"There is no such amount of {self.__class__.__name__}.")

    def show_amount(self):
        print(f"Amount of {self.__class__.__name__} is {self.amount}.")

    def change_limit(self, new_limit: int):
        self.limit = new_limit
        print(f"New {self.__class__.__name__} limit is {self.limit}")

    def __str__(self):
        return f"I'm {self.__class__.__name__} in amount of {self.amount} with limit {self.limit}."


class Electronics(Good):
    pass


class Clothes(Good):
    pass


class Food(Good):
    pass


if __name__ == "__main__":
    is_running = True
    g = None

    goods_type = input("Enter goods' type (<e> for Electronics, <c> for Clothes, <f> for Food): ")
    if goods_type == "e":
        g = Electronics(100, 50)
        print(g, end="\n\n")
    elif goods_type == "c":
        g = Clothes(500, 100)
        print(g, end="\n\n")
    elif goods_type == "f":
        g = Food(150, 40)
        print(g, end="\n\n")
    else:
        print("No such option, terminating...")
        raise Exception("Termination.")

    while is_running:
        action = input("Choose action (1 - show current amount, 2 - check amount, 3 - deliver items, "
                       "4 - sell items, 5 - change limit. To exit enter <q>): ")
        if action == "1":
            g.show_amount()
        elif action == "2":
            g.check_amount()
        elif action == "3":
            g.deliver_items(int(input("How many items you want to deliver? ")))
        elif action == "4":
            g.sell_items(int(input("How many items you want to sell? ")))
        elif action == "5":
            g.change_limit(int(input("Enter new limit ")))
        elif action == "q":
            print("Quitting...")
            is_running = False
            continue
        else:
            print("There's no such option, try again...")

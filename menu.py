class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingridients = {
            "water": water, 
            "milk": milk, 
            "coffee": coffee, 
        }

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=38000),
            MenuItem(name="espresso", water=200, milk=0, coffee=24, cost=20000),
            MenuItem(name="luwak", water=200, milk=150, coffee=24, cost=50000),
        ]

    def get_items(self):
        option = ""
        for item in self.menu:
            option += f"{item.name}/"
        return option
    
    def find_drinks(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("sorry oput of stock..")
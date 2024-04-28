class CoffeeMaker:
    def __init__(self):
        self.recources = {
            "water": 1000,
            "milk": 500, 
            "coffee": 250,
        }

    def report(self):
        print(f"water: {self.recources['water']}ml")
        print(f"milk: {self.recources['milk']}ml")
        print(f"coffee: {self.recources['coffee']}g")

    def is_ingridient_sufficient(self, drink):
        can_make = True
        for item in drink.ingridients:
            if drink.ingridients[item] > self.recources[item]:
                print(f"sorry, insufficient {item}.")
                can_make = False
        return can_make
    
    def make_coffee(self, order):
        for item in order.ingridients:
            self.recources[item] -= order.ingridients[item]
        print(f"here's you {order.name}. enjoy!")
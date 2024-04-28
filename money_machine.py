class MoneyMachine:

    currency = "Rp."

    currency_value = {
        "lima ribuan": 5000, 
        "sepuluh ribuan": 10000,
        "limapuluh ribuan": 50000,
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: {self.currency}{self.profit}")

    def process_coins(self):
        print("please insert your money.")
        for money in self.currency_value:
            self.money_received += int(input(f"how much {money}?: ")) * self.currency_value[money]
        return self.money_received
    
    def make_payment(self, cost):
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"here's your {self.currency}{change} change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("not enough money. here's the refund.")
            self.money_received = 0
            return False
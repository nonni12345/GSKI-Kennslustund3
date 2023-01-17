class Pizza:
    def __init__(self, toppings = [], served = False) -> None:
        self.toppings = toppings
        self.served = served

    def add_toppings(self):
        self.toppings.append("Pepperoni")
        return self.toppings
    
    def serve(self):
        self.served = True

    def __str__(self) -> str:
        rtrnStr = ""
        for i in self.toppings:
            rtrnStr += i

        return f"{self.toppings}\n{self.served}"

pizza = Pizza
print(pizza)
pizza.add_toppings()
pizza.serve()
print(pizza)
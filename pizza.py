
class Pizza:

    def __init__(self, id, toppings = [], served = False) -> None:

        self.id = id
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

class Pizzas:

    def __init__(self, pizzas = []) -> None:
        self.pizzas = pizzas


    def add_pizza(self, topping1, topping2=None, topping3=None):
        pizzaid = self.__get_id()
        toppings = [topping1]
        if topping2 != None:
            toppings.append(topping2)
        if topping3 != None:
            toppings.append(topping3)
        pizza = Pizza(id,toppings)
        self.pizzas.append(pizza)


    def __get_id(self):
        return len(self.pizzas)+1




# pizza = Pizza(1, ["pepperoni"])


# pizza.__geti
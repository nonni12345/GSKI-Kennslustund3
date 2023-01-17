
class Pizza:

    def __init__(self, id: int, toppings: list = [], served: bool = False) -> None:

        self.id = id
        self.toppings = toppings
        self.served = served

    def add_toppings(self, *toppings):
        for topping in toppings:
            self.toppings.append(topping)

    def serve(self):
        self.served = True


    def __str__(self) -> str:
        rtrnStr = ""
        for i in self.toppings:
            rtrnStr += i

        return f"{' '.join([str(x) for x in self.toppings])} Served: {self.served}"

class Pizzas:

    def __init__(self, pizzas = []) -> None:
        self.pizzas = pizzas
        self.allowed_toppings = ["Cheese","Pepperoni", "Mushroom", "Sausage", "Onions", "Peppers", "Olives", "Anchovies", "Tomato sauce", "Cheese", "Spinach", "Pineapple", "Ham", "Bacon", "Beef", "Chicken", "Tomatoes", "Jalapeños", "Feta cheese", "Artichokes", "Pesto sauce", "Barbecue sauce", "Garlic", "Basil", "Oregano"] # Generated py ChatGPT (OpenAI)


    def __validate_topping(self,topping):
        try:
            if topping.capitalize() in self.allowed_toppings:
                    return True
            raise ValueError
        except AttributeError:
            raise ValueError


    def __str__(self) -> str:
        output = ""
        for pizza in self.pizzas:
            output += f"{pizza}\n"
        
        return output


    def add_pizza(self, topping1: str, topping2: str | None=None, topping3: str | None = None):
        pizzaid = self.__get_id()
        toppings = []
        if self.__validate_topping(topping1):
            toppings.append(topping1)
        if topping2 != None:
            if self.__validate_topping(topping2):
                    toppings.append(topping2)
        if topping3 != None:
            if self.__validate_topping(topping3):
                    toppings.append(topping3)

    
        pizza = Pizza(pizzaid,toppings)
        self.pizzas.append(pizza)


    def __get_id(self):
        return len(self.pizzas)+1




pizzas = Pizzas()
pizzas.add_pizza("Pepperoni","Cheese","Ham")
pizzas.add_pizza("Pepperoni","S","Ham","A)


print(pizzas)
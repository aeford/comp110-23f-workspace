"""Defining a class!"""

from __future__ import annotations

class Pizza:

    #attributes
    #think of these as variable each instance of my class will have
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, inp_size: str, inp_toppings: int, inp_gluten_free: bool):
        """My constructor."""
        self.size = inp_size
        self.toppings = inp_toppings
        self.gluten_free = inp_gluten_free
        # returns a Pizza object

    def price(self) -> float:
        """method to calculate price of pizza."""
        if self.size == "large":
            price: float = 6.25
        else:
            price: float = 5.00
        price += .75 * self.toppings
        if self.gluten_free:
            price += 1.00
        return price
    
    def add_toppings(self, num_toppings: int):
        """Method to add toppings to existing pizza"""
        self.toppings += num_toppings

    def make_new_pizza_and_add_toppings(self, num_toppings: int) -> Pizza:
        """make a new pizza with existing properties and add toppings"""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza
    
    def __str__(self) -> str:
        pizza_info: str = f"PIZZA ORDER: size {self.size}, toppings: {self.toppings}, GF: {self.gluten_free}"
        return pizza_info


my_pizza: Pizza = Pizza("medium", 2, False)
print(my_pizza)
sals_pizza: Pizza = Pizza("large", 1, True)
print(sals_pizza)
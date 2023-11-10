"""Instantiating a Class."""

#import the class
from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("large", 10, True) #constructor
#accessing/setting attributes
my_pizza.toppings = 10
my_pizza.gluten_free = True

#printing out some values
print("my_pizza: ")
print(my_pizza)

print("Pizza: ")
print(Pizza)

print("Size attribute: ")
print(my_pizza.size)

print("Toppings: ")
print(my_pizza.toppings)


#creating a new pizza
sals_pizza: Pizza = Pizza("medium", 5, False)
print(sals_pizza.size)


#function that calculates price
def price(input_pizza: Pizza) -> float:
    """Calculate price of pizza."""
    if input_pizza.size == "large":
        price: float = 6.25
    else:
        price: float = 5.00
    price += .75 * input_pizza.toppings
    if input_pizza.gluten_free:
        price += 1.00
    return price

#calling price function
print(price(sals_pizza))
print(price(my_pizza))

#calling price method
print(sals_pizza.price())
print(my_pizza.price())

my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())

my_other_pizza: Pizza = my_pizza.make_new_pizza_and_add_toppings(2)
print(my_other_pizza.toppings)
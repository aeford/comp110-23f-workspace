"""Practice with Dictionaries."""

#Constructing a dictionary
ice_cream: dict[str, float] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Made my dictionary.")
print(ice_cream)

#adding to the dictionary
ice_cream["mint"] = 3
print("After adding mint:")
print(ice_cream)

#removing from the dictionary
ice_cream.pop("mint")
print("After removing mint:")
print(ice_cream)

#printing orders of chocolate
print(f"There are {ice_cream['chocolate']} orders of chocolate.")

#increase a value
ice_cream["vanilla"] = 10
print("After adjusting amount of vanilla:")
print(ice_cream)

#length of dictionary
print(f"There are {len(ice_cream)} key value pairs in my dictionary.")

#check if key in dictionary
print("Is chocolate in ice_cream?")
print("chocolate" in ice_cream)
print("Is mint in ice_cream?")
print("mint" in ice_cream)

#Loops through and print out every flavor and its number of orders
for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders.")

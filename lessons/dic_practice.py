"""Dictionary practice."""

#Constructing a dictionary
ice_cream: dict[str,int] = {"chocolate":12, "vanilla":8, "strawberry":5}

print("Made my dictionary.")
print(ice_cream)

#Adding a key, value pair to a dictionary
ice_cream["mint"] = 3

print("After adding mint:")
print(ice_cream)

#Removing a key, value pair to a dictionary
ice_cream.pop("mint")

print("After removing mint:")
print(ice_cream)

#Printing out how many value a specific key
print(f"There are {ice_cream['chocolate']} orders of chocolate.")

#Modify value of a specific key
ice_cream["vanilla"] = 10

print("After changing vanilla:")
print(ice_cream)

#Printing out how many key value pairs in the dictionary
print(f"The number of key value pairs: {len(ice_cream)}")

#Find out if a specific key is in the dictionary
print("is chocolate in ice_cream?")
print("chocolate" in ice_cream)
print("is mint in ice_cream?")
print("mint" in ice_cream)

#Conditional 
if "mint" in ice_cream:
    print(f"Number of order: {ice_cream('mint')}")
else:
    print("No orders of mint")

#Loop through and print out every flavor and its number of orders 
for key in ice_cream:
    #print <flavor> has <number of orders> orders"
    print(f"{key} has {ice_cream[key]} orders.")
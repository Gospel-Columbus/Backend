# creating a set in python

fruits = {"orange","pineapple","mango","pawpaw"}

for x in fruits:
	print(x)

print(len(fruits))


# using set constructor.
animals = (("lion","tiger","leopard","cheetah"))

for x in animals:
	print(x)

print(len(animals))


# set method 

fruits.add("banana")
print(fruits)


fruits.update(["guava","kiwi"])
print(fruits)


fruits.remove("orange")
print(fruits)


fruits.clear()
print(fruits)


del animals
print(animals)
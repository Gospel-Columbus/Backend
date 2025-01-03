animals = ["bear","tiger","lion","panda","elephant"]

#for x in animals:
    #print(x)


#print(animals[0])
#print(animals[-1])
#print(animals[1:3])
animals[0] = "dog"
print(animals)
print(len(animals))


''' 
# list constructor in python 
countries = list(("United Kingdom", 2 , True, "Australia","New Zealand"))
print(countries)

'''


#list method in python

fruits = ["orange","pineapple","banana","pawpaw"] 
# creating a list with python.
vegetables = ["kale","lettuce","cucumber"] 
# creating a list in python


# extending a list in python.
fruits.extend(vegetables)
print(fruits)

# appending a list in python
vegetables.append("water leaf")
print(vegetables)

#sorting a reverse list in python
fruits.sort(reverse=True)
print(fruits)


#counting a value in python list
print(fruits.count("orange"))


#checking value index in python list
print(fruits.index("banana"))


fruits.insert(1, "apple")
print(fruits)


fruits.pop()
print(fruits)


fruits.remove("orange")
print(fruits)


del fruits
print(fruits)
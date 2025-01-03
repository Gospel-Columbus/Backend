# creating a dictionary with python

person = {
    
    "name":"gospel",
    "surname":"columbus",
    "age":21
    }

for x in person:
    print(x)

print(person)
print(len(person))

#creating a dictionary constructor in python
automobile = dict (motorcar = "benz", motorcycle = "suzuki")
print(automobile)



#changing a value in python dictionary.
person["age"] = 22
print(person)


#using get method in python dictionary
print(person.get("surname"))


#using update method in python dictionary
person.update({"sex":"male"})
print(person)


#using keys method in python dictionary
a = person.keys()
print(a)


#using pop method in python dictionary
person.pop("age")
print(person)


#using clear method in python dictionary
person.clear()
print(person)


#using del method in python
#del person
#print(person)


#using a list in dictionary
my_dict = {
    'name':'Tim',
    'nationality':'African',
    'Qualification':'College',
    'friends':['lekan','israel','webcrawler']
    }
    
print(my_dict)
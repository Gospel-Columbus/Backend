#class 1
class Myclass:
    x = 5


#Instantiating
p1 = Myclass()
print(p1.x)



# class 2
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

#Instantiating 
p1 = Person('John', 87)

#Accessing the Attribute
print(p1.name)
print(p1.age)





#using a class with the input function. 3
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
name = input('Enter your name: ')
age = input('Enter your age: ')

p1 = Person(name, age)
print(p1.name)
print(p1.age)




#deleting an object in class

class Person:
    
    def __init__(self, name, age):
        
        self.name = name
        self.age = age


#Instantiating 
p1 = Person('John', 87)

#Accessing an Attribute
#print(p1.name)
#print(p1.age)

del p1

print(p1)
# function 1 
def greetings_function():
    print('Welcome')
greetings_function()



# function 2 
def greetings_function(name):
    print('Welcome' + name)
greetings_function('Gospel')




# function 3 
def greetings_function(name):
    
    print('Welcome ' + str(name))
    
greetings_function(34)




# function 4 
def greetings_function(name, age):
    
    print('Welcome ' + name + '. You are '+ str(age) + ' years old.')
    
greetings_function('John',27)



#function 5
def greetings_function(*names):
    
    print('Welcome ' + names[0])
    
greetings_function('John','Tim','Tom')




#function 6
def greetings_function(name, age):
    
    print('Welcome ' + name + '. You are '+ str(age) + ' years old.')
    
name = input('Enter your name: ')

age = input('Enter your age: ')

greetings_function(name,age)




#function 7
def my_function():
    return 5 + 4
    
print(my_function())



#function 8 
def add_numbers(num1, num2):
    
    return num1+num2
    
print(add_numbers(2, 3))



#function 9
def add_numbers(num1, num2):
    return num1+num2
num1 = int(input('Enter first number: '))

num2 = int(input('Enter second number:'))

print(add_numbers(num1, num2))
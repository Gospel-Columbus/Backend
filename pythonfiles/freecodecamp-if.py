
# if statement 1
a = False
b = 5


if a == True:
    print('A is true')
    
elif a != False:
    print('A is false')
    
elif a == 'Hey':
    print('Hey is not equals to a')
    
else:
    print('the condtions are not true')
  



# if statement 2 is a string 

value = input('Input a value: ')

if type(value) == str:
    
    print(value + ' is a string')
    
else:  
    print(value, 'is not a string ')






# if statement 3 is not a string 

value = int(input('Input a value: '))

if type(value) == str:
    
    print(value + ' is a string')
    
else:  
    print(value, 'is not a string ')




# if statement 4 
#This program checks if a number can be divided by 5

value = int(input('Input a value: '))

if value%5 == 0:
    print(value,' can be divide by 5')
    
else:
        print(value, 'can not be divided by 5')
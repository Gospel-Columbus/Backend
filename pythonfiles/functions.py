def sum(x,y):
	print(x + y)

#calling a function.
sum(4,5)



#using python return keyword value.
def sum(x,y):
    return x + y
print(sum(4,5))
print(sum(8,4))



#Using Default Parameter Value.
#Bluelime is a default parameter value.
def student_names(names="Bluelime"):
	print("Hello " + names)

#calling a function.
student_names()
student_names("John")
student_names("Jane")



#Using Keyword Arguments 
def more_num(a,b=7,c=10 ):
	print("a is ",a, "and b is ",b,"while c is ",c )

more_num(3,7)
more_num(23, c=17)
more_num(c=40, a=80)




#Assigning functions to variables
def mynum(x):
	return x + 1
num = mynum
#calling a function
print(num(7))
print(mynum(8))





#Global and Local Variable Scopes
#global variable
x = 10
def my_numbers():
    global x
    print(x)
    #local variable
    x = 7
    print("My fav number is ", x)

my_numbers()
print(x)




#Using  function pass keyword
def dream_home():
    pass



#Using VarArgs Parameter
def total_numbers(a=7, *numbers,**phonebook):
    print("My fav number is ", a)
    for num in numbers:
        print("num", num)

    for name,phone_number in phonebook.items():
        print(name,phone_number)

total_numbers(7,1,2,3,Jane=2222,John=4444,Angela=5555)



#Using  anonymous functions 1
a = lambda b: b + 4
print(a(4))


#Using anonymous functions 2
c = lambda d,e : d + e
print(c(7,8))


#Using anonymous functions 3
def ghost_number(n):
    return lambda f: f * n
double_num = ghost_number(2)
print(double_num(20))

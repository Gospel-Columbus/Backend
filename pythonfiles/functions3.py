#Using pass functions as arguments 
def mynum(b):
	return b + 1 

def addnum(c):
	newnum = 7
	return c(newnum) 

print(addnum(mynum))




#Using Python DocStrings
def add_numbers(d,e):
    ''' Adding two numbers.

    The values must be intergers'''
    print(d + e)

add_numbers(8,4)
print(add_numbers.__doc__)
#Implementing basic exception handling 1
#print(x)
x = 20
try:
    print(x)
except:
    print("Variable is not defined.")
else:
    print("Hello")

finally:
    print("You may get and error if no variable is specified")







#Implementing basic exception handling 2
#b = "Hello"

#print(int(b))

while True:
    try:
        n = int(input("Enter a whole number: "))
        break
    except ValueError:
        print("No valid integer entered")

print("Great you have entered an integer")





#Implementing basic exception handling 3
try:
    n = 12/ int(input("Enter a whole number: "))
    print("The value of your number is ", n)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
finally:
    print("Hope you entered a valid whole number.")




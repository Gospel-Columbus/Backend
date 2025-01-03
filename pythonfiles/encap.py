#encapsulate the methods and variables
class Cars:
	def __init__(self,speed,color):
		# Two underscore for encapsulating the variable 
		self.__speed = speed 
		self.__color = color 

	def set_speed(self,value):
		self.__speed = value

	def get_speed(self):
		return self.__speed


#Instantiating 
ford = Cars(250, "green")


#Instantiating 
nissan = Cars(300, "red")


#Instantiating
toyota = Cars(350, "blue")


#Accessing a method 
ford.set_speed(450)

#changing the Attribute 
ford.speed = 500 

#Accessing the method 
print(ford.get_speed())


#Accessing an Attribute
print(ford.color)
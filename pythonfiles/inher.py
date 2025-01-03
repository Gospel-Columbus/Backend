class Person:
	def __init__(self, fname,lname):
		self.firstname = fname
		self.lastname = lname

	#defining a method 
	def printname(self):
		print(self.firstname,self.lastname)


#instantiating 
florist = Person("Jane","Doe")


#Accessing a method
florist.printname()





#Inheritance
class Lawyers(Person):
	def __init__(self, fname, lname, casetype):
		self.firstname = fname 
		self.lastname = lname
		self.casetype = casetype

	#defining a method
	def printinfo(self):
		print(self.firstname,self.lastname,self.casetype)


#instantiating 
happy_lawyers = Lawyers("Jack","Smiley","criminal")



#Accessing a method 
happy_lawyers.printinfo()
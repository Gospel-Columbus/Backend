#creating a class 

class Instructors:
	companyName = "Bluelime"

	#defining a method 
	def __init__(self,course,duration):
		self.course = course
		self.duration = duration

	def printinfo(self):
		print("My Company name is ", Instructors.companyName)



#Instantiating a class 
elearning = Instructors("Python for beginners",7)

bls = Instructors("Django for beginners",8)


#changing the value of an Attribute
bls.course = "HTML for Beginners"


#Accessing a Method
bls.printinfo()



#Accessing an Attribute course
print(bls.course)

print(elearning.course)



#Accessing an Attribute duration
print(bls.duration)

print(elearning.duration)

'''
#Deleting an Attribute 
del bls.duration
print(bls.duration)

'''

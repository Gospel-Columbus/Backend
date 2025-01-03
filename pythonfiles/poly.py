#creating a basic polymorphic  print function

def addNumbers(a,b,c=1):
	return a + b + c

print(addNumbers(8,9))

print(addNumbers(8,9,4))



# creating a basic polymorphic class and method 

class UK():
	#creating a method 
	def capital_city(self):
		print("London is the capital of UK")

	def language(self):
		print("English is the primary language")


class Spain():
	#creating a method 
	def capital_city(self):
		print("Madrid is the capital of Spain")

	def language(self):
		print("Spanish is the primary language")




#Instantiating 
queen = UK()

#Accessing a method 
queen.capital_city()




#Instantiating 
zara = Spain()

#Accessing a method 
zara.capital_city()


#using for loop
for country in (queen,zara):
	country.capital_city()
	country.language()
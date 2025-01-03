#1 print each line

country_file = open('C:/Users/HP/Desktop/pythonfiles/countries.txt', 'r')

print(country_file.readline())

country_file.close()




# 2 print all the lines

country_file = open('C:/Users/HP/Desktop/pythonfiles/countries.txt', 'r')

print(country_file.readlines())

country_file.close()





# 3 accessing the index

country_file = open('C:/Users/HP/Desktop/pythonfiles/countries.txt', 'r')

print(country_file.readlines()[3])

country_file.close()





#4  using for loop in reading

country_file = open('C:/Users/HP/Desktop/pythonfiles/countries.txt', 'r')

for lines in (country_file.readlines()):
    print(lines)
    
country_file.close()


'''
# writing a file in python

country_file = open('C:/Users/HP/Desktop/pythonfiles/countries.txt', 'w')

country_file.write('This is the new way to build')

'''



#creating a new file in python

country_file = open('C:/Users/HP/Desktop/pythonfiles/newfile.txt', 'w')

country_file.write('This is the new way to build')





#moving the write up to a new line

country_file = open('C:/Users/HP/Desktop/pythonfiles/countries.txt', 'w')

country_file.write('\nmy name is gospel columbus')
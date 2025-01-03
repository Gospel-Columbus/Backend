# using nested list.
fruits = [
    ["apple", "berries", "kiwi"],
    ["oranges", "berries", "plums"],
    ["mangoes", "bananas", "coconuts"],
    ["pineapples"]
]

print(fruits[0][2]) #kiwi is column 0 and row 2

for row in fruits:
    for col in row:
            print(col)

for x in fruits:
    
    print(x)






    
#Nesting 2dlist with numbers

number_grid = [
    
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
    
]

print(number_grid[2][1])

#Nested for loop
for row in number_grid:
    
    for col in row:
        
     print(col)
     
     
#for row in number_grid:
#print(row)

#list comprehension offers a shorteer syntax when you want to create a new list based on the values of an existing list

# syntax:
#     newlist = [ expression(element) for element in oldlist if condition]
    
#     List comprehension is a powerful tool in Python for creating lists in a readable and efficient manner.
# It combines iteration, optional filtering, and transformation into a single concise statement.
# It can improve code readability and performance when used appropriately.

numbers = [1, 2, 3, 4, 5]
doubled = [number * 2 for number in numbers]

print(doubled)  # Output: [2, 4, 6, 8, 10]


a = [1,2,3]
b = [n*n for n in a]
print(b)

a = [1,2,3,1001,132,7,3.6]
b = [n for n in range(10) if n<5]
print(b)

b = [x for x in range(1,21) if x%2 ==0]
print(b)








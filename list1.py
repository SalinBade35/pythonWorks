# #removing elements/ specified items from list
# f = [1,2,7,2,2,3,4,5,6,7,8]
# f.remove(1)  # removes no duplication/ like terms but only the first occurence
# print(f)

# #f.remove(99) just shows the error
# print(f)

# #syntax:
# #       list_name.remove(item)


# for i in range(2, 4):   #removes 2, and 3
#     f.remove(i)
    
# print(f)

# list = [1,2,3,4,5,6,7,8,9,0]
# list.pop()
# print(list)
# list.pop()
# print(list)
# list.pop()
# print(list)
# list.pop()
# print(list)
# list.pop()
# print(list)
# list.pop()
# print(list)
# list.pop()
# print(list)
# list.pop()
# print(list)
# list.pop()
# print(list)
# list.pop()
# print(list)

# #syntax:
# #   list_name.pop(index_number)


# list111= [1,3,4,5,6,7,8]
# list111.pop(-1)

# print(list111)

# del list111[-1]

# print(list111)

# list7 = [1,2,3,4,56,7,8,9,77]
# list7.clear()
# print(list7)


# list7.append(12)
# print(list7)

# list7.insert(0,"Sampada")
# list7.insert(-1,"shrestha")
# list7.insert(-2,"fluffy")
# print(list7)

#List sort() method
# syntax:
#   LSIT_NAME.sort(reverse = Ture/False, key = myfun())


# list = ["A", "b" , "C", "D", "e"]
# list.sort()
# print(list)  # based on the ascii value the items are sorted

# list = ["A", "b" , "C", "D",3,2,1]
# print(list)

list= [ 3,2,1]
a = "python"
b = sorted(a)
print(b)
sorted_a = ''.join(sorted(a))  # Convert string to list, sort, and join back to string
print(sorted_a)  # Output: 'hnopty'


#print(list.sort())  #sort does not returns value so it shows none here
print(sorted(list))  #but sorted does returns value so it shows acutal values
print(list)


#sorted works for all strings, tuple, list, set, frozen set and so on 
#but the sort have the no ability to work with strings
 

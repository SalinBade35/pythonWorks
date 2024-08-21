a = "0123456789"
print(a[0:])
print(a[:0])   
print(a[-3:])
print(a[-3:0:-1]) 

print(a[2::2]) #2-2 ko gap ma auxa from second to last

#var[inital_value: last_value: interval]
#initial_value is included but 
#last_value is excluded
#interval can let it move forward and backwards


name = "Salin Bade"
name1 = " Varun, is, my, name, wanna, be, in, hall, of, fame"
print(name1.upper())
print(name1.capitalize())
print(name1.lower())

print(name1.replace("Varun", "Salin"))

#split 
a = " Data Science is my name "
print(a.split(",")) # split where it finds ,
print(a.split(" "))  #by default it splits where it sees whitespace
print(a.split())    #by default it splits where it sees whitespace
print(a.split("a")) # split where it finds a
print()

#loops


##Q1. let the user entre 3 number and find the largest and smallest amongst
a = int(input("entre number: "))
b = int(input("entre number: "))
c = int(input("entre number: "))

#for greatest
if(a>b and a>c):
    print(a, "is the greatest amongst the entred three ", a,b,c)
if(b>a and b>c):
    print(b, "is the greatest amongst the entred three ", a,b,c)
if(c>a and c>b):
    print(c, "is the greatest amongst the entred three ", a,b,c)

#for smallest
if(a<b and a<c):
    print(a, "is the smallest amongst the entred three ", a,b,c)
if(b<a and b<c):
    print(b, "is the smallest amongst the entred three ", a,b,c)
if(c<a and c<b):
    print(c, "is the smallest amongst the entred three ", a,b,c)
  
#odd even  
if(a%2 == 0):
    print(a, "is even")
else:
    print(a,"is odd")
if(b%2 == 0):
    print(b, "is even")
else:
    print(b,"is odd")
if(c%2 ==0):
    print(c, "is even")
else:
    print(c,"is odd")
    
#prime number:   
for i in range (2, a, 1):
    if(a == 1):
        print(a, "is a not a prime number")
        break;
    else:
        if(a % i  == 0):
            print(a, "is not a prime number")
            break
    
else:
    print(a, "is a prime number")
    
for i in range (2, b, 1):
    if(b == 1):
        print(b, "is a not a prime number")
        break;
    else:
        if(b % i  == 0):
            print(b, "is not a prime number")
            break
    
else:
    print(b, "is a prime number")
    
for i in range (2, c, 1):
    if(c == 1):
        print(c, "is a not a prime number")
        break;
    else:
        if(c % i  == 0):
            print(c, "is not a prime number")  
            break 
else:
    print(c, "is a prime number")


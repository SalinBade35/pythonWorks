def loop1():
    a = ['apple', 'banana', 'cherry', 'dragonFruit']
    #for i in range(0,len(a)):
        #print(f"a[{i}]: {a[i]}")
    

    for i, j in enumerate(a):
        print(f"a[{i}]: {j}")
        
def loop2():
    for i in range(15, 0, -3):
        print(i, end=" ")

#loop2()

def loop3():
    number = [x for x in range(11)]
    print(number)
#loop3()

def loop4():
    for i in range(0,10):
        for j in range(0, i):
            print("* ",end="")
        print()

loop4()
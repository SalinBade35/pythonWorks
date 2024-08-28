#match case

num = int(input("entre a number between 1 and 3:  "))

match num:
    case 1:
        print("one")
        
    case 2:
        print("two")
        
    case 3:
        print("three")
    
    #default case is written as _:  or other
    case other:
        print("number is not between 1 and 3")
    
    
    
    
# python match case with OR operator
def runMatch():
    num = int(input("Enter a number between 1 and 6: "))
    
    # match case
    match num:
        # pattern 1
        case 1 | 2:
            print("One or Two")
        # pattern 2
        case 3 | 4:
            print("Three or Four")
        # pattern 3
        case 5 | 6:
            print("Five or Six")
        # default pattern
        case _:
            print("Number not between 1 and 6")
            
runMatch()


# python match case with if condition
def runMatch():
    num = int(input("Enter a number: "))
    
    # match case
    match num:
        # pattern 1
        case num if num > 0:
            print("Positive")
        # pattern 2
        case num if num < 0:
            print("Negative")
        # default pattern
        case _:
            print("Zero")
            
runMatch()

# match case to check a character in a string
def runMatch():
    myStr = "Hello World"
     
    # match case
    match (myStr[6]):
        case "w":
            print("Case 1 matches")
        case "W":
            print("Case 2 matches")
        case _:
            print("Character not in the string")
            
runMatch()


# match case with python dictionaryu
def runMatch(dictionary):
    # match case
    match dictionary:
        # pattern 1
        case {"name": n, "age": a}:
            print(f"Name:{n}, Age:{a}\n")
        # pattern 2
        case {"name": n, "salary": s}:
            print(f"Name:{n}, Salary:{s}\n")
        # default pattern
        case _ :
            print("Data does not exist\n")

runMatch({"name": "Jay", "age": 24})
runMatch({"name": "Ed", "salary": 25000})
runMatch({"name": "Al", "age": 27})
runMatch({})

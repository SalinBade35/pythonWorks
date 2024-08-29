#wap to enter a number from user and print its individual digits on separate line

#this is my pagalpanti for solving this simple code in a long long complex manner hehaaaa

def main():
        def reverse1(num):
            rev = 0
            while num > 0:
                reminder = num % 10
                rev = (rev * 10) + reminder
                num = num // 10
            return rev



        def reverse2(num):
            rev = 0
            while num > 0:
                reminder = num % 10
                rev = (rev * 10) + reminder
                num = num // 10
            return str(rev)



        value = int(input("entre value: "))  #123

        var1 = reverse1(value)  #321

        var2 = (reverse2(var1))  #321  -> 123

        var3 = (var2)

        var4 = len(var3)

        for i in range(0,var4):
            print(f"{int(var3[i])}")
    
#main()



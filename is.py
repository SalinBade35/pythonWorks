x = 5
y = 5
z = x

print(x is z)
print(x is y)

a = ["apple", "banana"]
b = ["apple", "banana"]

print(a == b)
print(a is b) 

# == compares the value on the object
# is compares if the memory address is same or nor

print(6 & 3) # 6 and 3 is first converted to binary then it is added using and the result is in binary which is then converted to decimal which becomes 2

print(~3)

print(3 & 4)


# Output: 0
# Explanation:

# Binary representation of 3 is 0011
# Binary representation of 4 is 0100
# Bitwise AND: 0011 & 0100 results in 0000, which is 0 in decimal.
# print(~4)
# Output: -5
# Explanation:

# Binary representation of 4 is 0000 0100 (in 8 bits).
# Bitwise NOT flips the bits: 1111 1011.
# This is the two's complement representation of -5

print (8 >> 2)
print(4 >> 12)
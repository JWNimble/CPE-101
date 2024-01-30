"""Lab 1

CPE101

Sction 17

@author: Jack Forrester

"""

a = int(input("Enter a number: "))

print(((((a * 2) + 10) / 2) - a))

b1 = int(input("Enter a number: "))
b2 = int(input("Enter a number: "))
b3 = (b1 + b2)
b4 = (b2 + b3)
b5 = (b3 + b4)
b6 = (b4 + b5)
b7 = (b5 + b6)
b8 = (b6 + b7)
b9 = (b7 + b8)
b10 = (b8 + b9)

print(((b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9 + b10) / b7))

c1 = int(input("Enter a number: "))
n1 = (((c1 % 1000) % 100) % 10)
c2 = (((c1 // 1000) + ((c1 % 1000) - n1)) + (n1 * 1000))
c3 = ((max(c1, c2)) - (min(c1, c2)))
c4 = (c3 // 1000) 
c5 = ((c3 % 1000) // 100)
c6 = (((c3 % 1000) % 100) // 10)
c7 = (((c3 % 1000) % 100) % 10)
c8 = (c4 + c5 + c6 + c7)

print((c8 // 10) + (c8 % 10))

d1 = int(input("Enter a number: "))
d2 = (d1 / 7)
d3 = (d2 // 1)
d4 = (d2 % d3)
f1 = ((d4 * 10) // 1)
f2 = (((d4 * 10) % ((d4 * 10) // 1) * 10) // 1)
f3 = (((d4 * 100) % ((d4 * 100) // 1)  * 10) // 1)
f4 = (((d4 * 1000) % ((d4 * 1000) // 1) * 10) // 1)
f5 = (((d4 * 10000) % ((d4 * 10000) // 1) * 10) // 1)
f6 = (((d4 * 100000) % ((d4 * 100000) // 1) * 10) // 1)

print(f1 + f2 + f3 + f4 + f5 + f6)

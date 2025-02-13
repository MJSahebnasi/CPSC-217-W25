a = int(input("enter a side length: "))
b = int(input("enter a side length: "))
c = int(input("enter a side length: "))



# if a == b == c:
if a == b and b ==c:
    print("Equilateral")

if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("It's not a triangle!")


if (a == b and a != c) or (a == c and a != b) or (b == c and a != b):
# if (a == b) or (a == c) or (b == c): - not correct
    print("Isosceles")

if a != b and b != c and a != c:
    print("Scalene")

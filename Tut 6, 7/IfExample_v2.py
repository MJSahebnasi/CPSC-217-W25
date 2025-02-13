a = int(input("enter a side length: "))
b = int(input("enter a side length: "))
c = int(input("enter a side length: "))



# if a == b == c:
if a == b and b ==c:
    print("Equilateral")

triangle_validity_condition = (a + b <= c) or (a + c <= b) or (b + c <= a)
if triangle_validity_condition:
    print("It's not a triangle!")


if (not triangle_validity_condition) and ((a == b and a != c) or (a == c and a != b) or (b == c and a != b)):
# if (a == b) or (a == c) or (b == c): - not correct
    print("Isosceles")

if a != b and b != c and a != c:
    print("Scalene")

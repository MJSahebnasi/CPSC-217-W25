import math

num_books = int(input("type the number of books: "))
box_cap = int(input("type the box capacity: "))
print("you need this number of boxes: ")
print(math.ceil(num_books / box_cap))
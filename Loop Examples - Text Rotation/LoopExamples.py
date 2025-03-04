from SimpleGraphics import *

# rotate text
# text(100, 100, "hello")
# text(100, 100, "hello", ang=30)

# # 1 tree
# setColor("green")
# ellipse(0, 100, 150, 50)
# ellipse(40, 70, 70, 50)
#
# setColor("brown")
# rect(50, 120, 50, 100)

# how range works
# for i in range(5):
#     print(i)
# for i in range(2, 5):
#     print(i)

# # 5 trees
# for i in range(5):
#     margin = 160
#     setColor("green")
#     ellipse(0 + i * margin, 100, 150, 50)
#     ellipse(40 + i * margin, 70, 70, 50)
#
#     setColor("brown")
#     rect(50 + i * margin, 120, 50, 100)

# # n trees
# num_trees = int(input("number of trees: "))
# for i in range(num_trees):
#     margin = 160
#     setColor("green")
#     ellipse(0 + i * margin, 100, 150, 50)
#     ellipse(40 + i * margin, 70, 70, 50)
#
#     setColor("brown")
#     rect(50 + i * margin, 120, 50, 100)


# n trees, different rows, continuous

# answer = "y"
# y = 100
# while answer == "y":
#     num_trees = int(input("number of trees: "))
#     for counter1 in range(num_trees):
#         margin = 160
#         setColor("green")
#         ellipse(0 + counter1 * margin, y, 150, 50)
#         ellipse(40 + counter1 * margin, y - 30, 70, 50)
#
#         setColor("brown")
#         rect(50 + counter1 * margin, y + 20, 50, 100)
#         print("inside while")
#     answer = input("do you want to continue? (y/n)")
#     y = y + 150


# another nested loops ex
# for counter1 in range(1, 5):
#     for counter2 in range (1, 3):
#         # for k in range (10):
#             print(counter1 * counter2)

#  1 * 1
#  1 * 2
#  2 * 1
#  ...
# noOfrows = int(input(" enter the no of rows  "))
# noOfcol = noOfrows - 1

# for row in range(1, noOfrows):

#     for space in range(1, noOfcol):
#         print("-")

#     noOfcol = noOfcol - 1

#     for stars in range(1, row):
#         print("*")

#     print("\n")

rows = 5

# for i in range(5):
#     print('*' * i + ' ' * (len(range(5 - i))))

# print("\n")

# for i in range(5):
#     print('*' * i + ' ' * (len(range(5 - i))))
rows = 5
for i in range(5):
    print(' ' * (len(range(5 - i))) + '*' * i)

# for i in range(rows, 0, 1):
#     for j in range(0, i):
#         print("*", end='')

#     print("\r")
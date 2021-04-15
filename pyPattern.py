input = int(input("Enter number of rows:  "))

# for row in range(input):
#     print(' ' * (len(range(input - row))) + '*' * row)

# for row in range(input):
#     print('*' * (len(range(input - row))) + ' ' * row)

# for row in range(0, input):
#     for col in range(0, row):
#         print("*", end=' ')

#     print('\n')

# for row in range(input):
#     print('*' * row + ' ' * (len(range(input - row))))

for num in range(10):
    for i in range(num):
        print(num, end='')
    print("\n")

# for num in range(10):
#     print(num + len(range(num)) * ' ')


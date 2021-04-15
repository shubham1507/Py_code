def linSearch(arr, x):

    for i in range(len(arr)):

        if arr[i] == x:

            return i

    return -1


# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = linSearch(arr, x)
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)

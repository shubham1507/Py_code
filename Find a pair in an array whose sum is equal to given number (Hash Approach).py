def PrintPair(arr, sum):

    s = set()

    for i in range(len(arr)):

        temp = sum - arr[i]

        if (temp in s):

            print("Pair with given sum " + str(sum) +
                  " is (" + str(arr[i]) + ", " + str(temp) + ")")

        s.add(arr[i])


A = [1, 4, 45, 6, 10, 8]
n = 16

PrintPair(A, n)


# Complexity Analysis:

# Time Complexity: O(n).
# As the whole array is needed to be traversed only once.
# Auxiliary Space: O(n).
# A hash map has been used to store array elements.


def getPrintPair(arr, sum):

    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == sum:
                return arr[i], arr[j]
    return -1



# Driver function
arr = [1, 5, 7, -1, 5]

sum = 6

print("Count of pairs is",
      getPrintPair(arr, sum))
 

def reveserArray(array, start, end):

    while start<end:

        array[start],array[end] = array[end],array[start]

        start+=1

        end-=1
    




# Driver array

print("Original array")

A = [1,2,3,4,5,6,7,8,9]

print(A)

print("Reveresed array")

reveserArray(A, 0,8)

print(A)
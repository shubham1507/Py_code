def BinsearchArrayByiter(arr, target):

    low = 0
    high = len(arr)-1
    mid = 0

    while low <= high:

        mid = (low + high)//2

        if target < arr[mid]:

            high = mid-1

        elif target > arr[mid]:

            low = mid+1

        else:

            return mid

    return -1


arr = [1, 2, 33, 44, 55, 66]

target = 44

result = BinsearchArrayByiter(arr, target)


if result != -1:
    print("element present at index " + str(result))

else:
    print("element not present at any index ")

""" Bubble Sort """

# the basic principle of bubble sorting is the 'swapping' of numbers
# 'swapping' of numbers uses greater or less than operands


def sort(arr):
    for i in range(len(arr)-1, 0, -1):  # controls the outer loop for number of element
        # -1 means the index starts at 0, so we're starting before the index
        for j in range(i):  # after each iteration a value is getting fixed
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


arr = [5, 3, 8, 6, 7, 2]
sort(arr)

print(arr)


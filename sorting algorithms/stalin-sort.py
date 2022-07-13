arr = [6, 3, 2, 4, 5, 6]


def stalin_sort(arr):
    num1 = arr[0]
    counter = 0
    for i in range(1, len(arr)):
        if num1 > arr[i - counter]:
            del arr[i - counter]
            counter += 1
        else:
            num1 = arr[i - counter]

    return arr


print(stalin_sort(arr))

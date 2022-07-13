arr = [6, 3, 2, 4, 5, 6]


def selection_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        num1 = arr[0]
        for b in arr:
            if b < num1:
                num1 = b
        sorted_arr.append(num1)
        del arr[arr.index(num1)]


print(selection_sort(arr))

arr = [6, 3, 2, 4, 5, 6]
swap = True
while swap:
    swap = False
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            swap = True
            arr[i], arr[i+1] = arr[i+1], arr[i]
print(arr)

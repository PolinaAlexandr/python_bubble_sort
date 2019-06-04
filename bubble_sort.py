arr = [12, 22, 4, 23, 13, 14, 2016]

def bubble_sort(arr):
    last_item = len(arr) - 1
    for i in range(0, last_item):
        for item in range(0, last_item-i):
            print(arr)
            if arr[item] > arr[item+1]:
                arr[item], arr[item +1] = arr[item+1], arr[item]

    return arr


print("Starter list:", arr)
new_arr = bubble_sort(arr).copy()
print("Sorted list:", new_arr)



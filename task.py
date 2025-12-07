def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

nums = [123, 53, 76, 12, 78, 34, 90, 112, 45, 67, 89, 101, 234, 345, 456, 567, 678, 789, 890, 901, 234, 345, 456, 567, 678, 789, 890, 901]
print(selection_sort(nums))
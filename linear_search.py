def linear_search(arr, n, s):  # Corrected function name
    for i in range(0, n):
        if arr[i] == s:
            return i
    return -1

arr = [-4, 5, 6, 7, 8, 9, 3, 4]
n = len(arr)
s = 9
index = linear_search(arr, n, s)  # Using corrected function name

if index == -1:
    print("Item not found")
else:
    print("Item found at index", index)  # Added output for found index

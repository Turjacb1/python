def binary_search(arr, item):

  low = 0
  high = len(arr) - 1
  mid = 0

  while low <= high:
    mid = (high + low) // 2  # Integer division for floor operation

    if arr[mid] == item:
      return mid
    elif arr[mid] < item:
      low = mid + 1
    else:
      high = mid - 1

  return -1  # Item not found

# Example usage
arr = [1, 2, 4, 5, 67, 89, 100]
item = 5

index = binary_search(arr, item)

if index != -1:
  print("Item found at index:", index)
else:
  print("Item not found")

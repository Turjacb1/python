def selection_sort(arr):


  n = len(arr)

  for i in range(n):
    min_index = i
    for j in range(i + 1, n):
      if arr[j] < arr[min_index]:
        min_index = j

    # Swap the found minimum element with the first element of the unsorted sub-array
    arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
arr = [5, 9, 2, 88, 67, 82]
selection_sort(arr)
print("Sorted array:", arr)

def bubble_sort(arr):


  n = len(arr)
  count=0
  # Traverse through all array elements
  for i in range(n - 1):
    # Last i elements are already in place
    for j in range(0, n - i - 1):
      
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        count=count+1  # Swap elements using tuple unpacking
        # Count the number of swaps for optimization (optional)
        # counter += 1  # Uncomment if you want to track swap count
    
# Example usage
arr = [5, 9, 2, 88, 67, 82]
bubble_sort(arr)

print("Sorted array:", arr)


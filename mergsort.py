def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves
    merge_sort(left_half)
    merge_sort(right_half)
    
    # Merge the sorted halves
    i = j = k = 0
    
    # Merge the left and right halves back into the original array
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    
    # Check if any elements were left in the left half
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    
    # Check if any elements were left in the right half
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# Main execution
queue = [40, 30, 20, 10]
print("Original queue:", queue)

merge_sort(queue)
print("Sorted queue:", queue)
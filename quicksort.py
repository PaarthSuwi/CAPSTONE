def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return quick_sort(left)+middle+quick_sort(right)
    
queue = [40,30,10,20]
print("original",queue)
q = quick_sort(queue)
print("sorted",q)
    
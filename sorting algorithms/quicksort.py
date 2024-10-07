def partition(arr, l, h):
    pivot = arr[l]
    i = l + 1
    j = h
    while True:
        # Find the first element greater than or equal to the pivot from the left
        while i <= h and arr[i] < pivot:
            i += 1
        # Find the first element smaller than or equal to the pivot from the right
        while j >= l and arr[j] > pivot:
            j -= 1
        # If indices crossed, partitioning is done
        if i >= j:
            break
        # Swap elements
        arr[i], arr[j] = arr[j], arr[i]
    
    # Swap the pivot with the element at j
    arr[l], arr[j] = arr[j], arr[l]
    return j

def quicksort(arr, l, h):
    if l < h:
        j = partition(arr, l, h)
        quicksort(arr, l, j - 1)
        quicksort(arr, j + 1, h)

def print_array(arr):
    for i in arr:
        print(i, end=" ")
    print()

if __name__ == "__main__":
    arr = [10, 16, 8, 12, 15, 6, 3, 9, 5]
    print("Given array is:", arr)
    quicksort(arr, 0, len(arr) - 1)
    print("Sorted array is:", end=" ")
    print_array(arr)

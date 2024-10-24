#bubble sort
def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

if __name__ == "__main__":
    arr = [34,65,90,112,3,6,7]

    bubbleSort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print(arr[i], end=" ")

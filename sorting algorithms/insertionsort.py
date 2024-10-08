# Python program for implementation of Insertion Sort

# Function to sort array using insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        #checking the position and inserting at the correct position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#printing the element
def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

#main method
if __name__ == "__main__":
    arr = [23,2,45,16,12,6]
    insertionSort(arr)
    printArray(arr)

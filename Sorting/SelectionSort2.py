'''
SELECTION SORT
'''
# Function to take array input
def inputArray():
    arr = list(map(int,input().split(" ")))
    return arr

# Selection Sort 
def selectionSort(arr):
    length = len(arr)
    for i in range(length-1):
        minIndex = i
        for j in range(i+1,length):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i],arr[minIndex] = arr[minIndex],arr[i]
    return arr

# Input
array = inputArray()
# Output
print(f"Input Array : {array}")
print(f"Sorted Array : {selectionSort(array)}\n")
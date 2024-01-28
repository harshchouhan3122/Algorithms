'''
BUBBLE SORT
0 5 3 7 2 6 1
Input Array :  [0, 5, 3, 7, 2, 6, 1]
Sorted Array : [0, 1, 2, 3, 5, 6, 7]
'''
# Function to take array input
def inputArray():
    arr = list(map(int,input().split(" ")))
    return arr

# Bubble Sort 
def bubbleSort(arr):
    length = len(arr)
    for i in range(length-1):
        for j in range(length-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]              
    return arr

# Input
array = inputArray()
# Output
print(f"Input Array : {array}")
print(f"Sorted Array : {bubbleSort(array)}\n")
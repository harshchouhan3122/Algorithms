'''
BUBBLE SORT
'''
# Function to take array input
def inputArray():
    arr = list(map(int,input().split(" ")))
    return arr

# Bubble Sort Explained
def bubbleSort(arr):
    length = len(arr)
    loop_count = 0
    for i in range(length-1):
        loop_count += 1
        print(f"\n---> Loop Count : {loop_count}")
        print(f"arr : {arr}")
        for j in range(length-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]              
        print(f"arr : {arr}     --> we got the largest {i+1} element at the end")
    return arr

# def bubbleSort(arr):
#     length = len(arr)
#     for i in range(length-1):
#         for j in range(length-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]              
#     return arr

# Input
array = inputArray()
# Output
print(f"Input Array : {array}")
print(f"\nSorted Array : {bubbleSort(array)}\n")
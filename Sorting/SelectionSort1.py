'''
SELECTION SORT
'''
# Function to take array input
def inputArray():
    arr = list(map(int,input().split(" ")))
    return arr

# Selection Sort Explained
def selectionSort(arr):
    print("\n********************************  SELECTION SORT  ********************************")
    loop_count = 0 
    for i in range(len(arr)):
        # we will find the minimum value of item everytime and swap it with arr[i] then agin doing this with i++
        loop_count += 1
        print(f"\n---> Loop count : {loop_count}")
        print(f"        arr : {arr}")

        min_idx = i
        max_idx = i
        min = arr[min_idx]
        max = arr[max_idx]
        # print(f"min = arr[{i}] = {arr[i]}")
        # print(f"index(min) = index(arr[{i}]) = index({min}) = {i}")
        print(f"        max = {arr[max_idx]}, min = {arr[min_idx]} and index(max) = {i}, index(min) = {i}")

        for j in range(i+1,len(arr)):
            if arr[j] < min :
                min = arr[j]
                max_idx = i
                min_idx = j
    
        print(f"        max = {arr[max_idx]}, min = {arr[min_idx]} and index(max) = {max_idx}, index(min) = {min_idx}      (after iterating j)")
        if max_idx == min_idx:
            break
        # Swap this two value in every iteration of i 
        print(f"        --> swap(arr[{max_idx}], arr[{min_idx}])  --> swap({arr[max_idx]},{arr[min_idx]})")
        temp1 = arr[max_idx]
        temp2 = arr[min_idx]
        arr.pop(min_idx)
        arr.insert(min_idx,temp1)
        arr.pop(max_idx)
        arr.insert(max_idx,temp2)
        print(f"        arr : {arr}")

    return arr

# function to sort the array using Selection Sort
# def selectionSort(arr):
#     for i in range(len(arr)-1):
#         min_idx = i
#         max_idx = i
#         min = arr[min_idx]
#         max = arr[max_idx]
#         for j in range(i+1,len(arr)):
#             if arr[j] < min :
#                 min = arr[j]
#                 max_idx = i
#                 min_idx = j
#         if max_idx == min_idx:
#             break
#         temp1 = arr[max_idx]
#         temp2 = arr[min_idx]
#         arr.pop(min_idx)
#         arr.insert(min_idx,temp1)
#         arr.pop(max_idx)
#         arr.insert(max_idx,temp2)
#     return arr

# Input
array = inputArray()
# Output
print(f"Input Array : {array}")
print(f"\nSorted Array : {selectionSort(array)}\n")
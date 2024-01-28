
# Taking sorted Array input
def inputArray():
    arr = list(map(int,input().split(" ")))
    arr.sort()
    return arr

# Merge two sorted arrays
def mergeTwoSortedArray(arr1,arr2):
    i = 0
    j = 0
    arr3 = []
    while(i<len(arr1) and j<len(arr2)):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1

    while(i<len(arr1)):
        arr3.append(arr1[i])
        i += 1
    while(j<len(arr2)):
        arr3.append(arr2[j])
        j += 1

    return arr3


# Input
# array1 = inputArray()
# array2 = inputArray()
array1 = [1,4,9,10]
array2 = [2,3,6,7,8]

# Output
print(mergeTwoSortedArray(array1,array2))
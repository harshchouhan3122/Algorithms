def insertionSort(arr):
    length = len(arr)
    for i in range(1,length):
        j = i-1
        # temp = arr[i] 
        while(j>=0 and arr[j] > arr[j+1]):
            arr[j+1],arr[j] = arr[j],arr[j+1]
            j = j-1             # Decrement j for the while loop
            
            # arr[j+1] = arr[j]
            # j = j-1             # Decrement j for the while loop
            # arr[j+1] = temp
    return arr

# Input
array = [1,5,3,7,2,6,0]
# Output
print(" Input Array :",array)
print("Sorted Array :",insertionSort(array))
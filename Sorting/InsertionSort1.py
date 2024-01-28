# Explained Insertion Sort
def insertionSort(arr):
    length = len(arr)
    loop_count = 0
    for i in range(1,length):
        loop_count += 1
        print(f"\nLoop Count : {loop_count}")

        print(f"arr = {arr}")
        j = i-1
        temp = arr[i]
        print(f"i={i}, j={j}, temp={temp}")
 
        while(j>=0 and arr[j] > temp):
            arr[j+1] = arr[j]
            print(f"arr[j] = arr[{j}] = {arr[j]},   arr[j+1] = arr[{j+1}] = {arr[j+1]},   j={j}")
            # j = j          # decrement j for while loop
            # arr[j] = temp
            j = j-1          # decrement j for while loop
            arr[j+1] = temp
            print(f"arr[j] = arr[{j}] = {arr[j]},   j={j}")
            print()
        print(f"arr = {arr}")
    print()
    return arr

# def insertionSort(arr):
#     length = len(arr)
#     for i in range(1,length):
#         j = i-1
#         temp = arr[i] 
#         while(j>=0 and arr[j] > temp):
#             arr[j+1] = arr[j]
#             j = j-1
#             arr[j+1] = temp
#     return arr

# Input
array = [1,5,3,7,2,6,0]
# Output
print(" Input Array :",array)
print("Sorted Array :",insertionSort(array))
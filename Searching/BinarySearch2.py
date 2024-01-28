'''
arr = 1 3 5 4 2 6 8 9
then, arr = 1 2 3 4 5 6 8 9   (sorted array for Binary Search)
Find the index of the element 9 in the given array using Binary Search
'''

def inputArray():
    array = list(map(int,input().split(" ")))         # Single Line Array Input
    return array


def BinarySearch(array,element):
    array.sort()                    # Binary Search works only on the sorted array
    s = 0
    e = len(array)-1
    mid = 0

    while(s<=e):                    # when s>e means no element found 
        mid = (s+e)//2

        if array[mid] == element:
            return ("Index of {} : {} ".format(element,mid))
            
        elif (array[mid] < element):        # Element lies on the right side of the mid element
            s = mid+1

        elif (array[mid] > element):        # Element lies on the left side of the mid element
            e = mid-1

    if s>e :
        return "Element not exist!"
    
# Input
array = inputArray()
element = int(input())

# Output
print(BinarySearch(array,element))
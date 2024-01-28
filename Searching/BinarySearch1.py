'''
arr = 1 3 5 4 2 6 8 9
then, arr = 1 2 3 4 5 6 8 9   (sorted array for Binary Search)
Find the index of the element 9 in the given array using Binary Search
'''

def inputArray():
    # size = int(input(" "))                              # New Line Array Element Input
    # array = []
    # for i in range(size):
    #     array.append(int(input()))
    array = list(map(int,input().split(" ")))         # Single Line Array Input
    return array


def BinarySearch(array,element):
    array.sort()                    # Binary Search works only on the sorted array
    print("Sorted Array :",array)
    index = []
    for i in range(len(array)):
        index.append(i)
    print("     Indexes :",index,"\n")

    # s = starting index and e = ending index
    s = 0
    e = len(array)-1
    mid = 0
    count = 0

    while(s<=e):                    # when s>e means no element found 
        count += 1
        print("Loop Count : ",count)
        mid = (s+e)//2
        print("s={}, e={}, mid={}".format(s,e,mid))

        if array[mid] == element:
            # return mid
            print("\nNo. of time loop executed in Binary Search : ",count)
            return ("For {} : Index={} and Position={}.".format(element,mid,mid+1))
        elif (array[mid] < element):        # Element lies on the right side of the mid element
            s = mid+1
        elif (array[mid] > element):        # Element lies on the left side of the mid element
            e = mid-1

        print("s={}, e={}, mid={}, element={}".format(s,e,mid,array[mid]))
        print()

    if s>e :
        print("\nNo. of time loop executed in Binary Search : ",count)
        return "Element not exist!"
    
# Input
array = inputArray()
element = int(input())

# Output
print(BinarySearch(array,element))
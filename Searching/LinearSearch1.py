'''
arr = 1 3 5 4 2 6 8 9 
Find the index of the element 9 in the given array using Linear Search
'''
def inputArray():
    # size = int(input(" "))                              # New Line Array Element Input
    # array = []
    # for i in range(size):
    #     array.append(int(input()))

    array = list(map(int,input().split(" ")))         # Single Line Array Input

    return array

def LinearSearch(array,element):
    count = 0
    for i in range(len(array)):
        count += 1
        if array[i] == element:
            print("\nNo. of time loop executed in Linear Search : ",count)
            return ("Index of {} : {}".format(element,i))
    print("\nNo. of time loop executed in Linear Search : ",count)
    return "Element not found!"

# Input
array = inputArray()
element = int(input())

# Output
print(LinearSearch(array,element))
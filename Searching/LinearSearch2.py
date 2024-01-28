'''
arr = 1 3 5 4 2 6 8 9 
Find the index of the element 9 in the given array using Linear Search
'''
def inputArray():
    array = list(map(int,input().split(" ")))         # Single Line Array Input
    return array

def LinearSearch(array,element):
    for i in range(len(array)):
        if array[i] == element:
            return ("Index of {} : {}".format(element,i))
    return "Element not found!"

# Input
array = inputArray()
element = int(input())      

# Output
print(LinearSearch(array,element))
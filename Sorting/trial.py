arr = [1,3,4]

for i in arr:
    index = arr.index(i)
    if arr[index+1] - arr[index] == 2:
        arr[index+1] = i+1
        break

print(arr)
#Range sum (basic list slicing)

arr = [1,2,3,4,5,6,7,8,9]
print(arr[0::])
print(arr[1::])
print(sum(arr[2:5]))
print(sum(arr[::-1]))
print(min(arr[2:5]))
print(max(arr[2:7]))



#Running sum array
arr = [1,2,3,4,5,6,7,8,9]
for i in range(1 ,len(arr)):
    arr[i] += arr[i-1]  
print(arr)
    


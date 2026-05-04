
#Given an array, reverse it in-place (no extra space)
import math as m
arr = [ 1,2,3,4,5,6,7,8]
left = 0
right= len(arr)-1
while left< right:
    arr[left],arr[right] = arr [right], arr[left]
    left +=1
    right -=1
print(arr)
print(arr[::-1])
arr.reverse()
print(arr)


#Move all zeros to the end (order maintain cheyyali)
arr = [1,0,8,6,4,0,8,6,4,0,5,9]
j =0
for i in range(len(arr)): 
    if arr[i] != 0:
        arr[i] , arr[j] = arr[j] , arr[i]
        j+=1
print(arr)


#Move all zeros to the end (order maintain cheyyali)
arr = [1,0,8,6,4,0,8,6,4,0,5,9]
j =-1
for i in range(len(arr)-1,-1,-1):
    if arr[i] != 0:
        arr[i] , arr[j] = arr[j] , arr[i]
        j-=1
print(arr) 


#Given sorted array, find if there exists a pair with sum = k
arr = [1,2,3,4,5,6,7,8,9]
k = 13
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == k :
            print(arr[i],arr[j])

print("\n--------------------")    

arr = [1,2,3,4,5,6,7,8,9]
k = 13
s = 0
left = 0
right = len(arr)-1
while left < right:
    s = arr[left] + arr[right]
    if s==k:
        print(arr[left],arr[right])
        left += 1
        right -=1
    elif s < k:
        left += 1
    else:
        right +=1

arr = [1,2,3,4,5,6,7,8]
k = 3
for i in range(k,len(arr)):
    s = m
    m = s

    if
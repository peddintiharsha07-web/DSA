#Reverse array
arr = [3,4,5,6,7,8,9,9]
arr.reverse()
print(arr)


arr = [3,4,5,6,7,8,9,9,8]
n = len(arr)
for i in range(n//2):
    arr[i] , arr[n-1-i] = arr[n-1-i] , arr[i]
print(arr)

arr = [3,4,5,6,7,8,9,9,8,6]
print(arr[::-1])


print("\n-----------")
#sum of all elements
arr = [3,4,5,6,7,8,9,9,8,6]
t = 0
for i in arr:
    t +=i
print("sum of all element",t)

print("\n-----------")
arr = [3,4,5,6,7,8]
print(sum(arr))
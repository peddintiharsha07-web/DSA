
#largest element
arr = [2,4,5,6,7,8,99,8,7,6,52,4,3]
print("largest element",max(arr))

k = arr[0]
for i in arr:
    if i > k:
        k = i
print("maximum eliment",k)

#smallest element
print("smallest element",min(arr)) 

s = arr[0]
for j in arr:
    if j < s:
        s = j
print(s)

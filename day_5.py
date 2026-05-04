



arr = [4,5,6,7,6,5,3,8,9,5]
t =14
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == t:
            print(arr[i], arr[j])

print("\n-----------------------------")
arr = [2,3,4,5,6,7,8,9]
tar = 14
left = 0
right = len(arr)-1

while left < right:
    s = arr[left] + arr[right]


    if s == tar:
        print(arr[left],arr[right])
        break
    if s<tar:
        left +=1
    else:
        right -=1
 

 # move the zero last
arr = [2,3,0,9,6,0,7,0,3,2,5,4]
j = 0
for i in range(len(arr)):
    if arr[i] !=0:  
        arr[i], arr[j] = arr[j], arr[i]
        j +=1
print(arr)


arr = [2,3,0,9,6,0,7,0,3,2,5,4]
k = []

for i in arr:
    if i not in k:
        k.append(i)
print(k)

arr = [2,3,0,9,6,0,7,0,3,2,5,4]
k = []
for i in arr:
    if i != k:
        k.append(i)
print(k)

print("\n-------------------------------")

arr = [2,3,4,0,9,8,0,1,2,0,7,5,4]
k = 0 
for i in range(len(arr)):
    if arr[i] !=0:
        arr[i],arr[k] = arr[k],arr[i]
        k +=1
print(arr) 

arr = [2,3,4,5,4,3,2,7,8,9,0,0,4,3,3]
k = list(set(arr))
print(k)
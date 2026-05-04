

arr = [2,3,4,5,6,7,8,9]
t = 6
found = False
for i in range(len(arr)):
    if arr[i] == t:
        print("the index value is ", i)
        found= True
        break
if found ==False:
    print("not found")


#Element exists or not

arr = [2,3,4,5,6,7,8,9]
target = 8
found = False
for i in range(len(arr)):
    if arr[i] ==  target:
        print("yes it was exists")
        found = True
        break
if found == False:
    print("it was not exits")

#Count occurrences
arr = [2,3,4,5,6,7,8,7,6,5,4,4,3,3,5]
t = 5
c = 0
for i in arr:
    if i == t:
        c +=1

print("the target number was",c,"times count")

#first occurance
arr = [2,3,4,5,6,7,8,6,5,4,7,4,3,3,5]
t =7
found = False
for i in range(len(arr)):
    if arr[i] ==t:
        print("first occurance",i)
        found = True
        break


print("\n----------------")
#last occurance
arr = [2,3,4,5,6,7,8,6,5,4,7,4,3,3,5]
t =7
found = False
for i in range(len(arr)):
    if arr[i] ==t:
        last = i
print("last occurance",last)
        
#Find index of element
arr = [2,3,4,5,6,7,8,6,5,4,7,4,3,3,5]
print("index element", arr[3])


#find index element
arr = [2,3,4,5,6,7,8,6,5,4,7,4,3,3,5]
index = 14
for i in range(len(arr)):
    if i == index:
        print(arr[i])
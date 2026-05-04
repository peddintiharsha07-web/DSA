#count even & odd numbers
arr = [2,3,4,5,6,7,8,9,7,6,5,4,9,9,1]
even = 0
odd =  0
for i in arr:
    if i % 2 == 0:
        even +=1
    else:
        odd +=1

print(even)
print(odd)


#brute force
arr = [2,6,7,3,4,5,6,7,8,9,7,6,5,4,9,9,1,13,12,18,10]

even = sum(1 for i in arr if i % 2 == 0)
odd = len(arr)-even
print("Even numbers",even)
print("odd:", odd)

#Count numbers > X
arr = [2,6,7,3,4,5,6,7,8,9,7,6,5,4,9,9,1,13,12,18,10]
t =10
r = 0
for i in arr:
    if i >= t:
        r +=1
print(r)
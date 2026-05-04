arr = [2,3,4,5,6,7,8,9]
k = 2

win = sum(arr[0:k])
s = win
for i in range(k , len(arr)):
    win += arr[i] - arr[i-k]
    s = max(win,s)
print(s)

arr = [2,3,4,5,6,7,8,9]
k = 2

win = sum(arr[0:k])
s = win
for i in range(k , len(arr)):
    win += arr[i] - arr[i-k]
    s = max(win,s)
print(s)

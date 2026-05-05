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


def containsDuplicate(nums):
    s = []
    for i in nums:
        if i in s:
            return True
        s.append(i)
    return False

nums = [1,2,3,4,5,3]
print(containsDuplicate(nums))
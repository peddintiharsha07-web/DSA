#contains duplicate in array
arr = [1,2,3,4,5,3]
s =set()
k = False
for i in arr:
    if i in s:
        k = True
        break
    s.add(i)
print(k)

#two sum
arr = [1, 2, 3, 4, 5, 6]
t = 9
seen = {}

found = False
pairs = []  # pairs store cheyyadaniki

for i, num in enumerate(arr):
    diff = t - num
    if diff in seen:
        pairs.append((diff, num))  # pair store
        found = True
    seen[num] = i

# Print results
if found:
    print("Pairs:")
    for a, b in pairs:
        print(a, "+", b, "=", t)
else:
    print("No pair found")

print("Two Sum exists:", found)

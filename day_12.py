#longest common prefix

arr= ["green", "grape","ground", "gride", "greenhouse"]
res = ""
for i in range(len(arr[0])):
    c = arr[0][i]
    for j in range(1, len(arr)):
        if i == len(arr[j]) or arr[j][i] != c:
            print(res)
            exit(0)
    res += c    
print(res)      
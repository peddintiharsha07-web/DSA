
arr = input("Enter the pheranthis: ")
while "()" in arr or "{}" in arr or "[]" in arr:
    arr = arr.replace("()", " ")
    arr = arr.replace("{}", " ")
    arr = arr.replace("[]", " ")

if arr == " ":
    print("Valid")
else:
    print("not valid")


#second largest
arr = [3,4,55,6,7,8,8,22,9,33,77]

first = 0
sec = -1
for i in arr:
    if i > first:
        sec = first
        first = i

    elif i > sec and i != first:
        sec = i
print(sec)

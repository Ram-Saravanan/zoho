num = [1,2,3,4,5,6,6,5,4]
arr = []

for i in num:
    if i not in arr:
        arr.append(i)
print(arr)
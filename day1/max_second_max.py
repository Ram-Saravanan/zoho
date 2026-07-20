a = [1,2,34,5,666,4343,3,455]

max = float('-inf')
sec = float('-inf')

for i in range(len(a)):
    if a[i]>max:
        sec = max
        max = a[i]
    elif a[i]>sec and a[i]!=max:
        sec = a[i]

print(max)
print(sec)
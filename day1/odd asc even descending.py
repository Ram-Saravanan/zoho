a = [1,2,3,4,5,6,7,8,9]

l = 0

for r in range(len(a)):
    if a[r]%2!=0:
        a[l],a[r] = a[r],a[l]
        l += 1
print(a)
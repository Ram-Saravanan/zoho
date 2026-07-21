a = [1,24,7,4,3,2,9,8]

a.sort()

b = []

for i in range(1,len(a)-1):
    if a[i+1] == a[i]+1:
        b.append(i)

print(b)        
 
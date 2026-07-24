a = [2,4,5,0,0,5,6,7,4]

for i in range(len(a)-1):
    
    for j in range(i+1, len(a)):

        if (a[j] == 0):
            continue

        if(a[i] == a[j]):
            a[i] *= 2
            a[j] = 0

        break    

print(a)        
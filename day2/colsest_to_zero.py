a = [8,4,5,6,2,1]
b = 0
min = float('inf')
ind1, ind2 = 0, 0

for i in range(len(a)):
    for j in range(i+1,len(a)):

        b = abs(a[i] + a[j])

        if(b<min):
            min = b
            ind1 = i
            ind2 = j

print(a[ind1], a[ind2])
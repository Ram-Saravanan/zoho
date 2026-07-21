a = [1,2,3,6,7,8,9,20,21]

a.sort()

current = [a[0]]
longest = [a[0]]

for i in range(1,len(a)):
    if(a[i] == a[i-1]+1):
        current.append(a[i])

    else:
        if(len(current)>len(longest)):
            longest = current[:]
        current = [a[i]]

if(len(current)>len(longest)):
    longest = current[:]

print(longest)                
a = [1,2,3,4,5,6,7,8,9]

odd = []
even = []

for i in a:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

odd.sort()
even.sort(reverse=True)

print (odd + even)


## two pointer
# a = [1,2,3,4,5,6,7,8,9]
# l = 0

# for r in range(len(a)):
#     if a[r]%2!=0:
#         a[l],a[r] = a[r],a[l]
#         l += 1

# odd = sorted(a[:l])
# even = sorted(a[l:], reverse= True)

# print(odd + even)
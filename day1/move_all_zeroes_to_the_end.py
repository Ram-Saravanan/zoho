# REAL ACTUAL

a = [12,3,4,5,5,6,0,0,8,0,0,0,6,4]

l = 0

for r in range(len(a)):
    if a[r] != 0:
        a[r], a[l] = a[l],a[r]
        l += 1

print(a)        


## bruteforce
# a = [12,3,4,5,5,6,0,0,8,0,0,0,6,4]
# arr = []
# count = 0

# for i in a:
#     if(i != 0):
#         arr.append(i)
#     else:
#         count += 1    

# for i in range(count):
#     arr.append(0)    

# print(arr)    
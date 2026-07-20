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

## actual
# a = [12,3,4,5,5,6,0,0,8,0,0,0,6,4]

# for i in range(len(a)):
#     if a[i] == 0:
#         for j in range(i,len(a)-2):
#             a[j] = a[j+1]
#     a[len(a)-1] = 0 
# print(a)
# for i in range(0,len(a)):
#     if a[i]==0:
#         for j in range(i,len(a)-1):
#             a[j] = a[j+1]
#         a[len(a)-1]=0
#     if a[i]==0:
#         i-=1
# print(a)
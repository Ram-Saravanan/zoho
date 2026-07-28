a = ["tea", "eat", "ate", "met"]

fre = {}

status = False

for i in a:
    if i not in fre:
        fre[i] = 1
    else:
        fre[i] += 1  

for j in b:
    if j in fre:
        status = True
    else:
        status = False
        break    

print(status)
a = "hello world"
b = "world"

exist = False

for i in range(len(a) - len(b) + 1):
    match = True
    for j in range(len(b)):
        if(a[i+j] != b[j]):
            match = False
            break

        if match == True:
            exist = True
            break

print(exist)
s1 = "computer"
s2 = "cat"

s2 = set(s2)

for i in s1:
    if i not in s2:
        print(i , end= "")

# for i in range(len(s1)):
#     if s1[i] in s2:
#         pass

#     else:
#         print(s1[i], end="")
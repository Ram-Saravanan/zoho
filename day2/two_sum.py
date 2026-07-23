a = [2, 7, 5, 4, 7]
x = 9
seen = {}

for i in range(len(a)):
    find = x - a[i]

    if find in seen:
        print(seen[find], i)
        break

    seen[a[i]] = i 

# return the indices of two values that add up to x    
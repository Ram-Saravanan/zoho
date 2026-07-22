a = [1,5,-4,3,-8,2,0,-1,9]
max_sum = 0
current_sum = 0
best_start = 0
best_end = 0

for i in range(len(a)):
    if a[i] >= 0:
        current_sum += a[i]

    else:
        current_sum = 0

    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)
print(a[best_start:best_end])
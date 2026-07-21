a = [1, 2, -2, 4, -2, 6]

current_sum = 0
max_sum = float('-inf')

for num in a:
    current_sum += num
    max_sum = max(max_sum, current_sum)

    if current_sum < 0:
        current_sum = 0

print(max_sum)        
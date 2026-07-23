a = [1, 2, -2, 4, -2, 6]

current_sum = 0

max_sum = float('-inf')

for i in range(len(a)):

    current_sum = max(a[i],current_sum + a[i])

    if(current_sum > max_sum):
        max_sum = current_sum          

print(max_sum)

# max sum of largest contiguous subarray
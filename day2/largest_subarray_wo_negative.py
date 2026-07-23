a = [1,5,-4,3,-8,2,0,-1,9]
max_sum = 0
current_sum = 0

for i in range(len(a)):
    if a[i] >= 0:
        current_sum += a[i]

    else:
        current_sum = 0

    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)  

# contiguous subrray without negative values


## the solution if we want to print the subarray too

# a = [1, 5, -4, 3, -8, 2, 0, -1, 9]

# current_sum = 0
# max_sum = 0

# start = 0
# best_start = 0
# best_end = 0

# for i in range(len(a)):

#     if a[i] >= 0:
#         current_sum += a[i]

#         if current_sum > max_sum:
#             max_sum = current_sum
#             best_start = start
#             best_end = i

#     else:
#         current_sum = 0
#         start = i + 1

# print("Maximum Sum:", max_sum)
# print("Subarray:", a[best_start:best_end + 1])
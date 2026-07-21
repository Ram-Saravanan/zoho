a = [1,1,2,1]

freq = {}

for i in a:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1

for key, value in freq.items():
    if value == 1:
        print(key)          


## LeetCode 136 – Single Number

# Question:
# Given an integer array nums, every element appears twice except for one. Find that single element.

# Condition:

# Every element appears *exactly twice*
# One element appears once
# Time: O(n)
# Space: O(1)

# Code:

# nums = [4, 1, 2, 1, 2]
# ans = 0
# for num in nums:
#     ans ^= num
# print(ans)

# Output:
# 4

# Key Idea:
# a ^ a = 0
# a ^ 0 = a

# All duplicate numbers cancel out, leaving the unique number.
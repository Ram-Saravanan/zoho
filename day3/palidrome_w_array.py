a = [2,3,5,3,2]

left = 0
right = len(a)-1
pal = False

while left < right:
    if(a[left] == a[right]):
        pal = True
        left += 1
        right -= 1

    else:
        pal = False
        break

print(pal)

#125. Valid Palindrome

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         corrected = ""
#         s = s.lower()

#         for i in s:
#             if i.isalnum():
#                 corrected += i

#         return corrected == corrected[::-1]
        
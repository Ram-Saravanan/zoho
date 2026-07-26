a = "a,b$c"
b = list(a)

left = 0
right = len(a)-1

while left < right:
    if not b[left].isalnum():
        left +=1
    elif not b[right].isalnum():
        right -= 1       
    else:
        b[left], b[right] = b[right], b[left]
        left += 1
        right -= 1
        
print("".join(b))
a = "madam is driving a racecar with level civic radar"

a = a.split()

for i in a:

    left = 0
    right = len(i)-1

    while left < right:
        if(i[left] != i[right]):
            break
        
        left += 1
        right -= 1

    if(left >= right):
        print(i, end=" ")
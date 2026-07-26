a = "hello"
a = list(a)

vowels = {'a','e','i','o','u'}

left = 0
right = len(a)-1

while left < right:

    if a[left] not in vowels:
        left += 1

    elif a[right] not in vowels:
        right -= 1

    else:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1

print("".join(a))
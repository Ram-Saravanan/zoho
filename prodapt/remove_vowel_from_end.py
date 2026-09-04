a = ['a', 'e', 'i', 'o', 'u', 'i']

vowels = ['a', 'e', 'i', 'o', 'u']

l = len(a)-1

while l>=0 and a[l] in vowels:

    l-= 1
    pass

print(a[0:l+1])
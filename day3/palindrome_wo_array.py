a = 24542

original = a

rev = 0

while a > 0:
    last = a%10
    rev = rev*10 + last
    a //= 10

print(rev == original)
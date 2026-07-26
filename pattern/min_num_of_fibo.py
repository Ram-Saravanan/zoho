fib = [1,2]

n = 65

count = 0

while fib[-1] + fib[-2] <= n:          
    fib.append(fib[-1] + fib[-2])

print(fib)

for i in range(len(fib)-1, -1, -1):
    if fib[i] <= n:
        print(fib[i], end = " ")
        count += 1
        n -= fib[i]


print("\n",count)
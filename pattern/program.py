s = input()

n = len(s)
mid = n // 2

for i in range(n):
    for j in range(n):

        if i < mid:
            if j == i:
                print(s[i], end="")
            elif j == n - 1 - i:
                print(s[n - 1 - i], end="")
            else:
                print(" ", end="")

        elif i == mid:
            if j == mid:
                print(s[mid], end="")
            else:
                print(" ", end="")

        else:
            k = n - 1 - i

            if j == k:
                print(s[k], end="")
            elif j == n - 1 - k:
                print(s[n - 1 - k], end="")
            else:
                print(" ", end="")

    print()
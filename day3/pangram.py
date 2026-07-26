a = "The quick brown fox jumps over the lazy dog"
b = set()

for i in a.lower():
    if (i.isalpha()):
        b.add(i)

print(len(b) == 26)
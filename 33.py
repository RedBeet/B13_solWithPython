n = [i for i in range(100, 1000)]
for i in n:
    if "6" or "7" or "8" or "9" in str(i):
        n.remove(i)
for i in n:
    if len(set(str(i))) != 3:
        n.remove(i)

print(len(n))
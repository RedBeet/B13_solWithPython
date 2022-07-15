m = 0
n = []

for i in range(4):
    for j in range(5):
        for k in range(3):
            if i + j + k != 0:
                m += 1
                money = 5000 * i + 10000 * j + 50000 * k
                if money not in n:
                    n.append(money)
print(m + len(n))
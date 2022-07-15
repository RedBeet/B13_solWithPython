import math
n = 0

for a in range(1,7):
    for b in range(1,7):
        for c in range(1,7):
            if math.pow(b,2) - 12*a*c >= 0:
                n += 1

print(n)
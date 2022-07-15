import math
y = []
for i in range(0,3):
    for j in range(0,2):
        for k in range(0,5):
            n = math.pow(2,i) * math.pow(5,j) * math.pow(3,k)
            if n % 10 == 0:
                y.append(n)

sum = sum(y)
print(sum)
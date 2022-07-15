import math as m
l = [0] * 8
t = 0

for i0 in range(8):
    for i1 in range(8):
        for i2 in range(8):
            for i3 in range(8):
                for i4 in range(8):
                    for i5 in range(8):
                        for i6 in range(8):
                            for i7 in range(8):
                                if len(set(l)) == 8:
                                    l2 = []
                                    for i in range(4):
                                        for j in l:
                                            if j == i:
                                                l2.append(l.index(j))
                                    if 0 in l2 and 1 in l2:
                                        if l2.index(0) == l2.index(1) + 1 or l2.index(0) == l2.index(1) - 1:
                                            t += 1
                                l[7] += 1
                            l[6] += 1
                            l[7] = 0
                        l[5] += 1
                        l[6] = 0
                        l[7] = 0
                    l[4] += 1
                    l[5] = 0
                    l[6] = 0
                    l[7] = 0
                l[3] += 1
                l[4] = 0
                l[5] = 0
                l[6] = 0
                l[7] = 0
            l[2] += 1
            l[3] = 0
            l[4] = 0
            l[5] = 0
            l[6] = 0
            l[7] = 0
        l[1] += 1
        l[2] = 0
        l[3] = 0
        l[4] = 0
        l[5] = 0
        l[6] = 0
        l[7] = 0
    l[0] += 1
    l[1] = 0
    l[2] = 0
    l[3] = 0
    l[4] = 0
    l[5] = 0
    l[6] = 0
    l[7] = 0
t = int(t / m.factorial(4))
print(t)
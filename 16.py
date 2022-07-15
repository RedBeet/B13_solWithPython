c = [0] * 3
a = [0] * 4
t = []
for i0 in range(7):
    for i1 in range(7):
        for i2 in range(7):
            for i3 in range(7):
                for i4 in range(7):
                    for i5 in range(7):
                        for i6 in range(7):
                            if c[0] not in a and c[1] not in a and c[2] not in a:
                                if len(set(c)) == 3 and len(set(a)) == 4:
                                    car = set([])
                                    for j in c:
                                        if j == 0:
                                            car.add(j)
                                        if j == 1:
                                            car.add(j)
                                        if j == 2:
                                            car.add(j)
                                    for k in a:
                                        if k == 0:
                                            car.add(k)
                                        if k == 1:
                                            car.add(k)
                                        if k == 2:
                                            car.add(k)

                            a[3] += 1
                        a[2] += 1
                        a[3] = 0
                    a[1] += 1
                    a[2] = 0
                    a[3] = 0
                a[0] += 1
                a[1] = 0
                a[2] = 0
                a[3] = 0
            c[2] += 1
            a[0] = 0
            a[1] = 0
            a[2] = 0
            a[3] = 0
        c[1] += 1
        c[2] = 0
        a[0] = 0
        a[1] = 0
        a[2] = 0
        a[3] = 0
    c[0] += 1
    c[1] = 0
    c[2] = 0
    a[0] = 0
    a[1] = 0
    a[2] = 0
    a[3] = 0
    
print(len(t) - 1)
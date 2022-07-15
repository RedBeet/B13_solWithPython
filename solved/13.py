m = [0] * 3
w = [0] * 4
t = 0
for i0 in range(7):
    for i1 in range(7):
        for i2 in range(7):
            for i3 in range(7):
                for i4 in range(7):
                    for i5 in range(7):
                        for i6 in range(7):
                            if m[0] not in w and m[1] not in w and m[2] not in w:
                                setm = set(m)
                                setw = set(w)
                                if len(setm) == len(m) and len(setw) == len(w):
                                    if 0 in m and 6 in m:
                                        t += 1

                            w[3] += 1
                        w[2] += 1
                        w[3] = 0
                    w[1] += 1
                    w[2] = 0
                    w[3] = 0
                w[0] += 1
                w[1] = 0
                w[2] = 0
                w[3] = 0
            m[2] += 1
            w[0] = 0
            w[1] = 0
            w[2] = 0
            w[3] = 0
        m[1] += 1
        m[2] = 0
        w[0] = 0
        w[1] = 0
        w[2] = 0
        w[3] = 0
    m[0] += 1
    m[1] = 0
    m[2] = 0
    w[0] = 0
    w[1] = 0
    w[2] = 0
    w[3] = 0
    
print(t)
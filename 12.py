m = [0] * 4
w = [0] * 3
t = 0

for i0 in range(7):
    for i1 in range(m[0]+1, 7):
        for i2 in range(m[1]+1, 7):
            for i3 in range(m[2]+1,7):
                for j1 in range(7):
                    for j2 in range(w[0], 7):
                        for j3 in range(w[1], 7):
                            if w[0] not in m and w[1] not in m and w[2] not in m:
                                if m[0] + 1 == m[1] and m[2] + 1 == m[3]:
                                    if w[1] - 1 == w[0] and w[1] + 1 == w[2]:
                                        if m[1] +1 != m[2]:
                                            t += 1
                            w[2] += 1
                        w[1] += 1
                        w[2] = 0
                    w[0] += 1
                    w[1] = 0
                    w[2] = 0
                m[3] += 1
                w[0] = 0
                w[1] = 0
                w[2] = 0
            m[2] += 1
            m[3] = 0
            w[0] = 0
            w[1] = 0
            w[2] = 0
        m[1] += 1
        m[2] = 0
        m[3] = 0
        w[0] = 0
        w[1] = 0
        w[2] = 0
    m[0] += 1
    m[1] = 0
    m[2] = 0
    m[3] = 0
    w[0] = 0
    w[1] = 0
    w[2] = 0



print(t)
m = [0] * 9
w = [0] * 5
t = 0

for i0 in range(2):
    for i1 in range(2):
        for i2 in range(2):
            for i3 in range(2):
                for i4 in range(2):
                    for i5 in range(2):
                        for i6 in range(2):
                            for i7 in range(2):
                                for i8 in range(2):
                                    for j0 in range(2):
                                        for j1 in range(2):
                                            for j2 in range(2):
                                                for j3 in range(2):
                                                    for j4 in range(2):
                                                        if sum(m) + sum(w) == 3 and sum(m) >= 1 and sum(w) >= 1:
                                                            t += 1

                                                        w[4] += 1
                                                    w[3] += 1
                                                    w[4] = 0
                                                w[2] += 1
                                                w[3] = 0
                                                w[4] = 0
                                            w[1] += 1
                                            w[2] = 0
                                            w[3] = 0
                                            w[4] = 0
                                        w[0] += 1
                                        w[1] = 0
                                        w[2] = 0
                                        w[3] = 0
                                        w[4] = 0
                                    m[8] += 1
                                    w[0] = 0
                                    w[1] = 0
                                    w[2] = 0
                                    w[3] = 0
                                    w[4] = 0
                                m[7] += 1
                                m[8] = 0
                                w[0] = 0
                                w[1] = 0
                                w[2] = 0
                                w[3] = 0
                                w[4] = 0
                            m[6] += 1
                            m[7] = 0
                            m[8] = 0
                            w[0] = 0
                            w[1] = 0
                            w[2] = 0
                            w[3] = 0
                            w[4] = 0
                        m[5] += 1
                        m[6] = 0
                        m[7] = 0
                        m[8] = 0
                        w[0] = 0
                        w[1] = 0
                        w[2] = 0
                        w[3] = 0
                        w[4] = 0
                    m[4] += 1
                    m[5] = 0
                    m[6] = 0
                    m[7] = 0
                    m[8] = 0
                    w[0] = 0
                    w[1] = 0
                    w[2] = 0
                    w[3] = 0
                    w[4] = 0
                m[3] += 1
                m[4] = 0
                m[5] = 0
                m[6] = 0
                m[7] = 0
                m[8] = 0
                w[0] = 0
                w[1] = 0
                w[2] = 0
                w[3] = 0
                w[4] = 0
            m[2] += 1
            m[3] = 0
            m[4] = 0
            m[5] = 0
            m[6] = 0
            m[7] = 0
            m[8] = 0
            w[0] = 0
            w[1] = 0
            w[2] = 0
            w[3] = 0
            w[4] = 0
        m[1] += 1
        m[2] = 0
        m[3] = 0
        m[4] = 0
        m[5] = 0
        m[6] = 0
        m[7] = 0
        m[8] = 0
        w[0] = 0
        w[1] = 0
        w[2] = 0
        w[3] = 0
        w[4] = 0
    m[0] += 1
    m[1] = 0
    m[2] = 0
    m[3] = 0
    m[4] = 0
    m[5] = 0
    m[6] = 0
    m[7] = 0
    m[8] = 0
    w[0] = 0
    w[1] = 0
    w[2] = 0
    w[3] = 0
    w[4] = 0

print(t)
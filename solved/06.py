w1 = 0
w2 = 0
w3 = 0
m1 = 0
m2 = 0
m3 = 0

f = 0
t = 0

for i0 in range(7):
    for i1 in range(7):
        for i3 in range(7):
            for i4 in range(7):
                for i5 in range(7):
                    for i6 in range(7):
                        if w1 == w2 or w1 == w3 or w1 == m1 or w1 == m2 or w1 == m3 or w2 == w3 or w2 == m1 or w2 == m2 or w2 == m3 or w3 == m1 or w3 == m2 or w3 == m3 or m1 == m2 or m1 == m3 or m2 == m3:
                            f += 1
                        else:
                            if w1 + 1 == w2 or w1 - 1 == w2 or w1 + 1 == w3 or w1 - 1 == w3 or w2 + 1 == w3 or w2 - 1 == w3:
                                f += 1
                            else:
                                t += 1
                        m3 += 1
                    m2 += 1
                    m3 = 0
                m1 += 1
                m2 = 0
                m3 = 0
            w3 += 1
            m1 = 0
            m2 = 0
            m3 = 0
        w2 += 1
        w3 = 0
        m1 = 0
        m2 = 0
        m3 = 0
    w1 += 1
    w2 = 0
    w3 = 0
    m1 = 0
    m2 = 0
    m3 = 0

print(t)
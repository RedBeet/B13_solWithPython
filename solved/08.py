m1 = 0
m2 = 0
m3 = 0
w1 = 0
w2 = 0
w3 = 0
w4 = 0
w5 = 0

t = 0

for i0 in range(2):
    for i1 in range(2):
        for i2 in range(2):
            for i3 in range(2):
                for i4 in range(2):
                    for i5 in range(2):
                        for i6 in range(2):
                            for i7 in range(2):

                                if (m1 + m2 + m3) != 0 and (m1 + m2 + m3) != 3:
                                    sum = m1 + m2 + m3 + w1 + w2 + w3 + w4 + w5
                                    if 3 <= sum and sum <= 5:
                                        t += 1
                                w5 += 1
                            w4 += 1
                            w5 = 0
                        w3 += 1
                        w4 = 0
                        w5 = 0
                    w2 += 1
                    w3 = 0
                    w4 = 0
                    w5 = 0
                w1 += 1
                w2 = 0
                w3 = 0
                w4 = 0
                w5 = 0
            m3 += 1
            w1 = 0
            w2 = 0
            w3 = 0
            w4 = 0
            w5 = 0
        m2 += 1
        m3 = 0
        w1 = 0
        w2 = 0
        w3 = 0
        w4 = 0
        w5 = 0
    m1 += 1
    m2 = 0
    m3 = 0
    w1 = 0
    w2 = 0
    w3 = 0
    w4 = 0
    w5 = 0

print(int(t/2)) #서로 같은 조 -> 두 조가 겹치는 경우 제외하기
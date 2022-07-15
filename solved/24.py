a = 0
b = 0
c = 0
d = 0
e = 0
t = 0

for i0 in range(4):
    a += 1
    for i1 in range(4):
        b += 1
        for i2 in range(4):
            c += 1
            for i3 in range(4):
                d += 1
                for i4 in range(4):
                    e += 1

                    if a != b and b != c and b != e and c != d and c != e and d != e:
                        t += 1
                e = 0
            d = 0
            e = 0
        c = 0
        d = 0
        e = 0
    b = 0
    c = 0
    d = 0
    e = 0

print(t)
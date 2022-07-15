a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
t = 0

for i0 in range(3):
    a += 1
    for i1 in range(3):
        b += 1
        for i2 in range(3):
            c += 1
            for i3 in range(3):
                d += 1
                for i4 in range(3):
                    e += 1
                    for i5 in range(3):
                        f += 1
                        if 1 in [a,b,c,d,e,f] and 2 in [a,b,c,d,e,f] and 3 in [a,b,c,d,e,f]:
                            if a != b and b != c and c != d and d != e and e != f and f != a:
                                print([a,b,c,d,e,f])
                                t += 1
                    f = 0
                e = 0
                f = 0
            d = 0
            e = 0
            f = 0
        c = 0
        d = 0
        e = 0
        f = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0

print(t)
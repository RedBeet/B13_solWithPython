a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
t = 0

for i0 in range(2):
    for i1 in range(2):
        for i2 in range(2):
            for i3 in range(2):
                for i4 in range(2):
                    for i5 in range(2):
                        for i6 in range(2):
                            for i7 in range(2):
                                if a+b+c+d+e+f+g+h == 4:
                                    if a + b == 1:
                                        t += 1
                                
                                h += 1
                            g += 1
                            h = 0
                        f += 1
                        g = 0
                        h = 0
                    e += 1
                    f = 0
                    g = 0
                    h = 0
                d += 1
                e = 0
                f = 0
                g = 0
                h = 0
            c += 1
            d = 0
            e = 0
            f = 0
            g = 0
            h = 0
        b += 1
        c = 0
        d = 0
        e = 0
        f = 0
        g = 0
        h = 0
    a += 1
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0

print(int(t/2))
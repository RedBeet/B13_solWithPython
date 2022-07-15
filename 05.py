a = 0
b = 0
c = 0
d = 0
e = 0
t = 0

for i0 in range(0,5):
    for i1 in range(0,5):
        for i2 in range(0,5):
            for i3 in range(0,5):
                for i4 in range(0,5):
                    if a==0 and b==1: 
                        t += 1
                    elif a==1 and b==0:
                        t += 1
                    elif a==2 and b==3:
                        t += 1
                    elif a==3 and b==2:
                        t += 1
                    elif a==3 and b==4:
                        t += 1
                    elif a==4 and b==3:
                        t += 1
                    e += 1
                d += 1
                e = 0
            c += 1
            d = 0
            e = 0
        b += 1
        c = 0
        d = 0
        e = 0
    a += 1
    b = 0
    c = 0
    d = 0
    e = 0
                    
print(t)
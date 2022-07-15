p = [[] for col in range(5)]
t = []

for i0 in range(5):
    for i1 in range(5):
        for i2 in range(5):
            for i3 in range(5):
                p[i0].append("f0")
                p[i1].append("f1")
                p[i2].append("f2")
                p[i3].append("f3") #give flowers

                for j0 in range(5):
                    for j1 in range(5):
                        p[j0].append("c")
                        p[j1].append("c") #give chocolate

                        if len(p[0]) != 0 and len(p[1]) != 0 and len(p[2]) != 0 and len(p[3]) != 0 and len(p[4]) != 0:
                            print(p)
                            t.append(p)
                        p[j0].remove("c") 
                        p[j1].remove("c")
                p[i0].remove("f0")
                p[i1].remove("f1")
                p[i2].remove("f2")
                p[i3].remove("f3")
print(t)
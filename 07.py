t = 0
building = [[],[],[],[],[]]

for i0 in range(len(building)):
    building[i0].append(1)
    for i1 in range(len(building)):
        building[i1].append(1)
        for i2 in range(len(building)):
            building[i2].append(1)
            for i3 in range(len(building)):
                building[i3].append(1)
                for i4 in range(len(building)):
                    building[i4].append(1)

                    if building.count([]) == 2:
                        t += 1
                    
                    building[i4] = []
                building[i3] = []
            building[i2] = []
        building[i1] = []
    building[i0] = []

print(t)
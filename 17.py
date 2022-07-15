white = [0] * 6
black = [0] * 3
t = 0

for i0 in range(9):
    for i1 in range(9):
        for i2 in range(9):
            for i3 in range(9):
                for i4 in range(9):
                    for i5 in range(9):
                        for j0 in range(9):
                            for j1 in range(9):
                                for j2 in range(9):

                                    if black[0] not in white and black[1] not in white and black[2] not in white:
                                        l1 = []
                                        for k in range(9):
                                            for x in white:
                                                if x == k:
                                                    l1.append("white")
                                            for y in black:
                                                if y == k:
                                                    l1.append("black")
                                        print(l1)
                                        if l1[4] == "black":
                                            t += 1

                                    black[2] += 1
                                black[1] += 1
                                black[2] = 0
                            black[0] += 1
                            black[1] = 0
                            black[2] = 0
                        white[5] += 1
                        black[0] = 0
                        black[1] = 0
                        black[2] = 0
                    white[4] += 1
                    white[5] = 0
                    black[0] = 0
                    black[1] = 0
                    black[2] = 0
                white[3] += 1
                white[4] = 0
                white[5] = 0
                black[0] = 0
                black[1] = 0
                black[2] = 0
            white[2] += 1
            white[3] = 0
            white[4] = 0
            white[5] = 0
            black[0] = 0
            black[1] = 0
            black[2] = 0
        white[1] += 1
        white[2] = 0
        white[3] = 0
        white[4] = 0
        white[5] = 0
        black[0] = 0
        black[1] = 0
        black[2] = 0
    white[0] += 1
    white[1] = 0
    white[2] = 0
    white[3] = 0
    white[4] = 0
    white[5] = 0
    black[0] = 0
    black[1] = 0
    black[2] = 0

print(t)
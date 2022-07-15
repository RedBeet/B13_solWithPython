numbers = [i for i in range(10000, 100000)]
final = []
for i in numbers:
    print(i)
    I = str(i)
    if I.count("0") == 1 and I.count("1") == 1 and I.count("2") == 1 and I.count("3") == 1 and I.count("4") == 1:
        final.append(i)

print(final[38])
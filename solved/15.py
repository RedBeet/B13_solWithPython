numbers = [i for i in range(100, 1000)]
final = []
for i in numbers:
    stri = str(i)
    seti = set(stri)
    if len(stri) == len(seti):
        final.append(i)

print(final[149])
def howManyFx(x):
    if x >= 1:
        return x * howManyFx(x-1)
    else:
        return 1

print(howManyFx(4))
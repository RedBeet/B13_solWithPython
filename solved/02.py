howManyTriangles = 0

for a in range(1,20):
    for b in range(1,a+1):
        for c in range(1,b+1):
            if a+b+c==20 and b+c>a:
                howManyTriangles += 1
                
print(howManyTriangles)
a = [1,2,3,4,5]
b = [1,2,3,4]

def C(arr, n):
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
            
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in C(arr[i + 1:], n - 1):
                result.append([arr[i]] + j)
    
    

    return result

Ca = C(a,2)
Cb = C(b,2)

l = []
for i in Ca:
    for j in Cb:
        l.append([i,j])

for i in l:
    if i[0][1] - i[0][0] == i[1][1] - i[1][0]:
        l.remove(i)

print(len(l))
a = ["a1","a2"]
b = ["b1","b2","b3"]
c = ["c1","c2","c3","c4"]

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
    
l = []
l.extend(a)
l.extend(b)
l.extend(c)

sqr = C(l,4)
#한쪽에서 3개이상
#2개 2개
temp = list(sqr)
for i in sqr:
    aisin = 0
    bisin = 0
    cisin = 0
    for j in a:
        if j in i:
            aisin += 1
    for k in b:
        if k in i:
            bisin += 1
    for m in c:
        if m in i:
            cisin += 1
    if bisin >= 3 or cisin >= 3 or aisin == 0 or bisin == 0 or cisin == 0:
        temp.remove(i)


print(len(temp))
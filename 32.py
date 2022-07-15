m = ["m1", "m2", "m3"]
w = ["w1", "w2", "w3"]
a = []
a.extend(m)
a.extend(w)

def P(arr, n):
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in P(ans, n-1):
                result.append([arr[i]]+p)

    return result

president = P(a,2)
print(len(president))
for i in president:
    em = 0
    for j in m:
        if j in i:
            em += 1
    if em == 0:
        president.remove(i)

print(len(president))
print(president)
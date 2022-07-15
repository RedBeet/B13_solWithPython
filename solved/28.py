ABAC = [1,2,3,4,5,6]
BC = [1,2,3,4]

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
    
print(len(C(ABAC, 2)) * len(C(BC, 1)))
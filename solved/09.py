import math as m
n = 3
nt = 0


while nt != 56:
    n += 1
    nt = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and i != k and j!= k:
                    nt += 1
    nt = int(nt/m.factorial(3)) #i,j,k점들끼리의 순서 무시

ns = int(((n/2) * (n/2 - 1)) / 2) #원 위 직각삼각형 개수 문제의 변형으로 생각할 수 있음
print(ns)
def Divi(ar, n):
    count = 0
    for i in range(n):
        if ar[i] != 0:
            if ar[i] % 3 == 0:
                count += 1
    print(count)
    return count

n = int(input())
ar = []
for i in range(n):
    ar.append(int(input()))
Divi(ar, n)

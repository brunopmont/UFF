n = int(input())
v = list(map(int, input().split()))
tot = 1
maior = 0
for i in range(1, n):
    if v[i] == v[i-1]:
        tot += 1
    else:
        tot = 1
    if tot > maior:
            maior = tot
print('{}'.format(maior), end='\n')
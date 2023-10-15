n, h = map(int, input().split())
alt = list(map(int, input().split()))
movs = 0
for i in range(n-1):
    while alt[i] != h:
        if alt[i] > h:
            alt[i] -= 1
            alt[i+1] -= 1
            movs += 1
        elif alt[i]< h:
            alt[i] += 1
            alt[i+1] += 1
            movs += 1
print(movs)
#94 72 17 39 84 (84)
# 84 62 17 39 84
# 
#
#
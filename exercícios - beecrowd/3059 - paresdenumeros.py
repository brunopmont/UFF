n, i, f = map(int, input().split())
v = list(map(int, input().split()))
pares = []
c = 0
while len(v) > 1:
    for j in range(1, len(v)):
        if i <= v[0] + v[j] and v[0] + v[j] <= f:
            c += 1
    v.remove(v[0])
print(c)
n = int(input())
i = 0
pos = 0
hits = list(map(int, input().split()))
menor = min(hits)
for i in range(n):
    if hits[i] == menor:
        pos = i+1
        break
print(pos)
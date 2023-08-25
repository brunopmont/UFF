stts = 'S'
n, m = map(int, input().split())
posto = list(map(int, input().split()))
posto.append(42195)
for i in range(1, n+1):
    if posto[i] - posto[i-1] > m:
        stts = 'N'
print(stts)
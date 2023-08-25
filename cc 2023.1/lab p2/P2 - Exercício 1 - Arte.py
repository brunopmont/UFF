n = int(input())
h = list(map(int, input().split()))
som = h[0] + h[n-1]
stts = 'S'
for i in range(0, n):
    if (h[i] + h[n-1-i]) != som:
        stts = 'N'
print(stts)
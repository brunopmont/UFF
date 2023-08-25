n = int(input())
mapa = []
stts = [[] for i in range(n)]
cam = ''
for i in range(n+1):
    x = list(map(int, input().split()))
    mapa.append(x)
for i in range(n):
    for j in range(n):
        if (mapa[i][j] + mapa[i][j+1] + mapa[i+1][j] + mapa[i+1][j+1]) > 1:
            cam = 'S'
        else:
            cam = 'U'
        stts[i].append(cam)
for i in range(n):
    answer = ''
    for j in range(n):
        answer = answer + stts[i][j]
    print(answer)
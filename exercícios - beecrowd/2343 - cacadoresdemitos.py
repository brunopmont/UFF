mito = 0
x = 501
y = 501
mapa = [[0 for x in range(x)] for y in range(y)]
n=int(input())
for i in range(n):
    x, y = map(int, input().split())
    if mapa[y][x] == 1:
        mito = 1
    mapa[y][x] = 1
print(mito)
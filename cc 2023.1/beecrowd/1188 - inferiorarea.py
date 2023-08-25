op = str(input().upper())
matriz = [[float(input()) for i in range(12)] for i in range(12)]
s = 0
m = 0
for i in range(1, 6):
    s = s + sum(matriz[12-i][i:12-i])
m = s / 30
if op == 'S':
    print('{:.1f}'.format(s))
elif op == 'M':
    print('{:1.f]'.format(m))

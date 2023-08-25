matriz = []
l = int(input())
op = str(input().upper())
for i in range(12):
    c = []
    for j in range(12):
        x = float(input())
        c.append(x)
    matriz.append(c)
if op == 'M':
    print('{:.1f}'.format(sum(matriz[l])/12))
elif op == 'S':
    print('{:.1f}'.format(sum(matriz[l])))
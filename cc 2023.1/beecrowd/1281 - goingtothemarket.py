n = int(input())
for i in range(n):
    precos = {}
    gasto = 0
    p = int(input())
    for i in range(p):
        x = list(input().split())
        precos[x[0]] = float(x[1])
    c = int(input())
    for i in range(c):
        x = list(input().split())
        gasto = gasto + float(x[1]) * precos.get(x[0])
    print('R$ {:.2f}'.format(gasto))
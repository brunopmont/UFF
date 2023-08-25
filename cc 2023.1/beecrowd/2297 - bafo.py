t = 1
r = int(input())
while r != 0:
    aldo = 0
    beto = 0
    vencedor = ''
    for i in range(r):
        a, b = map(int, input().split())
        aldo += a
        beto += b
    if aldo > beto:
        vencedor = 'Aldo'
    elif beto > aldo:
        vencedor = 'Beto'
    print('Teste {}'.format(t))
    print(vencedor)
    print()
    t += 1
    r = int(input())
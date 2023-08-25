cont = 1
v = int(input())
while v != 0:
    b50, b10, b5, b1 = 0, 0, 0, 0
    if v >= b50:
        b50 = v // 50
        v = v - b50*50
    if v >= 10:
        b10 = v // 10
        v = v - b10*10
    if v >= 5:
        b5 = v // 5
        v = v - b5*5
    if v >= 1:
        b1 = v // 1
        v = v - b1*1
    print('Teste {}'.format(cont))
    print('{} {} {} {}'.format(b50, b10, b5, b1))
    print('')
    v = int(input())
    cont += 1
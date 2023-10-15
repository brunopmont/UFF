n = int(input())
t = 1
pedaços = 0
while n != -1:
    print('Teste {}'.format(t))
    t += 1
    if n == 0:
        pedaços = 4
    else:
        pedaços = 1 + 2**(n+1) + 4**n
    print(pedaços)
    print()
    n = int(input())
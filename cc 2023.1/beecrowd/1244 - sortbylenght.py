n = int(input())
for i in range(n):
    a, b = map(str, input().split())
    c = ''
    maior = 0
    if len(a) > len(b):
        maior = len(a)
        menor= len(b)
    else:
        maior = len(b)
        menor = len(a)
    for i in range(maior):
        if i < menor:
            c = c + (a[i] + b[i])
        else:
            if maior == len(a):
                c = c + a[i]
            elif maior == len(b):
                c = c + b[i]
    print(c)
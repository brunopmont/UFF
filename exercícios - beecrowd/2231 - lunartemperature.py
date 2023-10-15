import math
t = 1
n, m = map(int, input().split())
while n != 0 and m != 0:
    menor = 201
    maior = -201
    temp = []
    somatemp = []
    medtemp = []
    for i in range(n):
        temp.append(int(input()))
    somatemp.append(temp[0])
    for i in range(1, len(temp)):
        somatemp.append(temp[i] + somatemp[i-1])
    for i in range(n-m+1):
        j = i+m-1
        if i == 0:
            soma = somatemp[j]
        else:
            soma = somatemp[j] - somatemp[i-1]
        media = soma / m
        if media > 0:
            media = math.floor(media)
        else:
            media = math.ceil(media)
        if media > maior:
            maior = media
        if media < menor:
            menor = media
    print('Teste', t)
    print('{} {}'.format(menor, maior))
    print()
    n, m = map(int, input().split())
    t += 1
n = int(input())
while n != 0:
    times = {}
    maior = 0
    nomemaior = ''
    for i in range(n):
        nome, pontos = input().split()
        times[nome] = int(pontos)
    for i in range(n//2):
        partida = list(map(str, input().split()))
        gols = list(map(int, partida[1].split('-')))
        a = partida[0]
        b = partida[2]
        golsa = int(gols[0])
        golsb = int(gols[1])
        if partida[1][0] > partida[1][2]:
            times[a] = times[a] + 5
            times[a] = times[a] + 3 * golsa
            times[b] = times[b] + 3 * golsb
        elif partida[1][0] < partida[1][2]:
            times[b] = times[b] + 5
            times[a] = times[a] + 3 * golsa
            times[b] = times[b] + 3 * golsb
        elif partida[1][0] == partida[1][2]:
            times[a] = times[a] + 3 * golsa + 1
            times[b] = times[b] + 3 * golsb + 1
        if times[a] > maior:
            maior = times[a]
            nomemaior = a
        if times[b] > maior:
            maior = times[b]
            nomemaior = b
    if 'Sport' == nomemaior:
        print('O Sport foi o campeao com {} pontos :D'.format(times['Sport']))
    else:
        print('O Sport nao foi o campeao. O time campeao foi o {} com {} pontos :('.format(nomemaior, maior))
    print()
    n = int(input())
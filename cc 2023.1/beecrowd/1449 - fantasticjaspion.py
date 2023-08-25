t = int(input())
for i in range(t):
    dicio = {}
    letra = []
    m, n = map(int, input().split())
    for j in range(m):
        word = input()
        translate = input()
        dicio[word] = translate
    for k in range(n):
        letrajap = list(input().split())
        for z in range(len(letrajap)):
            if letrajap[z] in dicio:
                letrajap[z] = dicio[letrajap[z]]
        letra.append(letrajap)
    for k in range(len(letra)):
        print(' '.join(letra[k]), end = '\n')
    print()
import random
ideal = [1,2,3,4,5,6,7,8,9]
n = int(input())
t = 1
for z in range(n):
    matriz = []
    stts = 'SIM'
    for i in range(9): 
        linha = list(map(int, input().split()))
        matriz.append(linha)
    for i in range(9): #compara linhas
        if sorted(matriz[i]) != ideal:
            stts = 'NAO'
            break
    for i in range(9):
        l = []
        for j in range(9):
            l.append(matriz[j][i]) 
        if sorted(l) != ideal:
            stts = 'NAO'
            break
    for j in range(3): 
        for k in range(3): 
            s = []
            for m in range(3):
                for n in range(3):
                    s.append(matriz[j*3+m][k*3+n])
            if sorted(s) != ideal:
                stts = 'NAO'
                break
    print('Instancia {}'.format(t))
    print(stts)
    print()
    t += 1
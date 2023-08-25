n = int(input())
for z in range(n):
    final = 0
    matriz = []
    posmov = []
    for i in range(4):
        x = list(map(int, input().split()))
        matriz.append(x)
    for i in range(4):
        if 2048 in matriz[i]:
            final = 1
    if final == 1:
        matriz = []
    else:
        for i in range(3):
            for j in range(4):
                if matriz[i][j] == matriz[i+1][j] != 0 or matriz[i][j] != matriz[i+1][j] == 0:
                    if 'DOWN' not in posmov:
                        posmov.append('DOWN')
        for j in range(3):
            for i in range(4):
                if matriz[i][j] == matriz[i][j+1] != 0 or matriz[i][j+1] != matriz[i][j] == 0:
                    if 'LEFT' not in posmov:
                        posmov.append('LEFT')
        for j in range(3):
            for i in range(4):
                if matriz[i][j] == matriz[i][j+1] != 0 or matriz[i][j] != matriz[i][j+1] == 0:
                    if 'RIGHT' not in posmov:
                        posmov.append('RIGHT')
        for i in range(3):
            for j in range(4):
                if matriz[i][j] == matriz[i+1][j] != 0 or matriz[i+1][j] != matriz[i][j] == 0:
                    if 'UP' not in posmov:
                        posmov.append('UP')
    if (len(posmov)) == 0:
        print('NONE')
    else:
        for i in range(len(posmov)):
            if i == len(posmov) - 1:
                print('{}'.format(posmov[i]), end = '\n')
            else:
                print('{} '.format(posmov[i]), end = '')
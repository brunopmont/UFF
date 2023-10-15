n = int(input())
cont = 1
while n != 0:
    senha = [[0]*10 for i in range(6)]
    final = []
    for i in range(n):
        dados = list(input().split())
        dig = list(map(int, dados[0:10]))
        letra = dados[10:16]
        for j in range(6):
            if letra[j] == 'A':
                senha[j][int(dig[0])] += 1
                senha[j][int(dig[1])] += 1
            elif letra[j] == 'B':
                senha[j][int(dig[2])] += 1
                senha[j][int(dig[3])] += 1
            elif letra[j] == 'C':
                senha[j][int(dig[4])] += 1
                senha[j][int(dig[5])] += 1
            elif letra[j] == 'D':
                senha[j][int(dig[6])] += 1
                senha[j][int(dig[7])] += 1
            elif letra[j] == 'E':
                senha[j][int(dig[8])] += 1
                senha[j][int(dig[9])] += 1
    for i in range(6):
        a = str(senha[i].index(max(senha[i])))
        final.append(a)
    
    print('Teste', cont)
    print(final[0], final[1], final[2], final[3], final[4], final[5], end= " \n")
    print()
    n = int(input())
    cont += 1
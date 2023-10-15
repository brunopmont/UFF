t = int(input())
for i in range(t):
    p = 0
    caminho = []
    n = int(input())
    for j in range(n):
        move = input().split()
        if 'RIGHT' in move:
            p = p + 1
            caminho.append(+1)
        elif 'LEFT' in move:
            p = p - 1
            caminho.append(-1)
        elif 'SAME' in move:
            p = p + caminho[int(move[2])-1]
            caminho.append(caminho[int(move[2])-1])
    print(p)
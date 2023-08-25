while True:
    try:
        m, n = map(int, input().split())
        mapa = []
        movs = 0
        pos = [[0, 0], [0, 0]] #[x1,y1][x2,y2]
        for i in range(m):
            x = list(map(int, input().split()))
            mapa.append(x)
            if 2 in x:
                pos[1][0] = i
                pos[1][1] = mapa[i].index(2)
            if 1 in x:
                pos[0][0] = i
                pos[0][1] = mapa[i].index(1)
        movs = abs(pos[1][0] - pos[0][0]) + abs(pos[1][1] - pos[0][1])
        print(movs)
    except EOFError:
        break
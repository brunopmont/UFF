while True:
    try:
        board = []
        n, m = map(int, input().split())
        result = [[0 for i in range(m)] for i in range(n)]
        for i in range(n):
            x = list(map(int, input().split()))
            board.append(x)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1:
                    result[i][j] = 9
                else:
                    res = 0
                    if i != 0:
                       res = res + board[i-1][j]
                    if i != n-1:
                        res = res + board[i+1][j]
                    if j != 0:
                        res = res + board[i][j-1]
                    if j != m-1:
                        res = res + board[i][j+1]
                    result[i][j] = res
        for i in range(n):
            for j in range(m):
                print('{}'.format(result[i][j]), end='')
            print()
    except EOFError:
        break
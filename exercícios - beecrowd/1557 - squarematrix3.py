n = int(input())
while n != 0:
    char = len(str(4**(n-1)))
    matriz = [[0 for i in range(n)] for i in range(n)]
    for j in range(n):
        matriz[0][j] = 2**j
    for j in range(1, n):
        for k in range(n):
            matriz[j][k] = matriz[j-1][k]*2
    for j in range(n):
        for k in range(n):
            if k == n - 1:
                print(str(matriz[j][k]).rjust(char), end="")
            else:
                print(str(matriz[j][k]).rjust(char), end=" ")
        print()
    print()
    n = int(input())
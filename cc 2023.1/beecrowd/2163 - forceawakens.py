n, m = map(int, input().split())
matriz = []
achado = 0
val = [0, 0]
lista42 = []
i=1
j=1
y=0
for z in range(n):
    x = list(map(int, input().split()))
    matriz.append(x)
    if 42 in x and z != 0 and z != n-1:
        lista42.append(z)
while y < len(lista42) and achado == 0:
    j = 1
    i = lista42[y]
    while j < m-1 and achado == 0:
        anal = []
        if matriz[i][j] == 42:
            if matriz[i][j-1:j+2:2] == [7,7]:
                if matriz[i-1][j-1:j+2] == [7, 7, 7] and matriz[i+1][j-1:j+2] == [7, 7, 7]:
                    val[0] = i+1
                    val[1] = j+1
                    achado = 1
        j += 1
    y += 1
print('{} {}'.format(val[0], val[1]))
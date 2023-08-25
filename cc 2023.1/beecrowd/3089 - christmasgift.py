n = int(input())
while n != 0:
    listapares = []
    listapreco = list(map(int, input().split()))
    for i in range(n):
        y = listapreco[i] + listapreco[2*n-1-i]
        listapares.append(y)
    print('{} {}'.format(max(listapares), min(listapares)))
    n = int(input())
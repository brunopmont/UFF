n, t = map(int, input().split())
dados = list(map(int, input().split()))
maior = 0
somaj = 0
posmaior = 0
for i in range(n):
    somaj = 0
    for j in range(t):
        somaj = somaj + dados[i+j*n]
    if somaj >= maior:
        maior = somaj
        posmaior = i+1
print(posmaior)

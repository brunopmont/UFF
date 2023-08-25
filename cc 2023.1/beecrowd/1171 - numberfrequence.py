n = int(input())
lista = []
listasolo = []
cont = 0
for i in range(n):
    x = int(input())
    if x not in lista:
        listasolo.append(x)
    lista.append(x)
listasolo.sort()
for i in range(len(listasolo)):
    print('{} aparece {} vez(es)'.format(listasolo[i], lista.count(listasolo[i])))
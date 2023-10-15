n = int(input())
p = []
pord = []
temp = []
final = []
cont = 1
som = 0
for i in range(n):
    x = int(input())
    p.append(x)
    pord.append(x)
pord.sort(reverse=True)
for i in range(n):
    temp.append(pord[i])
    cont += 1
    if cont == 4:
        temp.remove(min(temp))
        final.append(temp)
        cont = 1
        temp = []
    if i == n-1:
        final.append(temp)
for j in range(len(final)):
    som = som + sum(final[j])
print(som)
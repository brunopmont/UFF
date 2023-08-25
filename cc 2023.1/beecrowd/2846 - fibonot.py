k = int(input())
cont = k
fib = [1]
fibn = []
f1 = 1
f2 = 1
j = 1
for i in range(24):
    f3 = f2 + f1
    f1 = f2
    f2 = f3
    fib.append(f3)
while j <= cont + 10:
    if j not in fib:
        fibn.append(j)
    else:
        cont += 1
    j += 1
print(fibn[k-1])
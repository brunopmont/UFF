x = int(input())
y = int(input())
res = 0
soma = 0
if x > y:
    res = x
    x = y
    y = res 
for i in range(x + 1, y):
    if i % 2 != 0:
        soma = soma + i
print(soma)
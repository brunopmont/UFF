n = int(input())
r = list(map(int, input().split()))
erro = 0
if n == 2:
    if r[1] < r[0]:
        erro = 2
else:
    for i in range(1, n):
        if r[i] < r[i-1]:
            erro = i + 1
            break
print(erro)
precos = {1001: 1.50, 1002: 2.50, 1003: 3.50, 1004: 4.50, 1005: 5.50}
p = int(input())
totpreco = 0
for i in range(p):
    x = list(map(int, input().split()))
    totpreco = totpreco + precos[x[0]] * x[1]
print('{:.2f}'.format(totpreco))

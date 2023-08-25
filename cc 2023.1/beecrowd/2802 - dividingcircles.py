n = int(input())
linhas = (n * (n - 1)) / 2
intersec = (n * (n-1) * (n-2) * (n-3)) / (1*2*3*4)
reg = linhas + intersec + 1
print(int(reg))
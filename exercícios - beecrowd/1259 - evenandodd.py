num = [[], []]
n = int(input())
for i in range(n):
    x = int(input())
    if x % 2 == 0:
        num[0].append(x)
    else:
        num[1].append(x)
num[0].sort()
num[1].sort(reverse=True)
for i in range(len(num[0])):
    print(num[0][i])
for i in range(len(num[1])):
    print(num[1][i])
n = int(input())
for i in range(n):
    x = int(input())
    f1 = 0
    f2 = 1
    if x == 0:
        f3 = 0
    elif x == 1:
        f3 = 1
    else:
        for j in range(1, x):
            f3 = f2 + f1
            f1 = f2
            f2 = f3
    print('Fib({}) = {}'.format(x, f3))
t = int(input())
for z in range(t):
    n, m = map(int, input().split())
    renas = []
    for i in range(n):
        x = list(map(str, input().split()))
        renas.append(x)
    for i in range(n):
        for j in range(n):
            if int(renas[i][1]) > int(renas[j][1]):
                res = renas[i]
                renas[i] = renas[j]
                renas[j] = res
            if int(renas[i][1]) == int(renas[j][1]):
                if int(renas[i][2]) < int(renas[j][2]):
                    res = renas[i]
                    renas[i] = renas[j]
                    renas[j] = res
                if int(renas[i][2]) == int(renas[j][2]):
                    if float(renas[i][3]) < float(renas[j][3]):
                        res = renas[i]
                        renas[i] = renas[j]
                        renas[j] = res
                    if float(renas[i][3]) == float(renas[j][3]):
                        if renas[i][0] < renas[j][0]:
                            res = renas[i]
                            renas[i] = renas[j]
                            renas[j] = res
    print('CENARIO ' + '{' + '{}'.format(z+1) + '}')
    for i in range(m):
        print('{} - {}'.format(i+1, renas[i][0]))
a,b = list(map(int, input().split()))

while a != 0 and b != 0:
    d = {}
    d1 = {}

    for x in range(a):
        d[x] = input().split()
    for x in range(b):
        d1[x] = input().split()

    soma = 0
    s = 0
    for i in range(b):
        o = d1[i]
        for x in range(a):
            r = d[x]
            for j in range(int(o[0])):
                if o[j+1] in r:
                    s = 1
            soma += s
            s = 0
    print(soma)
    a, b = list(map(int, input().split()))
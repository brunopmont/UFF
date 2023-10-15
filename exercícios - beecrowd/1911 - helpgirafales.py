n = int(input())
while n != 0:
    signs = {}
    falsesigns = 0
    for i in range(n):
        name, sign = map(str, input().split())
        signs[name] = sign
    m = int(input())
    for i in range(m):
        name, sign = map(str, input().split())
        if sign != signs[name]:
            erros = 0
            signtrue = list(signs[name])
            sign = list(sign)
            for j in range(len(sign)):
                if sign[j] != signtrue[j]:
                    erros += 1
            if erros > 1:
                falsesigns += 1
    print(falsesigns)
    n = int(input())
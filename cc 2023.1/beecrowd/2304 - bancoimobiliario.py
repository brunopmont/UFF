i, n = map(int, input().split())
D, E, F = i, i, i
for j in range(n):
    x = list(input().split())
    if x[0] == 'C':
        if x[1] == 'D':
            D = D - int(x[2])
        elif x[1] == 'E':
            E = E - int(x[2])
        elif x[1] == 'F':
            F = F - int(x[2])
    elif x[0] == 'V':
        if x[1] == 'D':
            D = D + int(x[2])
        elif x[1] == 'E':
            E = E + int(x[2])
        elif x[1] == 'F':
            F = F + int(x[2])
    elif x[0] == 'A':
        if x[1] == 'D':
            D = D + int(x[3])
            if x[2] == 'E':
                E = E - int(x[3])
            elif x[2] == 'F':
                F = F - int(x[3])
        elif x[1] == 'E':
            E = E + int(x[3])
            if x[2] == 'D':
                D = D - int(x[3])
            elif x[2] == 'F':
                F = F - int(x[3])
        elif x[1] == 'F':
            F = F + int(x[3])
            if x[2] == 'D':
                D = D - int(x[3])
            elif x[2] == 'E':
                E = E - int(x[3])
print(D, E, F)
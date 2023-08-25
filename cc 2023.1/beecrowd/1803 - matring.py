matring = []
string = []
size = 0
for i in range(4):
    x = list(str(input()))
    matring.append(x)
size = len(matring[0])
for i in range(1, size-1):
        f = matring[0][0] + matring[1][0] + matring[2][0] + matring[3][0]
        l = matring[0][size-1] + matring[1][size-1] + matring[2][size-1] + matring[3][size-1]
        m = matring[0][i] + matring[1][i] + matring[2][i] + matring[3][i]
        string.append(chr((int(f) * int(m) + int(l))%257))
print(''.join(string))
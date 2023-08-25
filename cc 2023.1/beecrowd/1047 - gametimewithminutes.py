hi, mi, hf, mf = map(int, input().split())
if hi > hf or (hi == hf and mi > mf):
    dt = hf * 60 + mf + (24 * 60 - (hi * 60 + mi))
else:
    dt = abs((hf * 60 + mf) - (hi * 60 + mi))
dh = dt // 60
dm = dt % 60
if hf == hi and mf == mi:
    dh = 24
    dm = 0
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(dh, dm))
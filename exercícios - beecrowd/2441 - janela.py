janela = [0 for i in range(600)]
f1, f2, f3 = map(int, input().split())
for i in range(200):
    janela[f1+i] = 1
    janela[f2+i] = 1
    janela[f3+i] = 1
print(janela.count(0) * 100)

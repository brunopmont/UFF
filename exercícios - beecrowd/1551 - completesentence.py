n = int(input())
for i in range(n):
    alf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alfnafrase = []
    frase = list(input())
    for i in range(26):
        if alf[i] in frase:
            alfnafrase.append(alf[i])
    if len(alfnafrase) == 26:
        stts = 'frase completa'
    elif len(alfnafrase) > 13:
        stts = 'frase quase completa'
    else:
        stts = 'frase mal elaborada'
    print(stts)
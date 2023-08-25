while True:
    try:
        soma = 0
        v = []
        m = int(input())
        c = 0
        resultado = ''
        for i in range(m):
            r = int(input())
            v.append(r)
        v.reverse()
        n = int(input())
        for j in range(0,m):
            if j % n == 0:
                soma = soma + v[j]
        for k in range(2, soma):
            if soma % k == 0:
                resultado = 'Bad boy! I’ll hit you.'
                break
            else:
                resultado = 'You’re a coastal aircraft, Robbie, a large silver aircraft.'
        if soma == 0:
            resultado = 'Bad boy! I’ll hit you.'
        if soma == 1:
            resultado = 'Bad boy! I’ll hit you.'
        if soma == 2:
            resultado = 'You’re a coastal aircraft, Robbie, a large silver aircraft.'
        print(resultado)
    except EOFError:
        break

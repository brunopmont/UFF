def encrypt(lista):
    for i in range(len(lista)):
        x = ord(lista[i])
        if((x >= 65 and x<= 90) or (x >= 97 and x<= 122)):
            lista[i] = chr(x+3)
    lista.reverse()
    pL = "".join(lista)
    return(pL)

def shiftchr(lista):
    for i in range(int(len(lista)/2),len(lista)):
        lista[i] = chr(ord(lista[i])-1)
    pL = "".join(lista)
    return(pL)

n = int(input())
for i in range(n):
    pL = encrypt([x for x in input()])
    pL = shiftchr([x for x in pL])
    print(pL)
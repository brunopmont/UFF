n1, n2, n3, n4 = map(float, input().split())
media = (n1*2 + n2*3 + n3*4 + n4*1) / 10
print("Media: {:.1f}".format(media))
if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
elif 5 <= media < 7:
    print("Aluno em exame.")
    ne = float(input(""))
    print("Nota do exame: {}".format(ne))
    mf = (media + ne) / 2
    if mf >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(mf))
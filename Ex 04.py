#NOTA:
try:
    nota = float(input("Digite sua nota: "))
    if nota < 0 or nota > 10:
        raise ValueError
except ValueError:
    print("Erro: A nota é Inválida.")
else:
    if nota >= 6:
        print("Aprovado!!")
    else:
        print("Reprovado :(")
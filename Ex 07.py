
def retorna_indice(lista,indice):
    try:
        valor = lista[indice]
        if type (indice) != int:
            raise TypeError
    except IndexError:
        print("Não existe esse índice na lista.")
    except TypeError:
        print("O índice deve ser um valor inteiro.")    

    except Exception:
        print('Algo deu errado.')
    else:
        print("O valor correspondente ao indice [%d] é: %s" % (indice, valor))



nomes = []
for i in range (5):
    n = input("Nome: ")
    nomes.append(n)
b = input("Indice: ")

retorna_indice(nomes,b)




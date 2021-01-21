def funcao_1():
    try:
        print('Início da função')
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for i in range(15):
            print(lista[i],end=' ')
    except IndexError:
        print("\nA partir do índice [11], os valores não existem.")
    except Exception:
        print("Algo deu errado. ")
    finally:
        print('Fim da função')

print('Início do programa')
funcao_1()
print('Fim do programa')

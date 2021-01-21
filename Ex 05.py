#Validação:
continua = True
while continua:
    try:
        n = int(input("Digite um número inteiro positivo: "))
        if n <= 0:
            raise TypeError
    except ValueError:
        print("O valor informado não é do tipo inteiro. ")
    except TypeError:
        print("O valor informado deve ser positivo.")
    except Exception:
        print("Algo deu errado. ")
    else:
        continua = False
        print("O número informado é valido. O número informado foi: %d."% n)
    finally:
        print("Obrigado por usar o programa. :)")

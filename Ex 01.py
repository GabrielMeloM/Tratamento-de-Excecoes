#Com tipo de INVÁLIDO:
try:
    c = int(input("Entre com um número: "))
    d = int(input("Entre com outro número: "))
    a = c/d
except ZeroDivisionError:
        print("Ops, o 2º número não pode ser zero.")
except ValueError:
    print("Ops, o 2º número de tipo inválido")
else:
    print("O resultado da divisao de %d / %d = %d" % (c,d,a))




#Com outro tipo de EXCEÇÃO - PARA PREVENIR - EXCEPTION
try:
    c = int(input("Entre com um número: "))
    d = int(input("Entre com outro número: "))
    a = c/d
except ZeroDivisionError:
        print("Ops, o 2º número não pode ser zero.")
except ValueError:
    print("Segundo número de tipo inválido")
except Exception:
    print("Ops. Algo deu ERRADO.")
else:
    print("O resultado da divisao de %d / %d = %d" % (c,d,a))
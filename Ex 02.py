#Usando ELSE: Se der tudo certo, ele mostra o resultado final.
try:
    c = int(input("Entre com um número: "))
    d = int(input("Entre com outro número: "))
except ZeroDivisionError:
    print("Ops, o 2º número não pode ser zero.")
except ValueError:
    print("Segundo número de tipo inválido")
except Exception:
    print("Ops. Algo deu ERRADO.")
else:
    print(a) 

#Usando finally independente do que aconteça o programa vai ser finalizado:  

finally:
    print('Final do programa. ')
'''Crie um dicionário para armazenar uma listagem de alunos. 
a)	Utilize como chave o RA do aluno e como valor o nome do aluno. -OK
b)	Os dados devem ser informados pelo usuário.-OK

c)	O RA de cada aluno deve ser composto por um número inteiro de exatamente 7 dígitos. -OK
-	Caso o RA informado não esteja no formato correto, deve ser gerada uma exceção do tipo
ValueError -OK
-	Caso o RA informado já exista no dicionário, deve ser gerada uma exceção do tipo TypeError.-ok

d)	Implemente a função buscar, que recebe como parâmetros de entrada o dicionário e o RA de
um aluno e retorna o nome desse aluno.
-	Caso o RA não exista no dicionário, a função deve gerar uma exceção KeyError

Observação: Você pode utilizar o código abaixo como exemplo e alterá-lo para gerar e tratar as exceções solicitadas.
'''

def buscar(dicionario, ra):
    try:
        if ra not in dicionario:
            raise KeyError
    except KeyError:
        print("RA não existe nesse dicionário. ")
    else:
        print(dicionario[ra])
    finally:
        print("Encerrando Programa...")
        
for i in range(5):
    repetir = True
    while repetir == True:
        try:
            ra = input('RA: ')
            qtd = len(ra)
            if qtd != 7:
                raise ValueError
            if ra in alunos:
                raise TypeError
            nome = input('Nome: ')
            alunos[ra] = nome
        except ValueError:
            print("RA incorreto. Verifique e tente novamente.")
        except TypeError:
            print("Esse número já foi cadastrado.")
        except Exception:
            print("Ops...\nAlgo deu errado")
        else:
            repetir = False


buscar(alunos, '1234567')

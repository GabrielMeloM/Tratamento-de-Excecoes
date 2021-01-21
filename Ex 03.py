
try:
    a = int(input("Digite um valor: "))
    if a <= 0:
        raise ValueError
except ValueError:
    print("O número informado deve ser maior que zero.")
except Exception:
    print("Algo deu errado :(")

if cargo != "Gerente" and cargo != 'Analista' and cargo != 'Gerente':
    raise UnboundLocalError
except UnboundLocalError:
    print("Cargo não existe nessa empresa")

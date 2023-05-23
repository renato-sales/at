while(True):
    nome = input("Digite o seu nome completo: ")
    try:
        ano = int(input("Digite o ano do seu nascimento: "))
        if ano >= 1922 and ano <= 2021:
            print("Nome: ", nome)
            print("Idade: ", (2022 - ano), " anos")
            break
        else:
            print("Você digitou um ano fora do intervalo estabelecido")
    except:
        print("Caracter inválido")

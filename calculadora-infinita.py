while(True):
    escolha = int(input("Digite 1: SOMA | 2: SUBTRAÇÃO | 3: MULTIPLICAÇÃO | 4: DIVISÃO | 0: SAIR "))
    if escolha == 0:
        break

    numero1 = int(input("Digite o primeiro valor "))
    numero2 = int(input("Digite o segundo valor "))

    def calculadora(numero1, numero2, operador):
        if operador == 1:
            operacao = numero1 + numero2
        elif operador == 2:
            operacao = numero1 - numero2
        elif operador == 3:
            operacao = numero1 * numero2
        elif operador == 4:
            operacao =  numero1 / numero2
        else:
            return
        return operacao
    
    resultado = calculadora(numero1,numero2,escolha)
    print("Resultado da operação: ", resultado)

print("Programa finalizado!")

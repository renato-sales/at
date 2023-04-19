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
        return 0
    return operacao

escolha = int(input(print("Digite 1: SOMA | 2: SUBTRAÇÃO | 3: MULTIPLICAÇÃO | 4: DIVISÃO " )))
resultado = calculadora(2,2,escolha)
print("Resultado da operação: ", resultado)

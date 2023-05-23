print("Resolução com FOR:")
for i in range(1,21,1):
    if i == 13:
        continue
    print(i,"º andar")

print("Resolução com WHILE:")
cont = 1
while (cont < 21):
    if cont != 13:
        print(cont,"º andar")
    cont = cont + 1

print("Outra resolução com WHILE:")
contador = 0
while (True):
    contador = contador + 1
    if contador > 20:
        break
    if contador != 13:
        print(contador,"º andar")
    
print("Resolução com WHILE, imprimindo em ordem decrescente:")
cont = 20
while (cont > 0):
    if cont != 13:
        print(cont,"º andar")
    cont = cont - 1

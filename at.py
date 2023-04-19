quantidadeRodas = int(input("Digite a quantidade de rodas do veículo: " ))
quantidadePessoas = int(input("Digite a quantidade de pessoas no veículo: "))
pesoBruto = int(input("Digite a quantidade de peso no veículo: "))

if quantidadeRodas > 1 and quantidadeRodas < 4:
	print("Veículos com duas ou três rodas")

elif quantidadeRodas == 4 and quantidadePessoas < 9 and pesoBruto <= 3500:
	print("Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;")

elif quantidadeRodas >= 4 and (pesoBruto >= 3500 and pesoBruto <= 6000):
	print("Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg")

elif quantidadeRodas >= 4 and quantidadePessoas > 8:
	print("Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas")

elif quantidadeRodas >= 4 and pesoBruto > 6000:
	print("Veículos com quatro rodas ou mais e com mais de 6000 kg")

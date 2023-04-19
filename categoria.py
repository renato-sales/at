quantidadeRodas = int(input("Digite a quantidade de rodas do veículo: " ))
quantidadePessoas = int(input("Digite a quantidade de pessoas no veículo: "))
pesoBruto = int(input("Digite a quantidade de peso no veículo: "))

if quantidadeRodas > 1 and quantidadeRodas < 4:
	print("Categoria A")

elif quantidadeRodas == 4 and quantidadePessoas < 9 and pesoBruto <= 3500:
	print("Categoria B")

elif quantidadeRodas >= 4 and (pesoBruto >= 3500 and pesoBruto <= 6000):
	print("Categoria C")

elif quantidadeRodas >= 4 and quantidadePessoas > 8:
	print("Categoria D")

elif quantidadeRodas >= 4 and pesoBruto > 6000:
	print("Categoria E")

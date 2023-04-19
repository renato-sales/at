programa
{
	funcao inicio()
	{
		inteiro quantidadeRodas = 4, quantidadePessoas = 0
		real pesoBruto = 6001

		se(quantidadeRodas > 1 e quantidadeRodas < 4){
			escreva("Veículos com duas ou três rodas")
		}
		senao se(quantidadeRodas == 4 e quantidadePessoas < 9 e pesoBruto <= 3500){
			escreva("Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;")
		}
		senao se(quantidadeRodas >= 4 e (pesoBruto >= 3500 e pesoBruto <= 6000)){
			escreva("Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg")
		}
		senao se (quantidadeRodas >= 4 e quantidadePessoas > 8){
			escreva("Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas")
		}
		senao se(quantidadeRodas >= 4 e pesoBruto > 6000){
			escreva("Veículos com quatro rodas ou mais e com mais de 6000 kg")
		}
	}
}

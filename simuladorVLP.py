investimentoInicial = float(input("Informe o investimento inicial: \n"))
taxaDesconto = float(input("Informe taxa de desconto: \n"))
taxaPorcentagem = taxaDesconto / 100

contador = 1
qntFluxocaixa = int(input("Quantos anos você tem previsto de fluxo de caixa: \n"))
valorPresenteLiquido = 0

while contador <= qntFluxocaixa:
    faturamento = float(input(f"Digite o valor do faturamento do ano {contador}: "))
    valorPresenteLiquido += faturamento / (1+taxaPorcentagem) ** contador
    contador += 1


if (valorPresenteLiquido - investimentoInicial) > 0:
    print(f"Seuprojeto é viavel")
else:
    print(f"Seu projeto é inviavel")

payback = valorPresenteLiquido/investimentoInicial

if payback > 1:
    print(f"A empreja já pagou")
else:
    print("A empresa ainda não se pagou")
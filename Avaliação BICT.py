import os


dic_compras = {'produtos': ["Milka com oreo", "Nutella", "Laka", "Doce de Leite", "Biscoito Passa-tempo"
	, "Dentaduras Fini", "Bis Chocolate Branco", "Amendoim Japones", "Sonho de Valsa", "Ouro Branco", "Baton"
	, "Kinder ovo", "Tortuguita", "Fandangos", "Pringles", "Ruffles"]
	, 'precos': [13.50, 9.00, 5.00, 6.00, 2.30, 4.99, 3.99, 2.00,1.00, 1.00, 0.75, 7.40, 1.20, 6.60, 13.00, 7.00]
	, 'estoque':  [9, 10, 13, 4, 23, 6, 15, 8, 40, 34, 20, 12, 21, 5, 3, 7]}

		
def switch(case,Total,carrinho):
	os.system('cls' if os.name == 'nt' else 'clear')
	if case == "1":
		print("\n************ Lista de Produtos ************\n")
		lista_produto()
	elif case == '2':
		carrinho,Total = Compras(Total,carrinho)
		return carrinho,Total

	elif case == '3':
		carrinho = Lista_Compras(Total,carrinho)
		Total = Total
		return carrinho,Total
	elif case == "4":
		return exit()
	else:
		print("\nOperação inválida!\n")
	return carrinho,Total


def lista_produto():
	
	for i in range(16):
		print(f"""\n{i}.{dic_compras['produtos'][i]}
  Preço: R${dic_compras['precos'][i]} 
  Quantidade: {dic_compras['estoque'][i]}""")


def Compras(Total,carrinho):

	print('\nQual o produto que deseja?')
	lista_produto()
	Produto = input('\nDigite o número do produto: ' )

	for i,produtos in enumerate(dic_compras['produtos']):
		if str(i) == Produto:
			if dic_compras['estoque'][i] == 0:
				print('\nAcabou o estoque desse produto!')
			else:
				Qtd = int(input('\nDigite a Quantidade que deseja: '))
				if Qtd > dic_compras['estoque'][i]:
					print('\nExcedeu a quantidade disponível do produto!')
				else:
					dic_compras['estoque'][i] = dic_compras['estoque'][i] - Qtd
					Preço = dic_compras['precos'][i] * Qtd
					Total += Preço
					carrinho, Total = Carrinho(dic_compras['produtos'][i],Qtd,Preço,Total,carrinho)

	return carrinho,Total


def Carrinho(Produto,Qtd,Preço,Total,carrinho):

	k = 0
	for i,compra in enumerate(carrinho['Produto']):
		if Produto == compra:
			carrinho['Qtd'][i] = carrinho['Qtd'][i] + Qtd
			carrinho['Preço'][i] = carrinho['Preço'][i] + Preço
			k = 1
		else:
			pass
	if k == 0:
		carrinho['Produto'].append(Produto)
		carrinho['Qtd'].append(Qtd)
		carrinho['Preço'].append(Preço)
	else:
		pass

	carrinho, Total = Lista_Compras(Total,carrinho)

	return carrinho,Total
	

def Lista_Compras(Total,compras):

	carrinho = compras

	if Total == 0:
		print("\nCarrinho Vazio!")
	else:
		print('\n************ Seu Carrinho ************')
		print('\n--------Produto-------Quantidade--------Preço--------')
		for i in range(len(carrinho['Qtd'])):
			print(f"\t{carrinho['Produto'][i]}\t\t{carrinho['Qtd'][i]}\t\t\tR${carrinho['Preço'][i]}")
		print(f'\nValor Total: R${Total}')
		print('\nDeseja Confirmar o pedido? S ou N')
		pag = input()

		if pag == 'S' or pag == 's' or pag == "Sim" or pag == "sim":
			carrinho,Total = pagamento(Total,carrinho)
		else:
			pass
		return carrinho,Total

def pagamento(Total, carrinho):
	print('\nMétodo de Pagamento: 1 Cartão / 2 Dinheiro')
	metodo = input()
	if metodo == '2':
		Total = Total - (Total * (10/100))
	else:
		Total = Total

	print('\nValor que será pago: ')
	valor = input()
	if Total > int(valor):
		print('Erro no pagamento!')
	else:
		troco = int(valor) - Total
		print(f'\nSeu troco foi: R${troco}')

		céd = 100
		totcéd = 0
		while True:
			if troco >= céd:
				troco -= céd
				totcéd += 1
			else:
				if totcéd > 0:
					print(f'Total de {totcéd} cédulas de  R${céd}')
				if céd == 100:
					céd = 50
				elif céd == 50:
					céd = 20
				elif céd == 20:
					céd = 10
				elif céd == 10:
					céd = 5
				elif céd == 5:
					céd = 1
				totcéd = 0
				if troco == 0 or troco < 1:
					break
		print('\nAgradecemos a sua compra, Volte Sempre!')
		carrinho = {'Produto':[],'Qtd':[],'Preço':[]}
		Total = 0
	return carrinho,Total


carrinho = {'Produto':[],'Qtd':[],'Preço':[]}
Total = 0

while True:
	print( '''
************ Menu de Opções ************

    	1.Lista de Produtos
    	2.Comprar Produtos
    	3.Carrinho de Compras
    	4.Encerrar o Programa
    	''' )
	case = input("Selecione o método: ")
	carrinho,Total = switch(case,Total,carrinho)
	input('\n***Aperte enter para continuar***')
	os.system('cls' if os.name == 'nt' else 'clear')

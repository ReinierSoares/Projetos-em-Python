# Cálculos Numéricos em Python - IFMA

import math
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Somatório de 1 a n termos
def somatorio(x):
    if x == 1:
        return 1
    else:
        return x + somatorio(x-1)

# Fatorial de x
def fatorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * fatorial(x-1)

# Série de Taylor para cálculo de uma exponencial (e^x)
def Taylor_exp(x):
	sum_exp = 0
	for n in range(0, 100):
		sum_exp += ((x ** n) / fatorial(n)) 
	return sum_exp

# Série de Taylor para cálculo do seno(x) em radianos
def Taylor_sin(x):
	sum_sin = 0
	for n in range(0, 100):
		sum_sin += (x ** ((2 * n) + 1)) * (((-1) ** n)/(fatorial((2*n)+1)))

	return sum_sin

# Série de Taylor para cálculo do cosseno(x) em radianos
def Taylor_cos(x):
	sum_cos = 0
	for n in range(0, 100):
		sum_cos += (x ** (2 * n))*((-1) ** n)/fatorial(2 * n)

	return sum_cos

# Método do Ponto fixo

# Método de Newton para o cálculo de raízes quadradas de um número positivo
def Raiz_Newton(x):
	xo = 1
	Tol = 0.000001

	def f(x):
		f = ((xo ** 2) - x)
		return f

	def f_linha(x):
		F_linha = 2 * xo	
		return F_linha

	while abs(f(x)) > Tol: 
		print(f"xo: {xo:.5f} | f(xo): {f(x):.5f}")
		print("-----------------------------------")
		xo = xo - f(x) / f_linha(x)

	return float(xo)

# Conversor de Graus para radiano
def Rad_Grau(rad):
	grau = rad * (180/math.pi)

	return grau

# Interpolação Linear da reta que passa por dois pontos
def Inter_Linear(x):
	x0 = int(input("\nDigite um ponto x0: "))
	x1 = int(input("\nDigite um ponto x1: "))

	y0 = int(input("\nDigite um ponto y0: "))
	y1 = int(input("\nDigite um ponto y1: "))

	y = y0 + ((x - x0) * ((y1 - y0) / (x1 - x0)))
	return y

# Método de Newton - Gregory
def Newton_Gregory(x):
	somatorio()

# Interpolação de Newton
def Interp_Newton(x,y,xp):
    n = len(x)
    fdd = [[None for x in range(n)] for x in range(n)]

    for i in range(n):
        fdd[i][0] = y[i]

    for j in range(1,n):
        for i in range(n-j):
            fdd[i][j] = (fdd[i+1][j-1] - fdd[i][j-1]) / (x[i+j] - x[i])

    xterm = 1
    yint = fdd[0][0]

    for order in range(1,n):
        xterm *= (xp - x[order - 1])
        yint += fdd[0][order] * xterm

    return float(yint)
	
# Operação Inválida
def default():
    print("\nOperação inválida!\n")

# Seleção da Operação
def switch(case):

	if case == "1":
		x = int(input("\nSomatório que deseja calcular: "))
		return print(f"O Somatório de 1 até {x} é: {somatorio(x)}")

	elif case == "2":
		x = int(input("\nFatorial que deseja calcular: "))
		return print(f"O Fatorial de {x} é: {fatorial(x)}")

	elif case == "3":
		x = int(input("\nA Exponencial que deseja calcular: "))
		return print(f"A exponencial de {x} é: {Taylor_exp(x):.9f}")

	elif case == "4":
		x = int(input("\nSeno que deseja calcular: "))
		return print(f"O Seno de {x} em radianos é: {Taylor_sin(x):.10f}")

	elif case == "5":
		x = int(input("\nCosseno que deseja calcular: "))
		return print(f"O Cosseno de {x} em radianos é: {Taylor_cos(x):.10f}")

	elif case == "6":
		x = int(input("\nRaíz que deseja calcular: "))
		return print(f"\nA raíz de {x} é: {Raiz_Newton(x):.4f}")

	elif case == "7":
		rad = float(input("\nO Radiano que quer em Graus: "))
		return print(f"O valor de {int(rad)} radiano em graus é: {Rad_Grau(rad):.5f}")

	elif case == "8":
		print("\nForma: Y = y0 + (X-x0)(y1-y0/x1-x0)")
		x = int(input("\nDigite o ponto X que queira calcular: "))
		return print(f"\nO Y do ponto escolhido {x} é: {Inter_Linear(x)}")

	elif case == "9":
		x = [0, 1, 2, 3]
		y = [5, 10, 30, 55]
		xp = float(input("Digite um numero x: "))
		yp = Interp_Newton(x,y,xp)
		print(f"O Y do ponto escolhido {xp} é: {yp}")
	# Mostrar o Gráfico da Curva
		t  = np.arange(-1.0, 5.0, 0.1)
		yt = []
		for i in t:
			yt.append(Interp_Newton(x,y,i))
		plt.plot(t,yt,'b-')
		plt.plot(x,y,'ro')
		plt.plot(xp,yp,'g*')
		plt.grid()
		plt.show()
		return 

	elif case == "10":
		return Newton_Gregory()

	elif case == "11":
		return exit()

	else:
		return default()

# Menu de escolha
while True:
    print( '''
************ Menu de Opções ************

    	1.  Somatório
    	2.  Fatorial
    	3.  Exponencial
    	4.  Seno em Radiano
    	5.  Cosseno em Radiano
    	6.  Raíz Quadrada
    	7.  Radiano para Graus
    	8.  Interpolação Linear
    	9.  Interpolação de Newton
    	10. Método de Newton-Gregory
    	11. Encerrar o Programa
    	''' )
    case = input("Selecione o método: ")
    switch(case)
    input('\nAperte enter para continuar')
    os.system('cls' if os.name == 'nt' else 'clear')
			


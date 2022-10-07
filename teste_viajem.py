"""Desafio
Rubens quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem de carro, sendo que seu carro faz 12 KM/L. Como ele não sabe fazer um programa que o auxiliar nessa missão, ele te pede ajuda. durante a viagem o tempo de viagem, deve-se gasto em tempo e a mesma velocidade média em km/h. Assim, você conseguirá passar para Rubens qual a distância percorrida e, calcular quantos litros será possível fazer em seguida a viagem que ele quer. Mostre o valor com 3 casas decimais após o ponto.

Entrada
O arquivo de entrada contém dois inteiros. O primeiro é o tempo gasto na viagem em horas e segundo é a velocidade média durante a mesma em km/h.

Saída
Imprima a quantidade de litros necessários para realizar a viagem, com três dígitos após o ponto decimal

 
Exemplo de Entrada Exemplo de Saída
10 85

70.833

"""
entrada = input().split()

tempo = int(entrada[0])
velocidade_m = int (entrada[1])


distancia = (tempo * velocidade_m)
litros = distancia/12

print(f"{(litros):.3f}")
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Digite o Ângulo que você deseja saber o seno, cosseno e tangente: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))


print(f'O Ângulo {angulo} tem o Seno de {seno:.2f}, o Cosseno de {cosseno:.2f} e a Tangente de {tangente:.2f}')


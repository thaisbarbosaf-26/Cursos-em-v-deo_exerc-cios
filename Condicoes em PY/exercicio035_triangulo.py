# Criar um programa que leia 3 valores e mostre se é possível formar um triÂngulo com eles.

a = float(input('Digite o valor do primeiro segmento de reta: '))
b = float(input('Digite o valor do segundo segmento de reta: '))
c = float(input('Digite o valor do terceiro segmento de reta: '))

if a+b > c and a+c > b and b+c > a:
    print(f'É possível formar um triangulo com os segmentos de reta {a}, {b} e {c}')

else:
    print(f'Não é possível formar um triângulo com os segmentos de reta {a}, {b} e {c}')

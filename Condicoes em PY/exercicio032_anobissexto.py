# Leia um número e informe se ele é bissexto ou não.

i = int(input('Digite o ano que vc deseja saber se é bissexto ou não (formato xxxx): '))


if i % 4 == 0 or i % 400 == 0:
    print(f'O ano {i} é bissexto.')
else:
    print(f'O ano {i} não é bissexto.')
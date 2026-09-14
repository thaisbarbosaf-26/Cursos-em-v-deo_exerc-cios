# O programa deve ler um número interio e informar se ela é par ou ímpar.

x = int(input('Digite um número inteiro, e saiba se ele é par ou ímpar: '))

if x % 2 == 0:
    print(f' O número {x} é PAR.')

else:
    print(f' O número {x} é ÍMPAR.')

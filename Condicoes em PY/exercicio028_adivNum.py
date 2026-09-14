# Adivinhe um número entre 0 e 5. E informe na tela se venceu ou perdeu.
#o número premiado é o 2.

nome = str(input('Qual é o seu nome? ')).strip()

#OPÇÃO 1: Considerando o número premiado = 2.
# num = int(input('Adivinhe o número premiado entre 0 e 5: '))

# if num == 2:
#     print(f'PARABÉNS {nome}! Você ACERTOU o número premiado!')

# else:
#     print(f'{nome} você ERROU o número premiado! O número premiado era 2.')


#opção 2: Considerando o número premiado aleatório entre 0 e 5.
import random
num = random.randint(0, 5)

x = int(input(f'{nome}! Adivinhe o número premiado entre 0 e 5: '))

if x == num:
    print(f'PARABÉNS {nome} ! Você ACERTOU o número premiado!!')

else:
    print(f'{nome}, você ERROU! O número premiado era o {num}.')


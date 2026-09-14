#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor.

i = int(input('Digite um número inteiro: '))

print('O número sucessor a este é o: {}'.format(i + 1))
print('O número antecessor a este é o: {}'.format(i - 1))


# #Outras formas de fazer:
# #OPÇÃO 1
# s = i + 1
# a = i - 1
# print('Considerando {}, O número sucessor é o: {} e o antecessor é o: {}'.format(i, s, a))


# #OPÇÃO 2
# print('Considerando {}, seu sucessor é: {} e seu antecessor é: {}'.format(i, (i + 1), (i - 1)))



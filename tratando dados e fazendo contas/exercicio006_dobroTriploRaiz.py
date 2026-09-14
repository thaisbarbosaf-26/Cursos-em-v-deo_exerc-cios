#Desafio 006: Montar um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada.
i = int(input('Digite um número: '))

print(f'O dobro desse número é: {i * 2}')
print(f'O triplo desse número é: {i * 3}')
print(f'A raiz quadrada desse número é: {i ** (1/2):.2f}')


# #Outras formas de fazer:    
# #OPÇÃO 1
# d = i * 2
# t = i * 3
# r = i ** (1/2)
# #print(f'O dobro desse número é: {d}, O triplo desse número é: {t} e A raiz quadrada desse número é: {r:.2f}')

# #OPÇÃO 2
# print('O dobro de {} é: {}, o triplo é: {} e a raiz quadrada é: {:.2f}.'.format(i, d, t, r))

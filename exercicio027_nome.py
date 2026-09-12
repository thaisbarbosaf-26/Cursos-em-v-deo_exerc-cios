#Programa que leia o nome completo de uma pessoa, que mostre o primeiro e o útlimo nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip().split()
print(f' Seu primeiro nome é: {nome[0]}')
print(f' E o último nome é: {nome[-1]}')

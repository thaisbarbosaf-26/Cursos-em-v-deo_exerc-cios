#Criar um programa que leia o nome de uma cidade e diga se consta o nome "Silva" em qualquer parte do nome da cidade:

cidade = input('Digite o nome da cidade: ').strip()

print('silva' in cidade.lower()) #lower p/ deixar tudo minúsculo e facilitar a busca, pois o usuário pode digitar "Silva" ou "silva" ou "SILVA" etc.

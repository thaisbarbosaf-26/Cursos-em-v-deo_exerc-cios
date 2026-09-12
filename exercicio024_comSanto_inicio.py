#Criar um programa que leia o nome de uma cidade e diga se começa ou não com o nome "Santo":

cidade = str(input('Digite o nome da cidade: ')).strip()

if cidade[:5].upper() == 'SANTO':
    print('A cidade começa com "Santo".')
else:
    print('A cidade não começa com "Santo".')
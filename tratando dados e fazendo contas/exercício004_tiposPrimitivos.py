i = input('Digite algo: ')

print('O tipo primitivo desse dado é',type(i))
print('Só tem espaços?', i.isspace())
print('É um número?', i.isnumeric())
print('É alfabético?', i.isalpha())
print('É alfanumérico?', i.isalnum())
print('Está em maiúsculas?', i.isupper())
print('Está em minúsculas?', i.islower())
print('Está capitalizada? (upper/lower)', i.istitle())

'''
# OUTRA FORMA DE FAZER O PRINT ACIMA É USANDO O .FORMAT() PARA COLOCAR TUDO EM UMA LINHA SÓ, COMO ABAIXO:
print('O tipo primitivo desse dado é {}, Só tem espaços? {}, É um número? {}, É alfabético? {}, É alfanumérico? {}, Está em maiúsculas? {}, Está em minúsculas? {}, Está capitalizada? {}'.format(type(i), i.isspace(), i.isnumeric(), i.isalpha(), i.isalnum(), i.isupper(), i.islower(), i.istitle()))
'''



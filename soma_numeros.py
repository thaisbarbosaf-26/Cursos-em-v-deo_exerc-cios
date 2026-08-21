n1 = int(input('Digite um número: ' ))
n2 = int(input('Digite outro número: ' ))
soma = n1 + n2

#Forma 1 de "print" 
#print ('A soma dos números é:', soma)

#Forma 2 de "print"
#print ('A soma entre: ', n1, 'e', n2, 'é igual a: ', soma) 

#Forma 3 de "print"
print ('A soma entre {} e {} é igual a: {}'.format(n1, n2, soma))

#2ª PARTE P/ SABER O TIPO DE VARIÁVEL E TIPO PRIMITIVO

i = input('Digite algo p/ saber o tipo de variável e seu tipo primitivo: ')
#P/ saber o tipo da variável
print(type(i))

#p/ saber seu tipo primitivo
print("Isso é um número? ", i.isnumeric())
print("Isso é uma letra? ", i.isalpha())
print("Está em maiúscula? ", i.isupper())
print("Está em minúscula? ", i.islower())

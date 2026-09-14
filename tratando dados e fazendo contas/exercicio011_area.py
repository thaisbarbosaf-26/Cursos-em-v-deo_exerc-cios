#Informe a largura e a altura de uma parede em metros, e calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

l = float(input('Informe a largura da parede em metros: '))
a = float(input('Informe a altura da parede em metros: '))

area = l * a
tinta_necessaria = area / 2

print(50 * '=')
print(f' A área total da parede é: {area:.2f} m²')
print(f' Sabendo que cada litro de tinta pinta 2 m², você vai precisar de {tinta_necessaria:.2f} litros de tinta para pintar a parede.')

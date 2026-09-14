# O programa deve ler 3 números e informar o maior e o menor entre eles.

x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))
z = float(input('Digite o terceiro número: '))

if x > y and x > z:
    print(f'O maior número é {x}.')
if y > x and y > z:
    print(f'O maior número é {y}.')
if z > x and z > y:
    print(f'O maior número é {z}.')

if x < y and x < z:
    print(f'O menor número é {x}.')
if y < x and y < z:
    print(f'O menor número é {y}.')
if z < x and z < y:
    print(f'O menor número é {z}.')



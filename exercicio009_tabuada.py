#Digite um número inteiro e mostre a tabuada deste número.

n = int(input('Qual número você deseja saber a tabuada?: '))

print('=' * 18)

for i in range (1, 11):


    print(n, 'x', i, '=', n * i)


print('=' * 18)


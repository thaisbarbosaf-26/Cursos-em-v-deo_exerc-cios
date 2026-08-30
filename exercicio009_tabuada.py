#Digite um número inteiro e mostre a tabuada deste número.

n = int(input('Qual número você deseja saber a tabuada?: '))

for i in range (1, 11):

    print(n, 'x', i, '=', n * i)



# O desafio é sortear a ordem de apresentação de trabalho de 4 alunos. A ordem deve ser aleatória.

n1 = str(input('Informe o nome do aluno 1: '))
n2 = str(input('Informe o nome do aluno 2: '))
n3 = str(input('Informe o nome do aluno 3: '))
n4 = str(input('Informe o nome do aluno 4: '))

alunos = [n1, n2, n3, n4]

#OPÇÃO 1: Utilizando a biblioteca random:
#import random
#random.shuffle(alunos)

#OPÇÃO 2: Outra forma de utilizar a biblioteca:
from random import shuffle
shuffle(alunos)

print(f'A ordem de apresentação do trabalaho será: {alunos}')

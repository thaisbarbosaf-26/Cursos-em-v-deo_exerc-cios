#Tarefa: Sortear entre 4 alunos, um deles para apagar o quadro:

#import random    --> OPÇÃO 1:

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]

#escolhido = random.choice(lista)  --> OPÇÃO 1:


#OPÇÃO 2: Outra forma de utilizar a biblioteca:
from random import choice
escolhido = choice(lista)

print(f'O aluno escolhido para apagar o quadro foi: {escolhido}')



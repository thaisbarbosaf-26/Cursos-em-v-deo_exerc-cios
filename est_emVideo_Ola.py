#DESAFIO 1 - Ler o nome do usuário e dar boas vindas.

nome = input("Qual é o seu nome? " )

print ("Seja muito bem vindo(a), ", nome, "!")

#DESAFIO 2 - Ler dia, mês e ano de nascimento. Msd deve ter data formatada.

dia = input("Qual é o dia do seu nascimento? ")
mes = input("Qual o mês do seu nascimento? (exemplo: JAN, FEV, MAR...) ")
ano = input("Qual o ano de seu nascimento? (ex: xxxx) ")

print ("Você nasceu no dia ", dia, "de", mes, "de",ano,". Correto?")

#DESAFIO 3 - Ler dois números e mostrar a soma.

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

print ("A soma dos números é: ", int(num1) + int(num2))



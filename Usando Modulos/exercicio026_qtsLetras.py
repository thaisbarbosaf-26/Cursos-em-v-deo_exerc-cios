# Criar programa que leia uma frase e mostre:
# 1) Quantas vezes aparece a letra "A";
# 2) Em que posição ela aparece a primeira vez;
# 3) Em que posição ela aparece a última vez.

frase =str(input('Digite uma frase: ')).upper().strip()

print(f'Na frase digitada, a letra A aparece {frase.count("A")} vezes.')
print(f'A primeira letra A aparece na posição {frase.find("A")}')
print(f'A última letra A aparece na posição {frase.rfind("A")}')

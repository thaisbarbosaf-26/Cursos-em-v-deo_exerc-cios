#O programa deve calcular o aumento de salário de um funcionário. Sendo que se maior que R$ 1.250,00 o aumento deve ser de 10%, caso inferior ou igual, deve ser de 15%.

salário = float(input('Digite o valor do salário do funcionário: R$ '))

if salário > 1250.00:
    print(f'O salário do funcionário de R$ {salário:.2f}, com o aumento de 10% passará p/ R$ {salário + (salário * 0.10):.2f}')

else:
    print(f'O salário do funcionário de R$ {salário:.2f}, com o aumento de 15% passará p/ R$ {salário + (salário * 0.15):.2f}')

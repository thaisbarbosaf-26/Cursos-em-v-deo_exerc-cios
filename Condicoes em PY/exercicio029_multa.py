# O programa deve verificar se o motorista ultrapassou 80km/h. Se sim, ele deve calcular o valor da multa, cobrando R$ 7,00 por cada km acima do limite.


x = float(input('Digite a velocidade do veículo em km/h: '))

if x > 80:
    multa = (x - 80) * 7
    print(f'Você ultrapassou o limite de velocidade! Deve pagar uma multa de R$ {multa:.2f}.')
else:
    print('Você está dentro do limite de velocidade!')

    
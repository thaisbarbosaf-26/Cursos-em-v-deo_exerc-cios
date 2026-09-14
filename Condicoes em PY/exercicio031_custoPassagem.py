# Pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km p/ viagens até 200km e R$ 0,45 p/ viagens mais longas.

x = float(input('Informe quantos km de distância tem a sua viagem: '))

if x <=200:
    vlr1 = x * 0.50
    print(f'O valor da sua passagem será de R$ {vlr1:.2f}.')
else:
    vlr2 = x * 0.45
    print(f'O valor da sua passagem será de R$ {vlr2:.2f}.')

    
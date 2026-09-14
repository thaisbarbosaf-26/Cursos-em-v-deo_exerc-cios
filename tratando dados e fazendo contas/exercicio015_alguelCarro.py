#Programa deve conter a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

km_percorrido = float(input('Informe quantos km você percorreu? '))
dias = int(input('Informe quantidade de dias que você alugou o carro? '))

print(f'Se você rodou {km_percorrido:.2f} Km em {dias} dias, o valor de pagamento será R$ {(km_percorrido * 0.15) + (dias * 60):.2f}')

#Converta temperatura de °C para °F e vice-versa.
celsius = float(input('Informe a temperatura em °C que você deseja converter para °F: '))
farenheit = (((celsius * 9)/5)) + 32 #neste caso ñ seria obrigatório colocar parênteses, pq os operadores aritméticos estão na ordem de precedência.

print(f'A temperatura de {celsius}°C convertida para °F é: {farenheit:.2f}°F')
#Leia um valor em metros e converta em centimetros e milimetros.

m = float(input('Quantos metros você deseja converter em cm e mm? '))

print(f'O valor em metros que você informou são: {m*100} cm e {m * 1000} mm')

#Incluindo demais unidades de medida:
print(f'Para seu conhecimento, o resultado com as demais unidades de medida resulta no seguinte: {m / 1000} Km, {m / 100} hm, {m / 10} dam, {m * 10} dm, {m * 100} cm e {m * 1000} mm.')
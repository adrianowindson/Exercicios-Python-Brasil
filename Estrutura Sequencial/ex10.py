# 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

grauCelsius = float(input('Digite a temperatura em Celsius: '))
grauFarenheit = (grauCelsius * 1.8) + 32
print('A temperatura convertida de Celsius para Farenheit: %.2f' %grauFarenheit)
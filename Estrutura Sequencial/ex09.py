#!/usr/bin/env python3
# 9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

grauFarenheit = int(input('Temperatura em Farenheit: '))
celsius = 5 * (grauFarenheit - 32) / 9
print("O valor em Farenheit Convertido para Celsius ficou: %.2f" %celsius)


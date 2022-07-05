# 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

a =int(input('Digite um inteiro: '))
b =int(input('Digite outro inteiro: '))
c =float(input('Digite um número real: '))

produto = (b/2) * (a*2)
soma = (a*3) + c
potencia = c**3

print(produto)
print(soma)
print(potencia)
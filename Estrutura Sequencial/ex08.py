# 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

horasTrabalhadas=int(input('Quantas horas trabalha no mês? '))
valorDaHora=float(input('Qual o valor da hora de trabalho?'))

salarioMensal = horasTrabalhadas * valorDaHora
print('O valor do salário mensal é: %.2f' %salarioMensal)
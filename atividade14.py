# Exercício Python 14: Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um
# aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario=float(input("seu salario: "))
if salario > 1250:
    aumento1=salario/100*10
    print(f"salario apos o aumento: {salario+aumento1}")
else:
    aumento2=salario/100*15
    print(f"salario apos o aumento: {salario+aumento2}")
#Salário

numero = int(input())
valor = int(input())
hora = float(input())
Salario=valor*hora
Salario = round(Salario,2)
print('NUMBER = {}'.format(numero))
print('SALARY = U$ {:.2f}'.format(Salario))
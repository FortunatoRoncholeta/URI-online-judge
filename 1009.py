#Salário com Bônus
nome=input()
salarioFixo=float(input())
vendasM=float(input())
comisao=0.15


valor_comisao=vendasM*comisao
salario_real=valor_comisao+salarioFixo

print("TOTAL = R$ {:.2f}".format(salario_real))
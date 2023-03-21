# Valor que custa a hora do trabalhador.
valor_horas = float(input('Digite Quando você ganha por horas trabalhadas: '))
# valor que ele ganha por horas:
horas_trabalhadas = float(input('Digite quantas horas você trabalhou: '))
# Variavel que soma horas trabalhadas com o valor da hora.
salario = valor_horas*horas_trabalhadas
# Variavel que calcula o salario liquido usado no ultimo print.
liquido= salario*76/100
# Print com todos os resultados.
print('Seu salario bruto R$:''%.2f'% salario)
print('Imposto de renda R$:','%.2f'% (salario*11/100))
print('INSS R$:','%.2f'% (salario*8/100))
print('Sindicato R$:','%.2f'%(salario*5/100))
print('Salario liquido R$:''%.2f'%liquido)
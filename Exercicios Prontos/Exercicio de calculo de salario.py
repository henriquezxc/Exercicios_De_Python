
# Nome do funcionario.
Seu_Nome = (input("Qual seu nome: " ))

# Inserir numero de identifição do mesmo.
Id_Funcionario = int(input("Digite seu ID: " ))

# Inserir as horas trabalhadas.
Horas = float(input("Digite as horas trabalhadas: "))

# Custo por horas trabalhadas.
custo = float(input("Digite o custo por horas trabalhadas: "))

# Impresão do resultado.
resultado = (Horas*custo)
print("Com base nos dados inseridos:")

# Reemprimir o nome inserido acima.
print("Seu nome: ",Seu_Nome)

# Reemprimir o seu numero de identificação.
print("Seu numero de identificação: ",Id_Funcionario)

# Reemprimir o custo por horas digitado acima, repetimos o (%.2f"% custo) para resultado em decimais.
print("Custo por horas trabalhadas: " "%.2f"% custo,'\n')
# Criei o '\n' apenas para dar espaço.

# Imprimir seu salario bruto em 2 casas decimais usando  ( "%.2f"% resultado ).
print("Seu salario neste mês e de: " "%.2f\n"% resultado)
# Comando abaixo apenas para da ESPAÇO no codigo ao printar.

# Adicionei esse codigo para quando foi usar o python não fechar a aplicação.
input(exit)
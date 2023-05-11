# Entrada dos numero que no fim vamos ver quem e o maior deles.
Numero1 = int(input("DIgite o Primeiro numero: "))
Numero2 = int(input("Digite o Segundo numero: "))
Numero3 = int(input("Digite o Terçeiro numero: "))

# Usamos a condição 'IF' para fazer a comparação das entradas.
if Numero1>Numero2 and Numero1>Numero3:
    print("O numero: ",Numero1,"e o maior de todos")
elif Numero2>Numero1 and Numero2>Numero3:
    print("O numero: ",Numero2, "e o maior de todos")
elif Numero3>Numero1 and Numero3>Numero2:
    print("O numero: ",Numero3,"e o maior de todos")
elif Numero1 == Numero2 and Numero3:
    print("são todos iguais, não temos resultado")
# Fim
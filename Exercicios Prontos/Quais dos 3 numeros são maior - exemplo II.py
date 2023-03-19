nun1=int(input("DIgite o primeiro numero: "))
nun2=int(input("Digite o segundn numero: "))
nun3=int(input("Digite o terçeiro numero: "))

if nun1>nun2 and nun1>nun3:
    print("O numero: ",nun1,"e o maior de todos")
elif nun2>nun1 and nun2>nun3:
    print("O numero: ",nun2, "e o maior de todos")
elif nun3>nun1 and nun3>nun2:
    print("O numero: ",nun3,"e o maior de todos")
elif nun1 == nun2 and nun3:
    print("são todos iguais, não temos resultado")
# Fim
nun1=int(input("DIgite o primeiro numero: "))
nun2=int(input("Digite o segundn numero: "))
nun3=int(input("Digite o terçeiro numero: "))

# Aqui verificamos quem e maior:
if nun1>nun2 and nun1>nun3:
    print("----------------------")
    print("O maior numero e:",nun1,)
    print("----------------------")
elif nun2>nun1 and nun2>nun3:
    print("----------------------")
    print("O maior numero e:",nun2)
    print("----------------------")
elif nun3>nun1 and nun3>nun2:
    print("----------------------")
    print("O maior numero e:",nun3)
    print("----------------------")
elif nun1 == nun2 and nun3:
    print("------------------------------------------------")
    print("São todos iguais, Por isso não temos resultados.")
    print("------------------------------------------------")

# Criei essa linha para ver quem e o menor da lista:
if nun1<nun2 and nun1<nun3:
    print("---------------------")
    print("o menor numero e",nun1)
    print("---------------------")
elif nun1<nun2 and nun1<nun3:
    print("----------------------")
    print("O menor numero e:",nun1)
    print("----------------------")
elif nun2<nun1 and nun2<nun3:
    print("----------------------")
    print("O menor numero e:",nun2)
    print("----------------------")
elif nun3<nun1 and nun3<nun2:
    print("----------------------")
    print("O menor numero e: ",nun3)
    print("----------------------")
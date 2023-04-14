Numero1=int(input("DIgite o primeiro numero: "))
Numero2=int(input("Digite o segundn numero: "))
Numero3=int(input("Digite o terçeiro numero: "))

# Aqui verificamos quem e MAIOR:
if Numero1>Numero2 and Numero1>Numero3:
    print("----------------------")
    print("O maior numero e:",Numero1,)
    print("----------------------")
elif Numero2>Numero1 and Numero2>Numero3:
    print("----------------------")
    print("O maior numero e:",Numero2)
    print("----------------------")
elif Numero3>Numero1 and Numero3>Numero2:
    print("----------------------")
    print("O maior numero e:",Numero3)
    print("----------------------")
elif Numero1 == Numero2 and Numero3:
    print("------------------------------------------------")
    print("São todos iguais, Por isso não temos resultados.")
    print("------------------------------------------------")

# Criei essa linha para ver quem e o MENOR da lista:
if Numero1<Numero2 and Numero1<Numero3:
    print("---------------------")
    print("o menor numero e",Numero1)
    print("---------------------")
elif Numero1<Numero2 and Numero1<Numero3:
    print("----------------------")
    print("O menor numero e:",Numero1)
    print("----------------------")
elif Numero2<Numero1 and Numero2<Numero3:
    print("----------------------")
    print("O menor numero e:",Numero2)
    print("----------------------")
elif Numero3<Numero1 and Numero3<Numero2:
    print("----------------------")
    print("O menor numero e: ",Numero3)
    print("----------------------")
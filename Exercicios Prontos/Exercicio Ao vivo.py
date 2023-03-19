numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if (numero1 > numero2):
    print(numero1, "e maior que",numero2)
elif (numero2 > numero1):
    print(numero2, "e maior que",numero1)
else:
    print("São iguais")
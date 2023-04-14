# Neste software vamos verificar feminino ou masculo.
# Se o usuario Digitar 'M' vai retornar MASCULINO.
# Se o usuario Digitar 'F' vai retornar FEMININO.

# Insersão da letra M ou F:
Entrada_Do_Usuario = (input("Digite a letra M ou F: "))
# Resultado usando "if":
if (Entrada_Do_Usuario == "m"):
    print("Masculino")
# Criamos o "elif" para diferenciar as letras Minusculas para Maiusculas:
elif(Entrada_Do_Usuario == "f"):
    print("Feminino")
elif Entrada_Do_Usuario == "F":
    print("Feminino")
elif Entrada_Do_Usuario == "M":
    print("Masculino")
# Usamos o comando "else" para caso nenhuma das opções acima servir, imprimir o print abaixo:
else:
    print("Sexo Inválido")
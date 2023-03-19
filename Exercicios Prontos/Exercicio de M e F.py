# Insersão da letra M ou F:
mf = (input("Digite a letra M ou F: "))
# Resultado usando "if":
if (mf == "m"):
    print("Masculino")
# Criamos o "elif" para diferenciar as letras Minusculas para Maiusculas:
elif(mf == "f"):
    print("Feminino")
elif mf == "F":
    print("Feminino")
elif mf == "M":
    print("Masculino")
# Usamos o comando "else" para caso nenhuma das opções acima servir, imprimir o print abaixo:
else:
    print("Sexo Inválido")
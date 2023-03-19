# Programa que verifica se a letra e vogal ou consoante:
print("O Programa so aceita entradas Minusculas")
letra = (input("Digite uma letra: "))
# Usamos "in" 
if letra in ("a","e","i","o","u"):
    print("A letra digitada e uma Vogal")
elif letra in ("b","c","d","f","g","h","j","k","l","ç","q","w","r","s","t","v","x","z","m","n"):
    print("A letra digitada e uma Consoante")
else:
    print("Opção invalida")
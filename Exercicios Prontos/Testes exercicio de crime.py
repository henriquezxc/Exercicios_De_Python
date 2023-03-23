crime1=(input('Telefonou para a vitima?: '))
crime2=(input('Esteve no local do crime?: '))
crime3=(input('Mora perto da vitima?: '))
crime4=(input('Devia para a vitima?: '))
crime5=(input('Já trabalhou com a vitima: '))

contadorSIM=0

if contadorSIM in range (0,5):
    if crime1 == "sim":
        contadorSIM +=1
    if crime2 == 'sim':
        contadorSIM +=1
    if crime3 == 'sim':
        contadorSIM +=1
    if crime4 == 'sim':
        contadorSIM +=1
    if crime5 == 'sim':
        contadorSIM +=1
print(contadorSIM)
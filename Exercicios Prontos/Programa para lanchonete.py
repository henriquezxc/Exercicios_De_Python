# Programa para caculo de cardapio
print('____________________________________')
print('** C   A   R   D   A   P   I   O  **')
print('------------------------------------')
print('CODÍGO     ESPECIFICAÇÃO       PREÇO')
print('____________________________________')
print('  1       Cachorro Quente     R$4.00')
print('  2         X-Salada          R$4.50')
print('  3         X-Bacon           R$5.00')
print('  4       Torrada Simples     R$2.00')
print('  5        Refrigerante       R$1,50')
print('____________________________________')
# Entrada do usuario onde e inserido o codigo do produto
codigo=int(input('Digite o Codigo referente ao produto Desejado: '))
# Entrada do usuario onde e inserido a quantidade de produtos
quantidade=int(input('Digite a Quantidade: '))
# Variaveis com valores dos produtos armazenados
um= 4.00
dois= 4.50
tres= 5.00
quatro= 2.00
cinco= 1.50
# Variaveis onde vamos usar para imprimir as informaçoes no fim do codigo
somar1= (um*quantidade) 
somar2= (dois*quantidade)
somar3= (tres*quantidade)
somar4= (quatro*quantidade)
somar5= (cinco*quantidade)

if codigo ==1:
    um * quantidade
    print('%.2f'%somar1)
if codigo ==2:
    dois * quantidade
    print('%.2f'%somar2)
if codigo ==3:
    tres * quantidade
    print('%.2f'%somar3)
if codigo ==4:
    quatro* quantidade
    print('%.2f'%somar4)
if codigo ==5:
    cinco* quantidade
    print('%.2f'%somar5)
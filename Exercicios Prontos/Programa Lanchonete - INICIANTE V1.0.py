# Programa para calculo de cardapio
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
Codigo_Do_Produto = int(input('Digite o Codigo referente ao produto Desejado: '))

# Entrada do usuario onde e inserido a quantidade de produtos
Quantidade_De_Produtos = int(input('Digite a Quantidade: '))

# Variaveis com valores dos produtos armazenados
Codigo_1 = 4.00
Codigo_2 = 4.50
Codigo_3 = 5.00
Codigo_4 = 2.00
Codigo_5 = 1.50

# Variaveis onde vamos usar para imprimir as informaçoes no fim do codigo
Soma_1 = (Codigo_1 * Quantidade_De_Produtos) 
Soma_2 = (Codigo_2 * Quantidade_De_Produtos)
Soma_3 = (Codigo_3 * Quantidade_De_Produtos)
Soma_4 = (Codigo_4 * Quantidade_De_Produtos)
Soma_5 = (Codigo_5 * Quantidade_De_Produtos)

# Usando IF Para fazer as condições de cada entrada.
if Codigo_Do_Produto == 1:
    Codigo_1 * Quantidade_De_Produtos
    print('%.2f'%Soma_1)

if Codigo_Do_Produto == 2:
    Codigo_2 * Quantidade_De_Produtos
    print('%.2f'%Soma_2)

if Codigo_Do_Produto == 3:
    Codigo_3 * Quantidade_De_Produtos
    print('%.2f'%Soma_3)

if Codigo_Do_Produto == 4:
    Codigo_4* Quantidade_De_Produtos
    print('%.2f'%Soma_4)

if Codigo_Do_Produto == 5:
    Codigo_5* Quantidade_De_Produtos
    print('%.2f'%Soma_5)
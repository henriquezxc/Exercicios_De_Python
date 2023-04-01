Lista = []
Produtos = ['Feijão','Arroz','Macarrão','Miojo']
Valores =  [ 8.59 ,   6.79   ,  2.79  ,   1.54 ]
# Printando as opões disponiveis no mercado.
print(Produtos[0],Valores[0])
print(Produtos[1],Valores[1])
print(Produtos[2],Valores[2])
print(Produtos[3],Valores[3])

Soma = Valores[0] + Valores[1]

for item in range(0,4):
    Carrinho_compras = str(input('Digite Os produtos desejado: '))
    Carrinho_Formatado = Carrinho_compras.upper
    if Carrinho_Formatado == 'FEIJAO':
        Lista.append(Carrinho_Formatado)
    if Carrinho_Formatado == 'ARROZ':
        Lista.append(Carrinho_compras)
    if Carrinho_Formatado == 'Macarrão':
        Lista.append(Carrinho_compras)
    if Carrinho_Formatado == 'Miojo':
        Lista.append(Carrinho_compras)
    
    
print(Lista)
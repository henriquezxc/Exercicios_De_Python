# Carrinho de compras onde irá receber os produtos selecionados pelo cliente.
# Ele começa vazio, pois ao longo do codigo o cliente irá adicionar como um carrinho de compras.
Carrinho = []
# Abaixo está os produtos disponiveis no Mercado:
Produtos = ['Feijão:','Arroz:','Miojo:']
Valores =  [ 8.59 ,   6.79 , 1.79 ]
# Printando as opões disponiveis no mercado:
for i in range(len(Produtos)):
    print(Produtos[i],Valores[i])
# Aqui vai a decisão do cliente, em qual produto vai escolher.    
for i in range(0,3):
    # O usuario inseri o produto desejado:
    Inserir_item_desejado = str(input('Quais os Produtos desejados: '))
    # Criamos a variavel "Input_cliente" para que toda entrada do usuario se torne Maiuscula
    # Assim não ocorre erros ao digitar letras diferentes Ex: Minusculas.
    Input_cliente = Inserir_item_desejado.upper()
    # Condicional para acrescentar os produtos na lista de compras
    if Input_cliente == 'FEIJAO':
        # Vamos apenas subir os valores para "Carrinho" para depois soma-los:
        Carrinho.append (Valores[0])
    if Input_cliente == 'ARROZ':
        Carrinho.append (Valores[1])
    if Input_cliente == 'MIOJO':
        Carrinho.append (Valores[2])
# Imprimir a soma do carrinho usando a função "SUM".
soma = sum(Carrinho)
print('Total a ser pago: R$ %.2f' % soma)
# Agradecimentos.
print("Obrigado pela compra! Esperamos que tenha gostado dos nossos produtos. Volte sempre!")










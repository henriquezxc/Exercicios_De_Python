# Programa para caculo de cardapio
print('___________________________________')
print('     L̲a̲n̲c̲h̲o̲n̲e̲t̲e̲ B̲e̲s̲t̲ L̲a̲n̲c̲h̲e̲s̲ 🍰    ')
print('____________________________________')
print('** C   A   R   D   A   P   I   O  **')
print('------------------------------------')
print('CODÍGO     ESPECIFICAÇÃO       PREÇO')
print('____________________________________')
print('  1       Cachorro Quente 🌭  R$4.00')
print('  2         X-Salada   🍔     R$4.50')
print('  3         X-Bacon    🍔     R$5.00')
print('  4       Torrada Simples 🥪  R$2.00')
print('  5        Refrigerante  🍾   R$1,50')
print('____________________________________')
# Entrada do usuario onde e inserido o codigo do produto.
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

import datetime
Horas = datetime.datetime.now()
Data_formatada = Horas.strftime("%d/%m/%y")
Hora_formatada = Horas.strftime("%H:%M:%S")

if codigo ==1:
    um * quantidade
    print('-------------------------------------------------')
    print( 'Sᴇᴜ ʟᴀɴᴄʜᴇ ғɪᴄᴏᴜ ɴᴏ ᴠᴀʟᴏʀ ᴅᴇ: R$',('%.2f'%somar1))
    print('-------------------------------------------------')
    notafiscal1= input('Dᴇsᴇᴊᴀ ɪᴍᴘʀɪᴍɪʀ ᴀ ɴᴏᴛᴀ ғɪᴄᴀʟ ᴅᴇsᴛᴀ ᴄᴏᴍᴘʀᴀ? SIM ᴏᴜ NÃO ?:')
    if notafiscal1 in ('sim','SIM','Sim'):
        print('_______________________')
        print(' N O T A   F I S C A L ')
        print(f' {Data_formatada}     {Hora_formatada}')
        print('Lanchonete Best Lanches')
        print('Produto Selecionado: - Cachorro Quente:')
        print('Código Do produto -------------------',codigo)
        print('Unidades --------------------------',quantidade,'x')
        print('Valor ------------------------ R$:',('%.2f'%somar1))
        print('_____________________________________________')
        print('𝙫𝙤𝙡𝙩𝙚 𝙨𝙚𝙢𝙥𝙧𝙚 🍔')
    if notafiscal1 in ('nao','Nao','NAO'):
        print('OK, Bom apetite e volte Sempre ')

if codigo ==2:
     dois * quantidade
     print('-------------------------------------------------')
     print(' Sᴇᴜ ʟᴀɴᴄʜᴇ ғɪᴄᴏᴜ ɴᴏ ᴠᴀʟᴏʀ ᴅᴇ: R$',('%.2f'%somar2))
     print('-------------------------------------------------')
     notafiscal2= input('Dᴇsᴇᴊᴀ ɪᴍᴘʀɪᴍɪʀ ᴀ ɴᴏᴛᴀ ғɪᴄᴀʟ ᴅᴇsᴛᴀ ᴄᴏᴍᴘʀᴀ? SIM ᴏᴜ NÃO ?:')
     if notafiscal2 in ('sim','SIM','Sim'):
        quantidade = quantidade
        print('_______________________')
        print(' N O T A   F I S C A L ')
        print(f' {Data_formatada}     {Hora_formatada}')
        print('Lanchonete Best Lanches')
        print('Produto Selecionado --------- X-Salada:')
        print('Código Do produto -------------------',codigo)
        print('Unidades --------------------------',quantidade,'x')
        print('Valor ------------------------ R$:',('%.2f'%somar2))
        print('_____________________________________________')
        print('𝙫𝙤𝙡𝙩𝙚 𝙨𝙚𝙢𝙥𝙧𝙚 🍔')
     if notafiscal2 in ('nao','Nao','NAO'):
        print('OK, Bom apetite e volte Sempre ')

if codigo ==3:
    tres * quantidade
    print('-------------------------------------------------')
    print( 'Sᴇᴜ ʟᴀɴᴄʜᴇ ғɪᴄᴏᴜ ɴᴏ ᴠᴀʟᴏʀ ᴅᴇ: R$',('%.2f'%somar3))
    print('-------------------------------------------------')
    notafiscal3= input('Dᴇsᴇᴊᴀ ɪᴍᴘʀɪᴍɪʀ ᴀ ɴᴏᴛᴀ ғɪᴄᴀʟ ᴅᴇsᴛᴀ ᴄᴏᴍᴘʀᴀ? SIM ᴏᴜ NÃO ?:')
    if notafiscal3 in ('sim','SIM','Sim'):
        print('_______________________')
        print(' N O T A   F I S C A L ')
        print(f' {Data_formatada}     {Hora_formatada}')
        print('Lanchonete Best Lanches')
        print('Produto Selecionado ---------- X-Bacon:')
        print('Código Do produto -------------------',codigo)
        print('Unidades --------------------------',quantidade,'x')
        print('Valor ------------------------ R$:',('%.2f'%somar3))
        print('_____________________________________________')
        print('𝙫𝙤𝙡𝙩𝙚 𝙨𝙚𝙢𝙥𝙧𝙚 🍔')
    if notafiscal3 in ('nao','Nao','NAO'):
        print('OK, Bom apetite e volte Sempre ')

if codigo ==4:
    quatro * quantidade
    print('-------------------------------------------------')
    print( 'Sᴇᴜ ʟᴀɴᴄʜᴇ ғɪᴄᴏᴜ ɴᴏ ᴠᴀʟᴏʀ ᴅᴇ: R$',('%.2f'%somar4))
    print('-------------------------------------------------')
    notafiscal4= input('Dᴇsᴇᴊᴀ ɪᴍᴘʀɪᴍɪʀ ᴀ ɴᴏᴛᴀ ғɪᴄᴀʟ ᴅᴇsᴛᴀ ᴄᴏᴍᴘʀᴀ? SIM ᴏᴜ NÃO ?:')
    if notafiscal4 in ('sim','SIM','Sim'):
        print('_______________________')
        print(' N O T A   F I S C A L ')
        print(f' {Data_formatada}     {Hora_formatada}')
        print('Lanchonete Best Lanches')
        print('Produto Selecionado -- Torrada Simples:')
        print('Código Do produto -------------------',codigo)
        print('Unidades --------------------------',quantidade,'x')
        print('Valor ------------------------ R$:',('%.2f'%somar4))
        print('_____________________________________________')
        print('𝙫𝙤𝙡𝙩𝙚 𝙨𝙚𝙢𝙥𝙧𝙚 🍔')
    if notafiscal4 in ('nao','Nao','NAO'):
        print('OK, Bom apetite e volte Sempre ')

if codigo ==5:
    cinco * quantidade
    print('-------------------------------------------------')
    print( 'Sᴇᴜ ʟᴀɴᴄʜᴇ ғɪᴄᴏᴜ ɴᴏ ᴠᴀʟᴏʀ ᴅᴇ: R$',('%.2f'%somar5))
    print('-------------------------------------------------')
    notafiscal5= input('Dᴇsᴇᴊᴀ ɪᴍᴘʀɪᴍɪʀ ᴀ ɴᴏᴛᴀ ғɪᴄᴀʟ ᴅᴇsᴛᴀ ᴄᴏᴍᴘʀᴀ? SIM ᴏᴜ NÃO ?:')
    if notafiscal5 in ('sim','SIM','Sim'):
        print('_______________________')
        print(' N O T A   F I S C A L ')
        print(f' {Data_formatada}     {Hora_formatada}')
        print('Lanchonete Best Lanches')
        print('Produto Selecionado ----- Regrigerante:')
        print('Código Do produto -------------------',codigo)
        print('Unidades --------------------------',quantidade,'x')
        print('Valor ------------------------ R$:',('%.2f'%somar5))
        print('_____________________________________________')
        print('𝙫𝙤𝙡𝙩𝙚 𝙨𝙚𝙢𝙥𝙧𝙚 🍔')
    if notafiscal5 in ('nao','Nao','NAO'):
        print('OK, Bom apetite e volte Sempre ')
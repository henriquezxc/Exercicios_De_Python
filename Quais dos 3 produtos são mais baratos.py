prego = float(input("Qual valordo PREGO R$: "))
parafuso = float(input("Qual valor do PARAFUSO R$: "))
porca = float(input("Qual valor da PORCA R$: "))

if prego<parafuso and prego<porca:
    print('-------------------------------------------------')
    print('Sua escolha deverá ser pregos, pois e mais barato')
    print('-------------------------------------------------')

elif parafuso<prego and parafuso<porca:
    print('---------------------------------------------------')
    print('Sua escolha deverá ser parafuso, pois e mais barato')
    print('---------------------------------------------------')

elif porca<parafuso and porca<prego:
    print('-------------------------------------------------')
    print( 'Sua escolha deverá ser porca, pois e mais barato')
    print('-------------------------------------------------')

elif porca == parafuso and prego:
    print('------------------------------------------------------------')
    print('está tudo com mesmo preço, Leve todos e aproveita a promoção')
    print('------------------------------------------------------------')

elif prego==parafuso:
    print('Prego está o mesmo valor que parafuso')

else:
    ('Algo deu errado, reinicie com preços certos !')
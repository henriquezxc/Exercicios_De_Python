Prego = float(input("Qual valordo PREGO R$: "))
Parafuso = float(input("Qual valor do PARAFUSO R$: "))
Porca = float(input("Qual valor da PORCA R$: "))

if Prego < Parafuso and Prego < Porca:
    print('-------------------------------------------------')
    print('Sua escolha deverá ser pregos, pois e mais barato')
    print('-------------------------------------------------')

elif Parafuso < Prego and Parafuso < Porca:
    print('---------------------------------------------------')
    print('Sua escolha deverá ser parafuso, pois e mais barato')
    print('---------------------------------------------------')

elif Porca < Parafuso and Porca < Prego:
    print('-------------------------------------------------')
    print( 'Sua escolha deverá ser porca, pois e mais barato')
    print('-------------------------------------------------')

elif Porca == Parafuso and Prego:
    print('------------------------------------------------------------')
    print('está tudo com mesmo preço, Leve todos e aproveita a promoção')
    print('------------------------------------------------------------')

elif Prego == Parafuso:
    print('Prego está o mesmo valor que parafuso')

else:
    ('Algo deu errado, reinicie com preços certos !')
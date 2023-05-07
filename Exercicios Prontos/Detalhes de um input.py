nome = str(input('Digite Seu nome completo: ')).strip()
nome_Listado = nome.split()

print(f"""
O nome digitado acima foi: {nome.title()}
A quantidade de letras considerando espaços e de: {len(nome)}
A quantidade de letras desconsiderando os espaços e de: {len(nome) - nome.count(' ')}
Nome com todas as letras Maiusculas é: {nome.upper()}
Nome com todas as letras Minusculas é: {nome.lower()}
O Primeiro nome digitado e: {nome_Listado[0].capitalize()}, tem a quantidade de > {len(nome_Listado[0])} < letras
""")
# O programa irá cacular a quantidade de litros que o veiculo irá gastar no percurso informado
# Entrada da quantidade horas gastas na viagem.
horas= int(input('Quantas horas será sua viagem?: '))
# Entrada da velocidade do veiculo.
velocidade= int(input('Qual será a velocidade Média do seu Veiculo?: '))
# Variavel pré definida da velocidade que será de 12Km/L.
consumo_Km= 12
# Variavel que irá fazer todo o calculo.
calculo=velocidade*horas/consumo_Km
# Impresão do resultado.
print('Seu Gasto De Combustível Será De: ''%.3f'%calculo,'Litros')
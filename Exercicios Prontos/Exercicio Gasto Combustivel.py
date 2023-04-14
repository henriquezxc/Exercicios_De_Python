# O programa irá cacular a quantidade de litros que o veiculo irá gastar no percurso informado
# Entrada da quantidade horas gastas na viagem.
Horas_De_Viagem = int(input('Quantas horas será sua viagem?: '))
# Entrada da velocidade do veiculo.
Velocidade_Media = int(input('Qual será a velocidade Média do seu Veiculo?: '))
# Variavel pré definida da velocidade que será de 12Km/L.
Consumo_Por_Km = 12
# Variavel que irá fazer todo o calculo.
Calculo = Velocidade_Media * Horas_De_Viagem/Consumo_Por_Km
# Impresão do resultado.
print('Seu Gasto De Combustível Será De: ''%.3f'%Calculo,'Litros')

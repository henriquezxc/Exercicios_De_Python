from time import sleep
import os

class ContadorSleep:
    def __init__(self,nome,contador,tempo):
        self.nome = nome
        self.cont = contador
        self.tempo = tempo

    def Contador(self):
        for i in range(self.cont):
            sleep(self.tempo)
            os.system('clear')
            print(f'{self.nome}')
            sleep(self.tempo)
            os.system('clear')
            print(f'{self.nome}.')
            sleep(self.tempo)
            os.system('clear')
            print(f'{self.nome}..')
            sleep(self.tempo)
            os.system('clear')
            print(f'{self.nome}...')
            sleep(self.tempo)

Nome_do_print = str(input('Digite o nome desejado: '))
contador_de_vezes = int(input('Digite as vezes da repetição: '))
temp_do_sleep = float(input('Digite a velocidade da execulção: '))

resultado = ContadorSleep(nome=Nome_do_print,contador=contador_de_vezes,tempo=temp_do_sleep)
resultado.Contador()
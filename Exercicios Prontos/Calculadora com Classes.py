from time import sleep

class Calcular():
    def __init__(self,a,b):
        self.numero1 = a
        self.numero2 = b
    def somar(self):
        return self.numero1 + self.numero2
    def multiplicar(self):
        return self.numero1 * self.numero2
    def Subtrair(self):
        return self.numero1 - self.numero2
    def Dividir(self):
        return self.numero1 / self.numero2
try:
    Entrada_1 = int(input('Digite o primeiro numero: '))
    Entrada_2 = int(input('Digite o segundo numero: '))

    Resultado = Calcular(Entrada_1,Entrada_2)

    print('Estamos fazendo calculo, aguarde...')
    sleep(2)
    print('So mais um momento...')
    sleep(2)

    print(f'''
    Resultado:
    A Soma é de: {Resultado.somar()}
    A Subtração é de: {Resultado.Subtrair()}
    A Multiplicação é de: {Resultado.multiplicar()}
    A Divisão é de: {round(Resultado.Dividir())}
    ''')

except ZeroDivisionError:
    print('Não e possivel dividir por ZERO!')
except ValueError:
    print('Entradas Invalidas')
except KeyboardInterrupt:
    print('Usuario encerrou o processo')
except:
    print('Erro Desconhecido')
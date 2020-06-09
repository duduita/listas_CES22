# CES22 - LISTA 4
# ALUNO: EDUARDO MENEZES MORAES 1 ANO COMP
# QUESTAO 3

# Classes da QUESTAO 1
class Veiculo:
    def __init__(self, motor):
        self.motor = motor

class Motor:
    def __init__(self, tipo):
        self.__tipo = "Motor" + tipo

class Caminhao(Veiculo):
    def __init__(self, motor):
        super(Caminhao,self).__init__(motor)

class Carro(Veiculo):
    def __init__(self, motor):
        super(Carro,self).__init__(motor)

class Moto(Veiculo):
    def __init__(self, motor):
        super(Moto,self).__init__(motor)

class MotorEletrico(Motor):
    def __init__(self):
        super(MotorEletrico,self).__init__("Eletrico")

class MotorHibrido(Motor):
    def __init__(self):
        super(MotorHibrido,self).__init__("Hibrido")

class MotorCombustao(Motor):
    def __init__(self):
        super(MotorCombustao,self).__init__("Combustao")

# Classe Fabrica
# Ela cria um objeto de acordo com  os inputs
# Basicamente, é um "else if" 
class factory:
  def criar_veiculos(self, veiculo):
    if veiculo == "Caminhao":
         return Caminhao(Motor(""))
    elif veiculo == "Carro":
         return Carro(Motor(""))
    elif veiculo == "Moto":
         return Moto(Motor(""))
    elif veiculo == "Carro eletrico":
         return Automovel(MotorEletrico())
    elif veiculo == "Moto a combustao":
         return Moto(MotorCombustao())

# Exemplo simples
Fabrica = factory()
carro1 = Fabrica.criar_veiculos("Moto a combustao")

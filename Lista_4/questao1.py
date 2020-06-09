# CES22 - LISTA 4
# ALUNO: EDUARDO MENEZES MORAES 1 ANO COMP
# QUESTAO 1

# Primeiramente, eu criei as superclasses com veículos (abstração) e motores (implementação)
# Classe Veiculo
class Veiculo:
    def __init__(self, motor):
        self.motor = motor

# Classe Motor  
class Motor:
    def __init__(self, tipo):
        self.__tipo = "Motor" + tipo

# Subclasses de Veículos
# Quando ela é criada, ela pega a "Super", isto é, a classe veículo, e "insere" motor nela
# É como se ela mandasse a classe Veículo criar um caminhão como determinado motor
class Caminhao(Veiculo):
    def __init__(self, motor):
        super(Caminhao,self).__init__(motor)

class Carro(Veiculo):
    def __init__(self, motor):
        super(Carro,self).__init__(motor)

class Moto(Veiculo):
    def __init__(self, motor):
        super(Moto,self).__init__(motor)

# Subclasses de Motor
# Com ela, eu consigo agora criar diferentes tipos de motores de acordo com meu input
class MotorEletrico(Motor):
    def __init__(self):
        super(MotorEletrico,self).__init__("Eletrico")

class MotorHibrido(Motor):
    def __init__(self):
        super(MotorHibrido,self).__init__("Hibrido")

class MotorCombustao(Motor):
    def __init__(self):
        super(MotorCombustao,self).__init__("Combustao")

# Exemplo Simples:
carroDoPadeiro = Carro(MotorEletrico())




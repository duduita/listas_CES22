# Métodos de classe
# Métodos de classe são métodos que são chamados sobre uma classe (comparar este com métodos de instância de classe ou métodos de objeto). 
# Seu significado pode variar dependendo da linguagem de programação:

# Em algumas linguagens (por exemplo, C++, Java), métodos de classe são sinônimos de métodos estáticos (ver seção abaixo),
# que são chamados com um nome de classe conhecido em tempo de compilação. this não pode ser usado em métodos estáticos
# Em outras linguagens (por exemplo, Smalltalk, Ruby, Objective-C), métodos de classe são métodos que são chamados sobre um objeto de classe, 
# que pode ser computado em tempo de execução, não existindo diferença entre chamar um método sobre um objeto regular ou um objeto de classe.
# Entretanto, ambos os métodos de instância e de classe são resolvidos dinamicamente e não há métodos "estáticos". Notavelmente, nesses métodos
# de classe, o this se refere ao objeto de classe
# Algumas linguagens possuem ambos. Por exemplo, em Python, pode-se criar métodos de classe e métodos estáticos usando os decoradores classmethod 
# e staticmethod, respectivamente. O primeiro possui acesso ao this (isto é, o objeto de instância, convencionalmente conhecido como self),
# enquanto o segundo não.


# Métodos Abstratos
# Um método abstrato é aquele com apenas uma assinatura e sem corpo de implementação.
# É frequentemente utilizado para especificar que uma subclasse deve fornecer uma implementação do método. 
# Métodos abstratos são usados para especificar interfaces em algumas linguagens de computador.

from abc import *
class Veiculo(metaclass = ABCMeta):
    @abstractmethod
    def transportar(self, fator):
        pass

# Onde a subclasse estende a classe principal
class Aeroplano(Veiculo):
    def transportar(self, pessoas):
        super().transportar(fator):
        self.combustivel = pessoas * fator * trecho

    def voar(self):
        return "Aeronave em vôo"


# Método Estático
# Um método estático é um método que pode ser chamado sem a instancia da classe.
# É útil para se fazer operações dentro da classe, como uma função de calculo de área por exemplo.

class MyClass(object):
    @staticmethod
    def the_static_method(x):
        print x

MyClass.the_static_method(2)

# Você pode ter a classe Circulo e métodos que pode ser chamados sem precisar de instancia, pois o objetivo é o calculo:

class Pizza(object):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    @staticmethod
    def compute_area(radius):
         return math.pi * (radius ** 2)

    @classmethod
    def compute_volume(cls, height, radius):
         return height * cls.compute_area(radius)

    def get_volume(self):
        return self.compute_volume(self.height, self.radius)
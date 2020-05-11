# Polimorfismo significa ter algo único em vários lugares. O polimorfismo é usado em classes distintas 
# compartilhando funções em comum. Porque as classes derivadas são distintas, suas execuções podem diferir. 
# Entretanto, as classes derivadas compartilham de uma relação comum, instâncias daquelas classes são usadas exatamente na mesma maneira.

# Exemplo simples:

class ObjetoGrafico(object):
    def __init__(self, centro):
        super(ObjetoGrafico, self).__init__()
        self._centro = centro

    @abstractmethod
    def desenha(self):
        pass

    def apaga(self):
        self.setPenColor(self.BACKGROUND_COLOR)
        self.desenha()
        self.setPenColor(self.FOREGROUND_COLOR)

    def movePara(self, p):
        self.apaga()
        self._centro = p
        self.desenho()


# 'Duck typing' é um programa de computador é uma aplicação em que o objeto possui certos métodos e propriedades,
# ao invés de somente o próprio objeto.

# Exemplo simples: um pato possui outras propriedades, e métodos.
class Duck:
    def fly(self):
        print("Duck flying")

class Sparrow:
    def fly(self):
        print("Sparrow flying")

class Whale:
    def swim(self):
        print("Whale swimming")

for animal in Duck(), Sparrow(), Whale():
    animal.fly()


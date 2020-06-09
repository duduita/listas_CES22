# CES22 - LISTA 4
# ALUNO: EDUARDO MENEZES MORAES 1 ANO COMP
# QUESTAO 5

import abc

# Class que define a interface
class Context:

    def __init__(self, state):
        self._state = state

    def request(self):
        self._state.handle()

# Classe abstrata para estado
class State(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def handle(self):
        pass

# As subclasses para estado
# Determinando um comportamento para cada tipo de estado
class Draft(State):
    def __init__(self):
        print("Draft")

    def handle(self):
        pass


class Moderation(State):
    def __init__(self):
        print("Moderation")

    def handle(self):
        pass

class Published(State):
    def __init__(self):
        print("Published.")

    def handle(self):
        pass

# Exemplo Simples:
def main():
    draft = Draft()
    moderation = Moderation()
    published = Published()

    # Rascunho
    context = Context(draft)
    context.request()
    
    # Moderation
    context = Context(moderation)
    context.request()

    # Publicado
    context = Context(published)
    context.request()

if __name__ == "__main__":
    main()
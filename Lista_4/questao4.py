# CES22 - LISTA 4
# ALUNO: EDUARDO MENEZES MORAES 1 ANO COMP
# QUESTAO 4

from tkinter import *
from abc import ABCMeta, abstractstaticmethod
import time

# Classe abstrata onde ficarão todos comandos
class ICommand(metaclass=ABCMeta):

# O método abstrato execute
    @abstractstaticmethod
    def execute():
        pass

# A Invoker Class
# Essa é a classe que determina os comandos de acordo com o estado atual
class Switch:

    # Aqui ela cria os conjuntos/listas para se preparar para registrar
    def __init__(self):
        self._commands = {}
        self._history = []

    # Define o histórico
    @property
    def history(self):
        return self._history

    def register(self, command_name, command):
        self._commands[command_name] = command

    # Ela vai dando append na lista que foi criada
    def execute(self, command_name):
        if command_name in self._commands.keys():
            self._history.append((time.time(), command_name))
            self._commands[command_name].execute()
        else:
            print(f"Command [{command_name}] not recognised")

# O recebedor da ação
class Cliente:
    def __init__(self):
        self.money = 0

    def depositar(self):
        self.money = self.money + 100
        print(self.money)

    def sacar(self):
        self.money = self.money - 50
        print(self.money)

# Os objetos, os quais implementam a interface Icommand
class depositar(ICommand):

    def __init__(self, cliente):
        self._cliente = cliente

    def execute(self):
        self._cliente.depositar()

class Sacar(ICommand):

    def __init__(self, cliente):
        self._cliente = cliente

    def execute(self):
        self._cliente.sacar()

# A função main (para exemplo)
if __name__ == "__main__":

    # Criado o objeto que recebe a ação
    CLIENTE = Cliente()

    SWITCH = Switch()

    # Seta os comandos dados para cada estado
    SWITCH_ON = depositar(CLIENTE)
    SWITCH_OFF = Sacar(CLIENTE)

def saldo():
    print("Seu saldo eh:", CLIENTE.money)

def depositar():
    SWITCH.register("Deposito", SWITCH_ON)
    SWITCH.execute("Deposito")
    print("Seu saldo ficou:", CLIENTE.money)

def saque():
    SWITCH.register("Saque", SWITCH_OFF)
    SWITCH.execute("Saque")
    print("Seu saldo ficou:", CLIENTE.money)

def historico():
    print("Segue o horario e acao tomada: ")
    print(SWITCH.history)

# Aqui começa a GUI

window = Tk()

# Foram feitos botões e uma janela simples
# Cada botão aciona um comando
window.title("Banco YANO")

window.geometry('350x200')

btn = Button(window, text="Saldo", command=saldo)

btn.grid(column=0, row=0)

btn = Button(window, text="Depositar 100", command=depositar)

btn.grid(column=1, row=0)

btn = Button(window, text="Saque 50", command=saque)

btn.grid(column=2, row=0)

btn = Button(window, text="Historico", command=historico)

btn.grid(column=3, row=0)

# O que faz a janela permanecer aberta
window.mainloop()


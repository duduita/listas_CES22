# CES22 - LISTA 4
# ALUNO: EDUARDO MENEZES MORAES 1 ANO COMP
# QUESTAO 2

import six
from abc import ABCMeta

# Declarando a classe abstrata Pizza
@six.add_metaclass(ABCMeta)
class Pizza(object):

   def get_cost(self):
      pass

   def get_ingredients(self):
      pass
   
   def get_tax(self):
      return 0.1*self.get_cost()

# Criando heranças para classe Pizza
class Pizza_Frango(Pizza):
   
   def get_cost(self):
      return 45.00
   
   def get_ingredients(self):
      return 'Frango, Queijo, Massa'

class Pizza_Doce(Pizza):
   
   def get_cost(self):
      return 30.00
   
   def get_ingredients(self):
      return 'Chocolate, Massa'

# Agora, criando um decorador, isto é, objeto capaz de alterar em tempo de execucação os meus métodos
# Com isso, é possível adicionar coisas nos objetos da classe Pizza_Frango, mudando, inclusive, os seus métodos

@six.add_metaclass(ABCMeta)
class Pizza_Decorator(Pizza):
   
   def __init__(self,decorated_pizza):
      self.decorated_pizza = decorated_pizza
   
   def get_cost(self):
      return self.decorated_pizza.get_cost()
   
   def get_ingredients(self):
      return self.decorated_pizza.get_ingredients()

class Bacon(Pizza_Decorator):
   
   def __init__(self,decorated_pizza):
      Pizza_Decorator.__init__(self,decorated_pizza)
   
   def get_cost(self):
      return self.decorated_pizza.get_cost() + 5
   
   def get_ingredients(self):
	   return self.decorated_pizza.get_ingredients() + ', Bacon'

class Refri(Pizza_Decorator):
   
   def __init__(self,decorated_pizza):
      Pizza_Decorator.__init__(self,decorated_pizza)
   
   def get_cost(self):
      return self.decorated_pizza.get_cost() + 10
   
   def get_ingredients(self):
      return self.decorated_pizza.get_ingredients() + ', Refri'

class Borda(Pizza_Decorator):
   
   def __init__(self,decorated_pizza):
      Pizza_Decorator.__init__(self,decorated_pizza)
   
   def get_cost(self):
      return self.decorated_pizza.get_cost() + 5
   
   def get_ingredients(self):
      return self.decorated_pizza.get_ingredients() + ', Borda'

class Confete(Pizza_Decorator):
   
   def __init__(self,decorated_pizza):
      Pizza_Decorator.__init__(self,decorated_pizza)
   
   def get_cost(self):
      return self.decorated_pizza.get_cost() + 10
   
   def get_ingredients(self):
      return self.decorated_pizza.get_ingredients() + ', Confete'

# Exemplo, criei dois objetos
pizza = Pizza_Frango()
pizza2 = Pizza_Doce()

# Adicionei Bacon
maisBacon = Bacon(pizza)

# Repare que mudou os ingredientes e o valor :)
print(maisBacon.get_cost())
print(maisBacon.get_ingredients())

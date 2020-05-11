# Questão 11

# *args
# É usado para passar um lista de argumentos variável sem palavras-chave em forma de tupla, 
# pois a função que o recebe não necessariamente saberá quantos argumentos serão passados.

# Exemplo simples:

def func_args(*args):
    print(f'tipo: {type(args)} conteúdo: {args}')
    for arg in args:
        print(f'tipo: {type(arg)} conteúdo: {arg}')


func_args(1, 'A', {'valor': 10})

#**kwargs
# Como a abreviação sugere, kwargs significa keyword arguments (argumentos de palavras chave). 
# Ele permite passar um dicionário com inúmeras keys para a função.

# Exemplo simples:

def func_kwargs(**kwargs):
    print(f'tipo: {type(kwargs)} contuedo: {kwargs}')
    for key, value in kwargs.items():
        print(f'atributo: {key}, valor: {value}')

func_kwargs(nome='James', sobrenome='Bond', cargo='Agente 007')
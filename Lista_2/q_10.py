#  Aqui será feito um simples exemplo, ao mesmo tempo que será explicado a ideia central de um decorador..

#  Na prática, o decorador age como uma embalagem de presente, acondicionando
#  a função sem alterar seu conteúdo (ele continua sendo um presente) mas deixando-o mais bonito.

#  Um decorador é uma função que expera OUTRA função como parâmetro

def my_shiny_new_decorator(a_function_to_decorate):

    # Dentro do decorador se define a função 'on the  fly' a 'wrapper'
    # Essa função será embalada ao redor da função principal
    # Então, ela poderá executar o código após isso, por exemplo:
    
    def the_wrapper_around_the_original_function():

        # Put here the code you want to be executed BEFORE the original function is called
        print("Before the function runs")

        # Call the function here (using parentheses)
        a_function_to_decorate()

        # Put here the code you want to be executed AFTER the original function is called
        print("After the function runs")

    # Até esse ponto a função "a_function_to_decorate" NUNCA foi executada
    # Nós retornaremos a wrapper function que nós recém criamos
    # A wrapper contém a função e o código para ser executado antes e depois. Está pronta para o uso nesse exemplo.
    return the_wrapper_around_the_original_function

# Agora imagine você criar uma função que nunca vai usar de novo
def a_stand_alone_function():
    print("I am a stand alone function, don't you dare modify me")

a_stand_alone_function() 
#outputs: I am a stand alone function, don't you dare modify me

# Bem, você irá usar o conceito de 'decorator' nela para extender seu comportamento
# Basta passar isso para o 'decorator', isso irá embalá-la dinamicamente em qualquer
# tipo de código que você quiser retornar para a sua nova função pronta a ser usada:

a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()

#Finalmente o output seria:
#Before the function runs
#I am a stand alone function, don't you dare modify me
#After the function runs
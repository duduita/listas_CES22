# Questão 1 e 2

# Conforme pedido da questão, baseado no código dado no livro-texto, editou-se para que pudesse ser mudada
# a cor do semáforo, assim como ativar o timer (após algum clique)

import turtle # Tess becomes a traffic light.
turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")
# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.
# This variable holds the current state of the machine
state_num = 0
temp = 3

def advance_state_machine():
    global state_num
    if state_num == 0: # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("blue")
        wn.ontimer(advance_state_machine, 3000)  # set the timer to explode in 3 sec
        state_num = 1
    elif state_num == 1: # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        wn.ontimer(advance_state_machine, 3000)  # set the timer to explode in 3 sec
        state_num = 2
    else: # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        wn.ontimer(advance_state_machine, 3000)  # set the timer to explode in 3 sec
        state_num = 0

def change_color_blue():
    global state_num

# Eu pensava que era para mudar a posição também, depois vi que era só a cor, aí ficou bem mais fácil.
#    if(state_num == 2):
#        tess.back(70)
#    if(state_num == 0):
#        tess.forward(140)

#    state_num = 1

    tess.fillcolor("blue")

def change_color_red():
    global state_num

# Eu pensava que era para mudar a posição também, depois vi que era só a cor, aí ficou bem mais fácil.
#    if(state_num == 1):
#        tess.back(70)
#    if(state_num == 0):
#        tess.forward(70)
#
#    state_num = 2
#
    tess.fillcolor("red")

def change_color_green():
    global state_num

# Eu pensava que era para mudar a posição também, depois vi que era só a cor, aí ficou bem mais fácil.
#    if(state_num == 1):
#        tess.back(140)
#    if(state_num == 2):
#        tess.back(70)

#    state_num = 0
 
    tess.fillcolor("green")

def change_pen_plus():
    if(tess.pensize() < 20):
        temp = tess.pensize() + 1
        tess.pensize(temp)
        print(tess.pensize())


def change_pen_minus():
    if(tess.pensize() > 1):
        temp = tess.pensize() -1
        tess.pensize(temp)
        print(tess.pensize())

# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")
wn.onkey(change_color_red, "R")
wn.onkey(change_color_green, "G")
wn.onkey(change_color_blue, "B")

wn.onkey(change_pen_plus, "+")
wn.onkey(change_pen_minus, "-")


wn.listen() # Listen for events
wn.mainloop()
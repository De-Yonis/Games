import turtle 
import os #allows us to interact with the operating system using text commands


window = turtle.Screen()
window.title("Play Pong @DeYonis")
window.bgcolor("blue")
window.setup(width = 800, height = 600)
window.tracer(0)
# stops the window from updating, so we manually do it, this speeds up the game quite a bit

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of the animation, sets it to maximum amount of speed
paddle_a.shape("square")
paddle_a.color("white")
# default size is 20*20 pixels
paddle_a.shapesize(stretch_wid=4, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of the animation, sets it to maximum amount of speed
paddle_b.shape("square")
paddle_b.color("white")
# default size is 20*20 pixels
paddle_b.shapesize(stretch_wid=4, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0) # As its on the opposite side of the screen 


#Ball
ball = turtle.Turtle()
ball.speed(0) #speed of the animation, sets it to maximum amount of speed
ball.shape("circle")
ball.color("white")
ball.penup() # so we don't draw a line everytime the turtle moves
ball.goto(0,0) # As its on the opposite side of the screen 
ball.dx = 1.8 # speed of the ball movement and direction it starts depending on the axis 
ball.dy = 1.8


board = turtle.Turtle()
board.speed(0) #animation speed
board.color("white")
board.penup()
# board.hideturtle()
board.goto(0,260)
board.write("Player A: 0      Player B: 0", align="center", font=("Ariel",22,"normal"))

#Score
a = 0
b = 0






#Moving paddle functions
def paddle_a_up():
    y_cord= paddle_a.ycor()
    y_cord += 20
    paddle_a.sety(y_cord)# so it starts from the last place and not the begining 

def paddle_a_down():
    y_cord= paddle_a.ycor()
    y_cord -= 20
    paddle_a.sety(y_cord)# so it starts from the last place and not the begining 


def paddle_b_up():
    y_cord= paddle_b.ycor()
    y_cord += 20
    paddle_b.sety(y_cord)# so it starts from the last place and not the begining     


def paddle_b_down():
    y_cord= paddle_b.ycor()
    y_cord -= 20
    paddle_b.sety(y_cord)# so it starts from the last place and not the begining   



# Keyboard binding
window.listen() # This listens for keyboard input

#FOR A
window.onkeypress(paddle_a_up,"w") 
window.onkeypress(paddle_a_down,"s") 

#FOR B
window.onkeypress(paddle_b_up,"Up") 
window.onkeypress(paddle_b_down,"Down") 





# Main game loop
while True:
    window.update()

    #Moving Ball
        #THE BALL STARTS OF AT 0, SO THE FIRST TIME IS GOING TO GO 2, THEN PLUS 2... dep on line 39,40
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top and bottom borders correction 
    if ball.ycor() > 297: 
        ball.sety(297)
        ball.dy *= -1
        os.system("afplay doh_homer.wav&")
        
    
    elif ball.ycor() < -297:
        ball.sety(-297)
        ball.dy *= -1
        os.system("afplay doh_homer.wav&")

    # Left and right borders correction 
    if ball.xcor() > 397:
        ball.goto(0,0) #it moves it to the coordinates, the centre
        ball.dx *= -1
        a += 1
        os.system("afplay all_right_homer.wav&")
        board.clear()
        board.write("Player A: {}      Player B: {}".format(a,b), align="center", font=("Ariel",22,"normal"))


    if ball.xcor() < -397:
        ball.goto(0,0)
        ball.dx *= -1
        b += 1
        os.system("afplay all_right_homer.wav&") #The & prevents lagging of sound 
        board.clear()
        board.write("Player A: {}      Player B: {}".format(a,b), align="center", font=("Ariel",22,"normal"))

    #Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1


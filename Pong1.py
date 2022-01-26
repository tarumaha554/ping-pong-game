
import turtle #it is a module for making small games
import winsound #for operating system

wn = turtle.Screen()#wn stands for window and screen is used for window screen
wn.title("Pong game")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)#screen size of the game window
wn.tracer(0)#stop window from updating to run the game faster

# Score
score_a = 0
score_b = 0
score_c = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)#speed of animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()#draw a line
paddle_a.goto(-350, 0)# for square position on axis

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)#speed of animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # adjusting the default size of the paddle
paddle_b.penup()#draw a line
paddle_b.goto(350, 0)# for square position on axis

# Paddle C
paddle_c = turtle.Turtle()
paddle_c.speed(0)#speed of animation
paddle_c.shape("square")
paddle_c.color("white")
paddle_c.shapesize(stretch_wid=1, stretch_len=5) # adjusting the default size of the paddle
paddle_c.penup()#draw a line
paddle_c.goto(0, -250)# for square position on axis

#Ball
ball = turtle.Turtle()
ball.speed(0)#speed of animation
ball.shape("circle")
ball.color("white")
ball.penup()#draw a line
ball.goto(0, 0)# for square position on axis
ball.dx = .2
ball.dy = -.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()#just to see the text nothing else
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0 Player C: 0", align="center", font=("Courier", 20, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor() #it returns the y coordinate
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() #it returns the y coordinate
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #it returns the y coordinate
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() #it returns the y coordinate
    y -= 20
    paddle_b.sety(y)


def paddle_c_right():
    x = paddle_c.xcor()
    x+=20
    paddle_c.setx(x)

def paddle_c_left():
    x = paddle_c.xcor()
    x-=20
    paddle_c.setx(x)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
wn.onkeypress(paddle_c_right, "Right")
wn.onkeypress(paddle_c_left, "Left")


# Main game loop
while True:
    wn.update()

    #Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # Border checking
    #top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) # second parameter is use for not delay in sound when bounce

    # #bottom
    # if ball.ycor() < -290:
    #     ball.sety(-290)
    #     ball.dy *= -1
    #     winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) 
    
    #left to center
    if ball.xcor() >390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A: {} Player B: {} Player C: {}".format(score_a, score_b, score_c), align="center", font=("Courier", 20, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    #right to center
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {} Player B: {} Player C: {}".format(score_a, score_b, score_c), align="center", font=("Courier", 20, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    #bottom to center
    if ball.ycor() < -290:
        ball.goto(0,0)
        ball.dy *= -1
        score_c +=1
        pen.clear()
        pen.write("Player A: {} Player B: {} Player C: {}".format(score_a, score_b, score_c), align="center", font=("Courier", 20, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    # paddle and ball collision
    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if(ball.ycor() < -240 and ball.ycor() > -250) and (ball.xcor() < paddle_c.xcor() + 40 and ball.xcor() > paddle_c.xcor() - 40):
        ball.sety(-240)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
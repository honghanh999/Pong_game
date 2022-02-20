# Part 1: Getting Started 

import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong game by Hong Hanh")
wn.bgcolor("pink")
wn.setup(width= 800, height=600)
wn.tracer(delay = 1)
# it stops the window from updating
# Tracer is used to turn the animation on-off and also set a delay for updating our drawing objects


# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
# The default size of a Turtle object is 20 pixels
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)



# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# Every time the ball moves, it moves by two pixels. Since x is positive, it;s going to move to the right to and since y is positive, it's going to move up to so it'd be kind of moving up and diagonally 
ball.dx = 2
ball.dy = -2 


# Pen
# model_name.class__name
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
# We don't wanna draw a line. When the pen moves, every turtle actually startss out at the dad center of the screen, then we move it somewhere
pen.penup()
# We don't wanna see the pen, we just wanna see the text that's going to write
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player:0", align = "center", font= ("Courier", 24, "normal"))


# Function
def paddle_a_up():
    # .ycor is from the turtle module and we assign that value to a variable called y
    y = paddle_a.ycor()
    y += 20
    # set y to do a new y
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding   
# This tells it to listen for keyboard input
wn.listen()
# press w to call the function paddle_a_up
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


# Main game loop
while True:
    # Every time the loop runs, it updates the screen
    wn.update()

    # Move the ball
    # The ball start 00, the first time through this loop, it's going to go to an x times the loop
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        # we set it back to 290
        ball.sety(290)
        # it reverses the direction
        ball.dy *=-1
        #if it's asynchronous, it will play the sound in the background. If it's not a synchronous program, we'll stop
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *=-1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player: {}".format(score_a, score_b), align = "center", font= ("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *=-1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player: {}".format(score_a, score_b), align = "center", font= ("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1 
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1 
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
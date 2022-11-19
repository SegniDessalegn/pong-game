import turtle
import math
import random

turtle.bgcolor("brown")
ball = turtle.Turtle()
ball.shape("circle")
ball.color("black")
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.shapesize(10, 1)
paddle_a.penup()
paddle_a.speed(0)
paddle_a.goto(-600, 0)

paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(10, 1)
paddle_b.penup()
paddle_b.speed(0)
paddle_b.goto(600, 0)

player_1_score = 0
player_2_score = 0
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.speed(0)
score_writer.goto(-450, 0)
score_writer.write(player_1_score, font=("normal", 200, "normal"))
score_writer.forward(100)
score_writer.goto(300, 0)
score_writer.write(player_2_score, font=("normal", 200, "normal"))
score_writer.pendown()


def paddle_a_up():
    if paddle_a.ycor() <= 240:
        y = 0
        y += 40
        paddle_a.goto(-600, paddle_a.ycor() + y)


def paddle_a_down():
    if paddle_a.ycor() >= -240:
        y = 0
        y -= 40
        paddle_a.goto(-600, paddle_a.ycor() + y)


def paddle_b_up():
    if paddle_b.ycor() <= 240:
        y = 0
        y += 40
        paddle_b.goto(600, paddle_b.ycor() + y)


def paddle_b_down():
    if paddle_b.ycor() >= -240:
        y = 0
        y -= 40
        paddle_b.goto(600, paddle_b.ycor() + y)


turtle.listen()
turtle.onkeypress(paddle_a_up, "w")
turtle.onkeypress(paddle_a_down, "s")
turtle.onkeypress(paddle_b_up, "Up")
turtle.onkeypress(paddle_b_down, "Down")
boarder = turtle.Turtle()
boarder.hideturtle()
boarder.speed(0)
boarder.penup()
boarder.goto(-600, 350)
boarder.pensize(10)
boarder.pendown()
for i in range(2):
    boarder.forward(1200)
    boarder.right(90)
    boarder.forward(700)
    boarder.right(90)

bigger_ball = turtle.Turtle()
bigger_ball.speed(0)
bigger_ball.penup()
bigger_ball.goto(0, 400)
bigger_ball.shape("circle")
bigger_ball.shapesize(2)
bigger_ball.color("blue")

hide_ball = turtle.Turtle()
hide_ball.speed(0)
hide_ball.penup()
hide_ball.goto(0, 400)
hide_ball.shape("circle")
hide_ball.shapesize(2)
hide_ball.color("red")

faster_ball = turtle.Turtle()
faster_ball.speed(0)
faster_ball.penup()
faster_ball.goto(0, 400)
faster_ball.shape("circle")
faster_ball.shapesize(2)
faster_ball.color("yellow")

bigger_ball.goto(0, random.randint(-350, 350))
hide_ball.goto(0, random.randint(-350, 350))
faster_ball.goto(0, random.randint(-350, 350))


def decide_size(ball):
    global size_ball
    if size_ball <= 100:
        size_ball += 10
        ball.shapesize(size_ball)
        ball.color("blue")


def decide_speed(ball):
    global speed_ball
    if speed_ball <= 20:
        speed_ball += 5
        ball.color("yellow")


def decide_hiding(ball):
    ball.hideturtle()


ball.penup()
x = ball.xcor()
y = ball.ycor()
ball.speed(0)
size_ball = 1
speed_ball = 10
score_writer.clear()
while True:
    if abs(ball.xcor())>620 or abs(ball.ycor())>370:
        ball.goto(0,0)
    ball.forward(speed_ball)
    ball.shapesize(size_ball)
    if ball.xcor() <= -600:
        print(ball.shapesize())
        if not score_writer.isvisible():
            score_writer.reset()
            score_writer.hideturtle()

        if not ((paddle_a.ycor() >= ball.ycor() and (paddle_a.ycor() - ball.ycor()) < 110) or (
                paddle_a.ycor() <= ball.ycor() and (-paddle_a.ycor() + ball.ycor()) < 110)):
            print(paddle_a.ycor(), "  ", ball.ycor())
            player_2_score += 1
            speed_ball = 10
            size_ball = 1
            ball.reset()
            ball.color("black")
            score_writer.penup()
            score_writer.speed(0)
            score_writer.speed(0)
            score_writer.goto(-450, 0)
            score_writer.write(player_1_score, font=("normal", 200, "normal"))
            score_writer.forward(100)
            score_writer.goto(300, 0)
            score_writer.write(player_2_score, font=("normal", 200, "normal"))
            score_writer.pendown()
            ball.left(random.randint(-60, 60))
            ball.speed(0)
            ball.penup()

        else:
            angle = math.degrees(math.atan((y - ball.ycor()) / (x - ball.xcor())))
            if abs(paddle_a.ycor() - ball.ycor() < 100):
                if not ball.isvisible():
                    ball.showturtle()
                if size_ball > 1:
                    size_ball -= 1
                    ball.color("blue")
                else:
                    ball.penup()
                    ball.color("black")
                if speed_ball <= 20 and speed_ball > 10:
                    speed_ball -= 0.25
                    ball.color("yellow")
                else:
                    ball.color("black")
                final_angle = -((paddle_a.ycor() - ball.ycor()) / 3) + 180 - 2 * angle
                if final_angle <= 90 or final_angle >= 270:
                    ball.left(180 - 2 * angle)
                    x = ball.xcor()
                    y = ball.ycor()
                else:
                    ball.left(final_angle)
                    x = ball.xcor()
                    y = ball.ycor()
            else:
                ball.left(180 - 2 * angle)
                x = ball.xcor()
                y = ball.ycor()

        initail_x_cor = ball.xcor()
        ball.forward(10)
        if initail_x_cor>ball.xcor():
            ball.right(180)
            while ball.xcor()<=-600:
                ball.forward(10)


    if ball.xcor() >= -20 and ball.xcor() <= 20:
        if abs(ball.ycor() - bigger_ball.ycor()) < 60:
            decide_size(ball)
            bigger_ball.goto(0, random.randint(-350, 350))
        if abs(ball.ycor() - faster_ball.ycor()) < 60:
            decide_speed(ball)
            faster_ball.goto(0, random.randint(-350, 350))
        if abs(ball.ycor() - hide_ball.ycor()) < 60:
            decide_hiding(ball)
            hide_ball.goto(0, random.randint(-350, 350))

    elif ball.xcor() >= 600:
        if not score_writer.isvisible():
            score_writer.reset()
            score_writer.hideturtle()
        if not ((paddle_b.ycor() >= ball.ycor() and (paddle_b.ycor() - ball.ycor()) < 110) or (
                paddle_b.ycor() <= ball.ycor() and (-paddle_b.ycor() + ball.ycor()) < 110)):
            print(paddle_b.ycor(), "  ", ball.ycor())
            player_1_score += 1
            speed_ball = 10
            size_ball = 1
            ball.reset()
            ball.color("black")
            score_writer.penup()
            score_writer.speed(0)
            score_writer.goto(-450, 0)
            score_writer.write(player_1_score, font=("normal", 200, "normal"))
            score_writer.forward(100)
            score_writer.goto(300, 0)
            score_writer.write(player_2_score, font=("normal", 200, "normal"))
            score_writer.pendown()
            ball.speed(0)
            ball.left(random.randint(150, 210))
            ball.penup()

        else:
            angle = math.degrees(math.atan((y - ball.ycor()) / (x - ball.xcor())))
            if paddle_b.ycor() - ball.ycor() < 100 and -paddle_b.ycor() + ball.ycor() < 100:
                if not ball.isvisible():
                    ball.showturtle()
                if size_ball > 1:
                    size_ball -= 1
                    ball.color("blue")
                else:
                    ball.color("black")
                if speed_ball <= 20 and speed_ball >10:
                    speed_ball -= 0.25
                    ball.color("yellow")
                else:
                    ball.color("black")
                final_angle = ((paddle_b.ycor() - ball.ycor()) / 3) + 180 - 2 * angle

                """if the bounce angle is beyond the allowed degrees"""
                if final_angle <= 90 or final_angle >= 270:
                    ball.left(180 - 2 * angle)
                    x = ball.xcor()
                    y = ball.ycor()
                else:
                    ball.left(final_angle)
                    x = ball.xcor()
                    y = ball.ycor()
            else:
                ball.left(180 - 2 * angle)
                x = ball.xcor()
                y = ball.ycor()

            initail_x_cor = ball.xcor()
            ball.forward(10)
            if initail_x_cor < ball.xcor():
                ball.right(180)
                while ball.xcor() >= 600:
                    ball.forward(10)


    elif abs(ball.ycor()) >= 350:  # to bounce the ball vertically
        angle = math.degrees(math.atan((x - ball.xcor()) / (y - ball.ycor())))
        ball.right(180 - 2 * angle)
        x = ball.xcor()
        y = ball.ycor()
        ball.forward(10)
        if abs(ball.ycor()) >= 350:
            while abs(ball.ycor()) >= 350:
                ball.forward(10)
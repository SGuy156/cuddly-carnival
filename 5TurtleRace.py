import turtle
import random

turtle.title("TURTLEEEEEEEEEEEEEEEEEEE RACINGGGGGG!!!! YEEEEEEEEEEEEEEEEEAAAAAAAAAAAAAHHHHHH")

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.color("blue")
t2.color("green")
t1.pensize(6)
t2.pensize(6)

t1.penup()
t2.penup()


t1.shape("turtle")
t2.shape("turtle")

t1.goto(-200,100)
t2.goto(-200,-100)


t1.fd(300)
t1.pendown()
t1.circle(60)
t1.penup()
t1.lt(90)
t1.fd(60)
t1.rt(90)
t1.bk(300)


t2.fd(300)
t2.pendown()
t2.circle(60)
t2.penup()
t2.lt(90)
t2.fd(60)
t2.rt(90)
t2.bk(300)


dice = [1,2,3,4,5,6]

while t1.pos() < (100,100) and t2.pos() < (100,-100):
    diceRNG1 = random.choice(dice)
    print("result of dice roll for turtle 1:", diceRNG1)
    print("Numbr of steps for turtle 1")
    print(20 * diceRNG1)
    t1.fd(20 * diceRNG1)
    diceRNG2 = random.choice(dice)
    print("result of dice roll for turtle 2:", diceRNG2)
    print("Numbr of steps for turtle 2")
    print(20 * diceRNG2)
    t2.fd(20 * diceRNG2)

    if t1.pos() >= (100,100):
        print("PLAYER ONE WINS!!")
        break
    elif t2.pos() >= (100,-100):
        print("PLAYER TWO WINS!!!")
        break

turtle.done()
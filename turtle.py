#Turtle race using turtle and random module
#Created by Shikha Singh

import turtle as t
from random import randint
from time import sleep

def heading(wn):
    wn.pu()
    wn.setpos(0,200)
    wn.write('Turtle Race',align='center',font=("Cooper Black", 30, "bold"))
    
def finishPoint(wn):
    wn.penup() 
    wn.setpos(-250,100)    
    wn.right(90)
    wn.pd()
    wn.forward(200)

    wn.pu()
    wn.setpos(250,100)
    wn.pd()
    wn.forward(200)

    
    wn.pu()
    wn.setpos(-260,40)
    wn.left(90)
    track(wn)
    wn.pu()
    wn.setpos(-260,-40)
    track(wn)
    wn.ht()
    
def track(wn):
    for i in range(27):
        wn.pd()
        wn.forward(10)
        wn.pu()
        wn.forward(10)
        wn.up()
def countdown(wn):
    for i in reversed(range(3)):
        wn.write('The race will start in {}'.format(i+1),align='center',font=("Arial", 20, "normal"))
        sleep(1)
        wn.undo()
    
def startRace(wn):
    r1,r2,r3=racer()
    score_r1=0
    score_r2=0
    score_r3=0
    
    for turn in range(180):
        v_r1=randint(1,5)
        v_r2=randint(1,5)
        v_r3=randint(1,5)
        r1.forward(v_r1)
        r2.forward(v_r2)
        r3.forward(v_r3)
        score_r1+=v_r1
        score_r2+=v_r2
        score_r3+=v_r3
        
    
        if score_r1>=510:
            r1.pu()
            r1.goto(-150,-190)
            r1.pd()
            wn.write('Black turtle wins',align='center',font=("Arial", 20, "normal"))
            break
        elif score_r2>=510:
            r2.pu()
            r2.goto(-150,-190)
            r2.pd()
            wn.write('Red turtle wins',align='center',font=("Arial", 20, "normal"))
            break
        elif score_r3>=510:
            r3.pu()
            r3.goto(-150,-190)
            r3.pd()
            wn.write('White turtle wins',align='center',font=("Arial", 20, "normal"))
            break
    
    
def racer():
    r1=t.Turtle()      
    r1.color('black')
    r1.shape('turtle')
    r1.up()
    r1.setpos(-260,68)
    r1.pd()

    r2=t.Turtle()  # defining player 2
    r2.color('red')
    r2.shape('turtle')
    r2.up()
    r2.setpos(-260,0)
    r2.pd()
    
    r3=t.Turtle()  # defining player 2
    r3.color('white')
    r3.shape('turtle')
    r3.up()
    r3.setpos(-260,-78)
    r3.pd()

    return r1,r2,r3

def main():
    wn=t.Turtle()

    scr=t.Screen()
    scr.bgcolor('gray')
    scr.title('TURTLE RACE')
    
    heading(wn)
    
    finishPoint(wn)
    
    track(wn)
    
    wn.setpos(0,-200)
    countdown(wn)
    
    startRace(wn)
    
    t.exitonclick()

main()

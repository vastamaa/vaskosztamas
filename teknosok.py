import turtle
from turtle import *
import random
import tkinter as tk
import keyboard


color_set = {"pink", "red", "blue", "green"}
color_array = []
for i in color_set:
    color_array.append(i)

#Ablak
wn = turtle.Screen()
wn.bgcolor("Snow")
wn.title("Teknős verseny")

#Felirat
turtle.hideturtle() # Teknős/kurzor elrejtése
turtle.speed(0)
turtle.color("Black")
turtle.penup()
turtle.setpos(-110, 130) # Pozíció
turtle.pendown()
turtle.write("FINISH LINE", font=("Arial", 30, "bold")) # Szöveg írás (font, méret, vastagság)
turtle.penup()

turtle.penup()
turtle.setpos(-154, -270) # Pozíció
turtle.pendown()
turtle.write("1", font=("Arial", 15, "bold")) # Szöveg írás (font, méret, vastag)
turtle.penup()

turtle.penup()
turtle.setpos(-54, -270) # Pozíció
turtle.pendown()
turtle.write("2", font=("Arial", 15, "bold")) # Szöveg írás (font, méret, vastagság)
turtle.penup()

turtle.penup()
turtle.setpos(46, -270) # Pozíció
turtle.pendown()
turtle.write("3", font=("Arial", 15, "bold")) # Szöveg írás (font, méret, vastagság)
turtle.penup()

turtle.penup()
turtle.setpos(146, -270) # Pozíció
turtle.pendown()
turtle.write("4", font=("Arial", 15, "bold")) # Szöveg írás (font, méret, vastagság)
turtle.penup()

#Vonal
turtle.pensize(5) # Vonal vastagság
turtle.setpos(-200, 190)
turtle.pendown()
turtle.forward(400)

def play():

    try:

        #Teknősök
        noemi = Turtle()
        noemi.speed(6)
        noemi.color(color_array[0])
        noemi.shape("turtle")
        noemi.shapesize(2,2,3)
        noemi.left(90)
        noemi.penup() # Toll felemelés
        noemi.goto(-150, -220) # Pozícionálás
        noemi.pendown() # Toll letétel

        tamas = Turtle()
        tamas.speed(6)
        tamas.color(color_array[1])
        tamas.shape("turtle")
        tamas.shapesize(2,2,3)
        tamas.left(90)
        tamas.penup()
        tamas.goto(-50, -220)
        tamas.pendown()

        david = Turtle()
        david.speed(6)
        david.color(color_array[2])
        david.shape("turtle")
        david.shapesize(2,2,3)
        david.left(90)
        david.penup()
        david.goto(50, -220)
        david.pendown()

        evelin = Turtle() 
        evelin.speed(6)
        evelin.color(color_array[3])
        evelin.shape("turtle")
        evelin.shapesize(2,2,3)
        evelin.left(90)
        evelin.penup()
        evelin.goto(150, -220)
        evelin.pendown()

        tamas_bool = False
        david_bool = False
        noemi_bool = False
        evelin_bool = False
        state = True
        finish_arr = []

        while(state):

            
            if(tamas.pos() < (-50, 215)):
                tamas.forward(random.randint(1,12))
                
            elif(tamas.pos() >= (-50, 215)):
                tamas.penup()
                tamas_bool = True
                if("Tamás" not in finish_arr):
                    finish_arr.append("Tamás")


                
            if(noemi.pos() < (-150, 215)):
                noemi.forward(random.randint(1,12))
                
            elif(noemi.pos() >= (-150, 215)):
                noemi.penup()
                noemi_bool = True
                if("Noémi" not in finish_arr):
                    finish_arr.append("Noémi")


                
            if(evelin.pos() < (150, 215)):
                evelin.forward(random.randint(1,12))
                
            elif(evelin.pos() >= (150, 215)):
                evelin.penup()
                evelin_bool = True
                if("Evelin" not in finish_arr):
                    finish_arr.append("Evelin")


                
            if(david.pos() < (50, 215)):
                david.forward(random.randint(1,12))
                
            elif(david.pos() >= (50, 215)):
                david.penup()
                david_bool = True
                if("Dávid" not in finish_arr):
                    finish_arr.append("Dávid")



            if(evelin_bool == True and david_bool == True and noemi_bool == True and tamas_bool == True ):
                state = False


        turtle.penup()
        turtle.setpos(180, 60)
        turtle.pendown()
        turtle.write("1. helyezett: {0}\n".format(finish_arr[0]), font=("Arial", 10, "bold"))
        turtle.penup()
        turtle.setpos(180, 40)
        turtle.pendown()
        turtle.write("2. helyezett: {0}\n".format(finish_arr[1]), font=("Arial", 10, "bold"))
        turtle.penup()
        turtle.setpos(180, 20)
        turtle.pendown()
        turtle.write("3. helyezett: {0}\n".format(finish_arr[2]), font=("Arial", 10, "bold"))
        turtle.penup()
        turtle.setpos(180, 0)
        turtle.pendown()
        turtle.write("4. helyezett: {0}\n".format(finish_arr[3]), font=("Arial", 10, "bold"))# Szöveg írás (font, méret, vastag)
        turtle.penup()

        turtle.done()

    except:
        print("A program futása megszakadt!")

def main():
    play()


if __name__== "__main__":
    main()
    

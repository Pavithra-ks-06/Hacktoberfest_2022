import turtle
 ​
 window = turtle.Screen()
 window.bgcolor("black")
 ​
 # Whole pumpkin
 pumpkin = turtle.Turtle()
 pumpkin.hideturtle()
 pumpkin.color("orange")
 pumpkin.dot(200)
 ​
 # The turtle to "carve" the pumpkin
 carver = turtle.Turtle()
 ​
 turtle.done()
 
 import turtle
 ​
 window = turtle.Screen()
 window.bgcolor("black")
 ​
 # Whole pumpkin
 pumpkin = turtle.Turtle()
 pumpkin.hideturtle()
 pumpkin.color("orange")
 pumpkin.dot(200)
 ​
 # The turtle to "carve" the pumpkin
 carver = turtle.Turtle()
 ​
 # "Flatten" the lower part of the pumpkin
 carver.penup()
 carver.setposition(-200, -100)
 carver.pensize(60)
 carver.pendown()
 carver.forward(600)
 carver.pensize(2)
 ​
 turtle.done()
 
 import turtle
 ​
 window = turtle.Screen()
 window.bgcolor("black")
 ​
 # Whole pumpkin
 pumpkin = turtle.Turtle()
 pumpkin.hideturtle()
 pumpkin.color("orange")
 pumpkin.dot(200)
 ​
 # The turtle to "carve" the pumpkin
 carver = turtle.Turtle()
 ​
 # "Flatten" the lower part of the pumpkin
 carver.penup()
 carver.setposition(-200, -100)
 carver.pensize(60)
 carver.pendown()
 carver.forward(600)
 carver.pensize(2)
 ​
 def carve_pumpkin(colour):
     carver.color(colour)
 ​
     # Make eyes
     def make_eye(start, orientation):
         carver.setheading(0)
         carver.penup()
         carver.setposition(*start)
         carver.pendown()
         carver.begin_fill()
         carver.forward(orientation * 40)
         carver.setheading(orientation * 135)
         carver.forward(orientation * 70)
         carver.end_fill()
 ​
     make_eye((-50, 20), 1)
     make_eye((50, 20), -1)
 ​
     # Make mouth
     carver.penup()
     carver.setposition(-50, -30)
     carver.setheading(45)
     carver.pendown()
     carver.pensize(1)
     carver.begin_fill()
     for _ in range(5):
         carver.forward(15)
         carver.right(90)
         carver.forward(15)
         carver.left(90)
     carver.setheading(260)
     carver.forward(20)
     carver.setheading(180)
     carver.forward(99)
     carver.end_fill()
 ​
     # Make nose
     carver.penup()
     carver.setposition(0, 0)
     carver.setheading(90)
     carver.shape("triangle")
     carver.stamp()
 ​
 carve_pumpkin("black")
 ​
 turtle.done()

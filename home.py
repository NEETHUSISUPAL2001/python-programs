import turtle as t

# Set up the turtle screen
screen = t.Screen()
screen.bgcolor("lightblue")

# Create a turtle object for the house
house = t.Turtle()
house.color("black")
house.fillcolor("dark green")
house.penup()

# Draw the house
house.goto(-100, -50)
house.begin_fill()
for _ in range(4):
    house.forward(200)
    house.left(90)
house.end_fill()

# Create a turtle object for the roof
roof = t.Turtle()
roof.color("black")
roof.fillcolor("brown")
roof.penup()

# Draw the roof
roof.goto(-120, 50)
roof.begin_fill()
for _ in range(3):
    roof.forward(240)
    roof.left(120)
roof.end_fill()

# Create a turtle object for the door
door = t.Turtle()
door.color("brown")
door.fillcolor("orange")
door.penup()

# Draw the door
door.goto(0, -50)
door.begin_fill()
for _ in range(2):
    door.forward(50)
    door.left(90)
    door.forward(100)
    door.left(90)
door.end_fill()

# Create a turtle object for the window
window = t.Turtle()
window.color("brown")
window.fillcolor("blue")
window.penup()

# Draw the window
window.goto(50, 0)
window.begin_fill()
for _ in range(4):
    window.forward(40)
    window.left(90)
window.end_fill()

# Close the turtle graphics window wheexpalin clicked
screen.exitonclick()

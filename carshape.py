import turtle as t

# Set up the turtle screen
screen = t.Screen()
screen.bgcolor("white")

# Create a turtle object for the car body
car = t.Turtle()
car.color("blue")
car.fillcolor("blue")
car.penup()

# Draw the car body
car.goto(-70, -30)
car.begin_fill()
car.forward(200)
car.left(90)
car.forward(50)
car.left(90)
car.forward(200)
car.left(90)
car.forward(50)
car.end_fill()

# Create a turtle object for the windows
windows = t.Turtle()
windows.color("black")
windows.penup()

# Draw the front window
windows.goto(20, 20)
windows.begin_fill()
windows.goto(90, 20)
windows.goto(65, 50)
windows.goto(20, 50)
windows.end_fill()

# Draw the rear window
windows.goto(100, 20)
windows.begin_fill()
windows.goto(150, 20)
windows.goto(150, 50)
windows.goto(100, 50)
windows.end_fill()

# Create a turtle object for the wheels
wheel = t.Turtle()
wheel.color("black")
wheel.penup()

# Draw the front wheel
wheel.goto(35, -10)
wheel.begin_fill()
wheel.circle(20)
wheel.end_fill()

# Draw the rear wheel
wheel.goto(135, -10)
wheel.begin_fill()
wheel.circle(20)
wheel.end_fill()

# Close the turtle graphics window when clicked
screen.exitonclick()

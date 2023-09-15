import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle object
pen = turtle.Turtle()

# Function to draw a square
def draw_square():
    for _ in range(4):
        pen.forward(100)
        pen.right(90)

# Function to draw a triangle
def draw_triangle():
    for _ in range(3):
        pen.forward(100)
        pen.left(120)

# Function to draw a circle
def draw_circle():
    pen.circle(50)

# Draw shapes
draw_square()
pen.penup()
pen.goto(200, 0)  # Move the turtle to a new location
pen.pendown()
draw_triangle()
pen.penup()
pen.goto(-200, 0)
pen.pendown()
draw_circle()

# Close the turtle graphics window when clicked
screen.exitonclick()

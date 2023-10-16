import turtle

def tell_purpose():
    print("This program draws 5 plus signs in a turtle window. The size and color of the pluses are both up to you!")



def get_sidelength():
    print("")
    length = float(input("please enter a value for the sidelength of each plus sign: "))
    return length()
    
def get_color1():
    print("")
    print("color options include, but are not limited to: yellow, gold, orange, red, maroon, violet, magenta, purple,")
    print("navy, blue, skyblue, cyan, turquoise, lightgreen, green, darkgreen, chocolate, brown, black, gray, white")
    print("a full list of colors can be found at https://cs111.wellesley.edu/labs/lab02/colors")
    print("")
    color1 = str(input("please enter a color for the first plus sign: "))
    return color1
'''
def get_color2():
    print("")
    color2 = input("please enter a color for the second plus sign: ")



def get_color3():
    print("")
    color3 = input("please enter a color for the third plus sign: ")


def get_color4():
    print("")
    color4 = input("please enter a color for the fourth plus sign: ")


def get_color5():
    print("")
    color5 = input("please enter a color for the fifth plus sign: ")
'''
def goto(x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_plus(size,color):
    turtle.begin_fill()
    turtle.color(color)
    for x in range(4):
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.right(90)
        goto(turtle.xcor() - size * 2, turtle.ycor() - size * 2)
    turtle.end_fill()


def main():
    tell_purpose()
    size = get_sidelength()
    color =get_color1()
    for x in range(5):
        draw_plus(sidelength, color1)


turtle.exitonclick()

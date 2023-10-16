# Jack Fones
# 10-16-2023
# this code creates five plus signs. The user enters a length to determine the size of the pluses and a color to decide
# the color.


import turtle


def tell_purpose():
    """
    this function prints out a line explaining what the code does to the user
    :return: no return
    """
    print(
        "This program draws five plus signs, one in the middle and one at each of the four points of the middle sign.")


def get_side_length():
    """
    This function asks the user for the size of the plus. the number the user types will be the size of each line of
    the plus in pixels. I also experimented with having a try and except command in case the user doesn't type in a
    valid number. Taught myself using https://docs.python.org/3/tutorial/errors.html
    :return: returns a float that will be the size of the plus
    """
    try:
        length = float(input("Enter the length of a side of the plus sign: "))
        return length
    except ValueError:
        print("Invalid number. Please enter a positive integer (ex. 100)")
        return get_side_length()  # if the user does not enter a valid number it will just run get_side_length again.


def get_color():
    """
    this function first prints out a line telling the user exactly what to type, and then asks for an input. I also
    tried to use a syntax error thing for this one, but I don't thing it works with strings.
    :return: returns a string that will be used for the color of each plus
    """
    print("Color options include, but are not limited to: yellow, gold, orange, red, maroon, violet, magenta, purple,")
    print(
        "navy, blue, skyblue, cyan, turquoise, lightgreen, green, darkgreen, chocolate, brown, black, gray, and white.")
    print("")
    print("A full list of colors can be found at https://cs111.wellesley.edu/labs/lab02/colors")
    print("")
    color = input("Enter the color of the plus sign: ")
    return color


def goto(x, y):
    """
    moves the pen to a specified coordinate w/o drawing a line
    :param x: the x coordinate
    :param y: the y coordinate
    :return: no return
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_plus_sign(size, color):
    """
    draws the actual plus. if you slow down the pen you see that it draws it in a really weird way, but it works so
    whatever.
    :param size: determines the size of the plus
    :param color: determines the color of the plus
    :return: no return
    """
    turtle.color(color)
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()


def main():
    """
    runs the code
    :return: no return
    """
    tell_purpose()
    size = get_side_length()
    color = get_color()
    turtle.speed(0)
    draw_plus_sign(size, color)
    goto(10 + (3 * size), 0)  # the math for these is kind of weird. it's taking the user input and multiplying it by
    # 3 so it moves to the correct place, as well as adding/subtracting 10 so there is a small gap between each plus.
    draw_plus_sign(size, color)
    goto((size * -3) - 10, 0)
    draw_plus_sign(size, color)
    goto(0, (size * -3) - 10)
    draw_plus_sign(size, color)
    goto(0, (size * 3) + 10)
    draw_plus_sign(size, color)


main()
turtle.exitonclick()

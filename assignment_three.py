import turtle


def tell_purpose():
    print(
        "This program draws five plus signs, one in the middle and one at each of the four points of the middle sign.")


def get_side_length():
    try:
        length = float(input("Enter the length of a side of the plus sign: "))
        return length
    except ValueError:
        print("Invalid number. Please enter a positive integer (ex. 100)")
        return get_side_length()


def get_color():
    print("Color options include, but are not limited to: yellow, gold, orange, red, maroon, violet, magenta, purple,")
    print(
        "navy, blue, skyblue, cyan, turquoise, lightgreen, green, darkgreen, chocolate, brown, black, gray, and white.")
    print("")
    print("A full list of colors can be found at https://cs111.wellesley.edu/labs/lab02/colors")
    print("")
    color = input("Enter the color of the plus sign: ")
    return color


def goto(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_plus_sign(size, color):
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
    tell_purpose()
    size = get_side_length()
    color = get_color()
    turtle.speed(0)
    draw_plus_sign(size, color)
    goto(10 + (3 * size), 0)
    draw_plus_sign(size, color)
    goto((size * -3) - 10, 0)
    draw_plus_sign(size, color)
    goto(0, (size * -3) - 10)
    draw_plus_sign(size, color)
    goto(0, (size * 3) + 10)
    draw_plus_sign(size, color)


main()
turtle.exitonclick()

import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def koch_snowflake(t, order, size, side=3):
    if side == 0:
        return
    else:
        koch_curve(t, order, size)
        t.right(120)
        koch_snowflake(t, order, size, side - 1)


def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    koch_snowflake(t, order, size)

    window.mainloop()


def main():
    try:
        order = int(input("Enter an order: "))
    except ValueError:
        print('Error: integer expected')
        return
    draw_koch_snowflake(order)


if __name__ == "__main__":
    main()

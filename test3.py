import turtle

t = turtle.Turtle()
turtle.bgcolor("red")
t.speed(100)


def star(t, size):
    if size <= 10:
        return
    else:

        for i in range(100):
            t.fd(size)
            star(t, size/2)
            t.left(216)

star(t ,200)
turtle.done()
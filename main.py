import turtle

def stair(number_of_stairs, stair_nb):
    for i in range(number_of_stairs):
        t.forward(stair_nb)
        t.left(90)
        t.forward(stair_nb)
        t.right(90)
        stair_nb -= 10
    t.forward(stair_nb)


# Create a turtle object
t = turtle.Turtle()
stair(5, 60)



turtle.done()

import turtle as t

class NameWriter(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")

    def write_name(self, name, x, y):
        self.goto(x, y)
        self.write(name, align="center", font=("Arial", 8, "normal"))
import turtle
import math
from typing import Tuple


class Renderer(turtle.Turtle):
    def __init__(self, pensize: int, screen_size: Tuple[int], speed: Tuple[int], title='Renderer') -> None:
        turtle.Turtle.__init__(self)

        self.screen = turtle.Screen()
        self.screen.setup(*[size + 50 for size in screen_size])
        self.screen.title(title)

        self.pensize(pensize)

        self.color('black', 'black')
        self.screen.tracer(*speed)

        self.penup()

        self.hideturtle()

    def draw_reg_pol(self, length: float, sides: int, color=['black', 'black'], mode='normal', fill=True):
        match mode:
            case 'outer':
                outer_radius = length / \
                    (2 * math.sin(math.radians(180) / sides))
                self.goto(self.xcor() + outer_radius - length/2, self.ycor())
            case 'inner':
                inner_radius = length / \
                    (2 * math.tan(math.radians(180) / sides))
                self.goto(self.xcor() + inner_radius - length/2, self.ycor())
            case 'normal':
                pass
            case _:
                pass
        self.color(*color)
        if fill:
            self.begin_fill()
        self.pendown()
        for _ in range(sides):
            self.forward(length)
            self.right(360/sides)
        if fill:
            self.end_fill()
        self.penup()

    def draw_shape(self, vertices: Tuple[tuple], color=['black', 'black'], fill=True):
        """
        Draw a shape defined by vertices, relative to current position.

        Example:
        Renderer.draw_shape(((0, 0), (5, 0), (2.5, 3.5)))
            3.5       #      
                    #####    
                  #########  
            0   X############
                0    2.5    5
            Where X is the staring position
        """

        x, y = self.pos()

        self.goto(vertices[0][0] + x, vertices[0][1] + y)
        self.pendown()
        self.color(*color)
        if fill:
            self.begin_fill()
        for vertex in vertices:
            self.goto(vertex[0] + x, vertex[1] + y)
        self.goto(vertices[0][0] + x, vertices[0][1] + y)
        if fill:
            self.end_fill()
        self.penup()
        self.goto(x, y)

    def write_text(self, text, color='black', align='center', font_config=('Courier', 50, 'bold')):
        self.color(color)
        self.write(text, False, align, font_config)

    def render_frame(self):
        self.screen.update()


if __name__ == '__main__':
    r1 = Renderer(1, (600, 400), (1, 0))
    r1.draw_reg_pol(100, 10)
    r1.draw_shape(((50, 0), (50, 10), (40, 0)))
    r1.goto(0, 0)
    r1.write_text('Renedrer')
    r1.pendown()
    r1.goto(0, 0)
    r1.right(90)
    r1.forward(500)
    r1.render_frame()
    r1.screen.exitonclick()

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

window_size = 800


def cos(x):
    return math.cos(math.radians(x))


def sin(x):
    return math.sin(math.radians(x))


class Curve:
    def __init__(self, point=(0, 0), length=100, angle=0):
        self.point = point
        self.angle = 90 - angle
        self.length = length
        self.draw()

    def draw(self):
        glBegin(GL_LINES)
        glVertex2f(self.point[0], self.point[1])
        glVertex2f(self.point[0] + self.length * cos(self.angle),
                   self.point[1] + self.length * sin(self.angle))
        glEnd()

class Cardioid:
    def __init__(self, pos=(0, 0), r=100, angle=0):
        self.position = pos
        self.r = r
        self.angle = 90 - angle
        self.draw()

    def draw(self):
        glBegin(GL_POINTS)
        for i in range(0, 360, 1):
            x = self.r * (1 + cos(i)) * cos(i) + self.position[0]
            y = self.r * (1 + cos(i)) * sin(i) + self.position[1]
            glVertex2f(x, y)
        glEnd()



class Ellipse:

    def __init__(self, a, b, xc, yc, angle=0):
        self.a = a
        self.b = b
        self.xc = xc
        self.yc = yc
        self.angle = 90 - angle
        self.draw()

    def draw(self):
        glBegin(GL_POINTS)
        for i in range(0, 360, 1):
            x = self.b * cos(i) * cos(self.angle) - self.a * sin(i) * sin(self.angle) + self.xc
            y = self.b * cos(i) * sin(self.angle) + self.a * sin(i) * cos(self.angle) + self.yc
            glVertex2f(x, y)
        glEnd()


class Peacock:
    def __init__(self, pos=(0, 0)):
        self.position = pos
        self.draw()

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    def draw(self):
        stick = Curve(self.position, 300, 0)
        stick.draw()
        self.eye((self.x, self.y + 300))

    def eye(self, pos):
        # draw an ellipsoid with the given position
        ellipsoid = Ellipse(50, 65, pos[0], pos[1], 0)
        ellipsoid = Ellipse(30, 50, pos[0], pos[1], 0)
        # card = Cardioid(pos, 50, 0)


def clear_screen():
    gluOrtho2D(-window_size, window_size, -window_size, window_size)
    glClearColor(0, 0, 0, 0)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    peacock = Peacock()

    glFlush()


def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("Boat")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    clear_screen()
    glutMainLoop()


main()

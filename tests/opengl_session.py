from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def set_pixel(x, y, color=[1,1,0]):
    glColor3f(*color)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def set_line(x1, y1, x2, y2, color):
    # line tickness 5
    # glLineWidth(500)
    glColor3f(*color)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def get_input():
    x_y = []
    x_y.append(float(input("x: ")))
    x_y.append(float(input("y: ")))
    return x_y

def plot():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(50)
    set_pixel(*get_input())
    glFlush()


def main():


    glutInit()
    glutInitWindowSize(1000, 1000)
    glutCreateWindow("first name")
    glutIdleFunc(plot)
    glutMainLoop()


main()

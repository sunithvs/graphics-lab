from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window_size = 800
point_size = 2

def set_point(x, y, color=(1, 1, 0))
    glColor3f(*color)
    glPointSize(point_size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    gl

def display():
    pass


def main():
    glutInit()
    glutInitWindowSize(500, 500)
    glutCreateWindow("Point")
    glutDisplayFunc(display)
    glutMainLoop()


main()

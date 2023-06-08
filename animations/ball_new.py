from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window_size = 800


def display():
    pass


def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("Point")
    glutDisplayFunc(display)
    glutMainLoop()


main()

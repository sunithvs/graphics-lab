from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def clear_screen():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(0, 100, 0, 100)


def main():

    glutInit()
    glut
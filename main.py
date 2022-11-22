#!/usr/bin/env python

import sys

from OpenGL.GL import *
from OpenGL.GLUT import *


def main():
    # Initialize OpenGL
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

    # Configure the display output
    glutGameModeString("2560x1024:24@60")
    glutEnterGameMode()

    # Setup callbacks
    glutKeyboardFunc(keyboard)
    glutDisplayFunc(display)

    # Begin!
    glutMainLoop()


def keyboard(key, x, y):
    if key == 'q':
        sys.exit(0)


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_LINES)
    glVertex2f(1.0, 1.0)
    glVertex2f(-1.0, -1.0)
    glEnd()

    glutSwapBuffers()


if __name__ == "__main__":
    main()

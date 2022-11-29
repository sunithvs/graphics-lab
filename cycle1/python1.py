from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import cos,sin,radians as rad
window_size=1000
x1=0
y1=0
x2=1
y2=.6
x3=.3
y3=1
x4=.2
y4=.6
def plot_points():
	global x1,y1,x2,y2,x3,y3,x4,y4
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_POLYGON)
	glVertex2f(x1,y1)
	glVertex2f(x2,y2)
	glVertex2f(x3,y3)
	glVertex2f(x4,y4)
	glEnd()
	glFlush()
	option=int(input("enter 1-translation 2-rotation 3-scaling"))
	if option==1:
		x=int(input("enter x inc"))/window_size
		y=int(input("enter y inc"))/window_size
		x1=x1+x
		y1=y1+y
		x2=x2+x
		y2=y2+y
		x3=x3+x
		y3=y3+y
		x4=x4+x
		y4=y4+y
	elif option==2:
		angle=float(input("enter angle"))
		x1=x1*cos(rad(angle))+y1*sin(rad(angle))
		x2=x2*cos(rad(angle))+y2*sin(rad(angle))
		x3=x3*cos(rad(angle))+y3*sin(rad(angle))
		y1=y1*cos(rad(angle))-x1*sin(rad(angle))
		y2=y2*cos(rad(angle))-x2*sin(rad(angle))
		y3=y3*cos(rad(angle))-x3*sin(rad(angle))	 
def main():
	 
	glutInit()
	glutInitWindowSize(window_size,window_size)
	glutCreateWindow("ff")
	glutIdleFunc(plot_points)
	glutMainLoop()
	 
main()

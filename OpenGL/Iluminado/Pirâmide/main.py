from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import sys

colors = {'Red': (1.,.0,.0),
		  'Wine': (.5,0,0),
		  'White': (1,1,1)}
radius = 5
angle = 0.1

total_sides = 6
max_sides = 10
min_sides = 3

height = 7
max_height = 10
min_height = -8

def draw_base():
	# DESENHA A BASE
	glBegin(GL_TRIANGLE_FAN)

	glColor3fv(colors['Red'])
	glVertex3f(0,0,0)

	vertex = []
	
	for i in range(total_sides + 1):
		angle = (i/total_sides) * 2 * math.pi
		x = radius * math.sin(angle)
		y = 0
		z = radius * math.cos(angle)
		vertex.append((x,y,z))
		glVertex3f(x,y,z)
	
	glEnd()

	# DESENHA O CONTORNO
	glColor3fv(colors['White'])

	last_vertex = vertex[-1]

	for v in vertex:
		glBegin(GL_LINES)
		x,y,z = v
		glVertex3f(x, y, z)	
		x,y,z = last_vertex
		glVertex3f(x, y, z)	
		glEnd()
		
		last_vertex = v

	return vertex

def draw_sides(vertex):
	glBegin(GL_TRIANGLE_FAN)
	
	# DESENHA AS LATERAIS
	top = (0,height,0)
	x,y,z = top

	glColor3fv(colors['Red'])
	glVertex3f(x,y,z)
	
	glColor3fv(colors['Wine'])
	
	for v in vertex:
		x,y,z = v
		glVertex3f(x, y, z)
	
	glEnd()

	# DESENHA AS LINHAS
	glColor3fv(colors['White'])	
	for v in vertex:
		glBegin(GL_LINES)
		x,y,z = top
		glVertex3f(x, y, z)
		x,y,z = v
		glVertex3f(x, y, z)	
		glEnd()

def mouse_click_effects(button, state, x, y):
	global height, total_sides, angle_view

	if button == 0 and state == 0 and total_sides < max_sides:
		total_sides += 1
	elif button == 2 and state == 0 and total_sides > min_sides:
		total_sides -= 1
	elif button == 3 and height < max_height:
		height += 0.1
	elif button == 4 and height > min_height:
		height -= 0.1

def draw():
	global angle

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glPushMatrix()
	
	glRotate(angle,1,1,0)

	vertex = draw_base()
	draw_sides(vertex)
	angle += 1

	glPopMatrix()
	glutSwapBuffers()

def timer(i):
	glutPostRedisplay()
	glutTimerFunc(30,timer,1)

def init():
	mat_ambient = (0.0, 0.7, 0.0, 1.0)
	mat_diffuse = (0.0, 1.0, 0.0, 1.0)
	mat_specular = (0.0, 1.0, 0.0, 1.0)
	mat_shininess = (10,)
	light_position = (10, 100, -10)
	glClearColor(0.0,0.0,0.0,0.0)
	glShadeModel(GL_FLAT)

	glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
	glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glLightfv(GL_LIGHT0, GL_POSITION, light_position)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_MULTISAMPLE)


def config():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
	glutInitWindowSize(800,800)
	glutCreateWindow("Piramide Iluminada")
	glutDisplayFunc(draw)
	glutMouseFunc(mouse_click_effects)
	glEnable(GL_MULTISAMPLE)
	glEnable(GL_DEPTH_TEST)
	glClearColor(0.,0.,0.,1.)
	gluPerspective(45,800.0/600.0,0.1,100.0)
	glTranslatef(0.0,-2,-25)
	glutTimerFunc(20,timer,1)
	init()
	glutMainLoop()

if __name__ == '__main__':
    config()

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

colors = {'YELLOW': (1.,.7,.0),
		  'DARK-YELLOW': (.2,.2,0),
		  'BLACK': (.0,.0,0)}
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

	glColor3fv(colors['DARK-YELLOW'])
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
	glColor3fv(colors['BLACK'])

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

	glColor3fv(255,0,0)
	glVertex3f(x,y,z)
	
	glColor3fv(colors['YELLOW'])
	
	for v in vertex:
		x,y,z = v
		glVertex3f(x, y, z)
	
	glEnd()

	# DESENHA AS LINHAS
	glColor3fv(colors['BLACK'])	
	for v in vertex:
		glBegin(GL_LINES)
		x,y,z = top
		glVertex3f(x, y, z)
		x,y,z = v
		glVertex3f(x, y, z)	
		glEnd()

def mouse_click_effects(button, state, x, y):
	global height, total_sides

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
	
	glRotate(angle,0,1,0)

	vertex = draw_base()
	draw_sides(vertex)
	angle += 1

	glPopMatrix()
	glutSwapBuffers()

def timer(i):
	glutPostRedisplay()
	glutTimerFunc(30,timer,1)

def config():
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
	glutInitWindowSize(1000,800)
	glutCreateWindow("Piramide")
	glutDisplayFunc(draw)
	glutMouseFunc(mouse_click_effects)
	glEnable(GL_MULTISAMPLE)
	glEnable(GL_DEPTH_TEST)
	glClearColor(0.,0.,0.,1.)
	gluPerspective(45,800.0/600.0,0.1,100.0)
	glTranslatef(0.0,-2,-25)
	glutTimerFunc(20,timer,1)

if __name__ == '__main__':
	glutInit(sys.argv)
	config()
	glutMainLoop()	
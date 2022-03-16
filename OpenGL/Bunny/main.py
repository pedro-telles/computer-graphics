from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from PLY_Reader import PLYReader, converter_helpper
import pprint as pp

angle = 0

def set_color(intensity):
	color = intensity
	
	glColor3f(color, color, color)

def draw_bunny_points(vertex):
	
	glTranslatef(0.1,0,0)
	glRotatef(angle,0,-0.5,0)
	set_color(1)

	for v in vertex:
		x1, y1, z1, _, _ = v.strip().split(' ')

		glBegin(GL_POINTS)
		glVertex3f(converter_helpper['float'](x1),
				   converter_helpper['float'](y1),
				   converter_helpper['float'](z1))
		glEnd()

def draw_bunny_faces(vertex, face):
	
	glTranslatef(-0.1,0,0)
	glRotatef(angle,0,0.5,0)

	for f in face:
		size, index_1, index_2, index_3 = f.strip().split(' ')

		x1, y1, z1, _, intensisty1 = vertex[converter_helpper['int'](index_1)].strip().split(' ')
		x2, y2, z2, _, intensisty2 = vertex[converter_helpper['int'](index_2)].strip().split(' ')
		x3, y3, z3, _, intensisty3 = vertex[converter_helpper['int'](index_3)].strip().split(' ')

		glBegin(GL_TRIANGLES)
		
		set_color(converter_helpper['float'](intensisty1))
		glVertex3f(converter_helpper['float'](x1),
				   converter_helpper['float'](y1),
				   converter_helpper['float'](z1))
		set_color(converter_helpper['float'](intensisty2))
		glVertex3f(converter_helpper['float'](x2),
				   converter_helpper['float'](y2),
				   converter_helpper['float'](z2))

		set_color(converter_helpper['float'](intensisty3))
		glVertex3f(converter_helpper['float'](x3),
				   converter_helpper['float'](y3),
				   converter_helpper['float'](z3))
		glEnd()

def draw():
	global angle

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	
	glPushMatrix()
	draw_bunny_points(data['vertex'])	
	glPopMatrix()

	glPushMatrix()
	draw_bunny_faces(data['vertex'], data['face'])
	glPopMatrix()
	
	angle += 10

	glutSwapBuffers()

def timer(i):
	glutPostRedisplay()
	glutTimerFunc(30,timer,1)

def config():
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
	glutInitWindowSize(800,800)
	glutCreateWindow("PLY")
	glutDisplayFunc(draw)
	glEnable(GL_MULTISAMPLE)
	glEnable(GL_DEPTH_TEST)
	glClearColor(0.,0.,0.,1.)
	gluPerspective(45,800.0/600.0,0.1,100.0)
	glTranslatef(0.0,-0.1,-0.5)
	glutTimerFunc(20,timer,1)

if __name__ == '__main__':

	object = PLYReader('bunny.ply')
	header, data = object.extract_data()
	glutInit(sys.argv)
	config()
	glutMainLoop()
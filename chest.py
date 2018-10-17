# -*- coding: UTF-8 -*-
######333
from OpenGL.GLUT import * # Se importan las librerias de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from random import randint, uniform,random
import math
import sys
##########variables iniciales
GL_PI = 3.1415
PI =3.14159265
SIZE = 800
NEAR_Z = 1.0
FAR_Z = 100.0	# For the frustum size.
TAM_ESC1 = 3
TAM_ESC2 = 10
TAM_ARR = 100
x_Angle = 0		# The rotation angles about x, y and z axis.
y_Angle = 0
z_Angle = 0
BOX_SIZE = 4.0
#####3333

def DibujaCuadrado():
	glBegin(GL_QUADS)
	#//Top face
	#glColor3f(1.0, 1.0, 0.0)
	glVertex3f(-BOX_SIZE / 2 , BOX_SIZE / 2, -BOX_SIZE / 2)
	glVertex3f(-BOX_SIZE / 2 , BOX_SIZE / 2, BOX_SIZE / 2)
	glVertex3f(BOX_SIZE / 2 , BOX_SIZE / 2, BOX_SIZE / 2)
	glVertex3f(BOX_SIZE / 2 , BOX_SIZE / 2, -BOX_SIZE / 2)

	#//Bottom face
	#glColor3f(1.0, 0.0, 1.0)# // Morado
	glVertex3f(-BOX_SIZE / 2  , -BOX_SIZE / 2, -BOX_SIZE / 2)
	glVertex3f(BOX_SIZE / 2  , -BOX_SIZE / 2, -BOX_SIZE / 2)
	glVertex3f(BOX_SIZE / 2  , -BOX_SIZE / 2, BOX_SIZE / 2)
	glVertex3f(-BOX_SIZE / 2  , -BOX_SIZE / 2, BOX_SIZE / 2)

	#//Left face
	#glColor3f(0.0, 1.0, 1.0)# // Cyan
	glVertex3f(-BOX_SIZE / 2  , -BOX_SIZE / 2, -BOX_SIZE / 2)
	glVertex3f(-BOX_SIZE / 2  , -BOX_SIZE / 2, BOX_SIZE / 2)
	glVertex3f(-BOX_SIZE / 2  , BOX_SIZE / 2, BOX_SIZE / 2)
	glVertex3f(-BOX_SIZE / 2  , BOX_SIZE / 2, -BOX_SIZE / 2)

	#//Right face
	#glColor3f(1.0, 0.0, 0.0)#// Rojo
	glVertex3f(BOX_SIZE / 2 , -BOX_SIZE / 2, -BOX_SIZE / 2)
	glVertex3f(BOX_SIZE / 2 , BOX_SIZE / 2, -BOX_SIZE / 2)
	glVertex3f(BOX_SIZE / 2 , BOX_SIZE / 2, BOX_SIZE / 2)
	glVertex3f(BOX_SIZE / 2 , -BOX_SIZE / 2, BOX_SIZE / 2)

	#glColor3f(1.0, 1.0, 1.0)
	glVertex3f(-BOX_SIZE / 2 , -BOX_SIZE / 2, BOX_SIZE / 2)
	glVertex3f(BOX_SIZE / 2 , -BOX_SIZE / 2, BOX_SIZE / 2)
	glVertex3f(BOX_SIZE / 2 , BOX_SIZE / 2, BOX_SIZE / 2)
	glVertex3f(-BOX_SIZE / 2 , BOX_SIZE / 2, BOX_SIZE / 2)
	#	//Back face : Polígono Texturizado
	#glColor3f(0.0, 0.0, 1.0)
	glVertex3f(-BOX_SIZE / 2 , -BOX_SIZE / 2, -BOX_SIZE / 2)
	glVertex3f(BOX_SIZE / 2 , -BOX_SIZE / 2, -BOX_SIZE / 2)
	glVertex3f(BOX_SIZE / 2 , BOX_SIZE / 2, -BOX_SIZE / 2)
	glVertex3f(-BOX_SIZE / 2 , BOX_SIZE / 2, -BOX_SIZE / 2)
	glEnd()

##
#33 En esta funcion se dibuja el Torus pasando por parametro las cordenadas en el plano de x,y,z, el tamano en w y la Q para la anchura.
def Torus(X,Y,Z,W,Q):
    innerRaidus=Q
    outterRaidus=1
    sides=50
    rings=50
    glTranslatef(X,Y,Z)
    glScalef(W,1.0,1.0)
    glutSolidTorus(innerRaidus,outterRaidus,sides,rings)


#####333
def reshapeTorus(x,y):

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(100.0,1,0.5,20.0)
    glViewport(0,0,x,y)#mover en la pantalla
######3333
####3333
### en esta funcion se define el cilindro y se dibuja en las cordenadas especificadas de X,Y
def DibujaCilindro (X, Y, LADOS):
    x = 0.0
    y = 0.0
    z = 0.0
    angle = 0.0
    radio = 0.0
    Contador = 0
    #### aqui se asignan los puntos usando un for entre 0 y tamano de arreglos a una lista
    Puntos1 = []
    for i in range(0, TAM_ARR, 1):
        Puntos1.append([])
    Puntos2 = []
    for i in range(0, TAM_ARR, 1):
        Puntos2.append([])

    z = 5.0
    radio = 1.5
    Contador = 0
    #### Mientras el angulo sea menor o igual a 2.0*PI de GL se dibujara el primer poligono
    #printf ("\n Puntos Primer Poligono ");
    angle = 0.0
    glBegin(GL_POLYGON)
    #glColor3f(1.0,0.0,1.0)
    while angle <= 2.0*GL_PI:
        Puntos1[Contador].append(radio*math.sin(angle)+X)##En esta linea se asigna los valores en puntos1 con el contador de cada angulo.
        Puntos1[Contador].append(radio*math.cos(angle)+Y)
        Puntos1[Contador].append(z)
        glVertex3d(Puntos1[Contador][0], Puntos1[Contador][1], Puntos1[Contador][2]) #Se dibuja pasando los parametros
        Contador = Contador + 1# se le suma al contador 1 por cada exitosa
        angle = angle + (2.0*GL_PI)/LADOS
    glEnd()

    #printf ("\n Puntos Segundo Poligono ");
    z = -5.0
    radio = 1.5
    Contador = 0
    angle = 0.0
    glBegin(GL_POLYGON)
    #glColor3f(1.0,0.0,0.0)
    while angle <= 2.0*GL_PI:
        Puntos2[Contador].append(radio*math.sin(angle)+X)
        Puntos2[Contador].append(radio*math.cos(angle)+Y)
        Puntos2[Contador].append(z)
        glVertex3f(Puntos2[Contador][0], Puntos2[Contador][1], Puntos2[Contador][2])
        Contador = Contador + 1
        angle = angle + (2.0*GL_PI)/LADOS
    glEnd()
    glFlush()

    for i in range( 0, LADOS, 1):
        glBegin(GL_POLYGON)
        glColor3f(1.0,1.0,1.0/(i+1))
        Temporal = 0
        if (i == int(LADOS-1)):
            Temporal = 0
        else:
            Temporal = i+1
        glVertex3f(Puntos1[i][0], Puntos1[i][1], Puntos1[i][2])
        glVertex3f(Puntos1[Temporal][0], Puntos1[Temporal][1], Puntos1[Temporal][2])
        glVertex3f(Puntos2[Temporal][0], Puntos2[Temporal][1], Puntos2[Temporal][2])
        glVertex3f(Puntos2[i][0], Puntos2[i][1], Puntos2[i][2])
        glEnd()
        glFlush()
##
def tresde(x,y,z,x1,y1,z1,q):
	glLineWidth(q)
	glBegin(GL_LINES)
	#parte de arriba de la linea
	glVertex3f(x1, y1, z1)
	#parte de abajo el origen btw
	glVertex3f(x, y, z)
	glEnd()
##
#Aqui es donde se llaman todas las funciones para dibujar el cilindro y los torus
def DibujaObjetos():
		#lado derecho
		glPushMatrix()
		glTranslatef(4.1,5,0)
		glRotatef(90,0,100,0)
		glColor3f(0.55, 0.47, 0.14)
		glScalef(1.2,-1.5,0)
		DibujaCilindro(0,2,20)		
		glPopMatrix()
		#lado izquierdo			
		glPushMatrix()
		glTranslatef(-4.1,5,0)
		glRotatef(90,0,100,0)
		glColor3f(0.55, 0.47, 0.14)
		glScalef(1.2,-1.5,0)
		DibujaCilindro(0,2,20)
		glPopMatrix()
		###
		#cuadrado
		glPushMatrix()
		glTranslatef(0,2, 0)
		glColor3f(0.72, 0.45, 0.20)
		glScalef(2.0,1.2,1)
		DibujaCuadrado()
		glPopMatrix()
		##logo
		glPushMatrix()
		glTranslatef(0,1.5,2.1)
		glRotatef(90,0,0,0)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(0.2,0.2,0)
		DibujaCilindro(0,2,20)
		glPopMatrix()
		#Torus sobre el logo
		glPushMatrix()
		glTranslatef(0,-0.4,2.2)
		glScalef(0.4,0.4,0)
		glColor3f(0.8, 0.2, 0.1)
		Torus(0.0,6.0,-1.7,1.6,0.5)
		glPopMatrix()
		#lineas izquierda frontal
		glPushMatrix()
		glTranslatef(-3,-0.4,2.1)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(-3.2,-0.4,2.1)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(-3.4,-0.4,2.1)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(-3.6,-0.4,2.1)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(-3.8,-0.4,2.1)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(-4,-0.4,2.1)
		glColor3f(0.80, 0.80, 0.80)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		#lineas derecha frontal
		glPushMatrix()
		glTranslatef(3,-0.4,2.1)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(3.2,-0.4,2.1)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(3.4,-0.4,2.1)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(3.6,-0.4,2.1)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(3.8,-0.4,2.1)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(4,-0.4,2.1)
		glColor3f(0.80, 0.80, 0.80)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		#linea izquierda interna frontal
		glPushMatrix()
		glTranslatef(-1.5,-0.4,2.1)
		glColor3f(0.658824, 0.658824, 0.658824)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,5)
		glPopMatrix()
		#linea derecha interna frontal
		glPushMatrix()
		glTranslatef(1.5,-0.4,2.1)
		glColor3f(0.658824, 0.658824, 0.658824)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,5)
		glPopMatrix()
		#lineas izquierda trasera
		glPushMatrix()
		glTranslatef(-3,-0.4,-2.1)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(-3.2,-0.4,-2.1)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(-3.4,-0.4,-2.1)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(-3.6,-0.4,-2.1)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(-3.8,-0.4,-2.1)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(-4,-0.4,-2.1)
		glColor3f(0.80, 0.80, 0.80)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		#lineas derecha trasera
		glPushMatrix()
		glTranslatef(3,-0.4,-2.1)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(3.2,-0.4,-2.1)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(3.4,-0.4,-2.1)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(3.6,-0.4,-2.1)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(3.8,-0.4,-2.1)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		glPushMatrix()
		glTranslatef(4,-0.4,-2.1)
		glColor3f(0.80, 0.80, 0.80)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,10)
		glPopMatrix()
		#linea izquierda interna trasera
		glPushMatrix()
		glTranslatef(-1.5,-0.4,-2.1)
		glColor3f(0.658824, 0.658824, 0.658824)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,5)
		glPopMatrix()
		#linea derecha interna trasera
		glPushMatrix()
		glTranslatef(1.5,-0.4,-2.1)
		glColor3f(0.658824, 0.658824, 0.658824)
		glScalef(1,4.8,0)
		tresde(0,1,0,0,0,0,5)
		glPopMatrix()
		##detalle en las lineas
		glPushMatrix()
		glTranslatef(-1.5,0.4,2.2)
		glRotatef(90,0,0,0)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(0.1,0.1,0)
		DibujaCilindro(0,2,20)
		glPopMatrix()
		##detalle en las lineas
		glPushMatrix()
		glTranslatef(1.5,0.4,2.2)
		glRotatef(90,0,0,0)
		glColor3f(0.90, 0.91, 0.98)
		glScalef(0.1,0.1,0)
		DibujaCilindro(0,2,20)
		glPopMatrix()
    #glutSwapBuffers()


#****************************************************************************************
def showMenu():
	#clear();
    print ("\n\n Introduccion a graficacion por computadora")
    print ("\n OpenGL PROGRAM FOR a 3D CHEST \n")
    print ("\n Welcome to The Cage Of Eden \n")
    print ("********************************************************************\n")
    print ("\n\n Operations: ")
    print ("\n Use the x/X,y/Y and z/Z keys for rotations about x,y and z axes.")
    print ("\n Use m or M to see this menu again.")

#****************************************************************************************
def init (): # Initializes the gl Graphics env and the program variables.
		global x_Angle
		global y_Angle
		global z_Angle
		x_Angle = 0.0
		y_Angle = 0.0
		z_Angle = 0.0

		glEnable(GL_DEPTH_TEST)	# Enable z-Buffering.
		showMenu()

#****************************************************************************************
def keyboardCallbackProc(key, x, y): # This is the callback procedure for capturing OpenGL Keyboard events.
		global x_Angle
		global y_Angle
		global z_Angle
		global p
		global q
		if key == 'x':
				x_Angle = x_Angle + 1
		elif key == 'X':
				x_Angle = x_Angle - 1
		elif key == 'y':
				y_Angle = y_Angle + 1
		elif key == 'Y':
				y_Angle = y_Angle - 1
		elif key == 'z':
				z_Angle = z_Angle + 1
		elif key == 'Z':
				z_Angle = z_Angle - 1
		elif key == 'M' :
				showMenu()
		elif key == 'm' :
				showMenu()
		elif key == b'\033' :				#ESCAPE Code for exiting program.
				sys.exit()
		elif key == 'P' :
				p = p + 1				
		elif key == 'Q' :
				q = q + 1
		glutPostRedisplay()

#****************************************************************************************
def reShapeCallbackProc(w, h): # This is the callback procedure for capturing reShape event for window resizing.
	#glViewport(0, 0, w, h)
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #gluPerspective(60.0, GLfloat(w)/GLfloat(h), NEAR_Z, FAR_Z)
    gluPerspective(60.0, w/h, NEAR_Z, FAR_Z)
    glMatrixMode(GL_MODELVIEW)

#****************************************************************************************
def displayCallbackProc(): # This is the callback procedure for capturing OpenGL Display events.
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glMatrixMode(GL_MODELVIEW)

	glLoadIdentity()
	glTranslatef(-0, -0, -20)	# Translate the object by 10 units in -ve z-direction.
	glRotatef(x_Angle, 1.0, 0.0,0.0)	# Translate the object by 10 units in -ve z-direction.
	glRotatef(y_Angle, 0.0, 1.0,0.0)	# Translate the object by 10 units in -ve z-direction.
	glRotatef(z_Angle, 0.0, 0.0,1.0)	# Translate the object by 10 units in -ve z-direction.
	DibujaObjetos()		# Draw

	glutSwapBuffers()

#****************************************************************************************
def main (): # The main program.
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(SIZE, SIZE)
	glutInitWindowPosition(350, 200)

	glutCreateWindow("Chest")
	init()				# Initialize the env. variables and the program global variables.

	glutDisplayFunc(displayCallbackProc)
	glutKeyboardFunc(keyboardCallbackProc)
	glutReshapeFunc(reShapeCallbackProc)
    #glutReshapeFunc(reshapeTorus)
    #glutIdleFunc(idleTorus)
	glutMainLoop()

main ()
#*************************** END OF PROGRAM ************************************************

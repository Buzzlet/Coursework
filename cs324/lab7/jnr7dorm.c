// dorm.c

#include <GL/glut.h>
#include <stdlib.h>

#define BED 1 // height of 10, 2.5 above, 7.5 below
#define CHAIR 2 // height of 9, 4.5 above, 4.5 below
#define DESK 3 // height of 11, 1 above origin, 10 below
#define LAMP 4 // height of 5, 5 above origin

  GLfloat position[] = {0.0, 17.0, 0.0, 1.0};

void myInit()
{
  glClearColor(0.5, 0.5, 0.5, 1.0);
  glDepthFunc(GL_LEQUAL);
  glEnable(GL_DEPTH_TEST);

  GLfloat global_ambient[] = {0.3, 0.3, 0.3, 1.0};
  GLfloat specular[] = {0.8, 0.8, 0.8, 1.0};
  GLfloat diffuse[] = {0.5, 0.5, 0.5, 1.0};


  glEnable(GL_LIGHTING);
  glEnable(GL_LIGHT0);

  glLightModelfv(GL_LIGHT_MODEL_AMBIENT, global_ambient);
  glShadeModel(GL_SMOOTH);

  glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse);
  glLightfv(GL_LIGHT0, GL_SPECULAR, specular);
  glLightfv(GL_LIGHT0, GL_POSITION, position);

  glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE);
  glEnable(GL_COLOR_MATERIAL);

}

void displayRoom()
{
  // floor
  glColor3f(0.12, 0.12, 0.6);
  glPushMatrix();
  glTranslatef(0.0, -1.0, 0.0);
  glScalef(1.0, 0.05, 1.0);
  glutSolidCube(40);
  glPopMatrix();

  // left wall
  glColor3f(0.05, 0.05, 0.05);
  glPushMatrix();
  glTranslatef(-21.0, 10.0, 0.0);
  glScalef(0.05, 0.5, 1.0);
  glutSolidCube(40);
  glPopMatrix();

  // right wall
  glPushMatrix();
  glTranslatef(21.0, 10.0, 0.0);
  glScalef(0.05, 0.5, 1.0);
  glutSolidCube(40);
  glPopMatrix();

  // back wall
  glPushMatrix();
  glTranslatef(0.0, 10.0, -21.0);
  glScalef(1.0, 0.5, 0.05);
  glutSolidCube(40);
  glPopMatrix();

  // ceiling
  glColor3f(0.04, 0.04, 0.04);
  glPushMatrix();
  glTranslatef(0.0, 21.0, 0.0);
  glScalef(1.0, 0.05, 1.0);
  glutSolidCube(40);
  glPopMatrix();
}

void display()
{
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
  glLoadIdentity();

  displayRoom();
  glPushMatrix();
  glTranslatef(-10.0, 10, -17.5);
  glCallList(DESK);
  glPopMatrix();

  glPushMatrix();
  glTranslatef(10.0, 10, -17.5);
  glCallList(DESK);
  glPopMatrix();

  glPushMatrix();
  glColor3f(0, 0.4, 0);
  glTranslatef(-15, 7.5, 7.5);
  glRotatef(90, 0, 1, 0);
  glCallList(BED);
  glPopMatrix();

  glPushMatrix();
  glColor3f(0, 0, 0.4);
  glTranslatef(15, 7.5, 7.5);
  glRotatef(90, 0, 1, 0);
  glCallList(BED);
  glPopMatrix();

  glPushMatrix();
  glTranslatef(5, 4.5, 0);
  glRotatef(-45, 0, 1, 0);
  glCallList(CHAIR);
  glPopMatrix();

  glPushMatrix();
  glTranslatef(-5, 4.5, 10);
  glRotatef(0, 0, 1, 0);
  glCallList(CHAIR);
  glPopMatrix();

  glPushMatrix();
  glTranslatef(-5, 11, -17);
  glCallList(LAMP);
  glPopMatrix();

  glPushMatrix();
  glTranslatef(15, 11, -17);
  glCallList(LAMP);
  glPopMatrix();

  // draw a box for ceiling light
  glPushMatrix();
  glColor3f(0.95, 0.95, 0.31);
  glTranslatef(position[0], position[1] + 2.5, position[2]);
  glScalef(3.0, 1.0, 6.0);
  glutSolidCube(1);
  glPopMatrix();

  glFlush();
  glutSwapBuffers();
}


void myReshape(int w, int h)
{
  glViewport(0, 0, w, h);
  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  gluPerspective(90.0, (GLfloat) w / (GLfloat) h, 1.0, 100.0);
  gluLookAt(0.0, 15.0, 25.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
  glMatrixMode(GL_MODELVIEW);
  glLoadIdentity();
}



void defineDisplayLists()
{
  GLuint myIndex = glGenLists(3);

  ///////////////////////// DEFINE A STANDARD BED /////////////////////////
  glNewList(myIndex, GL_COMPILE);
  // Matress
  glPushMatrix();
  glScalef(1.0, 0.15, 0.5);
  glutSolidCube(20);
  glPopMatrix();
  // One End
  glColor3f(0.42, 0.28, 0.22);
  glPushMatrix();
  glTranslatef(10.5, -2.5, 0.0);
  glScalef(0.1, 1.0, 1.0);
  glutSolidCube(10);
  glPopMatrix();
  // Other End
  glPushMatrix();
  glTranslatef(-10.5, -2.5, 0.0);
  glScalef(0.1, 1.0, 1.0);
  glutSolidCube(10);
  glPopMatrix();
  glEndList();

  /////////////////////// DEFINE A STANDARD CHAIR /////////////////////
  glNewList(myIndex+1, GL_COMPILE);
  // Chair seat
  glColor3f(0.3, 1.0, 0.3);
  glPushMatrix();
  glScalef(1.0, 0.25, 1.0);
  glutSolidCube(4);
  glPopMatrix();
  // Chair back
  glColor3f(0.42, 0.28, 0.22);
  glPushMatrix();
  glTranslatef(-1.825, 2.5, 0.0);
  glScalef(0.125, 1.0, 1.0);
  glutSolidCube(4);
  glPopMatrix();
  // leg 1
  glPushMatrix();
  glTranslatef(1.875, -2.5, 1.875);
  glScalef(.125, 1.0, .125);
  glutSolidCube(4);
  glPopMatrix();
  // leg 2
  glPushMatrix();
  glTranslatef(-1.875, -2.5, 1.875);
  glScalef(.125, 1.0, .125);
  glutSolidCube(4);
  glPopMatrix();
  // leg 3
  glPushMatrix();
  glTranslatef(1.875, -2.5, -1.875);
  glScalef(.125, 1.0, .125);
  glutSolidCube(4);
  glPopMatrix();
  // leg 4
  glPushMatrix();
  glTranslatef(-1.875, -2.5, -1.875);
  glScalef(.125, 1.0, .125);
  glutSolidCube(4);
  glPopMatrix();

  glEndList();

  ///////////////////////// DEFINE A STANDARD DESK ///////////////////////////
  glNewList(myIndex+2, GL_COMPILE);
  //Desk top
  glColor3f(0.42, 0.28, 0.22);
  //glColor3f(0, 0, 0);
  glPushMatrix();
  glScalef(1.0, 0.1, 0.5);
  glutSolidCube(20);
  glPopMatrix();
  // Desk large side
  glPushMatrix();
  glTranslatef(5.5, -5.5, 0.0);
  glScalef(0.45, 0.45, 0.5);
  glutSolidCube(20);
  glPopMatrix();
  // Desk top drawer
  glPushMatrix();
  glTranslatef(5.5, -3.5, 5.125);
  glScalef(7.0, 3.0, 0.25);
  glutSolidCube(1);
  glPopMatrix();
  // Desk bottom drawer
  glPushMatrix();
  glTranslatef(5.5, -7.5, 5.125);
  glScalef(7.0, 3.0, 0.25);
  glutSolidCube(1);
  glPopMatrix();
  // Desk small side
  glPushMatrix();
  glTranslatef(-9.5, -5.5, 0.0);
  glScalef(0.05, 0.45, 0.5);
  glutSolidCube(20);
  glPopMatrix();

  glEndList();

  //////////////////////// DEFINE A STANDARD LAMP /////////////////////////////
  glNewList(myIndex+3, GL_COMPILE);

  // base of lamp
  glColor3f(0.38, 0.68, 0.1);
  glPushMatrix();
  glTranslatef(0.0, 1.5, 0.0);
  glScalef(1.0, 3.0, 1.0);
  glutSolidCube(1);
  glPopMatrix();

  // lamp top
  glColor3f(0.95, 0.95, 0.31);
  glPushMatrix();
  glTranslatef(0.0, 2.5, 0.0);
  glutSolidSphere(1, 100, 100);
  glPopMatrix();

  glEndList();

  glListBase(myIndex);
}

void main(int argc, char **argv)
{
  glutInit(&argc, argv);
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
  glutInitWindowSize(500, 500);
  glutInitWindowPosition(0, 0);
  glutCreateWindow("Dorm");
  myInit();
  glutReshapeFunc(myReshape);
  glutDisplayFunc(display);
  defineDisplayLists();
  glutMainLoop();
}

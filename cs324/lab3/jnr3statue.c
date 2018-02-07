// statue.c

#include <GL/glut.h>
#include <stdlib.h>
#include <stdio.h>

#define BASE_HEIGHT 2.0
#define PEDESTAL_HEIGHT 3.0
#define PEDESTAL_RADIUS 7.0
#define CUBE_SIZE 5.0
#define CONE_SIZE 2.5
#define SPHERE_SIZE 3.0
#define SPHERE2_SIZE 2.0
int seed = 9001;
GLUquadricObj *pedestal;

// array index corresponds to order to be drawn (index 0 is on bottom)
// number corresponds to object to be drawn
// 0 = cube, 1 = cone, 2 = sphere, 3 = sphere2
int draw_order[4] = {0, 1, 2, 3};

void base()
{
  glPushMatrix();
  glScalef(1.0, .1, 1.0);
  glutWireCube(20);
  glPopMatrix();
}


void myPedestal()
{
  glPushMatrix();
  glRotatef(-90.0, 1.0, 0.0, 0.0);
  gluCylinder(pedestal,PEDESTAL_RADIUS, PEDESTAL_RADIUS, PEDESTAL_HEIGHT,25,25);
  glPopMatrix();
}


void myCube()
{
  glPushMatrix();
  glutWireCube(CUBE_SIZE);
  glPopMatrix();
}


void myCone()
{
  glPushMatrix();
  glRotatef(-90.0, 1.0, 0.0, 0.0);
  glutWireCone(CONE_SIZE, CONE_SIZE, 25, 25);
  glPopMatrix();
}


void mySphere()
{
  glPushMatrix();
  glutWireSphere(SPHERE_SIZE, 25, 25);
  glPopMatrix();
}


void mySphere2()
{
  glPushMatrix();
  glutWireSphere(SPHERE2_SIZE, 25, 25);
  glPopMatrix();
}

void myInit()
{
  srand(seed);
  glClearColor(0.5, 0.5, 0.5, 1.0);
  glColor3f(0.0, 0.3, 1.0);
  glDepthFunc(GL_LEQUAL);
  glEnable(GL_DEPTH_TEST);

  pedestal = gluNewQuadric();
  gluQuadricDrawStyle(pedestal, GLU_LINE);
}


void myReshape(int w, int h)
{
  glViewport(0, 0, w, h);
  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  gluPerspective(90.0, 1.0, 1.0, 50.0);
  gluLookAt(3.0, 25.0, 20.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
  /*glOrtho(-10.0, 10.0, -10.0 * (GLfloat) h / (GLfloat) w,
          10.0 * (GLfloat) h / (GLfloat) w, -20.0, 20.0);*/
  glMatrixMode(GL_MODELVIEW);
  glLoadIdentity();

}


void display()
{
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
  //printf("Entered display()!\n");
  glLoadIdentity();
  //glTranslatef(0.0, 0.0, -15.0);
  //glRotatef(15.0, 1.0, 1.0, 0.0);

  glColor3f(0.0, 0.3, 1.0);
  base();


  glTranslatef(0.0, BASE_HEIGHT / 2.0, 0.0);
  glColor3f(1.0, 0.0, 0.0);
  myPedestal();
  glTranslatef(0.0, PEDESTAL_HEIGHT, 0.0);

  // the idea here is that each object drawn will translate the coordinate
  // system to the top of the object drawn
  for(int i = 0; i < sizeof(draw_order) / sizeof(int); i++)
  {
    switch(draw_order[i])
    {
      // CUBE
      case 0:
        glTranslatef(0.0, CUBE_SIZE * 0.5, 0.0);
        glColor3f(0.0, 1.0, 0.0);
        myCube();
        glTranslatef(0.0, CUBE_SIZE * 0.5, 0.0);
        break;
      // CONE
      case 1:
        glColor3f(0.5, 0.0, 0.5);
        myCone();
        glTranslatef(0.0, CONE_SIZE, 0.0);
        break;
      // SPHERE
      case 2:
        glTranslatef(0.0, SPHERE_SIZE, 0.0);
        glColor3f(0.8, 0.8, 1.0);
        mySphere();
        glTranslatef(0.0, SPHERE_SIZE, 0.0);
        break;
      // SPHERE2
      case 3:
        glTranslatef(0.0, SPHERE2_SIZE, 0.0);
        glColor3f(0.75, 0.25, 0.5);
        mySphere2();
        glTranslatef(0.0, SPHERE2_SIZE, 0.0);
    }
  }

  glFlush();
  glutSwapBuffers();
}


void menu(int id)
{
  switch(id)
  {
    // clockwise
    case 0:
      for(int i = 0; i < sizeof(draw_order) / sizeof(int); i++)
      {
        if(draw_order[i] < (sizeof(draw_order) / sizeof(int)) - 1)
        {
          draw_order[i]++;
        }
        else
        {
          draw_order[i] = 0;
        }
      }
      break;
    // counter clockwise
    case 1:
      for(int i = 0; i < sizeof(draw_order) / sizeof(int); i++)
      {
        if(draw_order[i] != 0)
        {
          draw_order[i]--;
        }
        else
        {
          draw_order[i] = sizeof(draw_order) / sizeof(int) - 1;
        }
      }
      break;
    // Randomize
    // using a trial-and-error approach
    case 2:
      // reset the array
      for(int i = 0; i < sizeof(draw_order) / sizeof(int); i++)
      {
        draw_order[i] = -1;
      }

      // for each index, generate a unique number ranging from 0 to the length
      // of the array
      for(int i = 0; i < sizeof(draw_order) / sizeof(int); i++)
      {
        while(draw_order[i] == -1)
        {
          int numFound = 0;
          int randNum = rand() % 4;
          // check to see if the random number is already in the array
          for(int j = 0; j < sizeof(draw_order) / sizeof(int); j++)
          {
            if(draw_order[j] == randNum)
            {
              numFound = 1;
            }
          }
          // if the number isn't already in the array, add it
          if(numFound == 0)
          {
            draw_order[i] = randNum;
          }
        }
      }
      break;
    case 3:
      exit(0);
  }
}


void main(int argc, char **argv)
{
  glutInit(&argc, argv);
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
  glutInitWindowSize(500, 500);
  glutInitWindowPosition(0, 0);
  glutCreateWindow("Statue");
  myInit();
  glutReshapeFunc(myReshape);
  glutDisplayFunc(display);

  glutCreateMenu(menu);
  glutAddMenuEntry("Cycle Clockwise", 0);
  glutAddMenuEntry("Cycle Counter-Clockwise", 1);
  glutAddMenuEntry("Randomize", 2);
  glutAddMenuEntry("Quit", 3);
  glutAttachMenu(GLUT_RIGHT_BUTTON);
  glutMainLoop();
}

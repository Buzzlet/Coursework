// Program: linkedlist.c
// Class:   cs231
// Date:    09/21/2015
// Author:  Joel Ristvedt

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct node
{
    char value[50];
    struct node* next;
};


void printlist(struct node* root)
{
    // print root separately
    printf("\n%s ", root->value);
    struct node* current = root;

    // print string at each node until ent of list
    for(int i = 0; current->next != 0; i++)
    {
        current = current->next;
        printf("%s ", current->value);
    }
    printf("\n");
}


int main()
{
    int const LISTLEN = 5;
    struct node* root;
    struct node* current;
    char name[50];

    // make initial pointer
    root = (struct node*) malloc(sizeof(struct node));

    printf("\nEnter 5 names into a linked list one at a time: \n");
    fgets(name, 50, stdin);

    // handle root rather than iterable "current"
    for(int j = 0; j < 50; j++)
    {
        // don't copy over new lines
        if(name[j] != '\n')
        {
            root->value[j] = name[j];
        }
    }

    // make current pointer
    current = root;

    // for each item in the linked list make a node, set the string to a new
    // string and change next pointer
    for(int i = 0; i <  LISTLEN - 1; i++)
    {
        current->next = (struct node*) malloc(sizeof(struct node));
        char name[50];
        fgets(name, 50, stdin);
        current = current->next;
        for(int k = 0; k < 50; k++)
        {
            if(name[k] != '\n')
            {
                current->value[k] = name[k];
            }
        }
    }

    // signal end of linked list
    current->next = 0;

    // print list
    printf("Name List:");
    printlist(root);
}

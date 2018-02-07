// Program: hashtable2.c
// Date:    09/28/2015
// Class:   cs231
// Author:  Joel Ristvedt

/*
Description:

This program gets a bunch of alphanumeric strings to store into a hash table.
The program then loops allowing the user to search for strings until the they
enter a blank line.

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


// A single node of a linked list
struct node
{
    char value[7];
    struct node* next;
};

// A group of pointers needed for each linked list
typedef struct linkedlist
{
    struct node* root;
    struct node* current;
}linkedlist;


int hashkey(char* line, int max)
{
    int leftnum, midnum, rightnum, sum, key;

    leftnum = (line[0] * 256 + line[1]) | 0b0000000001010101;
    midnum = (line[2] * 256 + line[3]) & 0b1111111101010101;
    rightnum = (line[4] * 256 + line[5]) ^ 0b0000000001010101;
    sum = leftnum + midnum + rightnum;
    key = sum % max;
    return(key);
}


void printhashtable(linkedlist* hashtable, int size)
{
    struct node* current;
    for(int i = 0; i < size; i++)
    {
        printf("%2d", i);
        for(current = hashtable[i].root; current != NULL;
            current = current->next)
        {
            printf("%7s", current->value);
        }
        printf("\n");
    }
}


int searchhash(char* query, linkedlist* hashtable, int size)
{
    char query1[strlen(query)];
    strcpy(query1, query);
    struct node* current;
    for(int k = 0; query1[k] != '\0'; k++)
    {
        if(query1[k] == '\n') query1[k] = '\0';
    }
    int queryfound = -1;
    int key = hashkey(query1, size);
    for(current = hashtable[key].root; current != NULL;
        current = current->next)
    {
        queryfound = strcmp(query1, current->value);
        if(queryfound == 0)
        {
            goto end;
        }
    }
    end:
    return(queryfound);
}


int main()
{
    // make linelen longer than 6 just to be careful with memory
    int const LINELEN = 10;
    int const STRINGS = 150;
    int const HASHSIZE = 100;
    char line[LINELEN];
    int key;
    FILE *infp;
    linkedlist hashtable[HASHSIZE];

    // initialize the roots
    for(int j = 0; j < HASHSIZE; j++)
    {
        hashtable[j].root = NULL;
    }

    infp = fopen("/tmp/cs231_hashdata.dat", "r");
    for(int i = 0; i < STRINGS; i++)
    {
        // get string
        fgets(line, LINELEN , infp);
        for(int l = 0; line[l] != '\0'; l++)
        {
            if(line[l] == '\n') line[l] = '\0';
        }

        // generate index in hashtable
        key = hashkey(line, HASHSIZE);
        // handle root separately
        if(hashtable[key].root == NULL)
        {
            // make a node to point root to
            hashtable[key].root = (struct node*) malloc(sizeof(struct node));
            // make the new node's value the new line
            strcpy((hashtable[key].root)->value, line);
            // set current to point to root
            hashtable[key].current = hashtable[key].root;
            // point the new node to zero
            (hashtable[key].root)->next = NULL;
        }
        // if it's not the first with the particular hash key
        else
        {
            // make a new node
            (hashtable[key].current)->next = (struct node*) malloc(sizeof(struct node));
            // update current
            hashtable[key].current = (hashtable[key].current)->next;
            // make the new node's value the new line
            strcpy((hashtable[key].current)->value, line);
            // point next to zero
            (hashtable[key].current)->next = 0;
        }
    }
    fclose(infp);

    // Print instructions
    printf("\nHash Table\n");
    printf("This program will read alphanumeric keys from a file and put them into a hash\n");
    printf("table. The program will then print out the contents of the hash table, and\n");
    printf("it will allow you to enter a string to search for in the hash table until you\n");
    printf("enter a blank line.\n");

    // Print table
    printf("\nHash Table and Values: \n");
    printhashtable(hashtable, HASHSIZE);

    // Print prompt
    printf("Enter a string to see if it is in the hashtable (break with empty line): ");
    fgets(line, LINELEN, stdin);
    while(strcmp(line,"\n") != 0)
    {
        if(searchhash(line, hashtable, HASHSIZE) == 0)
        {
            printf("The string IS in the hash table!\nEnter another string: ");
        }
        else
        {
            printf("The string is NOT in the hash table!\nEnter another string: ");
        }
        fgets(line, LINELEN, stdin);
    }
}

/*
Analysis:

    In this program I made a second struct as my way of making an abstract
concept of a linked list. Doing it this way allowed me to not have to make an
array of current pointers. My progam uses a lot of loops and comparisons, but
not many moves and exchanges. It would have been nice if I could have had a
traversal function that accepted a behavior to do on each traversal, but I
didn't look into it too much. I wasn't able to fully get the searchhash 
function working on all lengths of strings.

*/

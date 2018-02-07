// Program: randgen.c
// Date:    09/09/2015
// Class:   cs231
// Author:  Joel Ristvedt

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int seed = 1337;
    printf("This program will return the first 25 numbers from a random\n");
    printf("number generator for which you enter a numerical seed.\n"); 
    printf("Enter a seed now: ");
    scanf("%d", &seed);
    printf("\n");

    srand(seed);

    int i = 0;
    // print rows
    for(; i < 5; i++)
    {
        int j = 0;
        // print columns
        for(; j < 5; j++)
        {
            // get a new number from 1-50000 each time
            int randnum = rand() % 50000;
            printf("%7d", randnum);
        }
        printf("\n");
    }
    printf("\n");
    return(0);
}

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{

    char line[50];
    int done = -1;

    printf("\n");
    printf("This program will echo whatever you say. Enter a string!\n");

    while(done != 0)
    {
        fgets(line, 50, stdin);

        if (strcmp(line, "\n") == 0)
        {
            done = 0;
        }
        else
        {
            printf("%s", line);
        }
    }
    return(done);
}

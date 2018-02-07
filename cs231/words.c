#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char line[200];
    
    printf("\nThis program will separate whatever words you enter.\n");

    fgets(line, 200, stdin);

    int linelen = strlen(line);

    int printindex = 0;
    int i;
    for(i = 0; i < linelen; i++)
    {
        // A manual emergency break for end of string
        if(line[i] == '\0')
        {
            i = linelen;
        }

        else if(line[i] == '\n' || line[i] == '\t' || line[i] == ' ')
        {

            for(; printindex < i; printindex++)
            {
                printf("%c", line[printindex]);
            } 
            // skips actual separator
            printindex++;

            printf("\n");

        }// else if

    }// for loop
    return(0);
}// main

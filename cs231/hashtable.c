// Program: hashtable.c
// Class:   cs231
// Date:    09/21/2015
// Author:  Joel Ristvedt

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int const TABLELEN = 5000;
    int const LINELEN = 4;
    char line[4];
    int leftnum, rightnum, sum, hashkey;

    // prompt
    printf("\nEnter a string of up to 4 characters long to get a hash key: ");
    fgets(line, LINELEN + 1, stdin);

    // don't consider \n to be part of string
    for(int i = 0; i < LINELEN; i++)
    {
        if(line[i] == '\n')
        {
            line[i] = 0;
        }
    }

    printf("\nInput: %c%c%c%c\n", line[0], line[1], line[2], line[3]);
    printf("ASCII VALUES:\n%c: %d\n", line[0], line[0]);
    printf("%c: %d\n", line[1], line[1]);
    printf("%c: %d\n", line[2], line[2]);
    printf("%c: %d\n", line[3], line[3]);

    leftnum = line[0] * 256 + line[1];
    rightnum = line[2] * 256 + line[3];
    printf("\nLeft pre-conversion: %d\n", leftnum);
    printf("Right pre-conversion: %d\n", rightnum);

    leftnum = leftnum | 0b0000000001010101;
    rightnum = rightnum & 0b1111111101010101;
    printf("\nLeft post-conversion: %d\n", leftnum);
    printf("Right post-conversion: %d\n", rightnum);

    sum = leftnum + rightnum;
    hashkey = sum % TABLELEN;
    printf("\nSum: %d\n", sum);
    printf("Hash key: %d\n\n", hashkey);

    return(0);
}

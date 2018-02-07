// Program: separatrenums.c
// Date:    09/09/2015
// Class:   cs231
// Author:  Joel Ristvedt

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int finddigits(int num)
// finds how many digits are in the entered number
{
    int digits = 0;
    int digitsfound = -1;
    int power = 0;
    while(digitsfound != 0)
    {
        // continually divide by multiples of 10 until the div is 0
        if(div(num, pow(10, power)).quot != 0)
        {
            digits++;
        }
        else digitsfound = 0;
        power++;
    }
    return(digits);
}


void printdigits(int num)
// finds each digit and prints it out
{
    int digits = finddigits(num);
    int i = 0;
    for(; i < digits; i++)
    {
        // first find the the number where the lowest digit is the digit being
        // sought after, then remove the last digit
        int digitsbefore = div(num, pow(10, i)).quot;
        int digit = div(digitsbefore, 10).rem;
        printf("Digit %d: %d\n", i+1, digit);
    }
}


int main()
{
    int usernum;
    printf("This program can reduce a five digit number into its components!");
    printf("\nEnter a 5 digit number: ");
    scanf("%d", &usernum);
    // this will only work on up to 10 digit numbers for some reason
    printdigits(usernum);
    return(0);
}

// Program: wordcount.c
// Class:   cs231
// Date:    09/04/2015
// Author:  Joel Ristvedt

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void printinfo()
// printinfo prints the directions about what this program does and how to use
// it.
{
    printf("\nWord Count\n");
    printf("This program will continually take lines from the keyboard and");
    printf("\necho the line back until a blank line is entered. The program");
    printf("\nwill then determine and display the number of lines, words and");
    printf("\ncharacters entered. Additionally the program will provide a ");
    printf("\ntable of used characters and their frequencies.\n");
    printf("\nBegin entering lines:\n");
    printf(">");

}

int countwords(char* line, int linelen, int wordcount)
/* countwords accepts a character array and separates the words at tabs, new
lines and spaces, prints out each word, and returns the updated count of words
entered by the user.

   parameters:
    line - a pointer to the char array holding the last entered line
    linelen - the length of line
    wordcount - the cumulative number of words entered
   returns:
    wordcount - the updated number of words entered

   local variables:
    printindex - index of character to print (or not print)
    i - counter to loop through the characters in the line
*/
{
    int printindex = 0;
    int i;
    printf("\nWORDS:\n");
    for(i = 0; i < linelen; i++)
    {
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
            wordcount++;
            printindex++;
            printf("\n");
        }
    }
    return(wordcount);
}


void populatechar(char* line, int* count)
/* populatechar takes a pointer to the line entered last entered by the user
and populates the the integer array count by one for each occurence of each
character.
   parameters:
    line - a pointer to the character array with the last line entered by user
    count - a pointer to the integer array of character frequencies

   local variables:
    index - current character of line being looked at
*/
{
    int index = 0;
    for(; index < 100 && line[index] != '\0'; index++)
    {
        // increases the value at the index of the integer equivalent of the
        // character being looked at
        count[(int)line[index]]++;
    }
}


int main()
/* main is the entry point of the wordcount program. The program continues to
loop until the user enters a line with only a new line character. It will then
determine and display the number of lines, words and characters cumulativly
entered by the user. The program will finally populate a table of characters
entered and their frequencies.

   local variables:
    line - a character array of the last entered line by the user
    count - an array of integers; the integers correspond to the frequencies
            of the characters with the integer value of the index
    done - the state of completion; -1 if not finished, 0 if finished
    linecount - number of lines entered by user
    wordcount - number of words entered by user
    charcount - number of characters entered by user
    linelen - the length of the line last entered by the user
*/
{
    char line[100];
    int count[128] = {0};
    int done = -1;
    int linecount = 0, wordcount = 0, charcount = 0, linelen = 0;
    printinfo();
    while(done != 0)
    {
        fgets(line, 100, stdin);
        linelen = strlen(line);
        // if the user wants to exit the program
        if(strcmp(line, "\n") == 0)
        {
            // display total line, word and char counts
            printf("\nLINES: %d\n", linecount);
            printf("WORDS: %d\n", wordcount);
            printf("CHARS: %d\n", charcount);

            // display the table of characters and their frequencies
            printf("\nCharacter Frequencies:\n");
            int j;
            for(j =0 ;j < 128; j++)
            {
                if(count[j] != 0)
                {
                    printf("%c: %d\n",(char)j, count[j]);
                }
            }
            done = 0;
        }
        // if the user entered a "non \n line" then echo what was written, 
        // print each word, and update the linecount, charcount, and wordcount
        // and update the character frequency table
        else
        {
            printf("\nINPUT: %s", line);
            wordcount = countwords(line, linelen, wordcount);
            printf("\n>");
            linecount++;
            charcount += linelen;
            populatechar(line, count);
        }
    }
    return(done);
}

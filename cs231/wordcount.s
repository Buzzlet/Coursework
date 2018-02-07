/*
Program: wordcount.s 
Date:    10/28/2015
Class:   cs231
Author:  Joel Ristvedt

Description: This program continues accepting lines and continually counting the
line, word and character frequencies (considering uppercase and lowercase to be
the same). Once the user wants to stop, the program displays the total frequencies
and the frequencies of each printable character. The program then asks the user
to enter a number corresponding to a line entered and it will echo it and repeat
ntil a negative one is entered.
*/

          .section .data

instruct: .ascii "Wordcount\nThis program accepts entered lines and echoes them\n"
          .ascii "and outputs a list of words from the line was input until a\n"
          .ascii "blank line is entered. The program will then output the total\n"
          .ascii "number of lines, words and characters and the frequency of\n"
          .ascii "the characters. You will then be allowed to review any lines\n"
          .asciz "you entered until you enter -1.\n"
prompt1:  .asciz "\nEnter a line or a blank line to finish: "
numimp:   .asciz "\n%d"
prompt2:  .asciz "\nEnter the number of a line (starts at 0) or -1 to finish: "
echo:     .asciz "Your line was: %s"
wordlist: .asciz "List of Words:\n"
newline:  .asciz "\n"
charprnt: .asciz "%c"
strprnt:  .asciz "%s"
numbuf:   .asciz "%d"
freqstr:  .asciz "Frequencies\nLines: %d\nWords: %d\nChars: %d\n"
charfreqs:.asciz "%c: %d\n"

linecnt:  .int 0
wordcnt:  .int 0
charcnt:  .int 0
linenum:  .int 0

strbuf:   .space 800
freqbuf:  .space 512 

          .section .text
          
          .global main
main:

          # print instructions
          movq $instruct, %rdi
          movq $0, %rax
          call printf
        
# get lines from user
          clrq %r13
          clrq %r12
getlines:  
          clrq %r14
          clrq %r15

          # print prompt1
          movq $prompt1, %rdi
          movq $0, %rax
          call printf
          
          # update %r15 with next open string location
          leaq strbuf, %r14
          movq linecnt, %r15
          imulq $80, %r15
          add %r14, %r15
          
          # get line from user using fgets
          movq %r15, %rdi
          movq $80, %rsi
          movq stdin(%rip), %rdx
          call fgets
          
          # quit if it's just a new line
          cmpb $'\n', (%r15)
          je linesdone
          
          # echo line
          movq $echo, %rdi
          movq %r15, %rsi
          movq $0, %rax
          call printf
 
          # print wordlist title
          movq $wordlist, %rdi
          movq $0, %rax
          call printf
          
# print chars and when there is a separator print new line and count

          # find next space, tab, or new line
          movq %r15, %r14
loop:     cmpb $0, (%r14)
          je incrline
          cmpb $' ', (%r14)
          je wordsep
          cmpb $'\t', (%r14)
          je wordsep
          cmpb $'\n', (%r14)
          je wordsep
          
          # increment the frequency of the character at the corresponding 
          # location in freqbuf
          leaq freqbuf, %r11
          clrq %r10
          movb (%r14), %r10b
          # make it so lowercase increments uppercase frequency instead
          cmpb $'a', %r10b
          jl notlower
          cmpb $'z', %r10b
          jg notlower
          subq $32, %r10
          
notlower:      
          imul $4, %r10
          add %r10, %r11
          incq (%r11)
          jmp printch
          
          # print new line and go back to loop through the rest
wordsep:  movq $newline, %rdi
          movq $0, %rax
          call printf
          incq %r14
          incq %r13
          jmp loop

printch:  # print the character, increment and jump to loop
          movq $charprnt, %rdi
          movq (%r14), %rsi
          xorq %rax, %rax
          call printf
          incq %r14
          incq %r12
          jmp loop

incrline:
          # increase line count and go back for next line
          incl linecnt 
          jmp getlines
          
# once the user enters only a blank line, the program continues here

linesdone:
          movq %r13, wordcnt
          movq %r12, charcnt 

          # print the total frequencies
          movq $freqstr, %rdi
          movq linecnt, %rsi
          movq wordcnt, %rdx
          movq charcnt, %rcx
          xorq %rax, %rax
          call printf
          
          # print the character frequencies
          mov $32, %r15
chrprntloop:
          pushq %r15
          movq $charfreqs, %rdi
          movq %r15, %rsi 
          imulq $4, %r15
          add $freqbuf, %r15
          movl (%r15d), %edx
          call printf
          # since in the add it overwrites %r1, restore it
          popq %r15
          incq %r15
          # if the character iterator is at 'a' skip to end of lowercase
          cmpq $'a', %r15
          jne cont 
          movq $123, %r15
cont:
          cmpq $127, %r15
          jne chrprntloop
          
loop2:        
          # print prompt2
          movq $prompt2, %rdi
          xorq %rax, %rax
          call printf
          
          # get number from user using scanf
          leaq numbuf, %rdi
          leaq linenum, %rsi
          xorq %rax, %rax
          call scanf
          
          # exit if linenum is -1
          movl linenum, %r13d
          incl %r13d
          je exit
          
          # update %r15 with the address of wanted string
          leaq strbuf, %r14
          movl linenum, %r15d
          imulq $80, %r15
          add %r14, %r15

          # print the line the user wants
          movq $echo, %rdi
          movq %r15, %rsi
          xorq %rax, %rax
          call printf
          jmp loop2
         
          
exit:     # exit
          movl $1, %eax
          movl $0, %ebx
          int $0x80
   
/*
Analysis: This program could be a lot more efficient. The call to
printf for each character when counting the characters is very
inefficient. The use of functions could make the source a lot easier
to understand.  
*/

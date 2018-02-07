/*
Program: sepwords.s
Date:    10/12/2015
Class:   cs231
Author:  Joel Ristvedt

Description: This program accepts a line from the user and separates the string
based on spaces, new lines and tabs.
*/


          .section .data

prompt:   .asciz "Enter a line: "
words:    .asciz "The words in your line are:\n"
newline:  .asciz "\n"
charbuf:  .asciz "%c"
sinp:     .asciz "%[^\n]s"
buf1:     .space 400

          .section .text
          
          .global main
          
main:
          # print prompt
          movq $prompt, %rdi
          movq $0, %rax
          call printf
          
          # gets line from user using scanf
          leaq sinp, %rdi
          leaq buf1, %rsi
          xorq %rax, %rax
          call scanf
          
          # prints the label for separate words
          movq $words, %rdi
          movq $0, %rax
          call printf
          
          # find next space, tab, or new line
          movq $buf1, %r14
loop:     cmpb $0, (%r14)
          je exit
          cmpb $' ', (%r14)
          je wordsep
          cmpb $'\t', (%r14)
          je wordsep
          cmpb $'\n', (%r14)
          je wordsep
          jne charprnt
          
          # print new line and go back to loop through the rest
wordsep:  movq $newline, %rdi
          movq $0, %rax
          call printf
          incq %r14
          jmp loop

charprnt: # print the character, increment and jump to loop
          movq $charbuf, %rdi
          movq (%r14), %rsi
          xorq %rax, %rax
          call printf
          incq %r14
          jmp loop

exit:     # print a final new line
          movq $newline, %rdi
          movq $0, %rax
          call printf

          # exit
          movl $1, %eax
          movl $0, %ebx
          int $0x80

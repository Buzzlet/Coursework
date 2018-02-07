/*

Program: random.s
Date:    11/07/2015
Class:   cs231
Author:  Joel Ristvedt

Description: Prints out random values ranging from 0 to 99999 in a 5x5 table

*/

          .section .data
numfmt:   .asciz "%6d"
newline:  .asciz "\n"
seed:     .int 1337

          .section .text
          
          .global main
          
main:     
          # call srand only one time to randomize
          movq seed, %rdi
          call srand
          
          clrq %r15
getrand:
          call rand
          incq %r15
          
          # divide the random number by 100000
          xorq %rdx, %rdx
          movq $100000, %rbx
          idivq %rbx
          
          # print out the remainder of the prior division
          movq $numfmt, %rdi
          movq %rdx, %rsi
          xorq %rax, %rax
          call printf
          
          # divide the count of random nums by 5
          xorq %rdx, %rdx
          movq %r15, %rax
          movq $5, %rbx
          idivq %rbx
          
          # determine if the remainder of prior division is 0, if so get another num
          cmpq $0, %rdx 
          jne getrand
          
          # otherwise print a new line
          movq $newline, %rdi
          xorq %rax, %rax
          call printf
          
          # if the program hasn't reached 25 random nums, keep going
          cmpq $25, %r15
          jne getrand
          
exit:     # terminate using exit
          movq $1, %rax
          movq $0, %rbx
          int $0x80

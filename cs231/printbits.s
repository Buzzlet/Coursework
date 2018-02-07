/*

Program: printbits.s
Date:    11/07/2015
Class:   cs231
Author:  Joel Ristvedt

Description: Gets a 3 digit number from the user and prints out the bits of the number

*/

          .section .data
prompt:   .asciz "Enter a three digit number: "
newline:  .asciz "\n"
numbuf:   .asciz "%d"
one:      .asciz " 1"
zero:     .asciz " 0"

num:      .int 0

          .section .text
          
          .global main
          
main:     
          # prompt user for 3 digit num
          movq $prompt, %rdi
          xorq %rax, %rax
          call printf
          
          # call scanf
          leaq numbuf, %rdi
          leaq num, %rsi
          xorq %rax, %rax
          call scanf
          
          # store num in register for easy use
          movq num, %r15
          # start out the bit to check at 2^9
          movq $1024, %r14
          # since %r14 will be overwritten, store it in %r13 too
          movq %r14, %r13
loop1:    
          # and operation on shifted bit and number
          movq %r13, %r14
          andq %r15, %r14
          
          cmpq $0, %r14
          jne prntone
          
          
          # print zero and shift right
prntzero: 
          movq $zero, %rdi
          xorq %rax, %rax
          call printf
          shrq %r13
          cmpq $0, %r13
          je exit
          jne loop1
                                 
          # print one and shift right
prntone:  movq $one, %rdi
          xorq %rax, %rax
          call printf
          shrq %r13
          incq %r12
          cmpq $0, %r13
          je exit
          jne loop1
          

          
exit:     
          movq $newline, %rdi
          xorq %rax, %rax
          call printf
          
          # terminate using exit
          movq $1, %rax
          movq $0, %rbx
          int $0x80

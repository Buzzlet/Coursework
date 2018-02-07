/*

Program: echoprint.s
Date:    10/12/2015
Class:   cs231
Author:  Joel Ristvedt

Description: This program gets three strings from the user echoing them as it
gets them and then finally prints them out in reverse order at the end.

*/

          .section .data
          
prompt:   .asciz "Enter a string: "
sbuf:     .asciz "Echoed string: %s"
finalout: .asciz "\nEntered lines: \n%s%s%s"
inpstr:   .space 240

          .section .text

          .global main

main:
          # print prompt
          movq $prompt, %rdi
          movq $0, %rax
          call printf

          # get the string using fgets
          leaq inpstr, %rdi
          movl $80, %esi
          movq stdin(%rip), %rdx
          call fgets          
                       
          # echo first string
          leaq sbuf, %rdi
          movq $inpstr, %rsi
          movq $0, %rax
          call printf
          
          # print prompt
          movq $prompt, %rdi
          movq $0, %rax
          call printf
          
          # get the next string using fgets
          leaq inpstr + 80, %rdi
          movl $80, %esi
          movq stdin(%rip), %rdx
          call fgets
          
          # echo second string
          leaq sbuf, %rdi
          movq $inpstr + 80, %rsi
          movq $0, %rax
          call printf
          
          # print prompt
          movq $prompt, %rdi
          movq $0, %rax
          call printf
          
          # get the third string using fgets
          leaq inpstr + 160, %rdi
          movl $160, %esi
          movq stdin(%rip), %rdx
          call fgets
          
          # echo the third string
          leaq sbuf, %rdi
          movq $inpstr + 160, %rsi
          movq $0, %rax
          call printf
          
          # print strings backwards
          movq $finalout, %rdi
          movq $inpstr + 160, %rsi
          movq $inpstr + 80, %rdx
          movq $inpstr, %rcx
          movq $0, %rax
          call printf
          
          # terminate using exit
          movq $1, %rax
          movq $0, %rbx
          int $0x80

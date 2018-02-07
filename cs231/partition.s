/*

Program: partition.s
Date:    12/06/2015
Class:   cs231
Author:  Joel Ristvedt
                                                                             80
Description: This program does the first partition on the first 30 numbers
loaded from a file. 

*/

          .section .data
numstrs:  .int 20
numlist:  .space 80
filename: .asciz "/tmp/cs231_strsort.dat"
numbuf:   .asciz "%6d"
newline:  .asciz "\n"
strbuf:   .space 80

          .section .text
          
          .global main
          

          
          
main:
          # open file to read from
          movq $2, %rax
          leaq filename, %rdi
          movq $0, %rsi
          movq $0644, %rdx
          syscall
          movq %rax, %r15
          
          leaq numlist, %r12
          addl $1, numstrs # since we decrement first, let's make sure we
                           # get all 30 numbers
          movl numstrs, %r14d
loop:
          decl %r14d
          je endloop
          
          # read numeric string from file 
          movq $0, %rax
          movq %r15, %rdi
          leaq strbuf, %rsi
          movq $6, %rdx
          syscall
          
          # convert numeric string to integer using atoi
          leaq strbuf, %rdi
          movq $0, %rax
          call atoi
          
          # increment address
          movl %eax, (%r12)
          addq $4, %r12
          jmp loop
          
endloop:
          # set up %r13 and %r14 for partition
          leaq numlist, %r13
          subl $2, numstrs # point at the beginning of the last, not the end
          movl numstrs, %r14d
          imulq $4, %r14
          addq %r13, %r14
          call partition
          
          movq $10, %r10
          pushq %r10
printloop:
          leaq numbuf, %rdi
          movl (%r13), %esi
          xorq %rax, %rax
          call printf
          popq %r10
          
          decq %r10
          pushq %r10
          cmpq $0, %r10
          jne increment
          movq $10, %r10
          pushq %r10
          
          leaq newline, %rdi
          xorq %rax, %rax
          call printf
          
increment:
          addq $4, %r13
          cmp %r13, %r14
          jge printloop
          
exit:     
          # close file 
          movq $6, %rax
          movq %r15, %rdi
          syscall
          
          # terminate using exit
          movq $1, %rax
          movq $0, %rbx
          int $0x80
          
# Partitions a list from a starting location to an ending location into
# two partitions based on the first value of the list
# Parameters:
# %r14 - upper address of region to be partitioned
# %r13 - lower address of region to be partitioned
partition:
          clrq %r11 # %r11 - leftPtrPtr 
          clrq %r12 # %r12 - rightPtrPtr
          movl (%r13), %r10d # %r10d - pivot
          movq %r13, %r11 # leftPtrPtr = low 
          movq %r14, %r12 # rightPtrPtr = high
outterwhile: # keep partitioning until the high and low pointers cross
firstwhile: # finds the next left number on the wrong side of pivot
          cmpl %r10d, (%r11) 
          jg secondwhile
          addq $4, %r11 
          jmp firstwhile

secondwhile: # finds the next right number on the wrong side of pivot
          cmpl (%r12), %r10d
          jge cont
          subq $4, %r12
          cmpq %r11, %r12
          jl end
          jmp secondwhile
cont:
          movl (%r11), %r9d # move lower number out of memory for compare 
          cmpl (%r12), %r9d
          jle outterwhile
          movl (%r12), %r8d # move higher number out of memory for swap
          movl %r8d, (%r11) # put higher number in lower spot
          movl %r9d, (%r12) # put lower number in higher spot
          
          cmpq %r11, %r12 # keep looping if the pointers haven't crossed
          jg outterwhile
end:      
          movl (%r12), %r9d
          movl %r9d, (%r13)
          movl %r10d, (%r12)
          ret

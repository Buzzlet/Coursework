/*

Program: radix_sort.s
Date:    11/24/2015
Class:   cs231
Author:  Joel Ristvedt
                                                                             80
Description: Sorts random numbers using the radix sort. The program will print
out a sorted list of 200 numbers and verify that they are sorted. It will then
sort a full list of 10000 numbers but only verify that the list is sorted. 

*/

          .section .data
numfmt:   .asciz "%6d"
newline:  .asciz "\n"

seed:     .quad 1337
listlen:  .int 100
maxval:   .int 50000
itemsize: .int 4
          
numbuf1:  .space 400
numbuf2:  .space 400
          
          .section .text
          
          .global main
          
main:
          # populate the list with 10000 random numbers with values up to 50000
          movq seed, %rdi
          call srand
          
          leaq numbuf1, %r15
          movl listlen, %r14d
          movl maxval, %r13d
          call get_rand_nums
          
          # check to see if the numbers are sorted
          leaq numbuf1, %r15
          movl listlen, %r14d
          movl itemsize, %r13d
          call is_sorted
          
          cmpq $0, %rdx
          
          # sort the first 200 numbers
          # print the first 200 numbers
          # check to see if the numbers are sorted
          #call is_sorted
          # sort all 10000 numbers
          # check to see if the numbers are sorted
          #call is_sorted
          
exit:
          # terminate using exit
          movq $1, %rax
          movq $0, %rbx
          int $0x80
          
# compares consecutive values until either they aren't in the right order or
# the end is reached
# params:
# %r15 - the starting address of list
# %r14 - the length of the list
# %r13 - the size of each element in the list
# returns:
# %rdx - 0 if sorted
is_sorted:
          movq $0, %rdx
loop:     movq %r15, %r12 # don't overwrite %r15
          movl (%r15), %r11d # use %r11 so the compare will only access memory once
          addq %r13, %r12 # use %r12 for compare 
          cmpl %r11d, (%r12)
          jl notsorted
          movq %r12, %r15
          decq %r14
          jne loop
          jmp endcheck
          
notsorted:
          movq $1, %rdx
endcheck: ret          

# populates the memory with the given number of numbers ranging from 0
# to the specified max starting at the given address, srand must be called first
# params:
# %r15 - starting address of list
# %r14 - number of numbers to generate
# %r13 - maximum value of generated numbers
# returns: none
get_rand_nums:
          call rand
          
          # divide the random number by maximum value
          xorl %edx, %edx # zero edx
          movl %r13d, %ebx 
          idivl %ebx # divide %eax by %ebx
          
          movl %edx, (%r15) # move remainder into current spot in list
          
          addq $4, %r15 
          decl %r14d
          cmpl $0, %r14d
          jge get_rand_nums
          ret

          

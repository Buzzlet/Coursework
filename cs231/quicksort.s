/*

Program: quicksort.s
Date:    12/15/2015
Class:   cs231
Author:  Joel Ristvedt
                                                                             80
Description: 

*/

          .section .data
instruct: .ascii "Quick Sort\n"
          .ascii "This program sorts numbers using the quick sort algorithm. "
          .ascii "The program will begin by sorting 200 numbers and printing "
          .ascii "them out in order and ensuring they are in order. Then "
          .asciz "it will sort all the numbers in the source file. \n\n"
instrlen: .long . - instruct
numstrs:  .int 100
numlist:  .space 400
endAddr:  .quad . - 4
filename: .asciz "/tmp/cs231_strsort.dat"
numbuf:   .asciz "%6d"
newline:  .asciz "\n"
strbuf:   .space 80


prints:  .macro a,b,c 
          movq $1, %rax # write syscall
          movq \a, %rdi # stdout = 1
          leaq \b, %rsi # %rsi = address of ouput buffer
          movq \c, %rdx # number of characters to output
          syscall
          .endm
          
          .section .text
          
          .global main
          
          
main:

          call doInstructions
          call getNumbers
          
          # setup for printNums
          leaq numlist, %r13
          movl numstrs, %r14d
          subl $2, %r14d # because I did things oddly in partition.s...
                         # make sure this is pointing at the right spot
          imulq $4, %r14
          addq %r13, %r14
          jmp printNums
back: # unsure why calling and returning would crash...
          
          # setup for is_sorted check function
          leaq numlist, %r15
          subl $1, numstrs
          movl numstrs, %r14d
          movl $4, %r13d
          call is_sorted
          
          # if %rdx = 0, let the user know the list is sorted
          
          # setup for quicksort
          pushq $numlist
          pushq endAddr
          leaq numlist, %r14
          movq endAddr, %r15
          call quicksort
          addq $16, %rsp
          #call printNums
          #call is_sorted
          
          
exit:     
          # close file 
          movq $6, %rax
          movq %r15, %rdi
          syscall
          
          # terminate using exit
          movq $1, %rax
          movq $0, %rbx
          int $0x80

# Sorts a list of numbers using the quick sort algorithm 
# Parameters:
# top of stack <- ending address <- number buffer address
# %r13 - for first call, this should be the number buffer address
# returns: None
quicksort:                # %r14-low, %r15-high
          pushq %rbp
          movq %rsp, %rbp
          movq 24(%rbp), %r14
          movq 16(%rbp), %r15
          call partition
          #pushq %r13
          pushq %r14
          cmpq %r14, %r15
          jle endsort
          call quicksort # low partition
          addq $16, %rsp
          popq %r13
          pushq %r12
          pushq %r15
          call quicksort # high partition
          addq $16, %rsp
          popq %rbp
endsort:  ret
          

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


# Prints out the instructions to the user
# Parameters: None
# Returns: None
doInstructions:
          prints $1, instruct, $instrlen
          ret


# Prints the numbers in a list in 10 columns
# Parameters:
# %r13 - starting address of number buffer
# %r14 - address of last number to print
printNums:
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
endprint:
          jmp back

# Reads the numbers from the file and stores them in numlist
# Parameters: None
# Returns: numlist is full of numbers!
getNumbers:
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
loop1:
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
          jmp loop1
          
endloop:
          ret                    
                                        
# Partitions a list from a starting location to an ending location into
# two partitions based on the first value of the list
# Parameters:
# %r15 - upper address of region to be partitioned
# %r14 - lower address of region to be partitioned
partition:
          clrq %r11 # %r11 - leftPtrPtr 
          clrq %r12 # %r12 - rightPtrPtr
          movl (%r14), %r10d # %r10d - pivot
          movq %r14, %r11 # leftPtrPtr = low 
          movq %r15, %r12 # rightPtrPtr = high
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
          movl %r9d, (%r14)
          movl %r10d, (%r12)
          movq %r11, %r13
          ret

/*  This is the program template for searching a binary tree.
 *  -  The program reads the binary tree from a file into the binTree array.
 *  -  The user is asked for a number to search for.
 *  -  The program calls the srchTree function to search for the number entered
 *  -  The srchTree function either continues to call serchTree recursivly
 *     until either the search number is found or a leaf of the tree is reached
 *  -  The srchTree function returns a 0 or 1 flag to indicate the search number
 *     was found or not found
 *  -  The main program prints the result of the search 
 */

    .section .data

intro:  .asciz  "Reading binary tree data from file...\n"
intro_len: 
        .quad   . - intro             # The assembler calculates the length 
                                      # of the introduction by subtracting the 
                                      # address of intro from the current
                                      # location of the location pointer.

request: .asciz  "Enter a number between 1-100 to search for:\n"
req_len: 
        .quad   . - request           # The assembler calculates the length 
                                      # of the request by subtracting the 
                                      # address of request from the current
                                      # location of the location pointer.

found:   .asciz  "The search number was found:\n"
fnd_len: .quad   . - found

notfound:.asciz  "The search number was NOT found:\n"
nfnd_len: .quad   . - notfound


filename:   
        .asciz  "/tmp/cs231_binaryTree.dat"     # filename to use for illustration
filen_len:
        .quad   . - filename          # The assembler calculates the length 
                                      # of the filename by subtracting the 
                                      # address of filename from the current
                                      # location of the location pointer.

newline:
        .ascii  "\n"
nl_len: .quad   . - newline           # The assembler calculates the length 
                                      # of the newline by subtracting the 
                                      # address of prompt from the current
                                      # location of the location pointer.

prtfmt: .asciz  "%d\n"                # print format string

buffer:  .space  10
binTree: .space  50 * 4           # Allocate enough space for 50 numbers in the tree 


sys_call: .macro  a,b,c,d 
     movq \a, %rax      # read/write () system call
     movq \b, %rdi      # %rdi = 1, fd = stdout
     movq \c, %rsi      # %rsi ---> address of to output 
     movq \d, %rdx      # %rdx = count of number of characters to write out
     syscall        # execute read/rite () system call
        .endm

fmtstr: .asciz "%d"
########################################################################

    .section .text
    .global main 
    
main:
         ## display string using write () system call
         sys_call  $1,$1, $intro, intro_len

         ## open file to read from
         sys_call $2, $filename, $0, $0644
         movq %rax, %r15         # the value of the file descriptor returned from the open is in %eax

         leaq binTree, %r14  # Store the address of binTree in %r14

loop:
         ## enter string using read () system call
         sys_call $0, %r15, $buffer, $4
         
         cmpq $0, %rax           # The number of characters read is returned in %eax; if 0, then exit
         je   getNum             # If no charactrers read then no more lines in file, go to continue 

         # Need to convert the numeric string to an integer; call the C function atoi to do that
         leaq buffer, %rdi       # Move the address of teh string to %rdi as the first parameter
         xorq %rax, %rax         # Clear %rax
         call atoi               # Call C atoi function  (numeric_value = atoi(numeric_string)
         movq %rax, %rbx         # Numeric result is returned in %rax; Store in %rbx for printing later on

         ## display input as a number using a call to the C printf function
         leaq prtfmt, %rdi       # move address of print format string to %rdi
         movq %rbx, %rsi         # %rsi contains the number from above that was converted using the atoi function 
         xorq %rax, %rax         # clear %rax
         call printf             # call C printf function

         # Move the number into the binTree array
         movl %ebx, (%r14)       # %r14 contains address to next position in the binTree
         addq $4, %r14       # Move the $r14 pointer to the next integer location in memory
 
         jmp loop                # Jump back to the beginning of the loop


getNum:  # After printing a blank line for spacing, prompt user to enter a search number
         
         # Close open file 
         sys_call $3, %r15, $0, $0
         # Print newline
         sys_call  $1,$1, $newline, nl_len

         ## display prompt using write () system call
         sys_call  $1,$1, $request, req_len


         ##  ENTER CODE HERE TO GET NUMERIC SEARCH INPUT FROM THE USER USING SCANF
         ##  YOU WILL NEED TO DEFINE A NUMERIC VARIABLE IN THE DATA SECTION
         ##  ABOVE TO LOAD THE SEARCH NUMBER INTO` 
         ## -------------------------------------------
         movq $fmtstr, %rdi
         movq $buffer, %rsi
         xorq %rax, %rax
         call scanf
         movq buffer, %r14
         ## -------------------------------------------


doSrch:  ##  ENTER THE SETUP FOR THE CALL TO THE RECURSIVE srchTree FUNCTION HERE
         ##  NOTE THAT THE srchTree FUNCTION WILL NEED THE FOLLOWING PARAMETERS
         ##  -  THE NUMBER TO SEARCH FOR
         ##  -  THE ADDRESS OF THE ROOT OF THE TREE (OR SUBTREE) TO SEARCH
         ## -------------------------------------------
         pushq %r15
         pushq $binTree

         ## -------------------------------------------

         call srchTree # returns in %r13

         ## ENTER ThE "CLEANUP" CODE NEEDED AFTER RETURNING FROM srchTree
         ## The srchTree FUNCTION SHOULD BE RETURNING THE SEARCH STATUS
         ## CAN YOU RETURN THE SEARCH STATUS IN A REGISTER OR DO YOU NEED TO USE THE STACK?
         ## -------------------------------------------
         addq $16, %rsp
         
         ## -------------------------------------------


         ## ENTER THE CODE HERE TO PRINT THE CORRECT SEARCH STATUS USING THE sys_call MACRO
         ## -------------------------------------------
         cmpq $0, %r13
         je nf 
         
         sys_call $1, $1, $found, fnd_len
         movq $prtfmt, %rdi
         movq %r13, %rsi
         xorq %rax, %rax
         call printf
         jmp exit
nf:      
         sys_call $1, $1, $notfound, nfnd_len


         ## -------------------------------------------


         ## terminate program via _exit () system call 
         ## but first close the file that is open
exit:    
         ## close the file that is open
         movq $6, %rax           # close() system call = 6
         movq %r15, %rdi        # %rdi = value of file descriptor that is stored in %r15d
         syscall                       # execute the close() system call

         movq $60, %rax           # %rax = 1 system call _exit ()
         movq $0, %rdi           # %rdi = 0 normal program return code
         syscall                 # execute system call _exit ()



         ## ENTER THE APPROPRIATE CODE TO IMPLEMENT THE srchTree FUNCTION HERE
         ## -----------------------------------------
srchTree:
         pushq %rbp
         movq %rsp, %rbp
         movq 32(%rbp), %r12 # search 
         movq 24(%rbp), %r11 # addr
         movq %r11, %r10
         subq $binTree, %r10
         cmpl %r12d, (%r11)
         je eq
         jl lt
         
         shlq $1, %r10
         addq $8, %r10
         
eq:
         movq $1, %r13
         popq %rbp
         ret
         
lt:      
         
         ## ---------------------------------------- 

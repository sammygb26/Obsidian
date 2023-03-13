We will look at how x86 manages memory. In general the CPU needs to fetch its program from memory. The **compiler** converts say some C code to *assembly code*. The **assembler** convers assembly code to machine code. The **linker** deals with dependencies and libraries. Finally the **loader** sets up the address space in memory and load machine cod in memory finally jumping to the first instruction of the program.

![[Pasted image 20230310100356.png]]

The **CPU** then reads from the EIP (instruction pointer). *EIP* is incremented after each instruction, then call, ret, jmp and conditional jmp change EIP.

### x86-32 Registers
The CPU maintains other special registers to speed up processing. So $\%e(a-d)x$ and $\%edx$ , $\%edi$ and $\%esi$. These are variable like register built into the program. Most instructions are performed on these registers as they are fast.

We also have the extended stack pointer $\%esp$ which points to the top of the stack. Then $\%ebp$ which point to the base of the stack frame of the current function call.

### Process layout
![[Pasted image 20230310100942.png]]

*Heap* is for dynamically allocated memory while the stack is made up of variables local to a function. Each address points to 8bits in memory and we use little-endian convention.

### Stack Frame
When we call a function we push things to the stack in a structured way. Each function gives a **stack frame**, this adds space for the local variables in the function.

![[Pasted image 20230310101429.png]]

To call a function we first push out arguments to the stack (in reverse order) so first argument can be read first. Before the function is first called we save the return address to the stack so we can return after we are done. When the function starts we save $\%esb$ so we can reset the environment after our function has called. Then we set $\%esb$ to the current $\%esp$. We can then allocate memory for our local variables. This ensures given $\%esb$ we know the location of the arguments relative to it. 

### Calling function
1. Push arguments onto the stack (in reverse)
2. Push the return address, i.e. the address of the instruction to run after control returns
3. Jump to the function's address

### Called function
4. Push the old frame pointer onto the stack (%ebp)
5. Set frame pointer (%ebp) to where the end of the stack is right now (%esp)
6. Push local variables onto the stack

### Returning function
7. Reset the previous stack frame %esp = %ebp, %ebp = (%ebp)
8. Jump back to the return address %eip = 4(%ebp)
What roles to the computer, assembler, linker and loader play in running a program? #flashcard #CS #MemoryManagement
	The **compiler** converts the code (be it C, C++ Rust etc) into *assembly code*. The **assembler** converts the assembly code to *machine code* (architecture specific). The **linker** allows dependencies and libraries to be run by the program. Then the **loader** sets up the program in memory (machine code and all). Finally the loader jumps to the first instruction of the program.

---
What is the function of the eip register and how does it change? #flashcard #CS #MemoryManagement 
	$eip$ points to the next instruction to be run. It increments after each instruction and can be modified by *call, ret, jump and conditional jump*.

---
What are the main x86-32 registers?  #flashcard #CS #MemoryManagement 
	We have $e(a-d)x$ as temporary registers, then $edi$, $esi$ also temporary registers. Then there is also the *extended stack pointer* $esp$ and *extended base pointer* $ebp$.

---
Where do the esp and ebp point during program execution?  #flashcard #CS #MemoryManagement 
	We will always be running functions. The $esp$ keeps track of the top of the **stack** where local variables are stored. This ensures when allocating new local variables we don't override old ones. Finally the $ebp$ points to the top of the stack frame for the previous function. When we return this means local variables "go out of scope".

---
What is a stack frame?  #flashcard #CS #MemoryManagement 
	A stack frame is the portion of stack memory taken up by a function. It is designated between the $esp$ and $ebp$. When the program returns the stack frame is thrown away as the $esp$ is moved to the old $ebp$ and the $ebp$ moved to the saved $ebp$ in the stack.

---
What takes place to call a function at a machine code level?  #flashcard #CS #MemoryManagement 
	To call a function 1) The arguments are pushed onto the stack (in reverse) 2) The return address is pushed onto the stack. 3) We jump to the functions address.

---
What is another name for the ebp?  #flashcard #CS #MemoryManagement 
	This is also called the frame pointer as it points to the base of the current stack frame.

---
What takes place just after a function is called at the machine code level?  #flashcard #CS #MemoryManagement 
	For this 1) the old frame pointer is pushed into the stack (making a new frame for this function) 2) The frame pointer $ebp$ is set to the start of the stack ($esp$) 3) Any local variables are pushed onto the stack making room for them.

---
What takes place as a function returns at the machine code level?  #flashcard #CS #MemoryManagement 
	At a machine code level first the previous stack frame is reset  $esp=ebp$ then $ebp$ is set to the saved frame pointer for the last function. Then we jump to the return address.

---

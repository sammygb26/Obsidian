Many programs can be taken over if they are insecure or leak valuable information. These programs can allow for **privilege escalation** which could lead to an attacker taking over a computer.

### Compiling and Linking
Before a program can be run the code we write must be converted into the correct machine code. A **compiler** converts the program to the code. Programs can either be **statically linked** or **dynamically linked** to their libraries. When a program is is **statically linked** programs have all libraries copied into them but this can waste space. In **dynamically linked** program the **loader** finds the libraries the program needs on the disk. Then when the program is run these libraries are read form disk into the process. In windows these libraries on the computer are called **dynamic linking libraries** (DLLs), while in many Unix system they are **shared objects**.

If arbitrary code is injected into a DLL this is called a DLL injection. It can allow arbitrary code to be leaked into legitimate programs.

### Simple Buffer Overflow Attacks
A buffer overflow is an attack where a process allocates a fixed sized buffer in memory to which information is stored and proper checks aren't done to ensure only up to the limit of the buffer is written. Without this a user can input more data than the buffer can store and the process will copy this data beyond the buffers limits. This will overwrite other data on the stack possibly return addresses allow a user to take over control flow.

##### Arithmetic Overflow
The simplest kind of overflow is *arithmetic overflow*. This is due to the limitations of the binary representation of numbers in the computer. Usually integers are signed so "011...1" is the larger positive numbers and "100...0" is the largest negative number. This numbering system is called **two's compliment** and works in many ways including making adding negative and positive numbers easy. But if we add one to the largest positive number we get the smallest negative number. This is the **arithmetic overflow**. It all happens since we are essentially doing addition in a modular number line. We can also get **arithmetic underflow** when we take away to many numbers. This isn't even limited to signed numbers as all fixed length representations have a max value at which they will overflow.

If we rely on this never happening we can introduce security vulnerabilities. 

### Stack-Based Buffer Overflow
Here the buffer being overflow is in the **stack**. A segment of memory that keeps track of active functions. Each function has a piece of memory called a **stack frame**. This stores local variables for the function aswell as the return address for the parent call. The stack grows so moving through the stack traces out all the function calls which have lead from $main$ to the current function. This structure means the CPU can deallocate memory for each function with ease.

![[Pasted image 20230414145227.png]]

For this attack the input with overflow from some buffer allocated in the stack and overwrite surrounding memory. For example if a variable is a string that will be executed as a command the overflow could overwrite this and write arbitrary commands.

In a **stack smashing** attack the attacker exploits a stack buffer vulnerability to inject malicious code into the stack and then overwrite the return address of the current routine so that the return jumps to the malicious code.

![[Pasted image 20230414145428.png]]

##### Seizing Control of Execution
In a realistic situation an attacker must guess the return address location and then overwrite it to jump to the attackers code. The OS makes this hard in two ways

1. The process cannot read memory from other programs so the malicious code must be stored in the program.
2. The address space is unpredictable and so we cannot just send some exact address and always hit the start of our malicious code bang on and it may change on different machines.

##### NOP Sledding
NOP is a machine code command which does nothing accept move the instruction counter forward. So if we have a large sequence of NOPs at the start of our malicious code no matter which one we hit we will be brough to the start of our program.

![[Pasted image 20230414150104.png]]

##### Trampolining / ROP
Even with the NOP sledge it may be hard to always hit our malicious code. Another way is to jump to known libraries which are **dynamically linked**. These may always be in the same location as they are loaded into a reserved piece of memory. We can also find *gizmos* and perform **return oriented programming**. The way this works is snippets of code at then end of functions may have side effects. For example pop the top of the stack into a register. So we can inject a sequence of return addresses and value into the stack. The system will then jump to gizmos which have the effect of loading the values we want into register they then return but since we control the stack they can be chained together allowing arbitrary code execution without injecting any code!

##### Ret2Libc attack
This is similar to the above ROP attacks but instead of jumping to gizmos we just run some libc function. For example system("/bin/sh") opening a shell. We can do this as the arguments are actually present on the stack and since we control it we control the arguments. The sequence will be $$func\_addr:return\_addr:args\dots$$As in trampolining we don't run any code on the stack so even if we cannot execute stack code we can still exploit.

###### Shellcode
When an attacker can execute arbitrary code they usually use it to spawn a shell so that then they can write arbitrary commands with ease. For this reason it is called **shellcode**. As it is executed on the CPU is must be written in machine code specific to the system called opcodes. This can be hard as null character may be required by cannot be copied as it denotes the end of a string.

All these attacks can exploit setUID programs to gain access to other user's programs.

##### Preventing Stack-Based Buffer Overflow Attacks
The root cause isn't the OS but bad programming practices. Programmers must use the correct safe functions to have safe programs that cannot be executed. Even better **safe languages** can be used which don't have these vulnerabilities.

Many OSs also have added protection to detect a stack-based buffer overflow. One technique is to detect when a buffer overflow has occurred and prevent program execution from continuing with possibly compromised data.

One way of doing this called a **canary** which is a value that is placed between a buffer and controlled data. The system checks the integrity of the canary and if it has been changes it knows the buffer has been overflown.

![[Pasted image 20230414152653.png]]

Another option is **point-guard** which XOR-encodes any pointers before and after they are used. This way an attacker cannot reliably write an address with a valid memory and cannot ensure the address they are jumping to does what they want. We can also prevent code injected form running by have W^X or **Data Execution Protection** basically memory is either write or execute but not both. This way we cannot inject shellcode and have it execute. We can also use **address space layout randomization** which rearranges the data of a process' address space so the attackers may find it hard to know where to jump to.

Many of these defence have new attacks which can overcome them.

### Heap-Based Buffer Overflow Attacks
Some memory isn't on the stack and so isn't cleared after a function returns. This memory resides in the **heap**. There are many problems here fore example if memory isn't deallocated after use it will remain used causing a **memory leak**. If this happens over and over again this can build up data not being used.

The heap has similar vulnerabilities to the stack. If a buffer is allocated then not written to with care a user could overflow it into other heap memory.

These are generally more complex than stack-based overflows and require a deeper understanding of garbage collection and the heap are implemented. The heap memory doesn't control control data and would alter the execution of the program directly. Instead these attacks aim to change the program and exploit by rewriting just this data.

##### Example
One possible example was the older implementation of malloc. Basically data chunks were implemented as a linked list. If you could overflow a block you could overflow the linked list pointer. It may point to some empty block which might than have data allocated to it. data that you may control. This way arbitrary data can be written.

Another way is to overwrite .dtors which is  section of code executed after main has returned. Overflowing this would allow arbitrary code execution before the program ends. Alternatively the **gloabal ofset table** could be overwritten. This tells the program where different functions absolute addresses are. If we can overwrite this we can make functions point to arbitrary places and so execute arbitrary code.

##### Preventing Heap-Based Buffer Overflow Attacks
Again the most important thing is to use safe functions. Other defenses have also been tried for example keeping heap pointer information in a different area and making the heap W^X.

### Format String Attacks
$printf$ is a special libc function. The basic idea is that you give it a format string and then it parses the remaining arguments into the format that string specifies. They can also *write* data for example with $\%n$ which specifies that the print function should write the number of bytes output so far to memory address stored as the first argument.

If the programmer doesn't set the format string themselves this allows the user to write their own. This could let the user write and execute their own code.

![[Pasted image 20230414155301.png]]

The solution is to always give a format string.
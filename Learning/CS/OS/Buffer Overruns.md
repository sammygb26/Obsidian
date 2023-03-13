The idea here is a buffer can be filled by a function like $gets$ but this can return a array longer that the buffer. It overflows deeper into the stack.

1. If a variables like for example $authenticated$ was initialized before the buffer. Then it may be overrun during execution and override the value in the stack. If this is checked later if is isn't changed an attach has fooled the program into believing some value is what is shouldn't be.

2. Another example could be a string that defined where a common is stored. If the program executes this later we could modify the program to execute an arbitrary file. This gets the privileges of the program running is and so if we are running as root we can obtain root privileges.

### Control Hijacking
Here a buffer overflow can change the flow of execution of the program. We load malicious code into memory (via buffer overflow) which is the code we want to execute. Then we overwrite $\%eip$ point to this malicious code. For example we can overwrite the $return$ address.

We need to inject *machine code* which the CPU will interpret. We can find the $\%ebp$ and we know the return address is 8 bytes above that. Once we have found the return address we need to know where our address is in memory. We can just try possible addresses until we get execution.

### Shellcode Injection
Here the **goal** is to "spawn a shell" - which gives the attacker general access to the system. The idea with a shell we can then execute any commands we want. We must inject the machine code instruction which we can obtain by compiling a C program for example. We must ensure *we don't have a null character* as if we do our program may stop reading the string we have entered. 

##### The Return Address
We want to find the address of the injected malicious code. If code is accessible we know how far the overflowed variable is form $\%ebp$. If code is not accessible we ty different possibilities. In 32 bits memory space there $2^{32}$ possibilities. One way is to add a **NOP Sled**. NOPs are command that do nothing they just increment the pointer. So if we land anywhere in this section we are brought to the start of our program.

### First Exploit
This was in 1988 when a computer work was written by Robert Morris. At the time this took down the entire internet. The problem was there was a bug that overwrote all memory crashing every system it infected.

### Opportunities
There are many features other than $gets$ that given opportunities for buffer overflowing attacks. For example $strcpy$, $strcat$, $gets$ and $scanf$. The issue is these **do not check bound of buffers they manipulate!!**.

1. $strcpy$ takes a destination pointer and a source pointer. It copies byte by byte until it reaches a null character 0.
2. $strcat$ takes in a destination pointer and source pointer and concatenates this at the end of the destination buffer. The idea being it can be added after a null character with sufficient memory. But this may be far larger than is needed.
3. $gets$
4. $scanf$ reads formatted input from the standard input.

##### Safe Functions
There are safe versions of these functions. Like for example $fgets$ which reads up to a fixed number of characters. This means your program is as secure as its programmer cautions. It is now up to the programmer to include all necessary checks in his program. Which isn't always done.

### Arithmetic Overflow
Limitation related to representation of integers in memory can also lead to problems. In 32 bits architectures, signed integers are expressed in **two's compliment notation**. $$0x00000000-0x7fffffff:\text{ are positive numbers $0-(2^{32}-1)$}$$ $$0x800000000-0xffffffff:\text{are negtive numbers $(-1)-(-2^{32}+1)$}$$
This issue is when we add over the final integers we wrap around and get a negative number. For example we may have a safe function that copies numbers and check if their some value is smaller than some value. We can have a buffer that is longer and this will overflow the check value and give a very small value.

The sum wraps around and becomes negative.

This may not even happen with addition but instead with just very large buffers being passed. The problem is the length is being converted between signed and unsigned integers.

##### Heap-based buffer overflows
Due to arithmetic overflow memory. **Dynamically allocated** and will persists across multiple function calls. This memory is allocate on the **heap** segment. Heap-based buffer overflow are more complex and require understanding garbage collection and heap implementation.

...

### Ariane 5 Disaster
Here in 1996 the Ariane rocket ignited. Then it suddenly flipped 90' and then self destructed at 4km. Then enquire found this was due to an overflow bug.

The key things here is the scales of the programs are too large to check all possible overflows.

### Format String
A format function takes a variable number of arguments from which one is the format string. Inspecting the format string defined how many arguments will be examined. By executing extra arguments that aren't expected we can get the printf to read the stack pointer or return address. They problem here is calling printf on a user input string allows control of this. Instead printf should always be called with a base that is programmer controlled.

This allows stack memory to be read at any location. We can walk up the stack until target pointer is found. This could leak passwords, sessions or crypto keys. We can write to any memory location ...

### TLS Heartbleed
Here a program can check check if a server is still alive b responding with a word for example "bird". We also send the number of byte sin the word. We could for example tell the server the word is bigger than it is. This will then reveal more bytes than are in the string.

This has been used to retrieve TLS master keys.
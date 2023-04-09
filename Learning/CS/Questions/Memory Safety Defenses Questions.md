What are the three key techniques for memory safety? #flashcard #CS #MemorySafetyDefenses
	1) **Use memory safe language** (vulnerabilities can't happen if they are made impossible by the language) 2) **Apply safe programming practices** (when using non safe programming language make sure to check bounds and ensure safety is achieved) 3) **Code hardening** (OS and compiler based techniques to defend against BOs)

---
What are some code hardening techniques? #flashcard #CS #BufferOverruns 
	There might be **stack canneries** (where variables are left in the code such they if they are overwritten BOs is detected and execution is stopped). **Data Execution Protection** we have W XOR X and code can either be written or executed so written so machine code cannot be injected and run. **Address Space Layout Randomization (ASLR)** here the location of the program in memory is changed so injected values wont point to where the user things they will.

---
How do memory safe language achieve their safety? #flashcard #CS #BufferOverruns 
	Memory safe language have well defined memory access so we always specify how a user can interact with memory explicitly. Check on array bounds and pointer dereferences are automatically included. Garbage collection (or other techniques) mean coder don't write memory management and so related errors aren't made.

---
What are some memory safe programming languages? #flashcard #CS #BufferOverruns 
	Some examples are Java, Python, Rust, Go ...

---
How can safe programming practices be followed for memory safety? #flashcard #CS #BufferOverruns 
	Safe Libc functions should always be used. User inputs should also be validated.

---
How do stack canaries work? #flashcard #CS #BufferOverruns 
	The **goal** is to detect stack buffer overflow before malicious code is executed. The **Idea** is to place a trap (the canary) in the stack. To overflow the return address the canary must be overwritten. Then before we return the **canary** is checked.

---
What properties must the canary have to work well? #flashcard #CS #BufferOverruns 
	It must be sufficiently unpredictable. Incrementing values don't work and there must be sufficiently many possibilities.

---
What are some limitations of stack canaried? #flashcard #CS #BufferOverruns 
	Some limitations are 1) It relies on the attack not being able to read the stack (but this is often the case) 2) It relies on the attacker not being able to jump over the canary 3) It assumes the attacker cannot guess the canary 4) These cannot detect heap overruns.

---
What is Date Execution Protection and Write XOR Execute? #flashcard #CS #BufferOverruns 
	It idea is to stop malicious injected code form being run. For this data must being either **executable** or **writable** (but not both). The stack and the heap are writable while text is executable. So even if malicious code is injected it cannot be executed.

---
How can DEP be overcome? #flashcard #CS #BufferOverruns 
	We can do this with ret2libc attacks where instead of running our own code we load arguments to run other code for example libc functions which give a lot of power. Alternatively ROP can be used in a similar way allow arbitrary code execution by using gadgets instead of usual machine code instructions.

---
What is ASLR? #flashcard #CS #BufferOverruns 
	This is address space layout randomization. The goal is to not allow the attacker to predict where things are in memory. For example libraries are at different position in address space. The problem is if memory can be read attacker can reverse the base address of these libraries and use that to execute code.

---

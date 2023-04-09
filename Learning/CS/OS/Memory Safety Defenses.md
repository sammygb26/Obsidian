Many different methods have been developed to defend against buffer overflows, buffer overreads and integer overflows.

1. **Use memory-safe languages** - checks on buffer bound are automated by the compiler 
2. **Apply safe programming practices** - when using non-memory safe languages check all the bounds, and validate user input
3. **Code hardening** - OS and compiler based techniques to defend against BOs
	1. Stack canaries
	2. Data Execution Protection
	3. Address Space Layout Randomization

### Memory-safe Languages
These are languages that re not vulnerable to BO attacks. Access to memory is well defined and checks are ensured to ensure this is carried out correctly. Then memory management is done my the languages (garbage collectors e.g.) and so it can ensures memory safety.

### Safe Programming Practices
We should use safe C libraries which ensures the inputs are defined in size and safe.

![[Pasted image 20230317165508.png]]

## OS Level Protection

### Stack Canaries
Here we are trying to detect a stack buffer overflow before execution of malicious code.  This can only *detect* when the stack is smashed. The plan is to lay a trap (canary) just before the stack and return pointer. The value stored should be random to ensure the attacker cannot leave it unchanged by an overflow.

![[Pasted image 20230317165909.png]]

The canary is checked before returning to make sure it has not changed.

##### Limitations
The canary still has some assumption which may not always be true:

1. The attacker does not earn the value of the canary which could happen if there is a **buffer overread**.
2. The attacker cannot *jump over* the canary - that is the memory writes are consecutive.
3. The attacker cannot guess the canary value - on 32-bits the attack may be able to *brute force* the value
4. The buffer overrun occurs on the stack - but this cannot detect heap overruns.

### Data Execution Protection (DEP) - Write XOR Execute (W^X)
Here we are trying to prevent malicious code from being executed. We do this by making regions in memory *either executable or writable*. But not both.

The **stack** and **heap** will be writable but not **executable** and not written because it only stores code. No malicious code can ever get executed even if it is injected.

##### Limitations of W^X: return-to-libc attacks
The attacker doesn't need to inject their own code. The libc library is linked to most C programs libc provides all the tool required to mount an attack.

![[Pasted image 20230317170847.png]]

### Address Space Layout Randomization (ASLR)
Here we want to stop the attacker from predicting the location of things in memory. We place standard libraries to random locations in memory. So for each process, exec() is situated at a different location

![[Pasted image 20230317171140.png]]

### OS Takeaways
Hackers can always develop complicated exploits. It boils down the programmer to do the defending. The most important measure is **safe programming**.  We must ensure whenever a program copies user-supplied input into a buffer we should ensure the program copies into the correct space in data.

![[Pasted image 20230317171400.png]]

[[Memory Safety Defenses Questions]]
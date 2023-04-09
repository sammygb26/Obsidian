What is the most basic buffer overrun attack?  #flashcard #CS #BufferOverruns
	In the most basic buffer overrun attack an unsafe user input function like gets is called. Usually this would just fill whatever buffer it is assigned to fill. But it allows users to input as many characters as they like. So instead the values can explode down into the stack overwriting other variables or return addresses.

---
What takes place in control hijacking (buffer overrun)? #flashcard #CS #BufferOverruns 
	Here we can overflow the return address and control where the program jumps to. We may also inject our own code and instruct the return address to jump us to that. This way we can inject our own program into a program. The trick here is loading malicious code and making eip point to it.

---
What is shell code? #flashcard #CS #BufferOverruns 
	The idea behind shell code is it is a piece of code that once run by the program will turn the program into a shell taking user input. At this point any privileges the program has can be used by the user to run shell commands like viewing or editing files.

---
What is a shell code injection attack? #flashcard #CS #BufferOverruns 
	Here we inject some shell code. Then we make eip jump to that code and run it. This will spawn a shell and give allow shell access with the privileges of the program being run.

---
When injecting code what can make it hard to run? #flashcard #CS #BufferOverruns 
	We need to find the code in memory. That is guess the address of the stat of the code. We may not always know this depending on the programs execution to that point.

---
How can we get past the problem of guessing a return address to run our injected code? #flashcard #CS #BufferOverruns 
	We can insert a **NOP** sled. NOP instructions only increment the instruction pointer. So if we can guess any of these NOP address they will being us to the start of our programmed.

---
What makes buffer overflow attacks possible and how can this be avoided? #flashcard #CS #BufferOverruns 
	Using unsafe libc functions makes this possible. For example gets, strcpy, strcat, scanf etc. These all don't check the bounds of the buffers they manipulate. To get around this **safe versions** like fgets should be used which must be passed the buffer length to be called.

---
What is the problem with the solution to buffer overflows being to just use the right functions? #flashcard #CS #BufferOverruns 
	The problem is it is now the implementation by the programmer that must be safe. But people can get lazy and ignore or be ignorantly of these issues. A way around this is to use **safe languages** which by their design don't allow these kinds of issues.

---
How can arithmetic overflow cause issues in and security flaws? #flashcard #CS #BufferOverruns 
	We may build secure systems assuming arithmetic overflows don't occur. For example checking if the sum of two strings is greater than some value. However if one string is so large it overflows then the value will be small when the secure system would assume it would be large in this scenario. This may allow crafted attacks to by pass checks or write to unexpected memory addresses.

---
What issue is created by shifting between int and unsigned int numbers? #flashcard #CS #BufferOverruns 
	Functions like memcpy despite being safe themselves can be made unsafe by relying on checking the size of the length input as an integer instead of an unsigned int. This is as int values can be negative. But this translates to the largest unsigned integer values.

---
What are heap overflow attacks? #flashcard #CS #BufferOverruns
	The heap contains dynamically allocated memory. But this can also be overflows although it doesn't have the same connection to flow control that the stack does (with return addresses). These attacks require understanding of **garbage collection and heap implementations**.

---
How do format string vulnerabilities work? #flashcard #CS #BufferOverruns 
	Functions like *printf* take in a string as an argument. This is used to figure out how many argument the function has taken. This way if the user control the format string passed they control how many arguments are read from the stack. The arguments are read up into the stack and so this can be used to read return addresses or sensitive information.

---
How can format string vulnerabilities be protected against? #flashcard #CS #BufferOverruns 
	These can be protected against by always passing in a format string for a user string to be printed as. This means the user string isn't interpreted as a format string and so not used to predict how much of the stack to print.

---
What is TLS Heartbleed? #flashcard #CS #BufferOverruns
	This is a vulnerability where a server echos some input the user sends. Allowing the user to verify the server is functioning. But the user can independently send a string and the length of the string. So any remaining characters are send by the server possible leaking private keys.

---


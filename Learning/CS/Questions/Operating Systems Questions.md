What does the OS provide? #flashcard #CS #OperatingSystems
	OS provides an interface between the users of the computer and the hardware of the computer. This keeps the users safe from themselves and other users.

---
In operating systems what are the two primary needs for security? #flashcard #CS #OperatingSystems 
	The needs come from **multi-users** (multiple users with different levels of access are operating on the same system) and **multi-tasking** (different possibly malicious applications with their own potentially confidential data need to be kept from interfering with each other)

---
What is the kernel in a Unix operating system? #flashcard #CS #OperatingSystems 
	The kernel is a key components of the OS it allows secure resource sharing between low level resources. This is done by system calls which run kernel function which are small programs.

---
What are the two execution modes a CPU can be in? #flashcard #CS #OperatingSystems 
	The two modes are **user mode** which has restricted access and **kernel mode** which has unlimited access but cannot be entered unless via a system call.

---
What are system calls? #flashcard #CS #OperatingSystems 
	System calls are how a user program accesses the hardware of the machine. These allow files to be read or IO devices interacted with. The way this works is arguments are loaded and then a kernel interrupt is triggered. This changes the execution mode and runs a special kernel program.

---
What is a process in Unix (what does it have uniquely)? #flashcard #CS #OperatingSystems 
	A process is an instance of a program. It has a *pid* that locates it in ram. It also has a *uid* (user ID) and a program name.

---
What does a program used to create a new program? #flashcard #CS #OperatingSystems 
	A fork is a system call used for this.

---
How is memory managed between processes? #flashcard #CS #OperatingSystems 
	Each process works in *virtual memory* which means it acts as through it controls the entire memory space. But the OS actually maps this address space to different parts of memory without the process knowing. This ensures process memory is kept disjoint and processes cannot interfere with each other.

---
What are the five segment of memory for an x86 program? #flashcard #CS #OperatingSystems
	The five segments are (from low addresses to high) the **text segment** (program code), **static data** (static variables in the source code), **heap** (dynamically allocated memory), **stack** (containing working memory) and a **reserved** segment for the kernel.

---
What are live CD attacks? #flashcard #CS #OperatingSystems 
	Here sensitive files Pagefile.sys and Hiberfile.sys (which contain VM management and paused process data) are stored on disk. They would usually be deleted when the system shuts show to prevent their data from being read but we can shut of the machine directly and so it can't wipe these files. We then read the memory directly via an external device.

---
How can live CD attacks be prevented? #flashcard #CS #OperatingSystems 
	These attacks can be prevented by encrypting the sensitive files then keeping the key in volatile memory.

---

In general we will focus on x86 and Unix like OSs. An **OS** provides and interface between the users of the computer and the hardware of the machine. The **user interacts** with the machine via Applications. The **applications** access the hardware (everything, WiFi, data etc) through the OS.

### Security
The need for security comes from multiple areas:

**Multi-users** - OSes must allow multiple users potentially with different levels of access on the same computer. The OS must be able to limit the rights of users. And **isolate different users**.

![[Pasted image 20230303100647.png]]

**Multi-tasking** - OSec must allow multiple application programs to run at the same time. But the OS must **isolate different applications** from interacting with each other when they aren't meant to.

### Essential Unix Architecture
Jus to go over some Unix details

**Kernel** - This is a key component of the OS, it allows secure resource sharing between low level resources. This is done my only allowing direct access to the hardware via **system calls** which the OS carries out.

**Execution mode** - There is a **user mode** which only has access to resources through syscall to kernel. Then **kernel mode** which gives direct access to resources.

**System calls** - are contained withing a collection of programs in libraries for example open(), close() and read() for files.

![[Pasted image 20230303101050.png]]

Since moving into kernel space involves direct interaction with hardware, an OS limits how an application can interact with its kernel, so as to provide both security and correctness

### Processes and process Management
A process is an instance of a program that is executing. Each program is identified with a unique identifier called a *pid* that locates it in RAM. To a *pid*, we can associate its CPU time, memory usage, user ID *uid*, program name etc. A process might control other processes via a fork. Child process inherits context rom parent processes.

### x86 CPU/Memory

![[Pasted image 20230303101340.png]]

To actually be executed the program must be loaded into RAM and uniquely identified. The RAM memory allocated to a program is its **address space**, this will be **disjoint** from other programs to ensure they can't interact with each other. It contains both the code for running programs its, input data and working memory. The CPU maintains the EIP (Extended Instruction Pointer) that points to the piece of memory being executed.

### x86 process memory layout (*simplified*)
The memory is broken into 5 segments in the OS model. The **text** segment which contains the code the process will execute. Then **static data** which contains static variables specified in the source code. The **heap** above that contains dynamically allocated memory. Then from the top we have **kernel reserved memory** and then the **stack** containing working memory of the program.

![[Pasted image 20230303101816.png]]

Generally we look at memory in terms of ranges. The stack grows down while the heap grows up at least in x86.

### Virtual Memory
The memory is isolated via **virtual memory**. The key thing is there is a finite amount of RAM but virtual memory allows programs to all act as they control the entire access space. The programs act as they get a whole contagious segment of memory. The virtual memory is mapped to real memory ram or disk, this way the program is isolated form memory details.

![[Pasted image 20230303102106.png]]

### Live CD attacks on memory
Virtual memory is mainly for resource efficiency and introduces some security concerns. For example in windows **Pagefile.sys** is a paging file which windows uses to store virtual memory contents Then **Hibderfil.sys** is a file that stores volatile memory contents when the system needs to enter or has entered hibernation. Then **Swapfile.sys** stores the idle and non active process data.

The OS is secured so that these files are deleted when the computer is powered down. If this isn't deleted sensitive memory could be kept and accessed later possibly maliciously. These files are mediated through the kernel. One possibility is

![[Pasted image 20230303102452.png]]

To mitigate this we encrypt the hard drive. Then even when booting externally we only see encrypted files.

# Security Principles
These are important principles to secure moderns systems in general.

### Defence-in-depth
Here we have layers of protection. The key idea is if one fails we still have multiple layers protecting the system. If one mechanism fails another steps in. We have **intentional redundancy**.

![[Pasted image 20230303102922.png]]

### Least Privilege
Here the idea is users should only get the bare minimum privileges to manipulate their data. So a torch application would only need to access the torch and not the location ,WiFi etc. The key thing is malicious entities may try to get extra privileges.

### Privilege Separation
Here we segment a system into components to which we can limit access. This allows least privilege by having different components with different  privileges. This limits damage cuased by a security of an individual component.

### Open Design
We cannot rely on **security through obscurity** having open design mobilizes the security community to hep find bugs and issues. Attackers aren't dissuaded by hidden design and so you just disadvantage defence by making systems secret.

### Economy of Mechanism
Here the idea is to keep a mechanism simple to ensure the use and implementation is secure. We can uncover vulnerabilities with simple systems.

### More Security Principles
**Fail -Safe defaults** - default configuration should be conservative, so new users should be granted least privileges.

**Complete mediation** - every access to a resource must be checked from compliance with security policy.

**Usable security** - UIs and security mechanisms should be designed with the ordinary user in mind - the users should be supported in interacting in a secure way with the system - you can't blame users, it doesn't help.

[[Operating Systems Questions]]

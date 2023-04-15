The **OS** (operating system) is a vital part of the computers working. It is the interface between the user of the computer and the computer's hardware. It has many tasks many of which involve security. For example it must allow **multiple users** who have different levels of access. It must also handle **multitasking** and not allow the myriad of applications (some of which may be critical) to be tampered or read by other (possible malicious) programs.

## The Kernel and IO
The kernel is the interface between the IO devices, CPU and memory and the user. There may also be non-essential OS system that run beneath the user but this all facilitates a safe and powerful zone user programs can run in called the **userland**.

![[Pasted image 20230413143630.png]]

### Input / Output Devices
There are many IO devices such as mice, keyboards, WiFi cards etc. Each has a **driver** which manages the details of operating the devices. It provides an **application programmer interface** (API) to user programs. The OS does the hard part of running the program behind the API.

### System Calls
Our user applications don't communicate directly with the  *low-level* hardware an way of calling for the kernel to deal with the request is needed. These are called **system calls** or *syscalls*. For example *open*, *close*, *read* and *write* may be syscalls for interacting with files. A common way is to handle these is **software interrupts** where a request by an application stops the current execution flow and switches to a handler for the interrupt. This way of doing things via an interrupt is usually called a **trap**. It ensures when kernel mode is entered it is done via a kernel defined program which can be used to ensure it is handling the hardware safely.

## Processes
This is an instance of a program which is currently executing. The program itself is stored in persistent storage but the process is an instance loaded into memory. Multiple processes can be run for the same program at once in RAM.

The kernel ensures all the running processes are given a fair share of the CPU's time. This ability is called **time slicing**. Each time slice is very small and each switch so fast as users we do not notice this.

### Users and the Process Tree
Programs can create other programs through a **fork**. Each program therefore has a parent program accept the first program. Programs inherit the user privileges of the parent program without a explicit reducing in privileges usually. This allows a tree of programs to be visualized. All programs come from the *init* program in Linux and any orphaned programs become children of it.

![[Pasted image 20230413145920.png]]

### Process IDs
Every process is identified by a unique positive integer called the **process ID** or PID (init has PID 0).

### Process Privileges
Permissions are given to program by associating them with users. On Unix-based OS systems each process has a **user ID** identifying the user associated with the program. There is also a **group ID** which identifier a group of users for a given process. 

Users and groups of users are given different levels of access. Unix-based system also have an **effective user ID** which is usually the same as the UID. But sometimes this is set the the EUID of the owner of the process.

### Inter-Process Communication
Processes may need to share resources with each other. One way is to use the filesystem. But this can be slow and leaves a trace of the communication others could read.

One way to do this is to use RAM. The processes can each write to a shared portion of RAM . Some other solutions are **pipes** and **sockets**. These create a tunnel from one process to another.  The communication takes place through an in memory object. At one end of the pipe data is created and it is consumed at the other.

### Signals
Rather than communicating directly via shared memory you may want to just send a message to a program asynchronously. This is done with **signals**. When a signal is sent the program is interrupted, then we check if there is a *signal handler* if there is it is executed. Otherwise the process isn't responding and it will be terminated.

### Remote Procedure Calls
This is what windows used instead of signals. This allows a program to call a *subroutine* in another program. Terminating a process is done by calling **TerminateProcess()** which will kill a process if the caller has permission to kill.

### Daemons and Services
Many program are run without the user. In Linux these are called *daemons*. These generally have higher privileges than the users since they are forked before the user logs in and they persist beyond a login session. In windows these are called **services**.

## The Filesystem
This is an OS abstraction of how the key non-volatile memory in a computer is handled. There is a hierarchy of folders/directories.

![[Pasted image 20230413152046.png]]

Folders contain folders and so there is a tree structure with files as leaves.

### File Access Control
The OS needs to determine who can run files, who can open files and who can write files. This is incapsulated in **file permissions**. Each resource has a set of permissions associated with it.

### File Permissions
These are checked by the OS to determine if a user can or cannot access a given resource. This s typically metadata for the file. Many unix-like OSs use a **file permission matrix**. In general it has a uid which maps to some use uid and a group id that matches to some group. Then defines for the **user** (owner who created the file), **group** (users belonging to the group with group id) and **other** for anyone else if the file can be **read**, **written** or **executed**. Each of these is a single bit for the user, group and other.

![[Pasted image 20230413152742.png]]

### Unix File Permissions
The read, write and execute bits are implemented in binary. Each 3bit sequence for the user, group and other can be represented as the decimal conversion for the binary. So 777 is 111|111|111 for the user, group and other.

When traversing folders permissions are also used. Read permission allow a user to list a directories contents, write permission allows a user to create new files in a folder and execute allow a user to traverse a folder.

## Memory Management
Every process is assigned a piece of memory. **Memory management** is used to keep track of this for all programs. In the unix standard way of doing things there are 5 segments of memory.

1. **Text** - Which contains the machine code of the program
2. **Data** - Which contains static program variables defined in the source code.
3. **BBS** - Named for an antiquated acronym **block started by symbol** which contains static variables that are initialized.
4. **Heap** - This contains dynamically allocated memory.
5. **Stack** - This segment houses a stack data structure that grows downwards. This keeps track of functions and holds local variables.

![[Pasted image 20230413194527.png]]

### Memory Access Permissions
Each memory segment has its own set of permissions. Again these will have read, write and execute permissions. For example the text segment usually doesn't have write permissions.

Generally processes do not have permission to change another processes memory without explicit permissions.

There is also a distinction between **kernel address space** (reserved for kernel essential problem) and **user space** (reserved for user programs).

### Contiguous Address Spaces
Generally programs act as though they have contiguous address space. For example an array is indexed from the start to the end in a contiguous chunk and the code text segment is a big chunk. But in many cases it wouldn't be possible to have all programs loaded in this way so an alternative is needed.

### Virtual Memory
Here all programs are isolated in their own virtual address space. They act as though they have access to the entire address space but in reality chucks of this virtual space are mapped to different parts of physical storage. When VM is accessed the **memory management unit** looks up the real address.

![[Pasted image 20230413201628.png]]

We can also use more memory than we have as parts of memory not used can be stored in the hard drive.

### Page Faults
Memory not used for a long time will be moved to the hard drive to save space (**paged out**). But the hard drive is 10,000 times slower than RAM and so when a block is accessed a **page fault** is triggered. This calls on the **paging supervisor** to find the desired memory and read it back into ram

![[Pasted image 20230413202030.png]]

## Virtual Machines
VM technology allows multiple OS to run on one computer acting as though they control different resources. The **virtual machine** software created a simulated environment where the OS can operate. A **hypervisor** or **VM monitor** inside manages this connection. The virtual OS is the **guest**. The VMM can also be run directly on hardware cutting out the host (original OS).

### Implementing VMs
There are two options for implementation **emulation** and **virtualization**. In **emulation** the OS systems are simulated by intermediate programs before the OS is contacted. This allows any architecture to be simulated (within physical constraints) but is slower. **Virtualization** connects the request directly to the OS acting as a seamless bridge. This is faster but you cannot simulate arbitrary architectures.


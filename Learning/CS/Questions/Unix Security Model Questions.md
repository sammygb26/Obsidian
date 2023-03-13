How is an access control policy defined in Unix? #flashcard #CS #UnixSecurityModel
	A control policy is defined as **Who** is allowed to access **what** and **how**. Then **who** is the subject, **what** is the objected (resource). Then **how** is the access operation (syscall).

---
What key assumptions are made in the Unix security model? #flashcard #CS #OperatingSystems 
	The key assumptions are the **who** can be determined via *authentication* and **complete mediation** is used to ensure access isn't gifted.

---
What is the reference monitor in Unix? #flashcard #CS #OperatingSystems 
	The **reference monitor** is a program that performs complete mediation for user operations on resources. This ensures the user is following the control policy.

---
What happens if the reference monitor's process is ended? #flashcard #CS #OperatingSystems 
	As the reference monitor is a key program and is closure causes the system to become unsafe this will lead to the while system shutting down.

---
What are the two kinds of account in Unix? #flashcard #CS #OperatingSystems
	There are **user accounts** associated with humans and **service accounts** which are associated with background processes.

---
In the passwd file how are users defined? #flashcard #CS #OperatingSystems 
	These are defined to have a username, password, uid (user ID), gid (group ID), uid info, home (folder) and shell.

---
How are file permissions defined in Unix? #flashcard #CS #OperatingSystems 
	All resources (sockets, directories, files) are managed as files. There are 3 permission defined for them read (r), write (w) and execute (x).

---
With respect to what entities are the file permission defined in Unix? #flashcard #CS #OperatingSystems 
 File permissions defined for the **owner**, **owner's group** and **other users**.

---
What account on Unix has special privileges? #flashcard #CS #OperatingSystems 
	The root account can change file ownership and so has access to the entire system.

---
What do the different permissions give access to when applied to a directory in Unix? #flashcard #CS #OperatingSystems 
	Execute gives permission to traverse a directory. Read give permission for files to be viewed.

---
What are the identified defined for a program when it comes to permissions? #flashcard #CS #OperatingSystems 
	Each program has a **read user ID**, **effective user ID** and **saved user ID**.

---
What is the real user ID for some process? #flashcard #CS #OperatingSystems 
	This is the ID of the user that started that process giving users permission to that process.

---
What is the effective user ID for some process? #flashcard #CS #OperatingSystems
	The effective user ID determine the process' privileges. This is generally the same but may specify a different user. This allow privileges to be changed via a fork.

---
What is the saved user ID for some process? #flashcard #CS #OperatingSystems 
	This is the effective user ID before the last modification. This can be used to revert privileges.

---
What do the setuid and seteuid system calls do? #flashcard #CS #OperatingSystems 
	$setuid$ changes the uid, euid and suid to some ID. While $seteuid$ only sets the euid and so can be revered. For an unprivileged process these can only set change euid to uid or suid.

---
How can seteuid cause a security vulnerability? #flashcard #CS #OperatingSystems 
	If we uses this to downgrade the privileges of a program it can attempt to regain those privileges and will be allowed as uid and suid have not been set. This can be fixed by using setuid.

---
How are privileges elevated using setuid? #flashcard #CS #OperatingSystems 
	Here programs can have the $s$ bit set. This means the file can be run and will gain the privileges of its user. The reason this isn't a problem is the user has the power to verify their program can't be exploited. This could for example allow user to *change passwords*.

---
What does it mean for Unix privileges to be course grained? #flashcard #CS #OperatingSystems
	This means privileges are defined per user instead of per program. This means any program a user runs has access to the entire user account. This may be too much in many cases. For example bank program may be run in the same space as a malicious one.

---
How are android permissions different from standard Unix ones? #flashcard #CS #OperatingSystems 
	Here programs are given their own space int the computer. This ensures they don't have the power to interact with each other and have the minimal privilege they require.

---

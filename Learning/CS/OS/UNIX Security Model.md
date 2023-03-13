We need to prevent users from messing with multiple programs running. We also need to prevent programs form messing with each other while having access to correct files. The **Unix security model** keeps different tasks isolated from one another while implementing features like permissions. In general we define a **access control policy** as:

![[Pasted image 20230306100402.png]]

**Who (The subject)** - is the entity attempting  to access a resource.
**What (The object)** - is what is trying to be accessed
**How (The access operation)** - read, write and execute

### Key assumptions for separation
These are assumption that the security model relies on to be secure.

1. The system know who the users is - this allows us to determine **who**. That is we are able to **authenticate** the user (usually done with user name and password)
2. **Complete mediation** - all requests are mediated - all request go to the reference monitor that enforces a specified access control policy.

![[Pasted image 20230306100802.png]]

In Unix a **reference monitor** performs complete mediation and grands permission to *users* to apply certain *operations* to a given *resource*. So that is the reference monitor should never be killed and if it is, all other processes should be killed also.

This key piece of software should also be bug free, as it is very security sensitive.

### Users
Two types of accounts exits on Unix which a unique identifier (uid). There are:

1. **User accounts** - associated with humans
2. **Service accounts** - associated with background processes

![[Pasted image 20230306101129.png]]

On entry in the /etc/passwd per account with fields $$\text{username:password:uid:gid:uid\_info:home:shell}$$The uid 0 user is the **root** uid. $\text{gid}$ is the group so permissions can be given by group. These are just sets of users.

### Groups
Groups are set of users that share resources. Every group has a name and a unique identified (gid). These are kept in /etc/group

![[Pasted image 20230306101410.png]]

These entries have the fields: $$\text{group\_name:password:gid:group\_list}$$Users can be part of many groups.

### File Permissions
All resources (sockets, directories, files) are managed as files 3 defined permissions read (r), write (w) and execute (x). Permissions are defined for the **owner**, the **owner's group** and the **other users**.

![[Pasted image 20230306101633.png]]

Root and owner can change file permissions but only root can change file ownership.

### Directory Permissions
Execute permission on a directory allow traversing  it. read permissions on a directory allows  lookup on that file.

![[Pasted image 20230306102550.png]]

### Processes
Users don't actually perform anything, a program/process must be run to perform some action. Each process has a unique identified, the process ID, pid. Each process is associated with the user that spawned it via a fork.

![[Pasted image 20230306102809.png]]

A child process inherits all permission from its parents. Process are given via a tree where in Unix the init process has the lowest level permissions. So there is a tree of processes going back to this init process. When a user is logged in their main process has lower permissions from the root.

##### Process user IDs
Each process has

1. **Real user ID (uid)** - the user ID that started that process giving the users permissions to the process.
2. **Effective user ID (euid)** - the user ID that determines the process' privileges. Generally this is the same but may specify a different user. This allows the privileges to change via a fork.
3. **Saved user ID (suid)** - the is the effective user ID before the last modification. This can be used to revert to previous privileges.

Users can change a process' ID as 

![[Pasted image 20230306103345.png]]

Generally there are some restrictions to this. Root can change euid/uid to arbitrary value $x$. But a unprivileged user can only change euid to uid or suid.

##### Dropping, privileges with setuid
For a program running to work a process wiht lower privileges using the following code.

![[Pasted image 20230306103832.png]]

So this run from root allows to spawn a new process with a new uid. But this would still allow root access as uid and suid.

![[Pasted image 20230306103842.png]]

Hence we must be careful to drop privileges.

##### Elevating privileges - setuid programs
Something we need to modify users privileges say to change passwords. The way this is done is with a **setuid** program. The idea is we allow all users to run a program (which we know well how it acts). Bellow the $s$ bit is said.  This just mean the file will run with its owners user id. The program being run here should change a root **shadow** file but the user can only access this in a basic way through the program which restricts access.

![[Pasted image 20230306104213.png]]

But these programs must be verified well as they give extreme privilege access.

### Unix Permissions are too coarse-grained
All applications install by a single user account have the same privileges. So they have access to anything the other users access. But we may run files which are **malicious** and it can cause damage. This doesn't separate privileges.

##### Android permission
Each app runs with a different users ID, apps do not interact and permissions are set per app.

![[Pasted image 20230306104848.png]]

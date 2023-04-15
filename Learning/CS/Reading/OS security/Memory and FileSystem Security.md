Then entire computers contents are within its filesystem so we must defend this first.

### Virtual Memory Security
Virtual Memory allows 

##### Windows and Linux Swap Files
On windows Virtual memory file locations are written to the disk in a *page file*. Linux requires a *swap partition* to be set up to contain this (but can also manage a swap file). This file must be kept secure as all program memory is contained within. For exaple it is deleted when the system shuts down.

##### Attacks on Virtual Memory
If an attacker were to power ff the machine without properly shutting down the drive could be read externally revealing this file. To mitigate this *encryption* should be used in all cases where untrusted partial have physical access to a machine.

### Password-Based Authentication
User accounts are given sensitive permissions. So how do we identify if the real user is present! We have to use **password-based authentication**.

**Authentication** is the problem of determining someone's identity or role. A standard way of course is the *username* and *password*.

Typically passwords are stored as hashed instead of in *cleartext*. This way if someone gets the store of passwords they must guess until they find the correct password. In a **dictionary** attack an attached uses a list of common words / passwords. Hashes them and compares them to the password store. There are usually far less permutations on these words than all the possible passwords with $n$ character.

One problem with just hashed passwords is hashing is *deterministic* and so the same password will always give the same hash. This has two downsides.

1. If an attacker cracks one user's password any other users with the same password can also be cracked.
2. Frequency analysis can be used showing which hashes are the most common passwords. Or are likely to be common passwords

##### Passwords Salt
This makes the dictionary attack more difficult. We add random noise before the hash. The effect of this isn't easily reversed even if we have cracked a similar password. This can be stored in plain as its effect still blocks frequency attacks since its effect cannot be reversed easily even when known. For this we store the **username**, **salt** and **salted hashed password**.$$(U,S,h(S||P))$$To check a password with salt we just find the entry with the correct $U$, then add salt to the entered password and hash it. If the hashes match we have authenticated.

### Password Authentication in Windows and Unix
In Windows system, password hashes are stored in a file called the **security Account Manager** file which users cannot access while the OS is running. Windows used to use a DES hash implementation used as the LAN Manager hash. This pads user passwords to 14 characters then converts all lowercase letters to uppercase ones and used the 7-byte halves to generate a DES key. They are then used to encrypt a stored strig giving two 8-byte ciphertexts. The space is reduce by using halves and uppercase letters only. There also was no salt and dictionary attacks were rather effective.

### Access Control and Advanced File Permissions
**Access control** defines how the operating system determines what users can do. This is the next step from authentication. Definitions:

- A **principal** is either a user or a group of users. It can be explicitly defined as a set of user (group)
- User **owner** refers to the user owning a file.
- Group **group** called the **owning group** is the default group associated with the file.
- Group **all** includes all users in the system and group **other** is **all/owner** (all without owner).
- A **permission** is a specific action on a file or folder (read, write, execute).
- A folder can also have **read** (list), **write** (new file) and **execute** (set current directory)

##### Access Control Entries and Lists
An **access control entry** (ACE) for a given file is made of a triplet *(principle, type permission)*, where type is either **allow** or **deny**. An access control list (ACL) is an ordered list of ACEs. How files inherit and define by default these entries is different for window and Linux.

##### Linux Permissions
Linux feature file permission matrices, which determine the privileges various users have for files. All permissions that are not granted are implicitly denied so you don't need to deny any permission explicitly. The **path-based** access control principle states in order to access a file, each ancestor folder in the file system tree must have *execute* permission and the file must have *read* permission.

Then **discretionary access control** (DAC) mean file owners have the power to change permission on those files.

Custom attributes can also be set up such as making files append-only or immutable (undeletable even for root). These are accessed with the chattr and isattr commands.

Linux now also supports a optional ACL-based permission scheme. ACEs are give to files for the **owner**, **group** and **other** principles but additional ACEs for specific users or groups called **named users** and **named groups** can be created. There is also a **mask** ACE which is the max allowable permission for the owning group and any named entities and groups. Giving access control the OS needs to select and ACE. In order the rules bellow apply and the first to apply gives the ACE used.

1. $U$ is the userid of the file owner -> the ACE for **owner**
2. $U$ is one of the names users: the ACE for $U$
3. one of the groups of $U$ is the owning group and the ACE for that group has the requested permissions: ACE for **group**.
4. One of the groups of $U$ is a named group $G$ and its ACE contains the requested permissions: ACE for $G$.
5. For each group $G$ of $U$ that is the owning group or a named group the ACE for $G$ doesn't contain the requested permissions: the **empty** ACE
6. Otherwise: the ACE for **other**

If the ACE for **owner** or **other** is empty then the selected ACE determines access. Otherwise the selected ACE is anded with the *mask* ACE. This whole system isn't used that much.

**Security-Enhanced Linux** (SELinux) is a version of Linux developed by the NSA. It has **mandatory access control** for almost all actions on a machine. The rules consist of a **subject** which is a process and an **object** which is the resource being accessed. This system embodies **least privilege**.

##### Windows Permissions
Windows uses an ACL model allowing users to create sets of rules for each user or group. These rules either **allow** or **deny** permissions and are **deny** by default. Different controls are *modify, read and execute, read, write and full control* (all permissions). There are also **advanced permissions** which further fine grain these permissions

Folders also have permissions **read** is synonymous with listing a folders contents, **write** allows you to create files. The same permission inheritance scheme as in Linux isn't used. Only the ACL of the file concerns whether it can be accessed. So files can be accessed in folders without access.

Generally folder have **inherited ACEs** coming from superfolders. There are also **explicit ACEs**.

### The SetUID Bit
We may also need to grant programs permissions the user running them doesn't have. For example changing a password. To solve this **unix like systems** have a **setuid** bit. If this is set the program runs with the effective user ID of its owner. So if the program is owned by root it runs as root and can change /etc/passwords.

There can also be a **setgid** bit which does the same thing but for groups.

The issue with this is if an attacker can take over these programs they have **elevated their permissions** to that of the owner!

### Example SetUID Program
Programs can called seteuid() to drop and restore its permissions. The program generally runs with the permissions of the user but briefly raises to write to a log file.

![[Pasted image 20230414130307.png]]


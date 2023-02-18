To have a secure system **security properties** must be given which define this secureness against **attacks**. The **design** of security is also important as with bad design adoptions will be low little security improvement will be achieved. **Testing** is important to ensure implementation of secure systems meet specification. Once deployed the system should be **monitored** to ensure continued security. **Patches** can be issued to improve this or remove newly discovered issues.

### Confidentiality, Integrity and Availability

![[Pasted image 20230209185338.png]]

##### Confidentiality
This is the **avoidance** of unauthorized disclosure of information. That is a confidential system keeps information secret while allowing it to be accessed by true users. To protect this the following concepts are used:

1. **Encryption** - The transformation of information using a secret, called an encryption key so that the information can only be revealed using a decryption key which is also secret. Finding the message another way should be hard or nay impossible.
2. **Access control** - This means only certain users can access certain information. Information is segregated between users.
3. **Authentication** - The proving of identity this can be done in many ways (passwords, pins, fingerprint scanners etc).
4. **Authorization** - This means a users is authenticated before access control is granted.
5. **Physical security** - This is keeping computers safe in a physical way limiting access either to people or other physical forces like floods and fires.

##### Integrity
This is ensuring **information** is not forged or changed in an unauthorized way. This can happen from an attacker of even a bug causing some crash and corruption of data. The **access control**, **authentication**, **authorization** and **physical security** will help ensure this along with:

1. **Backups** - Stores of data to be accessed if the main store is compromised
2. **Checksums** - This allows a file to be boiled down toa single value. Small changes down to the bit level change this value and so it can be used to verify if a file has changed.
3. **Data correcting codes** - These's are ways of storing data that allow small errors to be automatically corrected.

These all used **redundancy** to achieve their effect. **Metadata** also need to be protected which is information about a file that is not the main data. For example when it was opened and by who.

##### Availability
The is the property that **information is accessible**. A system is not functional if it cannot be accessed hence why this is a target of attacks. Somethings that help with this are:

1. **Physical protections** - Here we build in availability with the design and operation of our systems for example by having backups ready to go and making our system resilient to outages.
2. **Computational Redundancies** - these are computer system which are ready to take over availability if the main system fails. They ensure even if there is a break in connection a new one can quickly be made. But it would be costly and hard to remove all of these back-ups. **RAID** is an example of this meaning *redundant arrays of inexpensive disks*.

### Assurance, Authenticity, and Anonymity

![[Pasted image 20230209191723.png]]

##### Assurance
This is the provision of trust. How a system can prove it is secure. This is done with

1. **Policies** - Fixed ways a system operates that ensure security.
2. **Permissions** - Describes who has what access and so why malicious actors don't have access.
3. **Protections** - Preventative measure ensuring *policies* and *permissions* are met.

**Software engineering** is also important here as systems need to implemented correctly.

##### Authenticity
The ability to determine that the statements, policies and permissions issued are genuinely from a given person.

### Security Principles
**Economy of Mechanism** - The system should be simple and easily maintained to allow problem to be found and addressed.

**Fail-safe-defaults** - This means by default any agent has as little control as possible. This limits the power adversaries can gain easily.

**Complete mediation** - Every access to a resource must be checked to be compliant with security. This may get in the way of usability.

**Open design** - This means the design of a system is open and available to be revied by third partied and the public. This means system's security can be ensured and verified. The opposite is *security by obscurity* where the working of a system are kept secret to ensure security. However this has the problem that if the system is revealed security much harder to restore.

**Separation of Privileges** - Many layers of access should be required to change some resource. Hence the privileges of the different levels are seperated. This ensures a failure is one has as little impact as possible.

**Least privilege** - Each program and user has a little power as possible so if any are breached the smallest amount of power is gained.

**Least common mechanism** - Resource sharing should be minimized as this limits how much one potentially compromised mechanism has over other parts of the system.

**Phycological Acceptability** - This states that secure systems should be easy to use ensuring that users use them in the correct easy way. Security is no good if no-one uses it.

**Work factor** - The cost of breaking security of a resource should be comparable to the  system used. There is no sense protecting rubbish.

**Compromise recording** - Logs should be kept so that after an failure faults can be analyzed found and fixed.

![[Pasted image 20230209193849.png]]
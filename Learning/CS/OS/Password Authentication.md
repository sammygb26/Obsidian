**password authentication** is used to ensure only the correct users have access to resources. A standard authentication mechanism is **username** and **password**.

![[Pasted image 20230309100504.png]]

Passwords need to be **hard to guess** and **easy to remember**. But the issue here is having a secure password violates it being easy to remember.

### Network Attacks
Here a Man In The Middle can get a user name and password if they are sent over a network.

![[Pasted image 20230309100647.png]]

The solution is

![[Pasted image 20230309100656.png]]

### Social Engineering & Phishing Attacks
In **phishing** an attacker tricks the user into compromising the system like putting their info into a fake website. This may again allow the attack to place themselves in the middles between the user and the legitimate server.

![[Pasted image 20230309100832.png]]

### Defending against phishing - NCSC guidance
This is the guidance given to defend against phishing.

![[Pasted image 20230309100915.png]]

##### Layer 1 : Make it difficult for attacker to reach users
One example of how this can be done is anti spoofing software on a network or phishing detection software.

##### Layer 2 : Help user identify and report suspected phishing emails
Here we need to train users to detect emails. Then whenever there is a doubt make it easy to report emails. Here is an example from UofE

![[Pasted image 20230309101346.png]]

##### Level 3: Protect your organization from effects of undetected phishing emails
Here we can design our system to be robust to spoofing failures. For example assuming user names and passwords can be compromised how can we make the network secure. For example this can be done with multifactor authentication. Or **password management** can be used.

**Password managers** - are software that automatically fills in credentials in forms. But these only fill the form in on websites with the correct domain and so different websites are detected.

![[Pasted image 20230309101520.png]]

## Malware Attacks
In a **malware attack** a user will have installed malware on their machine. For example a **key-logger** that records keyboard stokes and intercept passwords when typed. This comes in level 3. If the username and passwords are found we could use **two factor authentication**. This way an attacker doesn't just need a password but also the user's phone for example.

![[Pasted image 20230309101728.png]]

## Online guessing attacks
This is an attack when we are remotely authenticating to a server. This happens on a **live system** (the server is running). We assume the username is known and then the attacker just guesses the *password* over and over again.

![[Pasted image 20230309101949.png]]

### Defence
There are different ways to defend against this attack

1. **Choose a good password** - we want to ensure the *space* of passwords is large. If there are only a small number of possible (say short) password the attacker can find the password quickly. Generally a website may have a password strength meter that ensure passwords are a given length. But this conflict with users need for an easy to use system.
2. **Rate limit** - impose a limit on the number of failed password attempts before locking the system for a set amount of time. This way the speed the attacker can search through the network is limited.
3. Include **captchas** - here there is a puzzle that must be solved along with the submission of the password. These are hard to read from the computer point of view and these remove the automated side of the computer task. However this is becoming harder with AI techniques in the mix.

## Offline Guessing Attacks
This is the most common password-related attacks on servers. In this scenario somehow an attacker has stolen a password database. For example via an exploit in the hardware or software or even an **insider attack**. The database has usernames associated with credentials

![[Pasted image 20230309102605.png]]

These are offline guessing attacks as the server isn't live. Here the server isn't required for authentication. One way is the encrypt the database. Another way could be to **derive a key from the password**. Here the attacker would require the entire user data to attempt to decrypt.

##### Unencrypted

![[Pasted image 20230309103115.png]]

This s a **bad idea** but often server still do this. A problem here is since user **reuse passwords** this can lead to many accounts being compromised. Hence if this happens not only the one account should be reset but instead all accounts.

### Encrypted

![[Pasted image 20230309103331.png]]

Here each password is encrypted with a database key. Stolen passwords cannot be decrypted, only admins have the key. So if a user forget their passwords only admins can find it again.

A problem is keys may be stolen along with the database. Plus admins can view all keys.

### Hashed
Here we store a hash of the passwords instead of the plaintext passwords. This makes sense as the hashes are OWF meaning we cannot resolve the password from the hash and CR meaning we cant find two passwords which both hash to the same value.

![[Pasted image 20230309103613.png]]

#### Brute force attack
Here we need to go overall all passwords, in a given space. If we have $\kappa$ possible characters and a length of $l$ we have $\kappa^l$ possible characters. Ensuring passwords are **strong** keeps $l$ long and $\kappa$ large and so makes this whole step harder.

### Dictionary attack
Here many common words and old passwords are added to a database. To crack a password we look through this list, concatenate and permute the passwords. This can cut down on the size of the space we need to explore. For example the top 25% of passwords make up 10% of passwords. This makes it easy to crack a small many passwords quickly.

![[Pasted image 20230309104625.png]]

Here a problems are:

![[Pasted image 20230309104717.png]]

The problem here is **frequency analysis** and **users picking the same answers**.

## Salt and Hash
Here we add some random value which we store in the database. But we store this before hashing and so this way we must check all hashes still for a given password.

![[Pasted image 20230309104949.png]]

The salt is a **large random numbers**.

We can also use **slow hash functions** $H(pwd)=h^{1000}(pwd)$ for example.

### Two Factor Authentication
This can also be used to defend against compromised passwords.

### Password managers
This makes dictionary and frequency attacks harder as passwords are very long, complected and different from other users passwords.

[[Password Authentication Questions]]
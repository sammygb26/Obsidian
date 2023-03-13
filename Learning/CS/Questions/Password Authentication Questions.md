What is the standard authentication mechanism for users? #flashcard #CS #PasswordAuthentication
	The standard model has each user associated with a username and password. To authenticate for a username the password is given.

---
What is required of passwords (these conflict)? #flashcard #CS #PasswordAuthentication 
	We require passwords to be hard to guess and easy to remember.

---
What is the network MITM attack on password authentication (+solution)? #flashcard #CS #PasswordAuthentication 
	Here an adversary can intercept a password on its way to a server. It then authenticates as the user and can pretend to be the server to the user. This can be prevented by *encrypting communication* properly.

---
How do social engineering and phishing attacks break password authentication? #flashcard #CS #PasswordAuthentication 
	To break password authentication a SE / phishing attack trick the user into giving up their password.

---
What are the 4 layers of defence against phishing (NCSC)? #flashcard #CS #PasswordAuthentication 
	The four layers are 1) Make it difficult for attackers to reach users 2) Help users identify and report suspected phishing emails 3) Protect against effect of undetected phishing 4) Respond quickly.

---
What is layer 1 of NCSC guidance on phishing and how can this be accomplished? #flashcard #CS #PasswordAuthentication 
	Layer 1 is the **make it difficult for attacker to reach users**. One way to do this is have anti spoofing software active and phishing email detection software.

---
What is layer 2 of NCSC guidance on phishing and how can this be accomplished? #flashcard #CS #PasswordAuthentication 
	Layer 2 is **help user identify and report suspected phishing emails**. This can be accomplished by training users on what emails look like. Or having banners that warm when emails come from outside an organization.

----
What is layer 3 of NCSC guidance on phishing and how can this be accomplished? #flashcard #CS #PasswordAuthentication
	Layer 3 is **protect you organization from effect of undetected phishing emails**. Here we can assume passwords are stolen. This can be remedied by using multifactor authentication and password managers.

---
How does multifactor authentication defend against stolen passwords? #flashcard #CS #PasswordAuthentication 
	With multifactor authentication users may require more than just passwords to access information for example physicals one-time-pin devices (banks) or authentication via an app on their phone or message sent to their phone.

---
How do password managers help when phishing emails get through? #flashcard #CS #PasswordAuthentication 
	Password managers can check the URL of pages you are entering your password into. This can ensure you aren't entering your details into some fake website which is phishing you.

---
What is the benefit of password managers once an email has already been stolen? #flashcard #CS #PasswordAuthentication 
	Password managers can ensure unrelated random passwords are used for all websites. Hence if a password is stolen it wont compromise multiple accounts.

---
How can a malware attack compromise passwords? #flashcard #CS #PasswordAuthentication 
	Malware are malicious programs run on a system unbeknownst to the user. They can install key-loggers which listen to the keystrokes of a user. This can reveal passwords.

---
How can passwords comprised by malware be defended against? #flashcard #CS #PasswordAuthentication 
	This requires two-factor authentication as then the attacker must compromise authenticating devices aswell.

---
What is the online guessing attack? #flashcard #CS #PasswordAuthentication 
	Here we have a server that authenticates some username and password. We assume the username is known and then the password is guessed over and over again.

---
What are the three ways to defend against an online guessing attack? #flashcard #CS #PasswordAuthentication 
	The three ways are to **choose a good password** (so its hard to guess), **rate limit** (so attacker can try very few passwords) and employ **captchas** which cannot be automated hence making password guessing tedious (AI problem).

---
What is the offline guessing attack? #flashcard #CS #PasswordAuthentication 
	In this scenario an attacker has been able to leak the database used to authenticate users.

---
What are the four cases for the authentication database if it is leaked by users? #flashcard #CS #PasswordAuthentication 
	1) Unencrypted 2) Encrypted 3) Hashed 4) Salt and Hash.

---
What is the problem with storing a password database unencrypted? #flashcard #CS #PasswordAuthentication 
	This means if the database is ever leaked all passwords will be leaked and can be used on other accounts. This also gives attacker an attacking tool as password databased can be used to build a list of common passwords used in dictionary attacks.

---
What are the benefits and negatives of using an encrypted database? #flashcard #CS #PasswordAuthentication 
	If an encrypted database is used. The benefits are the stolen passwords cannot be used or decrypted and only admins have the key. But users can still have passwords returned if they are forgotten. The negatives are attackers a likely able to get the decryption key if the database is already leaked. An **anyone** with the key can view all passwords (even admins **insider attack**).

---
How does a hashed password database work? #flashcard #CS #PasswordAuthentication
	Here for every users to don't store their password but a hash of their password. To authenticate a password we hash it and check if it matches.

---
What are the issues with only hashing passwords? #flashcard #CS #PasswordAuthentication 
	If we only hash passwords then if two passwords are the same they will have the same hash. This makes **brute force and dictionary attacks easier** and enables **frequency attacks**.

---
How does a brute force attack on a hashed password database work? #flashcard #CS #PasswordAuthentication 
	Here we simple work our way through all possible password for a user and check if their passwords match. If no *salt* is used any matching hashes can be cracked together.

---
How does a dictionary attack on a hashed password database work? #flashcard #CS #PasswordAuthentication
	Here we start with a list of common passwords and words used in passwords. We can then apply rules to mutate and combine these base words. This reduces the space of passwords we need to try. For each generated password we hash it and check it against the stored hash. If it matches we have found the password. If no *salt* is used any matching hashes will be cracked together.

---
How does a salt and hash password database work? #flashcard #CS #PasswordAuthentication 
	Here with a password we store a salt (long random number). Each password is XORed with the salt and then hashed before being stored. Passwords can still be authenticated by salting them first then hashing and finally checking.

---

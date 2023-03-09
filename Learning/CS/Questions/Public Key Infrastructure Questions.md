Public key encryption allows secure communication between parties but what is not solved?  #flashcard #CS #PublicKeyInfrastructure
	The problem of how the keys are established in the first case is still not solved we can't be sure the public key we are using truly belong to who we think it does.

---
What are some different options to give out public keys?  #flashcard #CS #PublicKeyInfrastructure 
	These might be **public announcements, publicly available directories, public-key authorities** and **public-key certificates**.

---
What is the problem with using public announcements to share public keys?  #flashcard #CS #PublicKeyInfrastructure 
	There is nothing to defend against forgeries as there cannot be cryptographic verification without public keys already established.

---
What is the problem with using a public-key authority to share public keys?  #flashcard #CS #PublicKeyInfrastructure 
	An issue with this is there is a bottleneck as everyone will need this authority to verify their keys.

---
How does public key-certificates mostly solve the key trust problem?  #flashcard #CS #PublicKeyInfrastructure
	The problem is solve here by having certificates that verify public keys. Once a key is verified it can be used to verify more keys. Each one must be signed by the layer above and as long as keys are given correctly we are all good.

---
What is required in a public key certificate?  #flashcard #CS #PublicKeyInfrastructure 
	A certificate contains some entities **ID information**, a **public key** and **CA information**. This is all hashed and a private key encrypted messages is sent so only the public key can decrypt it. The retrieved hash can be compared to the hash of the certificate information to check its authenticity.

---
What are root certifies?  #flashcard #CS #PublicKeyInfrastructure
	Root certificates are where the chain of trust bottoms out. Everyone needs verifying but this must end somewhere and it ends with these **root certificates**, they are build into browsers and can be used to check certificates at the highest level.

---
What are self-signed certificates?  #flashcard #CS #PublicKeyInfrastructure 
	If a website cannot be verified or doesn't want to deal with the verification process they can self sign. However there is no concoction to the chain of trust so these certificates are only used if the user wants to risk it.

---
What is revocation when it comes to certificates?  #flashcard #CS #PublicKeyInfrastructure 
	Sometimes public keys are given our wrongly or private keys are leaked. In these cases we require a way to pull the certificates out of circulation.

---

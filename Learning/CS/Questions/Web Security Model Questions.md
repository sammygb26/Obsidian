In web security was are the access control policies defined over? #flashcard #CS #WebSecurityModel
	The web security model has its **subjects** as JS scripts beings executed (on behalf of different websites). Then the **objects** are the DOM tree, DOM storage and HTTP cookies. Finally the access control policies used are the *Same Origin Policy* and the *Cookie Policy*.

---
What does the SOP specify as its policy? #flashcard #CS #WebSecurityModel 
	The *Same Origin Policy* says that JS objects can only access resources (DOM etc) from the same origin.

---
What defines if two resources have the same origin (SOP)? #flashcard #CS #WebSecurityModel 
	The origin is defined by the **protocol**, the **host** and the **port**. These must match *exactly* no extra no less. Most browsers treat explicit ports differently from explicit ports

---
How can elements loaded from different origin communicate given the SOP? #flashcard #CS #WebSecurityModel 
	For components to communicate using postMessage interface. This gets around the SOP but critically both side have to agree on its use.

---
What problem does the cookie policy attempt to solve? #flashcard #CS #WebSecurityModel 
	If malicious websites or JS can read cookies it can use this to authenticate fake HTTP requests. This allows attackers to hijack sessions bypassing authentication. But JS can access cookies and they aren't protected by the SOP.

---
What is the scope of a cookie identified by? #flashcard #CS #WebSecurityModel 
	The scope of a cookie is defined by (domain and path). This is defined by the header of the HTTP request the cookie is set in.

---
What are the restriction on what the server can set the domain of the cookie to? #flashcard #CS #WebSecurityModel 
	The **domain** of the cookie is limited so that it is must be a suffix of the domain that sent the cookie (excluding just the TLD). The **path** can be set to anything.

---
When is a cookie sent to the some server? #flashcard #CS #WebSecurityModel 
	A cookie is sent to a server if the cookies domain is a *suffix* of the URL's domain and the path is a prefix of the URL's path. The protcol and port don't matter as in the SOP.

---
How do the SOP and Cookie policy interact to give JS access to cookies? #flashcard #CS #WebSecurityModel 
	JS with an origin $O$ can access all cookies which are in scope of $O$ even if the origin doesn't match.

---
What are HTTP only cookies? #flashcard #CS #WebSecurityModel 
	These are cookies which cannot be accessed by JS. Instead they are only send within HTTP requests.

---
What are secure cookies? #flashcard #CS #WebSecurityModel 
	Secure cookies prevent cookie leaking by forcing a user to use a HTTP instead of HTTPs request. These two requests are in scope of the same cookies so cookies used to authenticate the secure site will be leaked in plaintext across the network. Secure cookies however will only be sent via TLS.

---
How does the SOP work with cross domain JS? #flashcard #CS #WebSecurityModel 
	The SOP means cross stie JS can be loaded and will execute **with the domain of the parent** with the parent being able to call functions form it. But it cannot be inspected (source).

---
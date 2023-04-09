What is session hijacking? #flashcard #CS #CrossSiteScripting
	This is the exploitation of a valid computer session to gain unauthorized access to information or services in a computer system.

---
What are some ways session hijacking can be performed? #flashcard #CS #CrossSiteScripting 
	*Predictable tokens* could be sued to self authenticate.  Mixed HTTP and HTTPS sites may leak secure tokens. **Cross site scripting** and **Cross-site request forgeries**.

---
What is the plan with an XXS attack? #flashcard #CS #CrossSiteScripting 
	The idea is we inject a malicious JS script into a response form a website. When the JS arrives it can be run as if the website sent it and so will have the same privileges and are able to access the DOM etc.

---
What is required for an XSS attack? #flashcard #CS #CrossSiteScripting 
	We needs a malicious server the user will visit and we need the user to be authenticated already on a vulnerable server. The malicious server injects code into the vulnerable server's response and it is authenticated via SOP.

---
What are the two kinds of XSS attack? #flashcard #CS #CrossSiteScripting 
	The two kinds are **stored** (where the script is injected into the vulnerable server and becomes stored *permanently* in some database/structure and later returned) and **reflected** (where the user is tricked into sending a request which itself contains the code which is injected into the response).

---
What are some XSS defence techniques? #flashcard #CS #CrossSiteScripting 
	Some defense techniques are **escaping/filer output**, **input validation**, **Setting HttpOnly on cookies** and **CSP**.

---
How does escaping/filter output combat XSS? #flashcard #CS #CrossSiteScripting 
	We can escape/filter characters for example > $\to$ $gt means it cannot be interpreted as part of a tag. We can also remove \<script> tags for example.

---
What is the problem with escaping and filtering? #flashcard #CS #CrossSiteScripting 
	The problem is this is error prone and can often lead to hidden vulnerabilities. For example adding scripts to the inside of img tags.

---
What is CSP (Context Protection Policy)? #flashcard #CS #CrossSiteScripting 
	IN CSP we have a *whitelist* of allowed scripts. So if a user adds in their owns scripts or links to them they will not be on the whitelist and so will not be run.

---
How does input validation protect against XSS? #flashcard #CS #CrossSiteScripting 
	Here we check inputs to a server against a template of what they should look like.  We compare against a expected form whitelist those that fit and remove those that don't.

---
How can setting HTTP only help with XSS attacks? #flashcard #CS #CrossSiteScripting 
	The goal of an XSS attack may be to retrieve a cookie to hijack a session. If HttpOnly is set they the attacker cannot retrieve the cookier to their own site and JS cannot access the cookie. But this doesn't prevent all XSS exploits.

---

What is the different between XSS and CSRF? #flashcard #CS #CrossSiteRequestForgeries
	In XSS we are attempting to inject a script as if it were from the vulnerable site. Then it runs with the correct privileges from SOP. CSRF just sends out a request which will have session cookies attacker as it is sent our from the user browser.

---
What is a CSRF attack? #flashcard #CS #CrossSiteRequestForgeries 
	In CSRF we force user to execute unwanted action on a web application they are current authenticated to. CSRF attacks target state changing requests and not theft of data as the attacker has no way to see the response to the forged request.

---
What are the main steps in a CSRF attack? #flashcard #CS #CrossSiteRequestForgeries 
	We build a exploit URL and trick the victim into making a request to the vulnerable server as if intentional. 

---
What does an attacker need to carry out an CSRF attack? #flashcard #CS #CrossSiteRequestForgeries 
	The attacker needs to be able to get the user to "click and exploit link" and the ability to have the victims visit attackers server while logged-in to the vulnerable server. The request structure to the server must also be **predictable** in form.

---
What are some CSRF defenses? #flashcard #CS #CrossSiteRequestForgeries 
	We can **check the referer**, **use CSRF Tokens** and use **SameSite cookies**.

---
How does checking the referer help combat CSRF attacks? #flashcard #CS #CrossSiteRequestForgeries 
	The *referer* describes the site which sent the request. If this isn't equal to the server domain the request is sent to this may be an CSRF. 

---
What are the problems with using the referer to defend against CSRF attacks? #flashcard #CS #CrossSiteRequestForgeries 
	The issue here is that passing the referer field can breach privacy and so many browser remove this field. we cannot expect users to send this and so cannot rely on it.

---
How do CSRF tokens work to combat CSRF attacks? #flashcard #CS #CrossSiteRequestForgeries 
	Here we make request unpredictable. CSRF tokens are sent along with the form to the browser. The attacker cannot build this token into their malicious link as it is unpredictable.

---
How must CSRF token be implemented to avoid replay attacks and other attacks? #flashcard #CS #CrossSiteRequestForgeries 
	They must be different for every request and must be unpredictable (no incrementing values).

---
How does the SameSite cookie attribute protect against CSRF attacks? #flashcard #CS #CrossSiteRequestForgeries 
	Cookies with this attribute are only sent with request sent from the site they are cookies for. This way CSRF attacks cannot be authenticated.

---

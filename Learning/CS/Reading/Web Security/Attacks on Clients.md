## Session Hijacking
An attacker takes over a TCP session in an attack called **session hijacking**. This can also be used to perform session hijacking on a HTTP session (as it runs over TCP). This can be particularly damaging if authentication was used to ensure the users identity but the session is subsequently hijacked. To hijack  HTTP session a adversary must intercept the HTTP traffic and also include any measure used to authenticate with their messages.

![[Pasted image 20230419145118.png]]

##### Defenses Against HTTP Session Hijacking
Sniffers and TCP session hijacking can be used to intercept and look into packets with with the server. These will contain the session information and so can be used to add session IDs to an attackers messages. So sniffing and TCP hijacking must be prevented.

To keep sessions safe *client-side* tokens must be kept encrypted so that they cannot be accessed by an adversary and mimicked easily. Furthermore server-side tokens should be hard to guess and predict (no successor functions and large space of possibilities).

We also need to defend against **replay attacker** where only messages are sent with old credentials to get authenticated. For this randomness should be incorporated into client side authentication and server side credentials should be invalidated / expire.

**Server-side trade-off** - Generally server side sessions are superior in terms of authenticity and easy of hijacking. But they can sometimes be more intensive since all sessions must be tracked.

## Phishing
Here attackers create dummy websites that appear the same to the client and trick the users into giving up their private information. The site can steal the information and either redirect the user to a real website or to a splash page saying the site is down for maintenance.

These attacks generally rely on the fact users wont examine a sites URL properly.

![[Pasted image 20230419150941.png]]

These emails are often sent out by *spammers* faking being from financial institutions. Generally one defence used in **blacklisting** common fraudulent sites.

##### URL Obfuscation
A popular technique used by phisher is to disguise the URL of the fake site so the victim can't tell anything is wrong. Hyperlinks can also be used to disguise links to phishing sites are regular sites.

![[Pasted image 20230419151233.png]]

One attack is called a **Unicode or **homeograph attack**. Basically Unicode characters are allowed for URLs for compatibility with other languages. The problem is very similar or even indistinguishable characters have different addresses. So its impossible to tell if the URL is correct.

## Click-Jacking
The basic idea is to exploit a user's mouse click get the user to do something they don't want to.

![[Pasted image 20230419184109.png]]

There are also many other ways to exploit this and sometimes no-script plugins are added to none of this can happen.

## Vulnerabilities in Mediant Content
Often media content can allow action to be executed that normally wouldn't

##### The Sandbox
This refers to the limited privileges a scrip running inside a program will have. This is to limit the power we give to such scripts.

![[Pasted image 20230419190606.png]]

For example JS can change the DOM but cannot execute con on a users machine outside the browser.

## Privacy Attacks
Information is a key resource on the internet and user privacy is constantly under attack because of this.

##### Third-Party and Tracking Cookies
Cookies can create many privacy concerns. Web severs set cookies through HTTP. But embedded images and files can set their own cookies when their HTTP responses come in. These are called **thirds party cookies**. These can be used to track users across multiple websites and break their privacy.

##### Protecting Privacy
Cookie duration and if third parties are allowed can be set in the browser.

## Cross-Site Scripting (XSS)
Here improper input validation allow malicious user to inject code into the web site which the user runs in their browser. There are two types 

##### Persistent XSS
Here the injected code stays on the website for some time and can be viewed by multiple users. An example would be a user description. An attacker could inject their own script to be saved along with the file.

![[Pasted image 20230419194011.png]]

The code once injected can do many things like access the DOM to find sensitive information or steal cookies to allow the attacker to take over a session.

![[Pasted image 20230419194142.png]]

##### Nonpersistent XSS
Here pare of the URL gets reflected into the DOM. This way a user can for example place a script in the URL then when the victim clicks on the link they are directed to the page and have the script execute.

![[Pasted image 20230419194506.png]]

##### Defenses Against XSS
Fundamentally the issue is the programmers failure to sanities input to the page. As defence many characters such as "<" and ">" should be escaped. Another option is to block scripts that aren't required on the user's side but this can be dangerous.

Filtering doesn't always work and often scripts can be **obfuscated** for example $<script>alert('hello');</script>$ encodes to

![[Pasted image 20230419195140.png]]

This is possible because of URL encoding which help interpret special characters safely. Script detection may be more complicated for example detecting if the cookie is being sent to an URL. But this to can be overcome

![[Pasted image 20230419195319.png]]

## Cross-Site Request Forgery (CSRF)
This exploits the power of malicious website to send messages from the clients machine. If the website can send a request exploiting the fact the user is logged in they can send controlling messages to the vulnerable website.

![[Pasted image 20230419195623.png]]

![[Pasted image 20230419195652.png]]

Following the cookie policy this request will be validated and the user will transfer funds to the attackers account.

There are different preventative measures. For example the server can check the *referer* header which specifies the website sending the request. Or the cookie could have the **same site** attribute set and so authentication cannot be done form the other website. Finally we can use a **CSRF token** which are random tokens sent to the client browser for every webpage. If they aren't present in a response the response isn't valid. So if these are random and the attacker can't guess them they can't make legitimate requests.
Different feature of websites are exploited by XSRFs.

### HTML forms
These allow personalized access to a webapp for different used. A standardized way to have user input. To allow this the different accounts are stored on the server and will return data when the user authenticates. For this the server maintains a **state** for your session. In this case the arguments will be passed in the URL of a GET request and in the body of a PUT request. Upon submitting a request all the *cookies in the scope of the URL will also be sent.

![[Pasted image 20230406125136.png]]

Another note is that even visiting one website many request may be made to different websites to get say images and tools form other websites. The SOP attempts to protect against abused of these multisite requests.

### CSRF Attacks
**OWASP** - CSRF forces a user to execute unwanted action on a web application in which they're currently authenticated. CSRF attacks target state-changing requests, not theft of data, since the attacker has no way to see the response to the forged frequent.

*Target* - user who has an account on vulnerable web application. The user must have an account that the user is logged into. The webserver isn't malicious but is badly implemented. The user muse also be *authenticated* at the time of the attack. For example with an authenticated session cookie.

**Main Steps** - users who has an account on vulnerable web applications have two steps. First we must *build an exploit URL* which will perform an action. Then we need to trick the victim to making the request to the vulnerable server as if intentional (this can take social engineering)

**Attacker tools** 1) ability get the the user to "click exploit link" 2) ability to have the victim visit attacker's server while logged-in to vulnerable servers.

The SOP cannot prevent this as pages can make request to multiple pages.

### Example
1. Alice logs in to bank.com and get a session cookie.
2. bank.com sends back a cookie so Alice doesn't have to re-authenticate.
3. bank.com form for requestion transfers uses a simple form stating with a get request. Say with *account* and *amount*. This is authenticated with Alice's cookie.
4. Alice then visits evil.com which includes a similar form include in their HTML. When the website is visited the document will call a basic form to submit. It is prefilled so a given amount say 100000 is sent to Eve.
5. Alice's authentication cookie is sent along with this request as it is in the domain of bank.com. The context doesn't matter to its processing.
6. bank.com the receives the request along with the cookies

### CSRF Flow
![[Pasted image 20230406130010.png]]

### CSRF Defenses
Using POST or GET makes no difference. Then using TLS also makes no difference as the attack doesn't affect the browser and requests send which are being exploited.

**Check the referer** - The client's HTTP request includes the referer header specifying the context from which this request was issued. The server ensure client's the HTTP request has come from the original site means that attacks from other sites will not function.

![[Pasted image 20230406131312.png]]

A problem with this is too much information is given and this allow analytics to be performed on the user. So referer may not be included and evil.com can instruct this.

**CSRF Tokens** - The idea is to make URLs unpredictable. The server stores CSRF token along user's session token. Includes a fresh CSRF token in every form as a hidden field. On every request , the server check that the supplied CSRF token is the valid one. This must be unpredictable. Ruby on Rails embeds secrets in every link automatically (so less error prone). To avoid any **replay attack** should be different in each server response.

![[Pasted image 20230406131525.png]]

It needs to be long enough to avoid replay attacks.

**SameSite Cookie** - Here cookies are only sent form a certain context. So evil.com's request will not be able to take the cookie along to the server. Cross origin request are blocked.

### Twitter SMS account Hijacking
Twitter allowed user to change account details using SMS. The phone allowed you to authenticate account changes. Another thing is CSRF tokens were used but not checked.

[[Cross Site Request Forgeries]]


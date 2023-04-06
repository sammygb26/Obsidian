
### Session Hijacking
**Session Hijacking** is the exploitation of a valid commuter session to gain unauthorized access to information services in a computer system. This makes sense as sessions are used to maintain use authenticated  state. This can happen in different ways:

**Session token theft vulnerabilities**
1. Predictable tokens - attacker can guess the token - Cookies should be unpredictable
2. HTTPS/HTTP - site has mixed HTTPS/HTTP pages and token is sent of HTTP and so can be read in plaintext - set Secure attribute so cookies are only sent over TLS - Always issue new session token when raising user from being anonymous (possibly over HTTP to authenticated over HTTPS)
3. Cross site scripting
4. Cross-site request forgeries

## XSS Attacks
**Cross Site Scripting** XSS attacks are type of injection, in which malicious scripts are injected into otherwise benign and trusted web sites.

- EXAMPLE

This would mean the JS has the permissions from the original server's data sent over for example with the origin of the service server. So they have access to the DOM etc.

Of course this is broader than session hijacking and can so many things.

### Ingredient of XSS Attacks
The goal of an attacker is to slip code into the browser under the guise of conforming to the SOP. For this we need

- $evil.com$ to provide a malicious script
- attacker trick the vulnerable server ($bank.com$) to send attacker's script to the user browser.
- Victims browser believed the scrip's origin is $bank.com$
- Malicious script runs with $bank.com$ access privileges.

There are two types of XSS attacker **reflected XSS** and **stored XSS**.

### Stored XSS Attacks
The injected script is **permanently stored on the target servers** such as in a database in a message forum visitor log comment field etc. An example of this is customizing homepages on Social Media apps. The victim retrieves the malicious script from the server when it requests the stored information. The browser just runs the script within the context f $bank.com$.

### Reflected XSS Attacks
The **injected script is reflected off the web server** e.g. in an error message, search result, that includes part of the request. Reflected attacks are deliver to victims via another rout such as an email message of on other web message.

The JS is not stored we just trick the victim into visiting an displaying some code. 

So this happens when some sort of user input is echoed into the browser without protection. **ALWAYS USE PROTECTION!**.

### XSS Example

...

### XXS Defence
The problem is **user supplied input**. One defence is **escaping**. Before we serve the HTTP response so that the browser only interprets them as a string.  But this doesn't always work and there are many ways t introduce JS.

**Input Validation** here we check the the inputs headers, cookies, query strings from fields, and hidden fields are expected from (whitelisting).

**CSP** Here the serve supplies a whitelist of the scripts that are allowed to appear on the page. This way injected JS cannot be added or loaded from elsewhere. But here we lock down what can be loaded.

**Http-Only attribute** - For cookies defends against session hijacking. This way JS cannot access the cookies and exfiltrate them.

##### RAW vs. Escaped Output
Escaping removes dangerous character and makes them only interpretable as text rather than parts of tags for example.

Web applications should provide the same security guarantees as those required for standalone applications. We want different domains to not be able to access each other resources. Say evil.com and bank.com. For this we need to describe an **access control policy**. With

*Subjects* - JS scripts being executed
*Objects* - DOM tree, DOM storage, HTTP cookies, the JS namespace
*Access control* - Same Origin Policy and Cookie Policy

### Same Origin Policy
The problem is scripts can manipulate the DOM of the page using the API for the document or window elements. JS can be added to any element to be triggered for a event. But what stops evil.com scripts accessing the DOM of the bank. 

**Part of the solution** : The same-origin policy - The SOP restricts how a document or script loaded from one origin (e.g. www.evil.com) can interact with resources from another origin. Each script has an origin

### SOP and windows/tabs
Windows and tabs have their origin derived from the URL of the webserver providing the content. For example with a URL $$protocol://host:port/path?args\#statement$$ then the origin will be $$protocol://host:port$$ without the path. This is based on the host matching the host string. The strings must match completely to give the same origin. Often an explicit port means a different origin (as apposed to an implicit one based on the protocol).

### SOP and JavaScript
We can load cross-origin scripts. Browsers will execute it with parent frame/window's origin. Cannot inspect source, but can call functions. The **origin** is inherited to the local machine as if it were local. So the JavaScript from another website can access the DOM from the origin. This works for widgets for example. But loading malicious JS can compromise the resources.

![[Pasted image 20230330174402.png]]

### SOP and Images
Browser can render cross-origin images., but SOP prevents page from inspecting it. The image has the origin of the page that loaded it.

![[Pasted image 20230330174418.png]]

### SOP and Frames
These can load cross-origin HTML but page cannot inspect or modify its content. Inspection of its DOM is prevented from the outside. The *parent* and *child* pages cannot interact in an IFrame.

![[Pasted image 20230330174427.png]]

### Cross-origin Communication
The postMessage interface allows windows to talk to each other no matter which origin they are from. It is a way around the SOP but it only works if both agree and so doesn't provide unfettered access.

![[Pasted image 20230330174505.png]]

## Cookies
Scripts can manipulate cookies stored in the browser using the API for documents elements. Scripts can access and send cookies to other domains. The problem is what prevents scripts on evil.com accessing cookies authenticating other pages. The **cookies policy** restricts how web server and a scripts access cookies in the browser. This is important and cookies are used for authentication.

**Access control for cookies** - Cookie Policy - The policy controls what can be set on a cookie. For example who can set cookies to which domain. Then when are cookies sent to different webserver. So how does the browser decide this.

##### Setting Cookies
Cookies maintain state. They have several attributes for example value, expiry, domain, path ,secure, HttpOnly (only sends of HTTP). Browsers can respond with cookies to be put into the cookie Jar. All cookies in the scop of the HTTP request will be sent along to the webserver.

When setting the scope of a cookies a (domain and path) will be sent. The domains that can be set must be a suffix of the webserver domain. So $sub.example.com$ can set a cookie for $example.com$. The path can be anything. The set cookie is sent in the header.

![[Pasted image 20230330175152.png]]

We also block top level domains and so cookies cannot be set for $.com$.

##### Sending Cookies
Cookies are automatically sent back to the server by the browser if the URL's scope contains the cookies. If the cookies domain is a suffix of the URL's domain it will be in the scope of any subdomain of its domain. So for a domain $example.com$ will be sent to $bar.example.com$. IF the cookie's path is a prefix of the URL's path e.g. $example.com/path$ will be sent to $example.com/path/main$.

### SOP vs Cookies Policy
For JS the browser applies the Cookie Policy and not the SOP. So JS with origin $O$ will have access to all cookies in the scop of O. According to the SOP $foo.example.com$ and $bar.exampe.com$ should be viewed as different origins and isolated. According to the cookie policy they are trusted to share cookies set with domain $example.com$.

**HttpOnly**: if enables scripting languages cannot access or manipulate the cookies This can prevent GA rom accessing cookies set by exmple.com. This can also help prevent malicious scripts from accessing cookies.

### Secure Cookies
What if the attacker manages to trick the victim to visit $http://bank.com$ instead of $https://bank.com$. But the cookies will be sent to the other $http://bank.com$ in cleartext. But we can now specify a cookies can be *secure* and only sent over a TLS channel.

[[Web Security Model Questions]]
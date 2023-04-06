What three parts interact to allow a web app to run? #flashcard #CS #WebBasics
	The three parts that need to interact are the browser, the webserver and possibly its database.

---
How does the browser communicate with the server in a website? #flashcard #CS #WebBasics 
	HTTP is used to communicate between the server and the client (browser).

---
What are URLs? #flashcard #CS #WebBasics 
	These are **Uniform Resource Locators** and they are used to identify some resource on the internet.

---
What are the different parts of a URL?#flashcard #CS #WebBasics 
	The different parts of a URL are the $Protocol::host:port/path?arg1=val1\&arg2=val2\#statement$ that is the parts are **protocol**, **host** (subdomain.domain.topdomain), **file path** at the host, then arguments and finally statements.

---
What are the two kinds of resources on the internet? #flashcard #CS #WebBasics 
	The two kinds of resources on the internet are static and dynamic (generated when requested).

---
What is the standard way to allow dynamic content from a URL? #flashcard #CS #WebBasics 
	The standard way is to include arguments in the URL.

---
How does the browser request a website? #flashcard #CS #WebBasics 
	The browser establishes a TCP connection with the server. This is then used to send a HTTP GET request.

---
What are the most common HTTP requests? #flashcard #CS #WebBasics 
	The most common HTTP requests are GET and POST. The idea behind GET is to request a specific resource. POST on the other hand is meant to have some side effect (state change on the server).

---
What are the parts of a HTTP request? #flashcard #CS #WebBasics 
	There is a **header** containing *request line* specifying the operation (GET POST...) then other fields like *Host*, *User-agent*, *accept*, *accept-language*, **referer** etc. There may also be a **body** but it a GET request this usually not included.

---
What are the parts of a HTTP response? #flashcard #CS #WebBasics 
	We have a *status code* specifying if all is well (200) or resource not found (404) and many others. Generally there will be a header section and then a body for example containing HTML for the browser to render.

---
What are forms in HTML? #flashcard #CS #WebBasics 
	Forms offer a standardized way for a browser to send information to the server. These have fields and then a submit operation. When the form is submitted generally POST or GET request will be sent to a server.

---
What is the standard way to add dynamic contents to a website? #flashcard #CS #WebBasics 
	The standard way to do this is to include JavaScript in the website. This is a language that is run in the browser and can add dynamic functionality locally to the browser. 

---
What are the components and steps in webpage rendering?  #flashcard #CS #WebBasics 
	The components taken in are HTML, CSS and JS. A **HTML parser** is used to create the DOM (Document Object Model). The **CSS parser** can then apply CSS operations to objects within the DOM. Finally any scripts are run by the JS engine.

---
How much access to the DOM does JS have?  #flashcard #CS #WebBasics 
	JS has complete access to the DOM for the webpage the JS is operating in.

---
What are the two ways to make HTTP stateful?  #flashcard #CS #WebBasics 
	We can use **cookies** or **hidden field forms**.

---
What are hidden fields in HTTP?  #flashcard #CS #WebBasics 
	Hidden fields are included in the HTML sent to the browser. When the browser makes another request to the server, these elements are sent over and they can be used to track who is logged into which instance of the webserver.

---
What are the problems with hidden fields? #flashcard #CS #WebBasics 
	Some of the problems with hidden fields are they're tedious to program as every webpage needs to include them. The session also ends as soon as the tab is closed.

---
What is the main benefit of using hidden fields to maintain state? #flashcard #CS #WebBasics 
	The main benefit is that every browser supports hidden fields.

---
What are cookies? #flashcard #CS #WebBasics 
	Cookies are small pieced of information send back with a HTTP response. The client stores this information and ends the cookie back whenever requesting from the same host as where the cookie originated (defined by domain and path).

---
What are the different attributes of a cookie? #flashcard #CS #WebBasics 
	Cookies will have a **name** a **value** and other **attributes** like domains, path, expiration date, version number and comments.

---
How are sessions implemented with cookies? #flashcard #CS #WebBasics 
	We can add a user identifying cookie then we store if this is authenticated when a server responds to a message.


---
What are the benefits of cookies? #flashcard #CS #WebBasics 
	Cookies are stored in the browser and not the HTML of the website (like hidden fields). Therefore sessions can be shared across tabs.

---
What are the main limitations of cookies? #flashcard #CS #WebBasics 
	Cookies can be disabled by the browser and so may not work for all users.

---
Why is it important to only send session identifiers over HTTPS? #flashcard #CS #WebBasics 
	If this isn't done an adversary can intercept a users traffic and authenticated themselves to the server as the user.

---
What are frames? #flashcard #CS #WebBasics 
	Frames allow one website to be run inside another. However the inner page and outer are not able to interact with each other's DOMs.

---
What are the goals in web security? #flashcard #CS #WebBasics 
	We want to a) prevent visiting malicious websites from compromising client machines. b) visiting malicious websites shouldn't compromise session with other websites. c) Sensitive data should be stored on websites should be protected.

---
In web security what are the main defence against websites compromising sites that visit them? #flashcard #CS #WebBasics 
	The main defenses are *JavaScript* sandboxing which means JS can only edit features of the browser.  Ensuring this is the case takes avoiding bugs and ensuring privilege separation within the browser.

---
In web security what is the main way we stop visiting malicious websites from compromising other websites the client is visiting? #flashcard #CS #WebBasics 
	The main way this is stopped is with the SOP which isolates websites we visit from each other.

---
What are the two kinds of attackers in web security? #flashcard #CS #WebBasics 
	We have a **web attacker** which controls a websites and has valid SSL and TLS certificates for that website. This website is also visited by th easier. **Network attacker** here we have an attacker that controls an entire network (along with the previous conditions).

---

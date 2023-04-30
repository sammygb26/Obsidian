The web has awakened a new frontier of attacks as a new generation of protocols were developed without security!

## HTTP and HTML
The web is basically a series of servers all of whome provide services that can be interpreted by a **web browser**. We connect to servers with IP addresses but DNS allows us to translate the host name to an IP address.

##### Uniform Resource Locators (URLs)
A web site is identified by a URL, which is basically a consistent naming system for webpages. For example $$http://www.example.com/directory/index.html$$Here $www.example.com$ is the directory, $directory$ is the name of the folder the file $file.html$ is requested. **HyperText Markup Language (HTML)** being a common format describing the content and layout of a page. If we don't specify the path then $index.html$ or $home.html$ is used.

##### Connecting to a Web Server
The $http$ part of the string specifies the *hypertext transfer protocol* which is used to get the web page. Given an URL the web brows first check the local DNS cache for the domain. If this isn't found it will query the DNS server to resolve the IP address. Once this is nailed down the client sends a TCP request to port 80 (usually, or 443 for HTTPS) and then sends over a HTTP request.

##### HTTP Request
This specifies the file the browser wishes to receive from the web server. The request usually starts with a command such as GET (get a resource) or POST (change server state somehow). Then the headers section identifies additional information.

##### HTML
The server responds with a response header followed by the requested information in the body. Usually the response header gives information about the server like type and version number of the software being used. Generally multiple request will be made per page.

![[Pasted image 20230419131021.png]]

##### HTML Forms
This is a HTML mechanism to allow users to provide input to a web site in the form of variables represented by name-value pairs. There are two mechanisms **GET** and **POST** variables.

**GET variables** - are added directly to the URL seperated by & symbol for example. $$http://www.example.com/form.php?first=Roberto\&last=Tamassia$$
**POST variables** - are included in the body of the text.

Generally it is recommended to use GET requests for operations such a querying a database where as inserting a record or sending or sending an email POST should be used.

##### Lack of Confidentiality in HTTP
By default HTTP transmits requests over TCP on port 80. The issue is there is no way to encrypt data and so data can be altered, inspected, updated all in the middle. So this method is insufficient for confidential information.

## HTTPS
The basic idea here is HTTP sent the same but with a TLS or SSL layer between providing Confidentiatlity. This is done with *certificate* which allow for public encryption between the server and browser.

![[Pasted image 20230419132935.png]]

The basic way this words is 

1. A browser (client) requests a connection with a server specifying the cryptographic protocols they can handle
2. The browser choses the best crypto function
3. The browser sends over a certificate identifying its public key
4. The web browser can generate a random number to be used as a private key then send it to the server
5. Data can now be transferred under the encryption of the shared key.

##### Web Server Certificates
These verify that the key really doesn't belong to the server. The idea is that a certificate authority who the client trusts has signed a certificate saying that a given public key belongs to the server. This generally includes

- The name f the CA issuing the certificate
- Serial number (unique among all certificates given by the CA)
- Expiration data of the certificate
- Domain name of the web site
- Organization operating the web site and its location
- Identifier of the public-key cryptosystem used by the web server
- Public key used by the web server in the HTTPS protocol
- Identifier of the cryptographic has function and public key cryptosystem used by CA to sign the certificate
- Digital signature over all other fields of the certificate

## Dynamic Content
In *static* content the pages doesn't change once it is sent to the users and can just be inspected. **Dynamic content** however changes as the user interacts with it. To provide changing content *scripting languages* were introduced. These basically run some code on the computer (not at the lowest level) interpreted by the client's browser. This is called **client-side scripting languages** but there are also **server-side scripting languages** which run on the server.

##### Document Object Model
The **document object model (DOM)** represents the contents of a page in an organized way. The tags in HTML are interpreted as objects and their nesting vies a child parent relationship giving he *DOM tree*.

##### Javascript
This is a powerful client side scripting language that gives a huge amount of tools to interact with the DOM. These are usually incorporated in their own files sent over HTTP or inside script tags.

It can handle events create functions for other objects to call and so on. It can change the contents of the web page by accessing the elements of the DOM.

## Sessions and Cookies
We need to keep track of the **session** with the use for example so they don't have to log in over and over again for very webpage they want. But this generally extends to all information maintained over the current page. Generally session identify are sent between the client and the server to identify them. Generally this information should be kept confidential to users. If someone can get this information they can perform *session hijacking* and pretend to be a user.

##### Sessions Using GET or POST
Here the servers send identifying information along with the webpage then when the next webpage is given the client sends this information with the request. It is protected by being in the DOM of the true website. HTTPS must always be used with this technique since the information send over could be stolen and used to request webpages as a client. This is even worse than if this were done with *cookie* as in the next section since all the information must be send in the response as it must all rest in the DOM. 

Another problem with this technique is the information is lost when a tab is closed and cannot be shared between tabs.

##### Cookies
Another common method for creating sessions uses small packets of data called **cookies** which are sent to the client by the webserver and stored on the client's machine. When the client visits the server if the domain of the cookie matches the server it is sent a long with the request. The server issue the cookie in the HTTP request (in the set-cookie field) but is is **saved** on the browser so it cannot be lost and can be shared between tabs.

##### Cookie Properties and Components
The cookies have **expiry dates** but this doesn't have to be set and by default will be wiped when the browser closes.

The domain field can be specified for a top-level domain or subdomains of a web site. Only host with a domain can set a cookie for that domain. Lower level domains can set higher level ones but not the other way around. So $mail.example.com$ can access cookies from $example.com$ and $mail.example.com$ but $example.com$ cannot access cookies from $mail.example.com$. In general hosts can access cookies set for their Tope-level domains but hosts can only set cookies  for domain one level up in the domain hierarchy. So $one.mail.example.com$ can read cookies from $example.com$ but can't set them. Also TLDs so .one or .com cannot have cookies set for them. These rules are all enforced at the browser level.

In general cookies can be sent unencrypted via HTTP. But secure flag cookies can only be sent of HTTPS.

HTTP-Only can also be set which ensures the cookie cannot be read by any JS and therefore cannot be found using XXS.

Same-site can also be set which prevent the cookie from being sent if the request wasn't made from the same domain for example another website making some request. This helps prevent XSRF attacks.

##### Server-Side sessions
Generally sending all information about a session over in cookies doesn't make sense and make it possible to steal information directly form the client's computer. Generally a **session ID** is send over to a client. The server keeps track of which client has which ID. These should be sufficiently random so that an attacker cannot guess the ID of a user.
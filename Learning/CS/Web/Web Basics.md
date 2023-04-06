When we secure the web we want to secure all the parts that make websites and web apps possible. The **client** uses a browser and at the other end there is a **web server**. The server may then also have a **database** where data is stored. We request content form a server it then responds with a documents via HTTP (HyperText Transfer Protocol one of many web protocols). IP addresses are used to level these machines (client and server) but we use URLs and then establish IP addresses hidden from the user.

### URLs
These are Uniform Resource Locators. These just identify some resource on the internet.

![[Pasted image 20230330161418.png]]

We first specify the **protocol** then we give the **host** (host name or IP address), then a **port** (which program on the server will we ask), **path** (file path we are looking for resources in - with static resources we stop here), **arguments** and **statements** (these allow dynamic files to be updated accordingly). Resources can be either **static** or **dynamic** Static resources like files are sent over the client simply while dynamic resources are generated via scripts. A standard way to allow dynamic content is to include argument which allow the user to augment their request for content.

### HTTP Requests
After establishing a TCP connection on the web server, the browser sends  HTTP requests to the server. These start with a **request line** (GET or POST command). These are then Header and Body sections. Generall a GET request will just send a header. But the body will contain the HTML for example in a GET response. Lots of information like accepted file types, user agent, accepted languages, accepted encoding and other are sent in the header. A POST request supplies data along with it but a GET request just requests a file.

![[Pasted image 20230330162205.png]]

##### Main Request Types
The two main request types are **GET** and **POST** although there are many others designate for different operations. 

**GET** - This is designated for requesting a given resource. Think loading a website or a file.

**POST** - This is meant to be used for operations which change the state on the server. For example POST might be used to log in or change some details like posting a message.

### HTTP Responses
The server processes the request and the returns a response to the browser. There will be a header section and then body. This will generally contain the document we are requesting (webpage etc). A *status code* will also be returned. With 200 for OK and 404 for resource not found (others also exist). We also send a *length* so the browser knows what to expect.

### Hypertext Markup Language (HTML)
This main body of a web page is encoded using HTML. These provide a structural description of a document using special tags. HTML also provides form which allow users to provide input to a website. Forms can submit data either using the GET (values encoded in header) or POST method (values encoded in body).

![[Pasted image 20230330163451.png]]

### Dynamic Contents
Pages with dynamic content can change their delivery to the client browser, instead of sending a predefined webpage. For providing dynamic content, scripting languages such as **JavaScript** were introduced. TO indicate to a browser that JavaScript is being used *script* tags are used. These can allow functions and programming constructs such as for, while, if then else statements etc. JS can also handle evens such as ser clicks or mouse movements.

Websites are more powerful now but this has also lead to many more attacks.

##### JavaScript - example
JS can control the entire page so if an adversary can control the  they can hijack the entire website.

![[Pasted image 20230330163655.png]]

### Webpage Rendering
A webpage send HTML, CSS and JavaScript. The HTML is sent to a HTML parser. It produces a **Document Object Model** (DOM) which is a representation for accessing the content of the page. CSS allows the nodes in the DOM to have style applied simply (done in a way that uses the tree structure). The JS engine then runs any JS on the page. This always listen to event to send them to JS. Once the DOM is completed it is sent to the painter this gives the webpage as we see it.

![[Pasted image 20230330163931.png]]

- JS in fact controls the DOM. They can alter/manipulate the content of the page and can access/update the DOM and so the entire webpage.

### How us state manages in HTTP session
**HTTP is stateless** when a client sends a request, the server sends back a response but the server doesn't hold any information on previous request. That is there is no session built into the protocol. But applications often are **stateful** and so this needs to be add on top. We would want to add some token that gets passed with the page. We either use

- Hidden fields
- Cookies

##### Hidden Fields
Here we pass information tot eh server each time we access the page. We include a hidden field in a form containing a session ID. Each time a website is returned it can encode the session ID it wants to use to keep track of us.  

![[Pasted image 20230330164522.png]]

If this is submitted the name and value are sent automatically in GET and POST requests.

**PROS AND CONS** - This request careful and tedious programming for each individual webpage. As all the pages are dynamically generate including this hidden field.  It also ends the session as soon as the webpage is closed. But this does work on all browsers.


### Cookies
A cookies is a small piece of information that a server sends to a browser and are stored in the browser. A cookies has a name and a values, and other attributes such as domain path and expiration data, version numbers comments etc. The browser automatically includes these in all its subsequent request to the originating host of the cookies. Cookies are only sent back by the browser to their originating host and not any other hosts. These can be used to uniquely identify a user and store other user info. But users can also *block cookies*.

Cookies are set on the clients system when the server uses the Set-Cookies field in the HTTP header of its response. This kind of information is only sent of HTTPS (secure) so that authentication information cannot be stolen by adversaries.

![[Pasted image 20230330170131.png]]

JavaScript can access cookies in the page they are running in. So JS can gain authentication information.

![[Pasted image 20230330170404.png]]

### Frames
These allow you to embed inside a webpage another webpage. This is done with an iframe tag. We say where the frame should be then we give a URL for some other resource we want to include. We want to make sure the inner page cannot alter the outer page and visa versa. The JS for example cannot access the DOM of other pages.

![[Pasted image 20230330170506.png]]

### Security Goals
The reason there is web security nowadays is as the web wasn't developed requiring security. It was developed for academics sharing papers. Web applications should provide the same security guarantees as those required for standalone applications.

1. visiting evil.com should not infect my computer with malware or read and write files - **Defence**: JavaScript sandboxed, avoid bugs in browser code and privileges are seperated.
2. visiting evil.com should not compromise my session with gmail.com for example **Defence**: same-origin policy - each website is isolated form all other websites
3. sensitive data stored on gomail.com should be protected. From server-side attacks where data can be manipulated from the client side

##### Threat Model
We may consider a **web attacker** who controls evil.com and may have obtained a valid SSL/TLS certificate from evil.com. Victim user visits evil.com.

Then the **network attacker** also control the whole network and can interrupt craft and send messages. (stronger)

[[Web Basics Questions]]
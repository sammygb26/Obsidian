What is the application layer and what kind of protocols run on it? #flashcard #CS #NetworkApplicationLayer
	In the network application layer we have different protocols like DNS, HTTP, HTTPS, FTP, SSH and so on. This all sits on TCP and UDP.

---
What are hosts with relation to URLs? #flashcard #CS #NetworkApplicationLayer 
	URLs are Uniform Resource Locators. This is a standardized way to request files and data. The host is a part of the URL which point to a server this request should be made to.

---
What is the form of host in a URL? #flashcard #CS #NetworkApplicationLayer 
	This is **subdomain.domain.topdomain**.

---
What are some URL security issues? #flashcard #CS #NetworkApplicationLayer 
	A major problem is people don't look at the URL carefully enough and once you own a higher level domain you can make up the lower level ones. This means a hacker could create the domain "facebook.network.com" if they owned network.com. The looks however like they own facebook.

---
What is the job of DNS? #flashcard #CS #NetworkApplicationLayer 
	**Domain Name System** is a way for domain names to resolve to IP addresses to be used in the transport layer. The reasons is that people can't remember IP addresses but they can remember domain names.

---
What is DNS? #flashcard #CS #NetworkApplicationLayer 
	The **Domain Name System** is an application layer protocol which allows domain names to be mapped to IP addresses. It is a distributed database that stores **resource records**.

---
What are the three types of records in DNS? #flashcard #CS #NetworkApplicationLayer 
	The three types of records are $A$ IP addresses associated with a host, $MS$ male server who you should main to and $NS$ name server who knows about domain names.

---
What is ICANN? #flashcard #CS #NetworkApplicationLayer 
	ICANN is a non-profit internet corporation that assigned names and number for DNS. It maintains servers that link to TLDs.

---
What are TLDs in DNS? #flashcard #CS #NetworkApplicationLayer 
	TLD are Top Level Domains. These are server for the last extension on the host part of a URL. You can register a website with these servers like for example one is .com so google will have registered google.com with them. Their server then points to the google server.

---
What are the two kinds of name resolution in DNS? #flashcard #CS #NetworkApplicationLayer 
	The two kinds are iterative resolution and recursive resolution.

---
How does interative name resolution work in DNS? #flashcard #CS #NetworkApplicationLayer 
	The idea here is our local machine successively asks different name servers who know where some host is. The name servers each point to the next server who knows the next step. But our computer must contact them all.

---
How does recursive name resolution work in DNS? #flashcard #CS #NetworkApplicationLayer 
	In recursive name resolution our PC only asks one name server for the host IP. This name server than itself contacts other name server who intern contact others until the host is found.

---
What happens in DNS caching? #flashcard #CS #NetworkApplicationLayer 
	In DNS caching each PC using DNS keeps a cache so it doesn't have to perform a DNS query for every single IP address. This ensure root and TLD servers aren't overloaded.

---
What privacy issues come from DNS caching? #flashcard #CS #NetworkApplicationLayer 
	This means if you are on the same machine as someone you can see what hosts they have visited.

---
What is the idea behind DNS cache poisoning? #flashcard #CS #NetworkApplicationLayer 
	In DNS cache poisoning we attempt to overwrite the cache entries so that some host name point to whatever IP address we want.

---
What security measures are in place within DNS to prevent cache poisoning? #flashcard #CS #NetworkApplicationLayer 
	Each DNS request has a 16-bit random request identifier which is sent in the response to identify it alone. Then we can also send the response to a random port. Known in advance by the requester.

---
How doe subdomain DNS cache poisoning (Kaminsky work)? #flashcard #CS #NetworkApplicationLayer 
	Here we somehow get the victim to request many subdomains from a local name server that don't exist. Then we spam the victim with responses to these requests with random return ports and request identifiers. There is about a 1 in a million chance of success but this can basically be brute forced and by change we will get the IP address we want into the cache.

---
What is DNSSEC? #flashcard #CS #NetworkApplicationLayer 
	This is a secure version of DNS with authentication for DNS answer origin, reply integrity, authenticated denial of existence. This is done via signed DNS replies at each step using asymmetric cryptography.

---
What is required for a DNS cache poisoning attack to be possible? #flashcard #CS #NetworkApplicationLayer 
	For this to be possible we need the query to have predictable identifiers and return ports. We need to respond quicker than the authoritative name server or we need the victim to accept unsolicited DNS records.

---
What are the refences against DNS cache poisoning? #flashcard #CS #NetworkApplicationLayer 
	We can 1) Add query randomization with the request identifier 2) Can add random return port. These each give $2^{32}$ possibilities.

---

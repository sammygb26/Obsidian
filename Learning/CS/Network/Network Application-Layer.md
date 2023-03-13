The **application layer** stays at the top. Here we will look at DNS. Things in this layer use UDP, TCP and the lower layers then add something. **DNS**, **HTTP**, **HTTPS**, **FTP**, **SSH** are all protocols on this layer.

![[Pasted image 20230130133933.png]]

# DNS
Uniform Resource Locators (URLs) are standardized formats for describing location and access methods for resources via the internet. The problem is IP addresses are hard to memorize and instead we learn the names in URLs (e.g. google.com).

![[Pasted image 20230130134002.png]]

##### Host
Is part of the URL. It can be broken up into **subdomain.domain.topdomain** the different layers allow different services. e.g. "profile.facebook.com".

##### URL Security
Often people can't tell where the URL is facing. People generally pick whichever one has the company name somewhere. So "facebook.evel.com" is owned by evel.com not facebook. It can be confusing and this opens the door to phishing.

### DNS Security
The DNS system resolves URLs to IP addresses. DoS attacks on these systems will take down the mapping and it takes many websites down. Without DNS servers you can still access the servers but you need to know the IP address.

In another case a DNS provider was phished and then the IP address was changed. This was done for the New York Times.

### How DNS Works
This is the **domain name system**. It is an application layer protocol mapping domain names to IP addresses. The mapping is many to many as long as some IP is found. Google for example maps to many IP addresses as they have many many servers for redundancy.

No one entity controls the recodes there is a distributed network of providers. There are different kinds of resource records.

- Addresses (A): record IP addresses associated with a host
- Male Server (MS) : who to main.
- Name Server (NS) : who knows about some domain.

We also have two or more labels seperated by dots. Top level domains like .com, .org. .net. There are also country codes .uk, .de, .it. There are also new top level domains .scot for example. 

**ICANN**: Non-profit internet corporation for assigned names and numbers. Keeps database of registered TLDs. Accredits registers for gTLDs.

There is in fact a tree of different domains. Starting with TLDs and going down.

![[Pasted image 20230130134212.png]]

##### Name Servers
A name server keeps a local database of DNS records, answers DNS queries and asks other name servers for records if they don't have some record. There are also authorities name server which stores reference version of DNS records for a zone (partial tree).

The records from the authorities server are usually cached so it doesn't have to be contracted all the time.

Roots servers are alterative for root TLDs and it is supervised by ICANN.

##### Name Resolution
A **resolver** is a program that retrieves DNS records form a name server. It connects to a name server (default rot or given). **dig** in Unix and lookup in windows will look up records for domains. These results are cached there are two ways to do this

- **Interactive Resolutions** - Name server refers client to autoreactive server which can answer request. Root servers are hard coded to allow TLDs to be found. We iterate down the layers until an A record is found.

![[Pasted image 20230130134357.png]]

- **Recursive Resolution** - Here the name server does the connection for us and find the IP for us. The name servers take the responsibility to resolve the request.

![[Pasted image 20230130134407.png]]

##### DNS caching
There would be too much network traffic if a path in the DNS tree would be traversed for each query. We set TTL to destroy records after. If we cannot find the request in the cache we then make the request.


In **interative** approach we keep a sequence of all the requests made and therefore we can check through the ones we have. Some servers are moving and therefore TTL may be small (this can also be done for attacks).

![[Pasted image 20230130134518.png]]

In a **recursive approach** the elements of the chain don't give recursion they just spit out the request

![[Pasted image 20230130134540.png]]

The **cache** is shared between all users for all DNS requests made. This can be inspected, there are some privacy issues as all domain name are logged.

### DNS Cache Poisoning
Here we give a DNS a false address records and get it cached. Mechanism: Queries issued over UDP on port 53. 16-bit **request identifier** in payload to match answers with queries. It has not **authentication**. Identifiers are send, to know what is being responded to. 

But this can be exploited if the identifier is **predictable** (incrementing number). If the attacker answers before authorities name server their we can overwrite the first answer. Some DNS server also ignore DNS requests.

BIND ATTACK?

##### Defence
We can randomize request identifier (16-bits). We can also use a random return port (16-bit).

We can also guess request ID addresses. If we have enough responses we may get lucky since there are only 32-bit.  

##### Subdomain DNS cache Poisoning
Here an attacker causes a victim to send many DNS requests for nonexistent subdomains some domain. Attacker sends victim forged NS response for requests. Format of forged responses to each request we get we send a request. We hope one of the responses we send will guess a correct number and we will poison the cache with the IP we want. Each response we force give us another identifier we could guess correctly to poison the cache. The spoof record points to attacker IP. 

![[Pasted image 20230130134626.png]]

This works best when you are close on a network as your responses will arrive first.

### DNSSEC
The goals of this protocol are authenticity of DNS answer origin, integrity of reply, authenticity of denial of existence. We have signed DNS replies at each step. Public-key cryptography. But this has slow deployment with root server since 2010.

Another option is DNS over HTTPS where the whole request is encrypted.

[[Network Application Layer Questions]]
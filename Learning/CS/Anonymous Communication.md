This is a new need other than *Confidentiatlity* and *integrity*. As context the internet is a public network where network traffic passes through devices other people control. This way part of your data is always public. Specifically the **routing information** in the IP layer. We cannot **encrypt everything** as the packets would be broken. We cannot encrypt the headers! 

The problem with headers being public is a lot of personal information is stored in the websites we visit.

![[Pasted image 20230217100633.png]]

This ca be used to **deanonymize datasets**. Websites can tell you where your IP address in the world.

![[Pasted image 20230217101119.png]]

In general IP you IP address is used as your ID. In general we are told if we are trying to hide something its already impossible.

## Anonymity

![[Pasted image 20230217101342.png]]

Where a **user's** identity is something that points to a physical person.

### Dinning Cryptographers (3DC)
Here 3 parties would like to anonymously communicate a bit of information. Either one of the three parties payed or the employer. 

##### 3DC Protocol
1. **Phase 1**: Each pair of cryptographers flips a coin (that only they can see). With heads =1 and tails = 0. Each cryptographer sees two coin flips.
2. **Phase 2**: Each participant publicly announces the result as follows
	- **Did NOT pay**: the XOR of the two coin flips they observed
	- **Did pay** the negation of the XOR of the two coins flips they observe
3. **Resolution**: If the XOR of the three announcers of the three announcers is
	- 0: employer prayed
	- 1: One of them paid

##### Superpose sending
This protcol can work for any number greater than 2 (it just doesn't make sense with 2). Sender want to anonymously broadcast a message $m$. For each bit $m_i$ of $m$.

1. Every pair of users generate a random bit (0,1)
2. Each user (except sender) announces (XOR of all n-1 observed bits)
3. the sender announces (XOR of all n-1 observed bits and $m_i$)
	- Every randomly generated but occurs in the sum twice and is cancelled by XOR bit $m_i$ occurs only once so isn't canceled out

##### Problems
This is impractical as it requires pair-wise shared secret keys (secure channels) between the participants (to share random bits). Require large amount of randomness and anyone can launch a denial of service attack and send the wrong but invalidating the whole transmission.

This is **information theory** anonymous.

### Crowds
The idea here is to randomly route the request trough a crowd of users. A crowd is a group of $m$ users; $c$ out of $m$ is corrupted. When we have a message we randomly send it to some user (initiator send to a random forwarder). 

![[Pasted image 20230217102552.png]]

A forwarder delivers the request directly to the server with a probability $1-p_f$ and goes to another forwarder with probability $p_f$. The response form the server is send via the same path back. The forwarders keep track of the messages they send. The network can be deanonymized via viewing the whole network and analyzing the time it takes for messages to move through the network.

### Chaum's Mix
This is a way to anonymize when we have an adversary who knows the entire network.

![[Pasted image 20230217103148.png]]

This is based on a special node called a mix. A mix takes in messages jumbles up the order (of the packets) and continues. This breaks the **timing connection** that can be used to deanonymize networks. The mixer waits for a given number of messages mixes them up in order then either sends them our randomly or sends them all out at once. We assume the pattern of bits going in and coming out looks different (this can be guaranteed by encryption). This is called **buffering**. We also **pad messages** so that the message size cannot be used to deanonymized messages. There are different kinds of mixes

1.  **Threshold mixes** - Wait until some amount is mixed then send out all messages. That is they only care about the number of messages in the queue. Nothing is sent out if there is nothing in the queue. We don't know the timing but we always know our $l$ messages are mixed together.
2. **Timing mixes** - Send out all messages at some time interval. The amount is not fixed only the time interval between the mix queue is released.
3. **Pooled mixes** - Send out all messages at some time interval if at least some number of messages are in the mix. If we have over a given amount we emit a fraction of our queue. We always have number of messages in the queue. We maintain a **pool**.

### Continuous Time Mix
This is a different time mix where the client chooses the timings of the messages. Here the **mix** has no input. Then this is kept secret so no one can understand the traffic.

If the delays are picked well (not constant or longer times). We should draw from a possibility distribution. We pick from a **memoryless** distribution like a poison or exponential distribution. This makes is very difficult for the adversary to guess the traffic of our client. We also must ensure the delay is long enough to allow mixing with other messages.

**Dummy messages** are are generated by the mixes themselves to prevent an attacker sending $n-1$ messages to a mix with a capacity $n$ allowing him to link the sender of the$n^{th}$ message with its recipient.

The encrypted data is send with an encrypted destination key (encrypted so only the mix ca read it). This way only the mix knows where the traffic is going. The output is the encrypted message. A global adversary knows $n$ packets went in $n$ went out but the messages are different (encryption) and the IP addresses are unknown.

Here the **anonymity set** is the size of the batch so with a size of $4$ then an adversary knows we sent our message with a probability $1/4$.

**Sender anonymity** - server doesn't know who send the message. But we can remove this by sending out IP address to a server.

##### Return Address
![[Pasted image 20230217104822.png]]

Here we send our encrypted IP address to only the server can read that and only the mix can reveal out IP address. We have to send a $K_2$ response key are our public key would deanonymize us.

### Mix Cascade
Here we don't trust any specific mix is malicious or honest. We route our messages through many different mixes. We hope there is a single honest mix. Then this system will work.

![[Pasted image 20230217105231.png]]

We have **nested encryptions** meaning each mix can pull back a layer of the encryption until the server is reached. Honest mix must apply *message padding*, *buffering* and *dummy messages*. This is vulnerable to a DoS attack but the messages are still safe.

### Limitations of Chaum's Mixnets
This is based on **asymmetric encryption** and so isn't efficient. **Dummy** message are also inefficient. **Buffering** is also very slow and makes these networks hard to use.

[[Anonymous Communication Questions]]
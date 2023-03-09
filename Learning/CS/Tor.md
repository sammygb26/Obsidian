This is a **low-latency** network that can only work against a local adversary (not a global adversary). *Layered* onion encryption is used to hid packets. All packets are the same size within the network. This is an **overlay network** where volunteers run Tor relays allowing messages to move through our machine.

![[Pasted image 20230227101441.png]]

We make layers of encryption. First with the guard. Then we make a deeper connection with another node in the network. Then a final layer with an exit node. Now we have a secure channel through the Tor network. We then use this connection to communicate with a network. Each node in the circuit removes a layer of encryption. As the packets exit the network is it unencrypted and can communicate with the client. We say local as if we could observe the entire network we could see the traffic going in and our of nodes allowing us to know which packets move between machines. This allows **end-to-end correlation** attack.

### End-to-End correlation

![[Pasted image 20230227102055.png]]

Here we match traffic patters from the start to the end. This way with two bad nodes timing attacks can occur. We can also use **crypto-tagging** where we exploit the malleability to write beneath the counters. This ways we can track traffic.

### Selective Dos
Here a malicious guard can remake a circuit when it detects that a circuit without a malicious node which it can then use EEC on.

![[Pasted image 20230227102522.png]]

### Website fingerprinting attack
With the packets the same size the timing of the packets can tell you what websites are being accesses.  This doesn't attack the tor network but just the fingerprint on the user's end.

![[Pasted image 20230227102629.png]]

Here the adversary uses to and make many confection to get a statistical fingerprint of different websites. **ML** can then be used to make a classifier that can classify the timing network,  this gives 90% accuracy. We then just observe the traffic to know what messages are being sent.

In general the feature used are *cumulative website size* and *direction of travel of packets*. But these are the targets that can be attackers to change how the network is functioning. Such as padding and timing on the website size. This allows websites who want to protect their client to do so.

**In the real world** - In the real world values get very low with many more classes. Then if traffic to websites are rare then we mostly get false positives due the the base rate falicy. These methods are also used on closed world models. But IRL there are many websites we will not have trained on that we don't know the look of an may be similar.

![[Pasted image 20230227103359.png]]

### Low Latency
Here End-to-end traffic correlation is difficult to avoid. Defence requires changing the shape of traffic patters. Attacks are not always successful and probabilistic and potentially difficult to actually pull of at internet scale.

# Internet Censorship
This is a dual to anonymous communication. If we can tell where someone is visiting a website we can censor the traffic. Hence anonymous communication prevents this if we don't want to just censor all traffic. Different **governments**, **corporations** and **service providers** are common censors. This prevents **publication** or **access** to content. We assume the rational actor doesn't want to block the entire internet.

![[Pasted image 20230227103844.png]]

Here websites which are not approved are blocked by the firewall. We could use a proxy which isn't blocked then allowing traffic to a website. This would then be blocked if the client is trying to access it.

### Common Censorship Resistance
##### No Single point of Failure
Here we public in many places so a adversary would need to take down many websites to stop your network. Here we can store multiple copies of content.  Se up in different jurisdictions, regions and operators. A problem is we require a lot of cooperation and redundant resources.

An example is *Tor bridges* which are not public but can still be used to access the Tor network. These must be found individually by the adversary.

##### Collateral Damage
Here we make it hard to split traffic that should and shouldn't be censored. So to censor the traffic this would harm much of the usual traffic.

We assume there is a desirable platform usage. Then we mix our traffic with that so it can't be distinguished. We then get this to the point the censor no longer sees it as worth it.

##### Do Not Look Suspicious
Here we hide traffic as normal traffic removing keywords and don't match the bad content.

We don't want to look random but we want to look like allowed usage. This could be achieved through **emulation** (where we try to work the same as usual traffic) or we **tunnel** (use the allowed application to embed our traffic). But this won't be good enough unless it is truly exact.

Here a TLS packet is labeled with an allowed domain. Then when it arrives it gets rerouted on arrival. But this doesn't work as well anymore are many providers don't provide this service any more.

##### Be Untraceable
Here we try to hid IP addresses this way the censor knows nothing to block.

An example is the **Tor Hidden Services** hidden .onion websites. Here we give the user a Rendezvous point. The user then says the **intro point** meet me at eh Rendezvous. Then both pass traffic through the Rendezvous.

![[Pasted image 20230227105422.png]]

[[Tor Questions]]

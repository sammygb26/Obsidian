# Information Theory
This covers topics like what information is, how we quantify it, measure it. What is *entropy*, *conditional entropy*. If we think about what information is we can define it as **facts learned**, **what is conveyed by a representation of an arrangement of sequence**, **the facts and figures that can be used by a computer program**, can think about what it is and how to measure it.

![[Pasted image 20220930151624.png]]

### Defining the amount of information
We will use probabilities to define the amount of information in an event $x$. We can start by defining the properties of some information function $I(x)$ that defines the information for some event $x$. We say $I$ is monotonically decreasing.

![[Pasted image 20220930151907.png]]

So rare events lead to a more information than common events. So if we are being more specific we have more information. We also say $I$ is additive in *independent events*.

![[Pasted image 20220930151958.png]]

That is if two events are independent the information gleamed from each individually is the same as both together. It doesn't matter what base we use; this gives us a choice of functions of the form $I(x)=\log(\frac1{p(x)})$. If we use base $2$ we measure in *bits* and base $e$ *nats*.

### Defining Similarity between two distributions
So we have two distributions $p_x(x)$ and $p_y(y)$ (defining histograms for example) we would like to know how similar or different they are. We can apply *Euclidian distance* but instead other terms can be used.

### History of Information Science
![[Pasted image 20220930152758.png]]

### Channel Coding
In this example we are sending information from  a **sender** to a **receiver**.  We want to use a minimal number of bits and we don't know any of the message before hand.

##### Sending coin flips
If we are sending a single coin flip we have two cases $p(H)$ and $p(T)$ both equal to $\frac12$ (we assume it is fare). Hence $I(x)=\log_2(p(H))=1$ and then if there are two coins $p(HH)=p(HT)=p(TH)=p(TT)=\frac14$ hence $I(x)=\log_2(4)=2$ again assuming a fair coin. So the number of bits is $\log_2(\frac1{p(x)})$. More common events need *less bits* and less common events need *more bits*.

If we are sending *ASCII* for example each letter has a representation with 8 bits. But this isn't efficient as the probability of each letter is different. So less bits should be used for the more common letters. This way less bits are used for the same encoding overall. We can also encode groups of letters that are more commonly together. That is the probability they are next to each other is higher so a more efficient encoding is possible.

### Entropy
Entropy is defined for a given distribution. We define the *entropy* of a distribution $p$ as

![[Pasted image 20220930154157.png]]

So it is the expected number of *bits* needed to send a message. A system with higher entropy will have more events with lower entropy.

![[Pasted image 20220930154258.png]]

$H(x)$ is **not** a function of $x$

##### Entropy of a coin
For different values of $u$ probability of getting a heads we can define the entropy for different values of $u$.

![[Pasted image 20220930154731.png]]

In the case $u=1$ or $u=0$ then we already know the outcomes and there is not entropy. In general the *entropy* of a distribution is higher when the distribution is closer to uniform. **Entropy** can be seen as a measure of uncertainty.

##### Conditional Entropy
We can also define the conditional entropy of some $x$ given $y$ we define this as: 

![[Pasted image 20220930154930.png]]

If $x$ and $y$ are independent then

![[Pasted image 20220930154954.png]]

This also leads to the fact that *conditional entropy* is always smaller than or equal to unconditional entropy. So $H(x|y)\le H(x)$.

![[Pasted image 20220930155103.png]]

Proof:

![[Pasted image 20220930155123.png]]

### Mutual Information
Since $H(x|y)\le H(x)$ the **extra** information $H(x)-H(x|y)$ we know about $x$ given $y$ is called the mutual information. The overlap in information we know.

![[Pasted image 20220930155245.png]]

### Cross Entropy
We say the entropy is $E_{x\sim p(x)}=[-\log p(x)]$ can be interpreted as a drawing a message $x$ from $p(x)$ and sending it with $-\log p(x)$ nats. This assumes we know $p$ but what if we do not. We instead estimate with some other distribution $q$. Then the *expected* number of nats (under $p$) with distribution $q$ is the cross entropy (distribution mismatch):

![[Pasted image 20220930155535.png]]

We need more nats if we encode messages with $q$ other than the true distribution $p$.

![[Pasted image 20220930155619.png]]

Proof:

![[Pasted image 20220930155707.png]]

### Kullback-Leibler divergence
The **extra** nats of encoding with the wrong distribution is the **Kullback-Leibler** divergence:

![[Pasted image 20220930155812.png]]

We know $KL(p||q)\le 0$ and if $p=q$ then $KL(p||q)=0$. This is often used as a measure of distance between two distributions but $KL(p||q)\ne KL(q||p)$. We can however take the average instead.

### Cross Entropy and log Loss
In multiclass classification we have:

![[Pasted image 20220930160121.png]]

The *log loss* will be:

![[Pasted image 20220930160216.png]]

where $y^*$ is the label. We can describe the cross entropy between the ground truth and learned distribution as 

![[Pasted image 20220930160309.png]]

Which we can minimize as a loss.


This was the same method used in [[Gaussian Mixture Models]]. As we continue to maximize our target for optimization gets further away. Instead of **gaussian** here the method will focus in general on a **latent variable model**.

### Abstract
We will use a new set of variables $X$ and $Z$. $X$ capture all observed data variables, $Z$ capture all unsee/hiddens/latent/unobserved variables. Then we want to capture a joint probability model parameterized by $\theta\in\Theta$. $$p(X,Z|\theta)$$ Together $X$ and $Y$ gives **all data** seen and unseen. In a general sense we are trying to maximize our *log likelihood*. But it may be hard to just maximize $X$ instead we want to include $Z$ to make the maths possible. So we maximize with $Z$ instead of without.

![[Pasted image 20221107151946.png]]

##### Jensen's  [[Gaussian Mixture Models]]
![[Pasted image 20221107152121.png]]

##### Kullback-Leibler Divergence  [[Information Theory]]
The second formula is what will be used later.
![[Pasted image 20221107152220.png]]

### Motivation
We know its hard to maximize with $X$ on it's own instead we will use the second formula including $Z$.

![[Pasted image 20221107152414.png]]

### Formulation
Let $q(X)$ be a discrete probability function on $Z$, that is 

![[Pasted image 20221107152449.png]]

We consider a probability $q(Z)$ where all $Z$ variables have a labeled probability (same step takin in [[Gaussian Mixture Models]] with $\gamma$). Then we get

![[Pasted image 20221107152607.png]]

we have a log of a sum here so we use **Jensen's inequality**. To give

![[Pasted image 20221107152706.png]]

##### Understanding why it works
We all this $\mathcal L(q,\theta)$. We want to visualize how these $\mathcal L$ parts work in terms of our parameter space to understand what we are doing when we optimize with it. This is as we control $q$ and $\theta$. The distribution $q$ we use will depend on this.

![[Pasted image 20221107153130.png]]

They will all be lower bounds of $\log p(X,\theta)$ but we need to pick the right $q$ and $\theta$ to maximize. When $q(Z)$ is a discrete probability function on $Z$ we say:

![[Pasted image 20221107153612.png]]

$\log p(X|\theta)$ is the evidence and $\mathcal L(q,\theta)$ is the Evidence Lower BOund (ELBO). In EM we maximize the ELBO with respect to $q$ and $\theta$.

![[Pasted image 20221107153723.png]]

So we take a function find it's maximum (which we know is $\le$ evidence). 

![[Pasted image 20221107153813.png]]

So we take a new $\theta$ to maximize $\mathcal L$

We can write our $\mathcal L$ out as follow

![[Pasted image 20221107153852.png]]

We can rewrite this as

![[Pasted image 20221107153935.png]]

![[Pasted image 20221107154002.png]]

This can be rewritten using the KL divergence as

![[Pasted image 20221107154027.png]]

Giving a formula for our $\log p(X|\theta)$ as

![[Pasted image 20221107154100.png]]

![[Pasted image 20221107154459.png]]

Hence to find $q$ we minimize KL (that is $p=q$). This will not change $\log p(X|\theta)$ at all hence it must increase $\mathcal L$.

![[Pasted image 20221107154646.png]]

### Formulation of EM
This gives the steps 

1. Choose an initial $\theta^{old}$
2. **Expectation Step**. Let $q^*(Z)=p(Z|X,\theta^{old})$ giving the best lower bound at $\theta^{old}$
![[Pasted image 20221107154802.png]]
3. **Maximization Step**
![[Pasted image 20221107154825.png]]

[[Expectation Maximization Questions]]

Is there a situation where maximizing $\theta$ will cause setting $p=q$ to lower $\mathcal L$ to below where it started?

Might minimizing KL divergence increase $\mathcal L$?
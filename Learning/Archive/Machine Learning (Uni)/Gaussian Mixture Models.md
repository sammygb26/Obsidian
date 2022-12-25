In [[K means]] we represent each cluster with a mean and then each point is in one cluster. This can be seen as too crude as it assumes each cluster can be represented by a single point. We replace $r_{nk}$ with a more relaxed non-binary number and if fact we will take this to be a *probability*. We want to cluster data form various types and shapes.

![[Pasted image 20221104151748.png]]

### Mixture Models

![[Pasted image 20221104152235.png]]

These are models that can cluster data of various types and **shapes**. Data points with simple *mixture models* can be from any distribution. This is similar to [[K means]] but is a richer representation.

##### Generative Process
We assume we want to generate the data above with two gaussians. For data $x_n$ select one of the gaussians with probability $\pi_k$, assuming $\sum_k\pi_k=1$. Se the parameter $z_{nk}=1$

![[Pasted image 20221104152506.png]]

That is the probability $x_n$ is in $z_{nk}$ given $\mu_k$ and $\Sigma_k$. But of course we can't just generate form one cluster. Instead we need to generate cluster from multiple datapoints where the probability we pick a point from each datapoint. So we generate a datapoint $\mathcal N(\mu_k, \Sigma_k)$ with a probability $\pi_k$.

This describes how we can reproduce a dataset with a generative process. But we need to calculate $\mu_k$ and $\Sigma_k$ from the observed data as well as how to generate the points from $\mathcal N(\mu_k,\Sigma_k)$. Hence giving $z_{nk}$ but we need $\mu_k$ and $\Sigma_k$ to get this hence we need to break the loop.

### Mixture of Gaussians
Complex probabilities can be approximated with linear superposition of $K$ gaussian densities. Hence we define $p(x)$ as 

![[Pasted image 20221104153256.png]]

We define $\mathbf z=\{z_1,z_2,\dots,z_k\}$ where $z_k\in\{0,1\}$ and $\sum_kz_k=1$. We als know that $p(x,z)=p(z)p(x|z)$ and $p(x)=\sum_zp(x)p(x|z)$.

![[Pasted image 20221104153512.png]]

Another quantity is $p(z|x)$

![[Pasted image 20221104153541.png]]

$\gamma(z_k)$ is the *responsibility* that component $k$ takes in explaining the observation $x$.
 
### Maximum Likelihood solution to GMM
Suppose we observe $X_{N\times D}=\{x_1,x_2,\dots x_N\}$. Assuming that the data pints are drawn independently the likelihood function of all $N$ datapoints is 

![[Pasted image 20221104153951.png]]

and so the log-likelihood will be

![[Pasted image 20221104154008.png]]

We can estimate $\pi_k$, $\mu_k$ and $\Sigma_k$ by differentiating $L$ with respect to these variables and using gradient-based optimization. But the sum in the $\log$ is a problem and can cause problem.

### Expectation Maximization
The EM method can be used to overcome challenges of using Maximum Likelihood. EM derives a lower bound $B$ on the likelihood $L$ such that $B<L$. Instead of maximizing $L$ directly EM maximizes $B$. But how would be determine $B$? Using Jensen's inequality

$$\log \mathbb E_{p(z)}[f(z)]\ge\mathbb E_{p(z)}[\log f(z)]$$

That is if we switch the log and expectation our value gets smaller.

We define $\gamma_{nk}$ to be positive and satisfying $\sum_{k=1}^K\gamma_{nk}=1$. Where $\gamma_{nk}$ is some probability distribution over $K$ components for the $n$-th data point

![[Pasted image 20221104154617.png]]

Where the expectation comes from the fact we are summing over a distribution with a probability. So we then apply **Jensen's inequality**

![[Pasted image 20221104154724.png]]

To finally get $B$ in the form

![[Pasted image 20221104154740.png]]


EM is an iterative process, maximizing the bound $B$ until convergence. For each update we take the partial derivative of the bound $B$ with respect to parameters set it to 0 and solve. This gives the two steps

![[Pasted image 20221104154853.png]]

The E-step is called such as we are updating the expectation. The M-step is the maximization step where we update $\pi_k$, $\mu_k$ and $\Sigma_k$. We can replace the parameter's with those of **any** distribution.

### Choosing the number of Components $K$ for GMMs
If we increase the number of components the likelihood goes to infinity as the likelihood becomes infinite.

![[Pasted image 20221104155258.png]]

[[Gaussian Mixture Models Questions]]
# Probability
We define a probability measure $\mathcal P$ in two cases.

### Discrete probability
Here we start with some set of events $\Omega$. Any subset of $\Omega$, $X$ is called and **event**. The probability measure is a function defining a mapping between these *events* and real numbers. That is the type of this function is $\mathcal P:2^\Omega\to \textbf R$ ($2^\Omega$ is the powerset of $\Omega$).  This function has three properties.

1. $0\le\mathcal P\le 1$ for any $X\subseteq \Omega$ 
2. $\mathcal P(\Omega)=1$ 
3. $\mathcal P(X\cup Y)=\mathcal P(X)+\mathcal P(Y)$ if $X\cap Y = \emptyset$  

We can also define a function $p$ that takes the elements of $\Omega$ to real vales. That is its type is $p:\Omega\to\textbf R$. We call this function the **probability mass function** (or *discrete probability function*) and it has the property that $$\mathcal P(X)=\sum_{\omega\in X}p(\omega)$$
##### Set Comprehensions
We can define event by qualifiers on $\omega$ for examples $$\mathcal P(\omega=3)=\mathcal P(\{\omega:\omega=3\})$$$$\mathcal P(w>3)=\mathcal P(\{w:w>3\})$$
### Continuous Probability Distribution
We define a $F$ a **cumulative distribution function** with the properties. 

1. $F:\textbf R\to[0,1]$ 
2. $F$ is monotonic, i.e., $F(X)<F(y)$ if $x<y$
3. $\lim_{x\to\infty}F(x)=1$ and $\lim_{x\to -\infty}F(x)=0$  

We define a **probability density function** $p$ as $p(u)=\frac{dF}{dx}(u)$ or $F(x)=\int_{-\infty}^xp(u)du$. Then we construct a *probability measure* $\mathcal P$ as $$\mathcal P(a<X<b)=\int_a^bp(u)du=F(b)-F(a)$$Hence if $\Omega=\textbf R$ then $\mathcal P:2^\Omega\to\textbf R$ takes a subset of $\textbf R$ as input.

##### Gaussian Distribution
Also known as a normal distribution is defined by the *probability density function*. $$p(x)=\frac1{\sqrt{2\pi\sigma^2}}\exp\left(-\frac1{2\sigma^2}(x-\mu)^2\right)$$This has the symbol $\mathcal N$ 

##### Sampling notation
We say $a$ is drawn from a Gaussian/normal distribution if $a\sim\mathcal N(\mu,\sigma^2)$. Just means $p(a)$ is defined as above for $a$.

##### Expectation
We define $$\textbf E[x]=\int_{-\infty}^\infty xp(x)dx\hspace{10pt} \textbf E[x]=\sum_{x\in\Omega}xp(x)$$

##### Low Of The Unicorn Statistician
$$E_{x\sim p(x)}[f(x)]=\int_{-\infty}^\infty f(x)p(x)dx$$
or when we have discrete probability$$E_{x\sim p(x)}[f(x)]=\sum_{x\in\Omega}f(x)p(x)$$
### Variables Notation
The *probability density* and *probability mass* functions aren't defined by their names as with a function $f(x)$ for example. But they are instead defined with the name of their variables. Hence $p(a)$, $p(b)$ and $p(c)$ are all different function defined on different variables. Then something like $p(a=x)$ and $p(b=x)$ is the probability density when $a=x$ or when $b=x$. This can also be written as $p_a(x)$

This matching principle can also be extended to more complex equation as with conditional probability.

![[Pasted image 20220926123417.png]]

or **bayes rule**

![[Pasted image 20220926123502.png]]

### Independence
We say some random variables are independent if $$p(x,y)=p(x)p(y)$$ for any $x\in \Omega_x$ and $y\in\Omega_y$. By this above definition we get $$p(y|x)=\frac{p(x,y)}{p(x)}=\frac{p(x)p(y)}{p(x)}=p(y)$$ 
### Independence of Expectation
We say $E[cx]=cE[x]$ as a simple rule. Then if $x$ and $y$ are independent. $E[x+y]=E[x]+E[y]$ and $E[xy]=E[x]+E[y]$.

### Random Variables
We will say a variable is random is it is associated with a probability distribution.

There are rules for combining random variables. For example if we have $x\sim\mathcal N(\mu_,\sigma_1^2)$ and $y\sim\mathcal(\mu_2,\sigma_2^2)$ then we have $$x+y\sim\mathcal N\left(\mu_1+\mu_2,\sigma_2^2+\sigma_2^2\right)$$Or another one that is more complex is if $u_1\sim U(0,1)$ and $u_2\sim U(0,1)$ then $$z_1=\sqrt{-2\log u_1}\cos(2\pi u_2)\sim\mathcal N(0,1)$$$$z_1=\sqrt{-2\log u_1}\sin(2\pi u_2)\sim\mathcal N(0,1)$$    

### Moment-generating functions
We define the moment generating function for some RV $x$ as $$M_x(t)=E[e^{tx}]=\int_{-\infty}^\infty e^{tx}p(x)dx$$But this equally means that $$M_x(t)=E\left[1+\frac t{1!}x+\frac{t^2}{2!}x^2+...\right]=1+\frac{t}{1!}E[x]+\frac{t^2}{2!}E[x^2]+..$$ Hence when we differentiate this function repeatedly and set $x=0$ we get $M'_x(0)=E[x]$ and $M''_x(0)=E[x^2]$, ...

This all comes to mean if $M_x(t)=M_y(t)$ then $x$ and $y$ have the same distribution.

### Linear Combination of Gaussians
We can prove that if $x\sim\mathcal N(\mu,\sigma^2)$ then $M_x(t)=E[e^{tx}]=e^{\mu t+t^2\sigma^2/2}$. This allows us the prove the that the linear combination of two gaussians $x_1\sim\mathcal N(\mu_1+\sigma_1^2)$ and $x_2\sim\mathcal N(\mu_2,\sigma_2^2)$ is $$a_1x_1+a_2x_2\sim\mathcal N(a_1\mu_1+a_2\mu_2,a_1^2\sigma_1^2+a_2^2\sigma_2^2)$$ This is true as

![[Pasted image 20220926130934.png]]

### Independent and Identically Distributed
We sat $x_1, x_2 ... x_n$ are independent and identically distributed if all have the same distribution and are mutually independent.

### Maximum Likelihood
If if we have some outcome say we flip a count 500 times and we get 300 heads. We know all flips are IID  then we want the probability of getting a hood to maximize the likelihood we got 300 out of 500. Hence maximize $$p(x_1,x_2,...x_n)=p(x_1)p(x_2)...p(x_n)=\prod_{i=1}^np(x_i)=\prod_{i=1}^n\beta^{X_i}(1-\beta)^{1-x_i}$$For a probability $\beta$ of getting a head. We can take the log of this and then differentiate to find the minimum hence where $\beta$ maximizes likelihood. Coming out to be $$\beta=\frac1n\sum_{i=1}^nx_i$$We can take the log as it is *monotonically increasing* and this doesn't change the argmax value which we are looking for.

[[Probability Questions]]
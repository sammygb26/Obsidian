# Linear Regression
For higher dimensions we will use a vector of weights instead of the standard weights. $S$ is called the **dataset** and is made out of pairs of input features to output values. We say $X$ is a array of all the *input features*. $y$ is the *ground truth* relating to these $X$s. $f(x)=w^Tx+b$ defines the plane we are trying to find with a vector $w$ of *weights*. We take a measure that minimizes some function $\mathcal L$. Defined on the dataset and values $w$ and $b$.

![[Pasted image 20220926152912.png]]

To minimize $b$ we can take the derivative with respect to $b$.

![[Pasted image 20220926153002.png]]

Once this is set to 0 we can get $b$ (assuming $L$ is minimal as a stationary point of $b$)

![[Pasted image 20220926153237.png]]

Giving $b=\bar y-w^T\bar x$ once we convert the summations averages. We now differentiate with respect to $w$ producing the following.

![[Pasted image 20220926153522.png]]

The sums can be broken up into matrix form then finally simplified using $X$ and $y$.

![[Pasted image 20220926153736.png]]

This finally gives $w$ as $$w=(XX^T)^{-1}Xy$$

### Features
We are fitting the plane $y=w^Tx+b$ but we can simplify this by appending a 1 onto all the features and then we can bring $b$ in. But we don't have to be stopped by just adding 1s. We can also add features defined on the data like for example polynomials on the data. We can fit it the same as before but we get a non-linear function defined (not just a plane).  We are still only performing linear regression however as our output is linear in these functions on the feature. For example we could fit a $\sin$ curve by adding this feature. But we would only be including a scaled version i.e. $w\sin(x)$ and not $\sin(wx)$ which would no longer be linear regression.

We can sum this all up with the model $f(x)=w^T\phi(x)$ where the function $\phi$ gives a vector of features.

### Probabilistic Interpretation
We cannot fit even data that strongly fits a line to a line it could be randomness causing this. We can assume it is gaussian for instance. So we can fit a line as before and add some $\epsilon_i\sim\mathcal N(0,1)$. That is we are saying $$y_i=w^T\phi(x_i)+\epsilon_i$$This comes to mean that $y_i\sim\mathcal N(w^T\phi(x_i), 1)$ so we are basically adding a variance of $1$ to $y_i$ values. Now we can express the likelihood of the ground truth $y$ values given $w$, if we take the $\log$ of this we get. $$\log\prod_{i=1}^N\frac1{\sqrt{2\pi}}\exp\left(-\frac12(y_i-w^T\phi(x_i))^2\right)$$Becoming the following sum $$\sum_{i=1}^N\left[-\frac12\log(2\pi)-\frac12(y_i-w^T\phi(x_i))^2\right]$$ With the principle of *maximum likelihood* applied over $w$ we will tiring to maximize this. We can remove constants as the maximum will be the same. And we can remove scaling by a constant factor as this equally will not change the max. This gives $$\frac1N\sum_{i=1}^N(y_i-w^T\phi(x_i))^2$$Which is **mean squared error**. That is assuming gaussian error on our results leads to a gaussian loss when 

### Linear Regression
The complexity of computing the solution for $w$ that is $(XX^T)^{-1}Xy$ is $O(N^3)$ where $N$ is the number of samples. Hence this doesn't work for *large* datasets. Instead approximation techniques can be used to simplify this.

### Matrix Calculus Linear Regression
We can create an analog of $X$ as $\Phi$ where $\Phi$ is a matrix of features that is $\Phi=\phi(X)$.  With this we can solve for the weight matrix in one go. In this form the loss can be expressed as $$L=||\Phi^Tw-y||_2^2$$This can be expanded and rewritten as follows.

![[Pasted image 20220927153850.png]]

We can then differentiate with respect to $w$ and get the following

![[Pasted image 20220927153920.png]]

[[Linear Regression Questions]]
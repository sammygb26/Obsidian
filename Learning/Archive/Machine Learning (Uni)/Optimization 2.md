# Optimization 2
We can take the example of *log loss*:

![[Pasted image 20221007151130.png]]

We can take the gradient of this with respect to $w$ but then we cannot find a single solution. We may want instead of trying to find a optimal solution instead find an approximate solution.

### Approximate Solutions
We say that $\hat x$ is an **approximate solution** if for a given $\epsilon>0$

![[Pasted image 20221007151319.png]]

We want it to be close in *function value* not the actual value distance $\hat x-x^*$.

### Gradient descent
This is an integrative algorithm consisting of the steps $$w_{t+1}=w_t-\eta_t\nabla L(w_t)$$The variable $\eta_t>0$ is called the step size and can depend on $t$. The slop of the tangent at the point $w_t$ will be $\nabla L(w_t)$. Hence we use this to choose what direction to go in. We need to pick the right $\eta_t$ in order to find a good solution as too small or too big will give suboptimal solutions. $\eta_t$ will *depend on $t$* that is the step size can depend on the number of steps we want to converge within.

##### Approximate Solutions for Iterative Algorithms
An iterative algorithm creates a sequence $x1,...,x_t$. We need to trade between $t$ and $\epsilon$. For very good solutions we  a large value of $t$. We would like to know how many $t$s we need to get within $\epsilon$. That is to **know** that $$f(x_t)-f(x^*)<\epsilon$$Hence to do this we want $\epsilon$ as a function of $t$.

There are many results we could get for example:

![[Pasted image 20221010123607.png]]

*Sublinear* is the usual case however **linear** and **quadratic** are also cases. We also write the order of these with respect to $\epsilon$ or $t$. That is how $t$ grows with respect to epsilon or $\epsilon$ grows with respect to $t$.

### Implications of Smoothness
Smoothness in $L$ we say the gradient doesn't change much with respect to any change in the $x$ values. This can be written in two ways (see above). If we have $x_{t-1}-x_t=\eta_t\nabla f(x_t)$

![[Pasted image 20221007152834.png]]

If we choose the right $\eta_t$ we are guaranteed to make a certain amount of progress dependent on $||\nabla f(x_{t-1})||_2^2$. 

![[Pasted image 20221007153159.png]]

### Implications of Strong Convexity
We say something is $\mu$ strongly convex if (lower bounded by a parabola):

![[Pasted image 20221007153238.png]]

Since we have a lower bound that is a parabola $R$. We can take a derivative with respect to it  and find its lowest point. That for every point we can define $R$ and then solve it to get a value that is less than every other $x$ value and hence also $x^*$. This allows us to create an upper bound how how far out $f$ value is form the optimal value.

For we find $R$ as $$R(x)=f(y)+(x-y)^T\nabla f(y)+\frac\mu2||x-y||^2$$Then we find it's derivative $\frac{\delta R}{\delta x}$ and se it to $0$ to find the optimal $x$ for $R$ relative to $y$. As $$x=y-\frac1\mu\nabla f(y)$$We can the plug this back into $y$ to find the optimal value of $R$ for any $y$ as $$\min_x R(x)=f(y)-\frac1{2\mu}||\nabla f(y)||_2^2$$Then we know $R$ is a lower bound for $f$ hence it's minimizer is $\le$ the minimum of $f$ ($f(x^*)$) so we know $$f(x^*)\le f(y)-\frac1{2\mu}||\nabla f(y)||_2^2$$Hence finally we can get $$f(y)-f(x^*)\le \frac1{2\mu}||\nabla f(y)||_2^2$$So given the derivative for any $y$ we can define an upper bound on how far its value is from the optimal solution.

### Guarantee of Gradient Descent
We start with a function that is both $\mu$-**strongly convex** and $L$-*smooth*. That is we have the conditions: $$f(x)\le f(y)+(x-y)^T\nabla f(y)+L||x-y||^2.\forall x, y\in \mathbb R^d$$and $$f(x)\ge f(y)+(x-y)^T\nabla f(y)+\frac\mu2||x-y||^2.\forall x, y\in\mathbb R^d$$Now we are looking at gradient descent so we will look at $x_t$ and $x_{t-1}$, we can take the first $L$-*smooth condition* to the following (using the fact that $x_{t-1}=x_t-\eta_t\nabla f(x_t)$): $$f(x_t)\le f(x_{t-1})-\eta_t(1-L\eta_t)||\nabla f(x_{t-1})||_2^2$$then we can differentiate $\eta_t(1-L\eta_t)$ to find that it is maximized when $\eta_t=\frac1{2L}$. Then for this value we also have $0\le1-L\eta_t\le1$ hence we can say:$$f(x_t)\le f(x_{t-1})-\eta_t||\nabla f(x_{t-1})||_2^2=f(x_{t-1})-\frac1{2L}||\nabla f(x_{t-1})||_2^2$$now at this point we can add $-f(x^\star)$ to both sides giving: $$f(x_t)-f(x^\star)\le f(x_{t-1})-f(x^\star)-\frac1{2L}||\nabla f(x_{t-1})||_2^2$$But we know from **strong convexity** that $$\forall x.  f(x)-f(x^\star)\le\frac1{2\mu}||\nabla f(x)||_2^2$$Which can be written another way as $$-\frac1{2\mu}||\nabla f(x)||_2^2\le f(x^\star)-f(x)$$We can combine this with the final part of the equation above to give us: $$-\frac1{2L}||\nabla f(x_{t-1})||_2^2=\frac\mu L\left(-\frac1{2\mu}||\nabla f(x_{t-1})||_2^2\right)$$Which can be worked into the equation original equation from the $L$-*smooth condition* to give:  $$f(x_t)-f(x^\star)\le f(x_{t-1})-f(x^\star)-\frac1{2L}||\nabla f(x_{t-1})||_2^2$$$$=f(x_{t-1})-f(x^\star)+\frac\mu L\left(-\frac1{2\mu}||\nabla f(x_{t-1})||_2^2\right)$$$$\le f(x_{t-1})-f(x^\star)+\frac\mu L\left(f(x^\star)-f(x_{t-1})\right)$$Finally rearranging the terms we find $$f(x_t)-f(x^\star)\le\left(1-\frac\mu L\right)(f(x_{t-1})-f(x^\star))$$That is with $\mu$-strong convexity and $L$-smoothness with each iteration of gradient descent (with $\eta_t=\frac1{2L}$) the distance of or approximate solution to our minima reduces by the fraction $(1-\frac\mu L)$ each iteration. Hence we can roll this out to find that given and initial value $x_0$ we have $$f(x_t)-f(x^\star)\le\left(1-\frac\mu L\right)^t\left(f(x_0)-f(x^\star)\right)$$In other words the **convergence is linear**.

### Log Loss
We can look at log loss again:

![[Pasted image 20221007154816.png]]

Then we can take the gradient with respect to $w$ to give

![[Pasted image 20221007154838.png]]

Then this function is all we need to update an approximate solution .

### Size of Data set
We know for MSE we can get a solution setting the derivative to 0 getting $\Phi\Phi^T)^{-1}\Phi y$. But this take $O(N^3)$. But gradient descent on log loss take $O(N)$ so can still be costly as we may need to do it many times. We instead use **stochastic gradient descent**. 

We sample $x_t$ and $y_t$ from a data set $S$. We can take the gradient and update $w$. Then we go until the solution is satisfactory. We can also talk about the gradient a a random variable as it now depends on our sample.

![[Pasted image 20221007155342.png]]

![[Pasted image 20221007155451.png]]

### Sub gradient
A sub gradient at $x$ is a vector $g$ that satisfies:

![[Pasted image 20221007155827.png]]

That is $g$ is some gradient which if we create a tangent with it will not go past the function.

[[Optimization 2 Questions]]
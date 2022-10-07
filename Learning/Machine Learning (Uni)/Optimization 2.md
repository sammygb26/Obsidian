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

![[Pasted image 20221007152211.png]]

*Sublinear* is the usual case however **linear** and **quadratic** are also cases. We also write the order of these with respect to $\epsilon$ or $t$. That is how $t$ grows with respect to epsilon or $\epsilon$ grows with respect to $t$.

### Implications of Smoothness
Smoothness in $L$ we say the gradient doesn't change much with respect to any change in the $x$ values. This can be written in two ways (see above). If we have $x_{t-1}-x_t=\eta_t\nabla f(x_t)$

![[Pasted image 20221007152834.png]]

If we choose the right $\eta_t$ we are guaranteed to make a certain amount of progress dependent on $||\nabla f(x_{t-1})||_2^2$. 

![[Pasted image 20221007153159.png]]

### Implications of Strong Convexity
We say something is $\mu$ strongly convex if (lower bounded by a parabola):

![[Pasted image 20221007153238.png]]

Since we have a lower bound that is a parabola. We can take a derivative with respect to it  and find its lowest point.

![[Pasted image 20221007153509.png]]

We plug the solution for the derivative back in.

### Guarantee of Gradient Descent
![[Pasted image 20221007154518.png]]

### Log Loss
We can look at log loss again:

![[Pasted image 20221007154816.png]]

Then we can take the gradient with respect to $w$ to give

![[Pasted image 20221007154838.png]]

### Size of Data set
We know for MSE we can get a solution setting the derivative to 0 getting $\Phi\Phi^T)^{-1}\Phi y$. But this take $O(N^3)$. But gradient descent on log loss take $O(N)$ so can still be costly as we may need to do it many times. We instead use **stochastic gradient descent**. 

We sample $x_t$ and $y_t$ from a data set $S$. We can take the gradient and update $w$. Then we go until the solution is satisfactory. We can also talk about the gradient a a random variable as it now depends on our sample.

![[Pasted image 20221007155342.png]]

![[Pasted image 20221007155451.png]]

### Sub gradient
A sub gradient at $x$ is a vector $g$ that satisfies:

![[Pasted image 20221007155827.png]]

That is $g$ is some gradient which if we create a tangent with it will not go past the function.
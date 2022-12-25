# Optimization
We can take a basic example using mean-squared error. We know that if 

![[Pasted image 20221006151144.png]]

then if we set $\frac{\delta L}{\delta w}=0$ we get

![[Pasted image 20221006151235.png]]

But for log loss:

![[Pasted image 20221006151252.png]]

We cannot solve setting the derivative to 0 for a singular solution. Instead we need to **optimize**. We want to se the idea of what a gradient it to find minimizing value.

![[Pasted image 20221006151422.png]]

We have some $f:\textbf R^d\to \textbf R$ and we want to find $\underset{x}\min f(x)$. We want to find a value for $x$ such that all other values of $f$ are larger.  We say $x^*$ is the **optimal solution** or *minimizer*. There my be one or many or none there is no way to know. However we will not  worry about finding more than one.

A function $f$ is **convex** if 

![[Pasted image 20221006151820.png]]

for every $x$, $y$ and $0\le \alpha\le 1$. The terms in the form $\alpha a+(1-\alpha) b$ is an interpolation between $a$ and $b$. Hence the above formula means a straight line interpolation between two values of $f$ (right) is always greater or equal to the function value if we interpolated and then passed through the $f$.

![[Pasted image 20221006152151.png]]

##### Properties
If $f$ is convex, then

![[Pasted image 20221006152257.png]]

for any $x$ and $y$.

![[Pasted image 20221006152316.png]]
(tutorial 1 ahh)

This means that if go along the tangent by the amount between $x$ and $y$  from $x$  we are always smaller than the true value of the function.

Then we want to find is **MSE** is convex in $w$.

![[Pasted image 20221006153136.png]]

##### Convexity of squared distance
We know some $\mathcal l(s)=(s-s')^2$ is convex in $s$ as 

![[Pasted image 20221006153329.png]]

##### Affine transform preserves convexity
Then we also know if $f$ is convex then $g(x)=f(Ax+b)$ is also convex. Which has a simple proof.

![[Pasted image 20221006153438.png]]

##### Nonnegative weighted sum of convex function
As above we can prove

![[Pasted image 20221006154021.png]]

##### Convexity of MSE
We know that a squared difference in convex and a weighted sum preserves this and an affine transform preserves this:

![[Pasted image 20221006154153.png]]
Hence MSE is convex.

### Optimality Condition
If $f$ is convex and $$\Delta f(x^*)=0$$at $x^*$ then $x^*$ is the minimizer of $f$.

![[Pasted image 20221006154340.png]]

In the case the function isn't convex then this gradient being 0 doesn't mean much.

![[Pasted image 20221006154517.png]]

### Convexity of log loss
Log loss in the binary case is:

![[Pasted image 20221006154549.png]]

We know $-y_iw^T\phi(x_i)$ is convex and the sum of these $\log(1+z)$ is convex if $\log(1+z)$ is. To prove this we can take the derivative and then take the second order derivative. We will then show this is positive:

![[Pasted image 20221006154802.png]]

Hence we know the *log loss* is a convex function.

### Strong Convexity
A function $f$ is $\mu$-strongly convex if

![[Pasted image 20221006155135.png]]

for any $x$ and $y$. That is $f(y)$ is greater than the intersected section from the tangent at $x$ by some quadratic amount based on the distance between $x$ and $y$. Every point on the function is **bound bellow** by a parabola.

### Lipschitz continuous
A function is $L$-Lipschitz if

![[Pasted image 20221006155511.png]]

for any $x$ and $y$. That is the change is $f$ is always smaller than the change in the inputs values times some $L$. Hence for a $x$ close to $x^*$ we know the values aren't far.

### Smoothness
When the gradient of $f$ is $L$-Lipschitz, then we say $f$ is $L$-smooth. Hence $f$ is $L$-smooth if

![[Pasted image 20221006155922.png]]

for any $x$ and $y$. $L$-smoothness also implies

![[Pasted image 20221006160018.png]]

[[Optimization 1 Questions]]


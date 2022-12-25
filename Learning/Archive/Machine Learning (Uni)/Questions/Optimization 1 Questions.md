What is the definition of a convex function using just the function itself? #flashcard #MachineLearningUni #Optimization
	We say a function $f$ is convex if $$f(\alpha x+(1-\alpha)y)\le\alpha f(x)+(1-\alpha)f(y)$$for every $x$ and $y$ and $0\le \alpha \le 1$.

---
What does the definition of a function being convex using just the definition of a function actually mean (f(ax+(1-a)y)<=af(x)+(1-a)f(y)? #flashcard #MachineLearningUni #Optimization 
	$$f(\alpha x+(1-\alpha)y)\le\alpha f(x)+(1-\alpha)f(y)$$This mean that an interpolated value between two point on the graph (LHS) is always greater than or equal two the function on the values if they were interpolated by the same fraction $\alpha$. That is any line connecting two point on the graph doesn't intersect the graph in-between those points.

---
What is the definition of a function being convex using its first order derivative? #flashcard #MachineLearningUni #Optimization 
	We say a function $f$ is convex if $$f(x)\ge f(y)+(x-y)^T\nabla f(y)$$for all $x$ and $y$ values.

---
What does the definition of a function being convex using first order derivative mean? #flashcard #MachineLearningUni #Optimization 
	$$f(x)\ge f(y)+(x-y)^T\nabla f(y)$$This means that for every point $f(y)$ every other point $f(x)$ is greater than the tangent to $f$ at $y$.

---
What is the definition of a convex function using the second order derivative? #flashcard #MachineLearningUni #Optimization 
	It would be that if $\nabla^2f(x)$ exists $f$ is convex if $\nabla^2f(x)\succcurlyeq 0$ for all $x$

---
With reference to monotonicity and the derivative of some function how can it's convexity be defined? #flashcard #MachineLearningUni #Optimization 
	The function $f$ is convex if its derivative $f'$ is monotonically never decreasing. $$\forall x,y\in\textbf R.x>y\implies f'(x)\ge f'(y).$$Is equivalent to $f$ being convex.

---
What does it mean for a matrix to be positive and positive semi-definite? #flashcard #MachineLearningUni #Optimization 
	A matrix is positive when all its "eigen values" are positive. That is its operation on a vector space is to not invert any vectors in direction. Then it is positive semidefinite if all its eigen values are greater than or equal to 0. So it could transform some vectors to 0 as well.

---
What does the notation $\min_xf(x)$ mean? #flashcard #MachineLearningUni #Optimization 
	This means we find the value of $x$ than minimizes the values of $f(x)$

---
What is the solution to $\min_xf(x)$ called? #flashcard #MachineLearningUni #Optimization 
	It is called the minimizer.

---
How can we write the definition of positive semidefinite for a matrix M? #flashcard #MachineLearningUni #Optimization 
	We say that for every vector $\textbf v$ a matrix $\textbf M$ is positive semidefinite if $$\textbf v^T\textbf{Mv}\ge 0$$

---
How can we prove a squared distance is convex? #flashcard #MachineLearningUni #Optimization 
	A squared distance is of the form $l(s)=(s-s')^2$ but if we take the second order derivative we find. $$\frac{\delta^2l}{\delta^2s}=2\ge0$$Hence $l$ must be convex for all $s$ and equally $s'$.

---
What does it mean for an affine transform to perserve convexity? #flashcard #MachineLearningUni #Optimization 
	We say an affine transform preserves convexity if we have some convex function $f$ then for a matrix $A$ and real number $b$ we have $$g(x)=f(Ax+b)$$Then $g$ is also convex.

---
What does it mean for a weighted sum of convex functions to be convex? #flashcard #MachineLearningUni #Optimization 
	This is written for $f1,..,f_k$ convex function with $\beta_1,...,\beta_k\ge 0$ then we know if $$f=\beta_1+...+\beta_kf_k$$then $f$ is also convex.

---
When is MSE convex? #flashcard #MachineLearningUni #Optimization 
	MSE is defined as $$L=\frac1N\sum_{i=1}^N(w^T\phi(x_i)-y_i)^2$$But $(w^T\phi(x_i)-y_i)^2$ is an affine transform on a squared difference. Now we know a squared difference is convex and that an affine transform would preserve this. The next operation is a summations. Hence we add together $N$ convex function. But a positive weighted sum of convex function is convex so this must be.

---
What is the optimality condition for convex functions? #flashcard #MachineLearningUni #Optimization 
	This means for a convex function $f$ if we have some $x^\star$ minimizer of $f$ then $\nabla f(x^\star)=0\iff f(x^\star)=\underset x{\min}f(x)$ 

---
How does the optimality condition explain the "solution" to a mean squared error loss? #flashcard #MachineLearningUni #Optimization 
	Since we can differentiate some MSE $f$ and it is convex this means for any value where $f'(x)=0$, $x$ is a minimizer of $f$ hence our solution.

---
What is the definition of a function being $\mu$-strongly convex? #flashcard #MachineLearningUni #Optimization 
	A function $f$ is a$\mu$-strongly convex if $$f(y)\ge f(x)+(y-x)^T\nabla f(x)+\frac\mu2||y-x||^2$$The basic meaning of this is there is a quadratic with gradient $\mu$ at every point that serves as a lower bound for $f$.

---
What does it mean for a function to be $L$-Lipschitz? #flashcard #MachineLearningUni #Optimization 
	A function is $L$-Lipschitz if for any $x$ and $y$ we have $$|f(x)-f(y)|\le L||x-y||$$That is the difference between the function on the values is always less than $L$ times the actual difference in the values that would go into the function.

---
What is the definition of a function being $L$-smooth? #flashcard #MachineLearningUni #Optimization 
	A function is $L$-smoother if $$||\nabla f(y)-\nabla f(x)||\le L||y-x||$$for any $x$ and $y$. That is its derivative is $L$-Lipschitz.

---
Given a gradient how can we know if the function it measures is $L$-smooth? #flashcard #MachineLearningUni #Optimization 
	If a derivative $f'$ of a function $f$ is $L$-Lipschitz for any $x$ and $y$ then it means $$f(y)\le f(x)+(y-x)^T\nabla f(x)+L||x-y||_2^2$$That is there is always a quadrative function with derivative slope $L$ that is an upper bound to $f$.

---

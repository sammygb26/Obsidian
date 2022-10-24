How is an approximate solution defined? #flashcard #MachineLearningUni #Optimization 
	An approximate solution is defined relative to some $\hat x$ which is a **minimizer**. We then define it by the function distance to this value $\epsilon$ $$f(\hat x)-f(x^*)<\epsilon$$

---
How does the definition of an approximate solution give more flexibility in what values we optimize towards?  #flashcard #MachineLearningUni #Optimization 
	The approximate solution definition only depends on the difference in $f$ function values. That is $f(\hat x)-f(x)$ not $\hat x-x$. This means we can work towards an approximate solution without knowing the true solution.

---
What is gradient descent?  #flashcard #MachineLearningUni #Optimization 
	This is an algorithm for finding approximate solutions to functions. The way it works is we calculate the gradient $\nabla L(w_t)$ for some the $t$th timestep. We can then **update** $w_t\to w_{t+1}$ with the step $w_{t+1}=w_t-\eta_t\nabla L(w_t)$. Here $\eta_t$ is called the learning rate for the $t$th timestep.

---
How does using a iterative algorithm to find an approximate solution allow us to define epsilon (distance from optimal solution value)?  #flashcard #MachineLearningUni #Optimization 
	When we are using an iterative algorithm this can sometimes allow us to define how confident in our approximate solution relative to the step we are on in the iterative alrithm. That is $\epsilon=O(f(t))$ for some $f$ we have defined.

---
What are the three different main results we can get for the relation between epsilon (distance form optimal value) and t the timestep? #flashcard #MachineLearningUni #Optimization 
	These are *sublinear*, *linear* and *quadratic*.

---
What is the form of epsilon in the sublinear case?  #flashcard #MachineLearningUni #Optimization 
	In this case $\epsilon$ has the form $c/t^2$.

---
What is the form of epsilon in the linear case?  #flashcard #MachineLearningUni #Optimization 
	In this case $\epsilon$ has the form $cr^{t}$ where $0<r<1$.

---
What is the form of epsilon in the quadratic case?   #flashcard #MachineLearningUni #Optimization 
	In this case $\epsilon$ has the form $cr^{2^t}$ where $0<r<1$.

---
What is the big 'O' relations between epsilon and t in the sublinear case?   #flashcard #MachineLearningUni #Optimization 
	This will be $\epsilon=O(1/t^2)$ or $t=O(1/\sqrt \epsilon)$

---
What is the big 'O' relation between epsilon and t in the linear case?   #flashcard #MachineLearningUni #Optimization 
	This will be $\epsilon=O(2^{-t})$ and $t=O(\log\frac1\epsilon)$ 

---
What is the big 'O' relation between epsilon and t in the quadratic case?   #flashcard #MachineLearningUni #Optimization 
	This will be $\epsilon=O(2^{2^{-t}})$ and $t=O(\log\log\frac1\epsilon)$ 

---
What are the implications of L-smoothness when we consider using gradient descent?   #flashcard #MachineLearningUni #Optimization 
	This implies that for some step $t$ we have $$f(x_{t-1})-f(x_t)\ge\eta_t||\nabla f(x_{t-1})||_2^2$$When $1\ge 1-L\eta_t\ge 0$ as if it was greater than $1$ it would increase $f(x_t)$ from $f(x_{t-1})$

---
Hos are the implication of L-smoothness when using gradient descent proved?   #flashcard #MachineLearningUni #Optimization 
	This is proved by using the definition of gradient descent $x_t=x_{t-1}-\eta_t\nabla f(x_{t-1})$. To replace all the $x_t-x_{t-1}$ terms. This allows a definition of $f(x_{t-1})-f(x)$ which relies purely on $L$, $\eta_t$ and $\nabla f(x_{t-1})$. Then by picking $\eta_t$ such that $0\le 1-L\eta_t\le1$ we can ensure the difference is always at least $\eta_t||\nabla f(x_{t-1})||_2^2$.

---
What are the implications of strong convexity?   #flashcard #MachineLearningUni #Optimization 
	A $\mu$-strongly convex function allows us to define how far we can at most be from the minimum $f(x^\star)$. As $$f(y)-f(x^\star)\le\frac1{2\mu}||\nabla f((y)||_2^2$$

---
How are the implication of mu-strong convexity used to prove an upper bound for epsilon (difference in solution value from optimal solution)?   #flashcard #MachineLearningUni #Optimization 
	$\mu$-strong convexity defined a parabola $R$ for every $y$ such that for every other value $x$ it is always lower. That is $R_y(x)$ is a lower bound of $f(x)$. We can take a derivative of $R$ with respect to $x$ to find the lowest point on $R$, $R(x)$. This will be in terms of $\mu$, $y$ and $\nabla f(y)$. Then since this is the minimum value possible for $R$ and $R$ is a lower bound for $f$ we know $R(x)\le f(x^*)$ where $x^*$ is the optimal value for $f$. Hence for every $y$ we can define a value that is at least a low as the minimum of $f$.

---
How does a function being mu-strongly convex and L-smooth lead to gradient descent performing linearly? #flashcard #MachineLearningUni #Optimization 
	The function being $L$ strongly convex allow us to pick $\eta_t=\frac1{2L}$ such that we ensure our distance to the solution changes by some fraction of our gradient norm. This can be rephrased as constantly moving towards a better approximate solution by a fraction of our gradient norm. Then we combine this with the result from $\mu$-strong convexity to find that our next distance to the minima is less than a fraction of our current distance. Hence we can say that if we start at some distance $x_0$ after $t$ integrations we will be within that fraction to the power of $t$ times our original distance from the minimum solution value.

---
If a function is L-smooth and mu-strongly convex and we optimize over it using gradient descent with an appropriate eta what can we guarantee about our distance from the minimum value after t iterations? #flashcard #MachineLearningUni #Optimization 
	Our distance will decrease with a linear rate. That is $\epsilon=cr^t$ where $c=(f(x_0)-f(x^\star))$ and $r=(1-\frac\mu L)$

---
What problem do we still have while optimizing over a dataset with $N$ elements? #flashcard #MachineLearningUni #Optimization 
	When we find an optimal definite solution like for example finding $(\Phi\Phi^T)^{-1}\Phi y$ takes $O(N^3)$ time, we can use gradient descent to get around this however each step in gradient descent may take $O(N)$ time and will be repeated many times so is still inefficient. Instead we can only use a fraction of our dataset $X$ each integration.

---
If we use SGD instead of GD what does this make our gradients and loss function? #flashcard #MachineLearningUni #Optimization 
	This makes our gradients and loss functions random variables so we will instead have to work with their expected values and derive distributions for how far our value is form the optimal value.

---
What can be said about that gradient of a $\gamma$-smooth convex function when we use SGD to optimize a solution over it? #flashcard #MachineLearningUni #Optimization 
	It can be shown that $$E_{x, y\sim U(s)}[L(\bar w_t)]\le L(w^\star)+\frac{||w_0-w^\star||}{2\eta t}+\frac{t\sigma^2}2$$where $\eta\le \frac1\gamma$.

---
When SGD is used what can be said about the gradient of the expected loss? #flashcard #MachineLearningUni #Optimization 
	The expected loss is equal to the average loss that is $$\mathbb E_{x, y\sim U(s)}[\nabla l(w;x, y)]=\nabla L(w)$$

---
What does the SGD result for smooth convex functions mean for runtime? #flashcard #MachineLearningUni #Optimization 
	It means the time to find a solution is on the order of $O(t)$ and independent of the size of the dataset.

---
What is a sub-gradient? #flashcard #MachineLearningUni #Optimization 
	This is used where functions aren't differentiable. We basically take a function value that cannot be differentiated and look for a gradient that makes sense. For example a sub gradient $g$ satisfies $$f(y)\ge f(x)+(y-x)^Tg$$

---

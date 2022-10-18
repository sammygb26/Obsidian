# Optimization 3
We have so far been looking at *unconstrained optimization*. For example $\underset{w}\min L(w)$. But instead we may want to perform **constrained optimization**. Say with the constraint $\text{s.t. }||w||^2\le 1$ (bounded norm). Then inequality is called a *constraint*. Solutions that satisfy the constraints are called *feasible solutions* (alternate to *unfeasible solutions*). We know how to test this but we want to bring the constraint into the objective. For example we instead perform:

![[Pasted image 20221013151435.png]]

We define $V\_$ as follows:

![[Pasted image 20221013151449.png]]

This is identical to the previous problem but cannot be differentiated. We can use approximation to get around this:

![[Pasted image 20221013151601.png]]

We replace a stepper function with a linear approximation. We have that $\forall s. \lambda s\le V\_(s)$.

### Lagrangian
In general if we have an optimization problem as follows:

![[Pasted image 20221013151837.png]]

Making the constraint in the form $h(w)\le 0$ is called making the constraint *canonical*. The **Lagrangian** is defined as:

![[Pasted image 20221013151902.png]]

$\lambda$ is called the **Lagrange** multiplier.

### Dual function
If $\bar w$ is a feasible solution meaning $h(\hat w)\le 0$, then $$L(\bar w)+\lambda h(\bar w)\le L(\bar w)$$meaning the value satisfying the **Lagrangian** always gives a value less that just the regular loss. This means that the lowest possible with the **Lagrangian** is less than the usual minima:

![[Pasted image 20221013152347.png]]
(with brackets around L(w) and hh(w))

Since we are minimizing over $w$ this is now a function of $\lambda$.

![[Pasted image 20221013152430.png]]

For any $\lambda$ we can say that for any $\lambda$ $$g(\lambda)\le L(w^\star)$$(from above). Where $w^\star$ is the optimal solution for $L(w)$ subject to $h(w)\le 0$.

![[Pasted image 20221013152709.png]]

Since $g(\lambda)\le L(w^\star)$ for any $\lambda$ 

![[Pasted image 20221013152752.png]]

The problem

![[Pasted image 20221013152806.png]]

is called the dual problem. The whole **dual problem** can be written compactly as:

![[Pasted image 20221013152910.png]]

For every feasible solution $\hat x$, $h(\hat x)\le0$  Then $\lambda$ has to be 0 (as $h(s)\le0$). But if there isn't a feasible solution then $\lambda\to\infty$ as $h(s)\ge 0$.

### Unigram Model
This is a type of model where we estimate the probability for a number of words.

![[Pasted image 20221013153229.png]]

We can take the simple intuitive solution:

![[Pasted image 20221013153252.png]]

There are 18 words in this example (we can ignore others as their probability will be 0). We assign each word a $v$ a probability $\beta_v$. Then probability of a word is $$p(w)=\prod_{v\in V}\beta_v^{\mathbb 1_{v=w}}$$ This is basically the mathematical equivalent of indexing it an array. We assume each word is independent of each other (false assumption). To find $\beta$ we can maximize the likelihood given the dataset. The likelihood of $\beta$ given the data is 

![[Pasted image 20221013153630.png]]

Since $\beta$ is a probability vector we have the assumption and requirement that:

![[Pasted image 20221013153800.png]]

We need this as if we maximize likelihood all $\beta$ values will go to $\infty$ so we need our requirement. So we get the optimization problem.

![[Pasted image 20221013153926.png]]

Its **Lagrangian is**

![[Pasted image 20221013153948.png]]

We want to optimize this problem so we take the derivative and set it to 0.

![[Pasted image 20221013154223.png]]

The dual problem is ugly (below). So how can we solve for $\lambda$.

![[Pasted image 20221013154245.png]]

![[Pasted image 20221013154455.png]]

Hence we get the intuitive solution:

![[Pasted image 20221013154515.png]]

The idea is this is a constraint optimization problem hence we can solve other problems with the the same techniques.

### Projection
![[Pasted image 20221013154613.png]]

Here we are projecting $u$ onto the vector $v$. Dividing by $||v||$ ensure we get a unit vector. The projection is just a quantity not a vector. If we have $N$ data-points then we may want to perform a sum squared projection (giving us LHS), (bracket on the other size of the $\sum$, inside):

![[Pasted image 20221013154909.png]]

We arrive at $\sum_{i=1}^N(x_i^Tw)^2=w^TXX^Tw$ by noting that a sum of squares is really a dot product between two identical vectors. Then we can unpack that vector to be $w^TX$. This can be through of as the spread of the data, sum of projection quantities. It will do this for different quantities directions.

![[Pasted image 20221013155502.png]]

Hence we can make a **maximization problem**. That is we are taking:

![[Pasted image 20221013155537.png]]

This problem is scale invariant, the direction matters not the length:

![[Pasted image 20221013155602.png]]

So we can set the length of $w$ to 1. Hence the problem is equivalent to:

![[Pasted image 20221013155701.png]]

The **Lagrangian** is:

![[Pasted image 20221013155720.png]]

We can find an optimal solution by taking the gradient with respect to $w$:

![[Pasted image 20221013155752.png]]

We can find an optimal solution where $w$ is an *eigen vector*. Hence to maximize $\lambda$ (find maximal spread) we need to find the maximal eigen vector. So we take $XX^T$ find its maximum eigen vector via SVD.

![[Pasted image 20221013160213.png]]

Is called the *Rayleigh* quotient.

[[Optimization 3 Questions]]


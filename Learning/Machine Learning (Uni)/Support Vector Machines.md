SVMs where developed in the 90s long after the original logistic regression and perceptron. We can start by thinking about **logistic regression** using a *sigmoid function*. $$\sigma(x)=\frac1{1+e^{-x}}$$ Which we maximize using *maximum likelihood estimation*. With this function we can create a linear classified by treating the output as a probability.

![[Pasted image 20221110151742.png]]

As in bellow the line $w^Tx + w_0$ is negative an positive on the otherwise of the line. The sigmoid maps them to $(0,1)$. The boundary is at $w^Tx+w_0=0$. Decision boundaries also exist in higher dimensions with the same formula. We can get many different classifiers that fit some data. We want to maximize **generalization**.

![[Pasted image 20221110152018.png]]

Take the above case both the first graphs are 100% accurate with the training data. We can quantify this with the idea of how large the **margins** are, visualized in the third graph. The idea is this would generalize better. *SVM*s consider the dashed lines in the third graph and try to maximize the distance between them. Then the decision boundary is defined as the line in between the two. We define these two lines as $$w^Tx+w_0=+1\hspace{32pt}w^Tx+w_0=-1$$
We want to propose two lines are satisfied by all the points in the appropriate class bring on the right side of the line.

![[Pasted image 20221110152428.png]]

### Margin
We want to maximize the margin between the lines with the symbol $r$ this has the formula $r=\frac1{||w||}$. This is as this line is defined by the distance between two pints $p_1$ and $p_2$ we get:

![[Pasted image 20221110152720.png]]

### SVM
We are training to maximize $\max_w\frac1{||w||}$ with the conditions that 

![[Pasted image 20221110152823.png]]

This can be converted and seen to be simplified into the following minimization problem

![[Pasted image 20221110152911.png]]

This is a quadratic optimization problem making it convex and there is also a global minimum. Hence solving this gives a global solution. The solution itself is given by 

![[Pasted image 20221110153030.png]]

The **support vector** make up $w$ hence their name as $w$ is a weighted sum of $y_i$, $x_i$s. For classification we just take the sign of the output

![[Pasted image 20221110153147.png]]

##### Why +1 instead of +$\epsilon$
We can see that whatever $\epsilon$ we choose we get a similar problem hence the values don't matter.

### Solution
We want this

![[Pasted image 20221110153315.png]]

We can the the Lagrange multiplies $\alpha_i\ge0$ for the Lagrangian as

![[Pasted image 20221110153351.png]]

Where $\alpha=(\alpha_1,\dots,\alpha_n)$ and 

![[Pasted image 20221110153426.png]]

We can optimize this using calculus

![[Pasted image 20221110153445.png]]

Putting this result in to the Lagrangians yields:

![[Pasted image 20221110153525.png]]

The necessary and sufficient conditions for $w^\star$ to be an optimum are

![[Pasted image 20221110153634.png]]

This last part means that either $\alpha_i^\star=0$ or $y_i(w^Tx_i+w_0)-1=0$.

### Hard vs Soft Margin SVM
We cannot solve SVM if we cannot make margins empty of values. Instead we allow some value sin the margins. We add a deviation $\Psi_i$ for each training sample. We then minimize the total size of these $\Psi_i$s. Where $C(x)$ is out count function

![[Pasted image 20221110153950.png]]

The condition means that $\Phi_i$ is the distance to the margin for all $x$.

We do not minimize $\Psi_i$ per say but use it to allow differentiation instead of just counting the $\Psi$s.

![[Pasted image 20221110153927.png]]

We can use a **hinge** loss which does penalize values greater than $0$. That is $$l(t)=\max(0,1-t)$$

![[Pasted image 20221110154301.png]]

### Non-linear SVMs
We want to map our vectors into higher dimensional space called **feature space** where the classes are linearly classifiable. We then map it back to the original space.

![[Pasted image 20221110154426.png]]

THis gives the steps

![[Pasted image 20221110154451.png]]
4) Then we map back into normal vector space.

This mapping is expensive in terms of calculations. Hence we need the **Kernel Trick**.

### Kernel Trick
Instead of applying the *non-linear* transformation and carrying out calculations in the feature space, use a kernel function $k(x_i,x_j)$ such that $$k(x_i,x_j)=\phi(x_i)^T\phi(x_j)$$

An example of a kernel that maps data to a feature space explicitly would be

![[Pasted image 20221110154747.png]]

Where this actually gives 6-dimensional space. However instead of using all these kernels we instead can use **popular kernels**. (polynomial <> is dot product)

![[Pasted image 20221110154848.png]]

### Making Kernels
We want to ensure if a kernel works as an inner product in a feature space. It needs to satisfy that

![[Pasted image 20221110155000.png]]

If $K$ is semi-definite it can be used for SVM.

##### Mercer's theorem
Suppose $k$ is a continuous symmetric non-negative definite kernel, then $k$ an be expressed as

![[Pasted image 20221110155122.png]]

where $\{\phi_i\}$ are eigen-functions, $||\phi_i||=1$ and $\{\lambda_i\}$ are positive eigen values $\lambda_i>0$

We can also make kernel **from kernels** letting $k_1$, $k_2$ and $k_3$ are kernels we can create a new kernel $k$

![[Pasted image 20221110155250.png]]

### Generalization error of SVM (NE)
Assuming the class $\mathcal F$ of real-values function on the ball of radius $R$ in $\mathbb R^n$ as

![[Pasted image 20221110155357.png]]

If a classifier $sng(f)\in sng(\mathcal F)$ has margin at least $\gamma$ on all the training example, with probability at least $1-\delta$ over $n$ random examples, $f$ has error no more than

![[Pasted image 20221110155457.png]]

where $k$ is the number of labelled training example with margin less than $\gamma$ $c$ is a constant,

![[Pasted image 20221110155527.png]]

### Experiments on US postal Services Database

![[Pasted image 20221110155635.png]]

### Look at notes at end of slides!

- problem requires $n\times n$ matrix (can be very large for large matrices)


When we reuse test-set we can end up overfitting to it. For example when we remake the test sets there is a performance test set. A *positive* side is that the performance on each is highly correlated.

![[Pasted image 20221027151913.png]]

### Capacity-generalization tradeoff
With probability $1-\delta$, for all $h\in\mathcal H$.

![[Pasted image 20221027152025.png]]

As the capacity of $\mathcal H$ increases our minima for $L_s$ goes up. From this we see the training error always goes down however the generalization error eventual goes back up.

### Degree 9 polynomial
![[Pasted image 20221027152600.png]]

### Large hypothesis classes
We can compare two $\mathcal H$s 

![[Pasted image 20221027152332.png]]

$\mathcal H_1$ is a finite VC-dimension, while the VC dimension of $\mathcal H_2$ is infinite. The easiest way to decrease training error is to increase the capacity of the hypothesis class. A way to get around this is with **weight decay**.

![[Pasted image 20221027152640.png]]

We can look at how this changes the degree 9 polynomial found. We get something more like this:

![[Pasted image 20221027152719.png]]

### L2 Regularization
This is the name for the above method. The way it works out that while using *gradient descent* this means every update we reduce the weights by a small amount. Hence the other name **weight decay**.

![[Pasted image 20221027152936.png]]

This is the **lagrangian** of:

![[Pasted image 20221027152955.png]]

The idea of a *lagrangian* is a way to understand why this works. This is constrained by some $B$ but as $\lambda$ is also free its value doesn't matter too much and will be worked out in runtime. Hence the $L_2$ regularize has an effect of controlling the capacity of the hypothesis class.

![[Pasted image 20221027153225.png]]

(look at shattering definition again)

### Rademacher complexity
Rademacher complexity (in binary classification) on a data set $S$ is defined as:

![[Pasted image 20221027153500.png]]

Where $\sigma\in\{+1,-1\}^n$ is uniformly chosen. The $x_i$s are given by the dataset $S$. This is the expected performance on then $n$ dataset which have random labels. In binary classification for $n$ points Rademacher complexity is defined as:
![[Pasted image 20221027154010.png]]

### Rademacher Complexity Bounds
With probability $1-\delta$, for all $h\in\mathcal H$

![[Pasted image 20221027154039.png]]

With probability $1-\delta$, for all $h\in\mathcal H$

![[Pasted image 20221027154106.png]]

### Linear classifiers with bounded norm
If $S=\{x:||x||\le r\}$ and $\mathcal H=\{x\mapsto w^Tx:||w||\le B\}$,

![[Pasted image 20221027154225.png]]

### Stability
This is the idea that if we have a dataset and we swap out one sample will we get a different classifier and how much would it change. Getting a very similar classifier means our learning algorithm is **stable**. If $S$ is the data set, then $S^{(i)}$ is the same data set with the $i$-th data point replaced with another random datapoint (from the same distribution $\mathcal D$).

![[Pasted image 20221027155315.png]]

Proof:

![[Pasted image 20221027155343.png]]

The first step is given by using the definition of $L_{\mathcal D}(S)=\mathbb E_{(x,y)\sim\mathcal D}[l(s,x,y)]$. This means **stable learning algorithms** don't overfit.

### Lipschitz loss
If the loss is $p$-Lipschitz continuous, 

![[Pasted image 20221027155745.png]]

We only need a bound on $||A(S^{(i)})-A(S)||$.

### Lipschitz and strongly convex
If a function is $p$-Lipschitz continuous and $\lambda$-strongly convex,

![[Pasted image 20221027155936.png]]

Where $x^*$ is the minimizer as this reduces the $\lambda$-strong convexity definition. We can have a bound

![[Pasted image 20221027160008.png]]

### Back to L2 regularizer
$\frac\lambda2||w||^2$ is $\lambda$-strongly convex. Hence $L_S(w)+\frac\lambda2||w||^2$ is strongly convex if $L_S(w)$ is. So we can make any convex function strongly convex. Then if the loss is also $p$-Lipschitz we find that when $A(S)=\min_{w\in\mathcal H}L_S(w)+\frac\lambda2||w||^2$ we find that 

![[Pasted image 20221101114000.png]]

Then if we pass this bound through the definition for $p$-Lipschitz we get

![[Pasted image 20221101114135.png]]

Meaning adding L2 regularization to a $p$-Lipschitz loss makes it have stable learning and hence doesn't overfit.

![[Pasted image 20221027160246.png]]

[[Generalization 3 Questions]]
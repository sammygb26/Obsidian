Many (but not all) generalization bounds have the following form.

![[Pasted image 20221024152312.png]]

Where $n$ is the number of samples $C(\mathcal H)$ is a capacity measure of $\mathcal H$ (size of $\mathcal H$ as it may be infinite). This is a theorem about **uniform convergence** as we are looking at a relation between the generalization and training loss and it is true for all $h$.

**Sample complexity** - we get get our sample size in a confidence range. We start with the relation on $\epsilon$ then we can find $n$ in terms of $\epsilon$ and other value where $\epsilon$ is just the difference between our generalization error and test error:

![[Pasted image 20221024152840.png]]

This becomes the following:

![[Pasted image 20221024152823.png]]

### VC Generalization Bounds
Vapnik-Chernonenkis generalization bounds:

![[Pasted image 20221024153123.png]]

Where $d$ is called the VC dimension. This is for linear classifiers $\mathcal H=\{x\to w^T\phi(x):w\in\mathbb R^p\}$, VC-dim$(\mathcal H)=p+1$. For multilayer perceptron with $p$ edges, VC-dim$(\mathcal H) = O(p\log p)$. These results are independent of learning algorithms and independent of how ERM is done.


### Shattering - Capacity Measure
Given $n$ data points, there are $2^n$ ways of labeling them $\{+1,-1\}$. A set of $n$ points is shattered by $\mathcal H$ if classifiers in $\mathcal H$ can produce all $2^n$ ways of labeling. VC dimension is the larger number of points that $\mathcal H$ can shatter. For example in 2D with lines the VC-dimension is 3 as we cannot shatter 4 points with a line in 2D.  In general is it $p+1$. We can shatter 4 points with a 2-layer MLP in 2D so neural networks have larger VC dimension.

### Interpreting Generalization Bounds
We have the bound

![[Pasted image 20221024154309.png]]

Means when $\mathcal H$ is large $\min_{h\in\mathcal H}L_s(h)$ can be lower as there are more options for $h$. But when $\mathcal H$ is large $d$ becomes large. This gives the **capacity generalization tradeoff**

![[Pasted image 20221024154443.png]]

### Optimization
We can only do ERM for a limited number of cases for example $w=(XX^T)^{-1}Xy$ in linear regression. Convergence for an optimizer tell us how many iteration we need to get:

![[Pasted image 20221024154656.png]]

Hence performing SGD just gets us close to ERM. 

![[Pasted image 20221024154920.png]]

We can about generalization of zero-one loss not the cross entropy or the log likelihood. In this context cross entropy and log likelihood are called **surrogate losses**. Surrogate losses are easier to optimize than the task loss and usually have some connection to the task loss. For example log loss is easier to optimize than zero-one loss and is a smooth approximation of zero-one loss.

### Hence we get three errors
**Optimization Error** - mismatch between surrogate loss and the task loss. This is controlled by the optimization of the algorithm
**Estimation Error** - Controlled if we do ERM and have uniform convergence. Controlled by the capacity of $\mathcal H$ and the size of the training set.
**Approximation Error** - Controlled by the capacity of $\mathcal H$.

### Underfitting
A model is underfitting if there is another model that has a lower training error. A model $h$ is underfits if there is a $f$ such that $L_S(f)<L_S(h)$ The better $f$ is unknown unless we find it. All model are underfitting with respect to ERM. When people say we are **underfitting** they simply mean there is room to improve the training error.

### Overfitting
A model is overfitting if there is another model that has a higher training error but lower test error. So we fit too much to the test set. A model $h$ is overfitting if there s $f$ such that $L_S(f)>L_S(h)$ and L_{S'}(f)<L_{S'}(h). The $f$ is unknown unless we find it. Models can overfit even though the gap $|L_S(h)-L_{S'}(h)|$ between training and testis not large. When people say a model is overfitting they simple mean there is a gap between the training and test error.

### In Practice
We minimize a **surrogate** lost son the training set $S$ i.e. doing ERM. We can only do ERM approximately most of the time because of the optimization difficulty. 

### Test set
Test error on a test set is used to approximate generalization error. Test set is supposed to be considered as an independent data drawn from the unknown distribution. Sometimes we have 
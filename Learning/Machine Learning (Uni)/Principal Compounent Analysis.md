PCA is used to understand data and compress it without losing much information. This is important given the amount of data create nowadays. Compression is important in order to *visualize* and *process* our data. PCA linearly combines our variables and allows us to drop projection that are less informative.

### Motivation
With $m$ feature vectors each with $d$ dimensions in $X$. In **Dimensionality Reduction** we want to reduce the number of dimensions or features in the vectors to $k$ making a new dataset $Z$. There can be ways to reduce our datasets we could remove random data or *combine columns*. We want to do this to **visualize** (in order to look at the data with our own eyes), **explore** (part of visualization but we can not get it in a form we understand) and **compress** (make it take up less space).

1. Reducing the number of columns $d\to k$ by deletion is not meaningful as we will loose random data.
2. Columns of $Z$ are uncorrelated to we are not wasting dimensions
3. It ok the make data less explainable

### Geometrics
In PCA we are attempting to define some mapping of higher dimensions into lower dimensions that preserves as much information as possible (variance).

$X_{m\times d}\to Z_{m\times k}$ where $k<d$. Hence a way to get this is $Z_{m\times k}=X_{m\times d}U_{d\times k}$. Now each $Z=[z_1 z_2\dots z_k]$ and $X=[x_1,x_2\dots x_d]$ and $U=[u_1 u_2\dots u_k]$. 

1. Principal components are sequences of projections of the data, mutually uncorrelated and ordered in variance. 
2. The columns $u_{1\dots k}$ are **orthonormal** so that $u_i^Tu_j=0$ if and only if $i\neq j$ and $u_i^Tu_i=1$

### Derivation (Maximum Variance Formulation)
There are three key approaches **Maximum variance formulation**, minimum error formulation and probabilistic formulation. $$\max_{u_1}\text{Var}[z_1]=\max_{u_1}\text{Var}[Xu_1]$$That is we want the first principal component to have the maximum variance in $Z$, so when transforming our dataset $X$.  Now given that $\text{Var}[y]=y^Ty$ and $X^TX=\Sigma_X$ we can get: $$\max_{u_1}z_1^Tz_1=\max_{u_1}u_1X^TXu_1=\max_{u_1}u_1^T\Sigma_{X}u_1$$ We constrain $u_1^Tu_1=1$ (as this is required my PCs being orthonormal) then we use a **lagrangian**.  $$\max_{u_1}u_1^T\Sigma_Xu_1\hspace16pts.t.\hspace16pt||u_1||=u_1^Tu_1=1$$ $$L(u_1,\lambda_1)=u_1^T\Sigma_xu_1-\lambda_1(u_1^Tu_1-1)$$ Which we can then differentiate to get $$\frac{\partial L}{\partial u_1}=2\Sigma_Xu_1-2\lambda_1u_1=0$$Hence we at the max point we get $\Sigma_Xu_1=\lambda_1u_1$ which defines $\lambda_1$ and $u_1$ as the eigen-vector eigen-value of $\Sigma_X$. Plugging our stationary value to we get $$\text{Var}[z_1]=u_1^T\Sigma_Xu_1=u_1^T\lambda u_1=\lambda_1u_1^Tu_1=\lambda_1$$Hence if we want to maximize variance we simple need to pick that largest eigen value and eigenvector pair. The maximum variance $u_1$ is found to be the eigen vector with the largest eigen value. There will be $d$ of these with never increasing values. Then we can repeat this to get $u_{1\dots k}$. Then we we also know these are orthonormal as they are eigenvectors. This makes the $V$ matrix which is equal to the first $k$ eigen vectors of $X^TX$.

### Application
An application of this is visualizing the common causes for different variables in a dataset or at least allowing them to correlate together.

![[Pasted image 20221031163108.png]]

We can see that only 1/2 eigenvalue(s) predicts most of the variance. Hence we can plot this and visualize the causes of the data.

The eigen vector decomposition of $\Sigma_X$ takes time $O(d^3)$ SVD of $\Sigma_X=O(d^3)$
The singular value decomposition of $\Sigma_X$ has a computational cost of $O(d^3)$
The singular value decomposition of $X$ has computational cost $O(md^2)$
Eigen vector decomposition of Gram matrix $K=XX^T$ is $O(d^3)$

### Bad Things to Do with PCA
PCA to avoid overfitting is bad idea. Instead we would use regularization. Doing dimensionality reduction before linear classification is also a bad idea Linear Discriminant Analysis (LDA) instead.

![[Pasted image 20221031163647.png]]


This is a clustering algorithm allowing us to organize objects into groups. Like [[Principal Component Analysis]] we do not need labels to perform this technique only the datapoints. As this can be used with no labels we could use the clusters as labels for our own understanding. **Clustering** is a category of methods where we categorize objects into groups where the elements are similar within a group.

### Problem
**Aim**: Identify clusters of data points in multi-dimensional space. We have a set of data $\{x_1,x_2,\dots,x_N\}$ of $d$-dimensional variables $x$. We want to create a *known* number of clusters $K$. Fixing $K$ simplifies the problem hugely.

We are mapping a dataset into different groups. We can formalize the groups by showing their means as $X$. This way the data can be compressed and simplified into $K$ points.

![[Pasted image 20221103152145.png]]

**Specific goal**: Given a $K$, find an assignment of datapoints to cluster and the set of vectors $\{\mu_k\}$ (the $X$ points above) to represent these clusters. The assignment rule ($r_{nk}=1$ if $x_n$ is in cluster $k$, unknown otherwise problem is solved) and all $\mu_k$s are **unknown**.

### Algorithm
A solution to the above problem is to minimize the squared distance of each data point to its closest vector $\mu_k$. That is we want to minimize the **distortion function** 

$$J=\sum_{n=1}^N\sum_{k=1}^Kr_{nk}||\textbf x_n-\mu_k||^2$$

To minimize this we must find $r_{nk}$ and $\mu_k$ for all $n$ and $k$. We must assume values for all values then we can partially differentiate to reduce $J$.

This gives the $K$-means algorithm
1. We randomly select $\mu_{k=1,\dots,K}$
2. Minimize $J$ with respect to $r_{nk}$, keeping the $\mu_k$ fixed
3. Minimize $J$ with respect to $\mu_k$, keeping the $r_{nk}$ fixed
4. Repeat steps 2 (Expectation) and 3 (Maximization) steps until convergence

##### 2 Minimize J with respect to $r_{nk}$ keeping $u_k$ fixed
$J$ us a linear function of $r_{nk}$ and terms with different $n$s are independent. So to minimize $J$ with respect to $r_{nk}$ all we must to is pick for each $n$ the value of $r_{nk}$ such that it has the smallest $||\textbf x_n-\mu_j||^2$. So we perform $$r_{nk}=\begin{cases}1&\text{if $\arg\max_j||\textbf x_n-\mu_j||^2$}\\0&\text{otherwise}\end{cases}$$

##### 3 Minimize J with respect to $\mu_k$ keeping $r_{nk}$ fixed
$J$ is a quadratic function of $\mu_k$ and can be minimised by setting its derivative with respect to $\mu_k$ to 0 that is $\frac{\partial J}{\partial \mu_k}=0$. We find

![[Pasted image 20221104195551.png]]

### Example

![[Pasted image 20221103153921.png]]

This would have the following graph for $J$

![[Pasted image 20221103154159.png]]

$J$ can only reach 0 as $K\to N$ this is when each point has its own cluster to itself. We can also have poor cluster found for example where clusters are used up on outlier points.

### How to choose $K$

![[Pasted image 20221103155041.png]]

we know as $K\to N$ $J\to0$ but then we loose the benefits of clustering as we haven't really done any clustering. There are several methods to find $K$ which rely on domain expertise, elbow and silhouette methods, and gap statistics.

### How to initialize $\mu_k$
We also need to find our $\mu_k$ values in order to cluster around them. This is as the results is sensitive to the initialization of $\mu_k$.

![[Pasted image 20221103155142.png]]

Many methods have been tried:

1. Random initialization (the above case can happen)
2. Often times $\mu_k$s are initialized to a subset of data (Forgy initialization)
3. Repeat clustering for various initial and select the best set of $\mu_k$s
4. K-means++ (Arthur and Vassilvitskii 2007)

It is often better to just use **domain knowledge**.

### Hard assignment vs Soft assignment
![[Pasted image 20221103155500.png]]

We can get data-points in-between in which case we can choose to not assign them (noise) this is called **hard-assignment**. Or we could represent a cluster with covariance and mean. This way each point get represented with a probability of being in any cluster.

[[K means questions]]
# K Means
## Unsupervised and Supervised Learning
This is an [[Unsupervised Learning]] method for understanding data, this one in particular looks as **cluster analysis**.  An example would be if we measure a bunch of lemons and oranges say their weight and height.  We could see some sort of clustering with the data. We ant to just generate label for our data that don't correspond to a real label only what our machine sees. There is no meaning from this until we add it.
![[Pasted image 20220131085819.png]]

**Unsupervised learning** is different from [[Supervised Learning]] where we use a training set the is labeled to guess the category of some data. Each point will have a label and features. We then have to find the label of some unseen point given its features.
![[Pasted image 20220131085835.png]]

## Numbers of Clusters
For groups of points it cam be quite hard to decide the true numbers of clusters even from the same example.
![[Pasted image 20220131090200.png]]

## Why Cluster
Clustering us useful for analyzing data and it can be used to understand users or scientific data. We can also use clustering to **compress** data where we group points and then represent a cluster by one point instead. This is called **vector quantization**.

## Types of Clustering
**Partitional Clustering** -> In this we give each data point to one cluster and the clusters don't overlap.
**Hierarchical Clustering** -> In this each point belongs to a hierarch of clusters for example we split the space into two then further split each division further. This can give us control on the level of granularity by controlling the number of clusters.
![[Pasted image 20220131090735.png]]

Clustering will always take some function that measures distance between points, and between points and the center of clusters.

**Hierarchical** clustering can also be given in a dendrogram. This comes from the distance function where the x-axis is the distance between clusters partitioned by the clustering. We can here define the number of clusters and the granularity by deciding a cutoff.
![[Pasted image 20220131090911.png]]

There are two ways to make a hierarchical cluster first with **top down** clustering where we break the space down into two clusters we then break this down into more clusters. Then we have **agglomerative** or **bottom up** where we look for two points closest together. We then group them together can make them a point. We do this for all points at the same time giving a tree hierarchy.

## K-means Clustering Algorithm
The aim is to divide a set of n D-dimensional datapoints into K clusters (where we decide K). 
**Algorithm** ->    First we initialize K cluster centers $m_k$ where $1\le k\le K$ 
						While the algorithm is not converged -> We assign each $x_i$ to the closest cluster centers and we recompute the means based on the new cluster points. Here $m_k=\frac{1}{|C_k|}\sum_{i\in C_k}x_i$. Go back t other start of this step and reassign points.
						We are converged when after one of these reassignments no points switch.

#### Distance Measure
We need some measure of distance to tell us where our points are relative to the means. We want a function $d(\underline{x},\underline{y})$ we can easily use the Euclidian distance function $|\underline{x}-\underline{y}|=\sqrt{\sum_{j=1}^D{x_i-y_i}}$. We could in theory use other distance functions however.

#### Initialization Methods
There are different methods for finding the data points.
1. We pick random points as the cluster centers
2. We randomly assign points to clusters and compute means
3. We choose points with extreme values far form the overall mean.
4. We set all the the whole means and perturb from this.

#### Convergence
Convergence is reached when an assignment of points doesn't change after an iteration. K-means is guaranteed to converge however these convergent solutions are not unique so we can get different clusterings.

## K-Means Evaluation
How do we decide how good some clustering is and how well our algorithm has done.
![[Pasted image 20220131093208.png]]
If we look at this example there are centers that aren't centered on data. We have an **error function** giving a measure of the spread around the clusters. Here both variables are in standard units.

#### Mean Squared Error Function
This is also called **intertie**. We say a point $i$ belongs to a clusters $k$ then $i\in C_k$. So then 
$$
E=\frac{1}{n}\sum_{k-1}^{K}||x_i-m_k||^2
$$
This is then called a minimum variance clustering when we minimize this function. 
#### Failures
The error function above gives a failure of k-means when we have different scales. Take the example below.
![[Pasted image 20220131093642.png]]
Since the x-distance is much smaller and the y-distance is much higher. That is there is more variance in the y than the x. A solution to this is to use standardized variables.

We can also see that small relative clusters can eat up points from larger ones who's center is pulled away by their greater size.
![[Pasted image 20220131094001.png]]
The reasons for this is that the error of the $E$ function is not taking into account the variance of the clusters. This can be overcome by [[Gaussian Mixture Models]] also known as **expectation maximization algorithm**.

#### How to choose k?
There is no correct way to do this without knowing some detail about the data. We can use a **scree plot** and we see as $K$ increases $E\to0$ We are looking for an elbow where the change in error for one more cluster becomes low. A problem can also arise when even though our error function is low locally we cannot move to the true lowest minimum.
![[Pasted image 20220131094621.png]]
There is a lot of research into how to get rid of minimums. One way is using the **online** version instead of the **batch** version. In **batch** we assign all point then compute new means. In **online** we randomly assign points and after each assignment change the means. There is also the need for efficient distance measures. Another problem is the **curse of dimensionality** where distance becomes a worse measure and points becomes further apart with more and more dimensions. We can use **dimensionality reduction** techniques like [[Principle Components Analysis]] to get around this.

[[K Means Questions]]

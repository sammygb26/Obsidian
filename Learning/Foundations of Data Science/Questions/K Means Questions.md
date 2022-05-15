What is K means? #flashcard #FDS #KMeans
	K Means is a technique used for cluster analysis. We get a machine to train a labeler that decides on clusters throughout some dataset.

---
How does the number of clusters change the behavior of K-Means? #flashcard #FDS #KMeans 
	K-Means depends a lot on the number of clusters and we have to choose that. It cannot decide how many clusters there are. It will just continue it subdivision as far as we say.

---
What are the use of clustering? #flashcard #FDS #KMeans 
	Clustering can be used to analyze data and understand patters. It can also be used for compression as we represent a cluster by a single value at the mean and a wight. This is called vector quantization (as we quantize to the cluster mean).

---
What are the two types of clustering? #flashcard #FDS #KMeans 
	These are partitional clustering and hierarchical clustering. In partial clustering every point is assigned one cluster and they don't overlap. In hierarchical clustering there are many cluster that build up a hierarchy. As we go down the hierarchy the clusters get smaller and smaller.

---
How does k-means work? #flashcard #FDS #KMeans 
	We have some $D$-dimensional datapoints and we want $K$ clusters. We initialize $K$ cluster centers so $m_k$ for $1\le k\le K$ we then assign each point to a cluster based on how close the center is to that point. We can then update the centers by taking the average of the positions of the elements of the clusters. We repeat this until the number of points under each center doesn't change (when the centers don't change).

---
How can the choice of centers influence the running of the algorithm and what are the different techniques to choose the means? #flashcard #FDS #KMeans 
	The choice of means can change the eventual cluster produced and in fact this algorithm can have many outcomes. The choice of centers determines in part the outcomes therefore. There are four options. We can pick random points, assign each point to a cluster than calculate means, pick extreme points we can set to the mean and then perturb.

---
How can we evaluate the error in a k-means cluster assignment? #flashcard #FDS #KMeans 
	We can use a sum of squared distances from the cluster means. This would cause smaller tighter cluster rather than more inaccurate ones to be better performing.

---

What is the main difference between k-means and (gaussian) mixture models? #flashcard #MachineLearningUni #GaussianMixtureModels
	In K-means there was **hard assignment** means a point either belonged to a cluster or it didn't in (G)MMs this is relaxed and each point is described by the probability of it being in any given cluster.

---
How are mixture models described? #flashcard #MachineLearning #GaussianMixtureModels 
	Mixture models are described by a number of distributions in space which are our clusters. We can then calculate for points in this space the probability they belong to any given  cluster.

---
How might we generate our dataset given the means and covariances of gaussian cluster describing it?  #flashcard #MachineLearning #GaussianMixtureModels 
	For any point $x_n$ we can say the probability that it was generated for a given dataset with mean $\mu_k$ and covariance $\Sigma_k$ is $$p(x_n|z_{nk}=1,\mu_k,\Sigma_k)=\mathcal N(\mu_k,\Sigma_k)$$where $z_{nk}$ describes what cluster $x_n$ is in. The chance of any point being in cluster $k$ randomly is $\pi_k$ hence we select a cluster from the distribution described by the $\pi_k$ values and then generate a point from a gaussian distribution with corresponding mean and covariance to $k$.

---
What is the probability some point belongs to a k cluster in a GMM? #flashcard #MachineLearning #GaussianMixtureModels 
	This is defined as $$p(z_k=1)=\pi_k\text{ where $0\le\pi_k\le1$ and $\sum_{k=1}^K\pi_k=1$}$$

---
What is the probability of some assignment z of a point is in GMM? #flashcard #MachineLearning #GaussianMixtureModels 
	This would be $$p(\mathbf z)=\prod_{k=1}^K\pi_k^{z_k}$$where $\mathbf z=\{z_1,z_2,\dots,z_k\}$. Hence this is just $\pi_k$ for whichever $k$ such that $z_k=1$.

---
What is the probability of some point given an assignment z? #flashcard #MachineLearning #GaussianMixtureModels 
	The point will be drawn from a gaussian distribution for whichever point has $z_k=1$ this way we have $$p(x|\mathbf z)=\prod_{k=1}^K\mathcal N(x|\mu_k,\Sigma_k)^{z_k}$$

---
What is the responsibility for some zk assignment to cluster k value value for a datapoint? #flashcard #MachineLearning #GaussianMixtureModels  
	This will be $$\gamma(z_k)=p(z_k=1|x)=\frac{\pi_k\mathcal N(x|\mu_k,\Sigma_k)}{\sum_{j=1}^K\pi_j\mathcal N(x|\mu_j,\Sigma_j)}$$which is the probability some a gaussian generated $x$ normalized over al the other gaussians.

---
How can we solve the GMM problem with maximum likelihood? #flashcard #MachineLearning #GaussianMixtureModels 
	We have a dataset $X$ and we want to find $\pi$, $\mu$ and $\Sigma$ for all $k$ hence we maximize $$p(x|\pi,\mu,\Sigma)=\prod_{n=1}^N\sum_{n=1}^K\pi_k\mathcal N(x_n|\mu_k,\Sigma_k)$$which we can do by maximizing log likelihood which is $$L=\log p(x|\pi,\mu,\Sigma)=\sum_{n=1}^N\log\left(\sum_{n=1}^K\pi_k\mathcal N(x_n|\mu_k,\Sigma_k)\right)$$

---
What is the problem with solving GMM through maximum likelihood and how is this solved?  #flashcard #MachineLearning #GaussianMixtureModels 
	The problem is that we take the log of a sum and so to maximize the whole equation we can like maximize for a few points this means the gaussians will collapse as some points giving infinite values. To get around this **expectation maximization** is used.

---
What is the key idea behind expectation maximization?  #flashcard #MachineLearning #GaussianMixtureModels 
	The key idea is that instead of maximizing our likelihood $L$ directly we find some function $\mathcal B$ that is always small than $L$ and so by maximizing $\mathcal B$ we maximize $L$.

---
What is Jensen's inequality?  #flashcard #MachineLearning #GaussianMixtureModels 
	This is $$\log \mathbb E_{p(z)}[f(z)]\ge\mathbb E_{p(z)}[\log f(z)]$$That is we can swap a $\mathbb E$ and a $\log$ to get a function that is always smaller.

---
What is the formula found for B in order to run expectation maximization? #flashcard #MachineLearning #GaussianMixtureModels 
	The formula for $\mathcal B$ is $$\mathcal B=\sum_{n=1}^N\mathbb E\left[\log\frac{\pi_k\mathcal N(x_n|u_k,\Sigma_k)}{\gamma_{nk}}\right]\le L$$

---
What are the two steps in the EM algorithm? #flashcard #MachineLearning #GaussianMixtureModels 
	These are expectation where we find the optimal $\gamma_{nk}$ values the maximization where we find the optimal $\pi_k$, $\mu_k$ and $\Sigma_k$ values.

---
How are the gamma values found in the E step in EM? #flashcard #MachineLearning #GaussianMixtureModels 
	These are found via the formula $$\gamma_{nk}=\frac{\pi_k\mathcal N(x_n|\mu_k, \Sigma_k)}{\sum_{j=1}^K\mathcal N(x_n|\mu_j,\Sigma_j)}$$that is the normalized probability a given point is in any of the distributions.

---
How is the pi, mean and covariance values calculated for a given dataset? #flashcard #MachineLearning #GaussianMixtureModels 
	$\pi_k$ is calculated as the the average responsibility so average gamma values for $k$: $$\pi_k=\frac1N\sum_{n=1}^N\gamma_{nk}$$ Then the mean values are calculated via a weighted average of all points by the clusters relative responsibility to them $$\mu_k=\frac{\sum_{n=1}^N\gamma_{nk}x_n}{\sum_{n=1}^N\gamma_{nk}}$$Then the covariance is the weighted covariance of all points by the clusters relative responsibility to them $$\Sigma_k=\frac{\sum_{n=1}^N\gamma_{nk}(x_n-\mu_k)(x_n-\mu_k)^T}{\sum_{n=1}^N\gamma_{nk}}$$

---
How does the the likelihood reached by EM change ad the number of components K changes?  #flashcard #MachineLearning #GaussianMixtureModels 
	If we increase the number of components the likelihood goes to infinity as the mean can match the point and the mean reduces to nothing.

---

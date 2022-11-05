What does K means aim to do? #flashcard #MachineLearning #KMeans
	In K means we are trying to assign every point to a cluster. We want to ensure similar data points are close together. Hence allowing us to examine out data.

---
What is the specific problem formulation in K means?  #flashcard #MachineLearning #KMeans 
	We are given $N$ data points and we want to classify each of the points to one of $K$ clusters. We want to do this in a way such that similar data points are all in the same cluster.

---
What is the mathematical aim of K means?  #flashcard #MachineLearning #KMeans 
	We are given $N$ datapoints so a dataset $X=\{x_1,x_2,\dots,x_N\}$ and we want to for each $x_n$ and $k$ predict $r_{nk}$ which is $1$ if $x_n$ belongs in cluster $k$ and $0$ otherwise. We want to find this where all $\mu_k$s (the center of each cluster) is unknown.

---
What is the distortion function in K means want what does it mean?  #flashcard #MachineLearning #KMeans 
	This distortion function is $$J=\sum_{n=1}^N\sum_{k=1}^Kr_{nk}||\textbf x_n-\mu_k||^2$$ this is the summed distance from each point to its clusters mean (center). Hence is minimized if the cluster means and assignments fit the data well.

---
How is K means solved with reverence to the distortion function? #flashcard #MachineLearning #KMeans
	K means is solved by interactively refining the $\mu_k$ values and then the $r_{nk}$ values. So first we fix $\mu_k$ and note we can change the $r_{nk}$ values to minimize each $x_n$ values distance to its cluster (pick the nearest one). Then differentiating $J$ for each $k$ we find $\mu_k$ to be the average of the points in the $k$ cluster (all $x_n$s with $r_{nk}=1$).

---
What happens to the distortion value reached in K means as we increase K? #KMeans #MachineLearning #KMeans
	As $K$ reaches $N$ the values for $J$ (distortion) reached becomes $0$ as each datapoint can have its own datapoint such that the means is that point and so the distortion from the means is 0.

---
What problems can be run into when it comes to initializing the means in K means? #flashcard #MachineLearning #KMeans 
	The final minima reached will be dependent on the initial means so they can lead to poor clustering such that clearly different clusters are identified as the same.

---
What methods can be tried to reduce K means error? #flashcard #MachineLearning #KMeans 
	We can initialize to a subset of the data to try to get a more average estimation of values. We can repeat the clustering various times and select the best. Or we can use K-means++. But often it is better to use domain knowledge.

---
What is hard vs soft assignment in clustering? #flashcard #MachineLearning #KMeans 
	In **hard assignment** we simply assign each datapoint to a cluster in a binary way. In **Soft assignment** we instead give a probability a data point is in each cluster.

---

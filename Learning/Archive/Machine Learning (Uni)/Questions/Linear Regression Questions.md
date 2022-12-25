What is S called in linear regression and what is its form?  #flashcard #MachineLearningUni #LinearRegression
	$S$ is the dataset and it made out of pairs of $x$ feature vectors and $y$ ground truth values. It describes loosely what values should lead to what models given by our network.

---
What is the model in linear regression?  #flashcard #MachineLearningUni #LinearRegression
	The model is a function we are trying to create going form $x$s to $y$s. In linear regression it has the form $f(x)=w^Tx+b$ without any use of *feature* and $f(x)=w^T\phi(x)$ when features are used.

---
What is L in linear regression?  #flashcard #MOB #LinearRegression 
	This is the loss or just some function we are trying to minimize as it describes how badly out model fits the data.

---
What values is found for b in standard linear regression without features?  #flashcard #MOB #LinearRegression 
	The values of $\bar y-w^T\bar x$ is found that is the average $y$ values minus the averages of the $x$ features weighted by the weights $w$.

---
What is $X$ in linear regression and broadly machine learning?  #flashcard #MOB #LinearRegression 
	This is a matrix of the $x$ feature vectors. 

---
What it $w$ found to be linear regression?  #flashcard #MOB #LinearRegression 
	$w$ is found to be $(XX^T)^{-1}Xy$ 

---
How can b be brought into w with the use of a dummy feature?  #flashcard #MOB #LinearRegression 
	The idea is if we append a 1 onto every $x$ values we can treat b as simply the weight corresponding to this.

---
What does the idea of feature to the model we are creating as we add more features?  #flashcard #MOB #LinearRegression 
	Every time we add a feature we are simple adding another term to our model which is weighted into our calculation of $y$. We can do this with any arbitrary function on our input features. But we can never do more they weights in these values. We cannot change their shape for example. That is we are still *linear in the features*.

---
How does assuming a gaussian distribution lead to means squared error?  #flashcard #MOB #LinearRegression 
	When we assume a gaussian distribution on the data then work through maximizing the likelihood given the weights $w$ we find that the maximum is equal to if we were maximizing an MSE.

---
What is the problem with finding w via inverting the matrix (XX^T)?  #flashcard #MOB #HardwareSoftwareArchitecture 
	This takes time $O(N^3)$ in the number of samples in $X$ hence cannot be used for large datasets.

---
	
What are the three main uses of PCA? #flashcard #MachineLearning #PCA
	The three main uses of PCA are 1) **Data compression** 2) **Data visualization** and 3) **Data Processing**.

---
What does PCA aim to accomplish in terms of dimensions? #flashcard #MachineLearning #PCA
	PCA aims to reduce the number of dimensions such that data can be describes using as little information as possible. We reduce $d\to k$ such that all the new dimensions are uncorrelated and hence we aren't wasting any information.

---
In PCA to take our X matrix of dimension d to k to becomes Z what do we need? #flashcard #MachineLearning #PCA
	We need a new matrix $U$ of dimensions $d\times k$ such that $XU=Z$. When $X$ has dimensions $m\times d$ and $Z$ has dimensions $m\times k$.

---
What are the principal components in terms of projections? #flashcard #MachineLearning #PCA
	The principal components are projections of the data onto axis such that all the original datapoints are uncorrelated in these new projected values.

---
How are the PCA components ordered? #flashcard #MachineLearning #PCA 
	They are ordered in terms of the variance the dataset has within the projection they describes. That is the data projected in the first PCA has the largest possible share of the variance. The second has the largest possible share left over from that and so on.

---
What are we trying to maximize when finding u1 the first principal component? #flashcard #MachineLearning #PCA
	We are maximizing the variance in the projection of $u_1$ for our dataset. That is we are maximizing $$\text{Var}[z_1]=\text{Var}[Xu_1]$$

---
How can we compute the variance in a principal components axis given the data has zero mean? #flashcard #MachineLearning #PCA 
	If some data *vertically stacked* has zero mean then the variance is $X^TX$. Hence $\text{Var}[Xu_1]$ becomes $$\text{Var}(z_1)=\text{Var}(Xu_1)=u_1^TX^TXu_1=u_1^T\Sigma_Xu_1$$

---
What constrain must we have on the $u_k$ principal components while maximizing the variance in their axis? #flashcard #MachineLearning #PCA 
	We must maintain $||u_1||=u_1^Tu_1=1$

---
What is the lagrangian created to solve PCA? #flashcard #MachineLearning #PCA 
	After we add the condition that $||u_1||=1$ combines with our maximization problem $\max_{u_1}u_1^T\Sigma_Xu_1$ we get $$L(u_1,\lambda_1)=u_1^T\Sigma_Xu_1-\lambda_1(u_1^Tu_1-1)$$

---
What is the solution to maximizing the variance in a given axis for PCA? #flashcard #MachineLearning #PCA
	This will be the eigen values and eigen vectors of the covariance matrix of the data $\Sigma_X$. That is the values fulfilling $$\Sigma_xu_1=\lambda_1u_1$$Where $\text{Var}[z_1]=\text{Var}[Xu_1]=u_1^T\Sigma_Xu_1=\lambda_1$ since $||u_1||=1$. Hence $u_1$ is the eigen vector with the largest eigen value $u_2$ the second largest and so on.

---
What are some things PCA isn't good for? #flashcard #MachineLearning #PCA 
	It isn't goof for reducing overfitting and it isn't good to use before linear classifiers.

---

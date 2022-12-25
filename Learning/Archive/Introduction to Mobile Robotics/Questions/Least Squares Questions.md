What is least squares method? #flashcard #MOB #LeastSquares
	The least squares method is a way of estimating a value behind some mode. That is we take some readings $y$ and a model that would produce this $y$ then we predict the $x$ that formed the $y$.

---
What is the squared error criterion? #flashcard #MOB #LeastSquares 
	This is the criterion for the solution to least squares is is $$\hat x_{LS}=\arg\max_x\mathcal L(x)=\arg\max_x\left(\sum_{i=1}^Ne_i^2\right)$$

---
With a linear model what is the form of the model with m measurement and n variables in least squares? #flashcard #MOB #LeastSquares 
	This would be $$\textbf y=\textbf{Hx}+\textbf v$$ Where $\mathbf H$ is the Jacobian matrix of partial derivative of $\mathbf y$ with respect to $\mathbf x$.

---
With a least squared method give H and y what is the x solution? #flashcard #MOB #LeastSquares 
	After differentiating the loss we find $$\hat x_{LS}=(\mathbf H^T\mathbf H)^{-1}\mathbf H\mathbf y$$

---
What is weighted least squares? #flashcard #MOB #LeastSquares 
	This is a version of least squares where we weight the measurement so that some are more important to our final answer than others. Say for example by the variance in the error for each reading$$\mathcal L(\textbf x)=\frac{e_1^2}{\sigma_1^2}+\frac{e_2^2}{\sigma_2^2}+\dots+\frac{e_m^2}{\sigma_m^2}$$

---
Given the covariance matrix R what is the loss for weighted least squares? #flashcard #MOB #LeastSquares 
	The loss for least squares is $$\mathcal L(\textbf x)=\frac{e_1^2}{\sigma_1^2}+\frac{e_2^2}{\sigma_2^2}+\dots+\frac{e_m^2}{\sigma_m^2}=\mathbf e^T\mathbf R^{-1}\mathbf e=(\mathbf y-\mathbf H\mathbf x)^T\mathbf R^{-1}(\mathbf y-\mathbf H\mathbf x)$$

---
What is the x solution with weighted least squares and covariance matrix R? #flashcard #MOB #LeastSquares 
	One we have differentiated the loss $$\mathcal L(x)=(\mathbf y-\mathbf H\mathbf x)^T\mathbf R^{-1}(\mathbf y-\mathbf H\mathbf x)$$We can find the solution values to be $$\hat{\mathbf x}_{WLS}=(\mathbf H^T\mathbf R^{-1}\mathbf H)^{-1}\mathbf H^T\mathbf R^{-1}\mathbf y$$

---
What is the idea with recursive least squares? #flashcard #MOB #LeastSquares 
	With recursive least squares we need to continually update a estimation of the state as we get more measurements. Hence we need an update function taking in a predicted state and some measurements and adjusting our prediction. 

---
What will the errors be in recursive least squares with a linear model? #flashcard #MOB #LeastSquares 
	With a linear model $\mathbf H_k$ for timestep $k$ we will have the errors as $$\mathbf e_k=\mathbf y_k-\mathbf H_k\mathbf x$$

---
What is the correction term in recursive least squares? #flashcard #MOB #LeastSquares 
	This is $$\mathbf y_k-\mathbf H_k\hat{\mathbf x}_{k-1}$$for an update from $k-1$ to $k$.

---
What is the update for recursive least squares estimation? #flashcard #MOB #LeastSquares 
	This is $$\hat{\mathbf x}_k=\hat{\mathbf x}_{k-1}+\mathbf K_k(\mathbf y_k-\mathbf H_k\hat{\mathbf x}_{k-1})$$where $\mathbf K_k$ is the gain matrix.

---
What is the error in recursive least squares? #flashcard #MOB #LeastSquares 
	This will be $$\mathcal L_{RLS}=\mathbb E[(\mathbf x-\hat{\mathbf x}_k)^2]=\mathbb E[\mathbf e_k^T\mathbf e_k]=\sigma^2_k$$That is we want the minimum variance of the latest estimation.

---
What is the formula for the gain matrix in RLS? #flashcard #MOB #LeastSquares 
	This is $$\mathbf K_k=\mathbf P_{k-1}\mathbf H_k^T(\mathbf H_k\mathbf P_{k-1}\mathbf H_k^T+\mathbf R_k)^{-1}$$

---
What is the update for Pk in RLS? #flashcard #MOB #LeastSquares 
	This will be $$\mathbf P_k=(\mathbf I-\mathbf K_k\mathbf H_k)\mathbf P_{k-1}$$

---

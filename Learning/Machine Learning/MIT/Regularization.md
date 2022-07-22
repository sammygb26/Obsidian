# Regularization
A major problem in machine learning is **overfitting**, reducing **variance**. This is when the network is trained to capture the noise in the data and therefore doesn't generalize to the true data. In **regularization** the coefficients are constrained/ regularized / shrank towards 0. It discourages learning a more *complex*, *flexible* model to avoid the risk of overfitting. In standard machine learning we have a loss function for example in a simple regression our loss function could be a simple Residual Sum of Squares (RSS) loss:

![[Pasted image 20220704201318.png]]

With noise in the data this setup will fit the noise and the coefficients won't generalize well to future data.

### Ridge Regression
We can modify *RSS* by adding a shrinkage quality. This will be the squared sum of the $\beta$ coefficients.

![[Pasted image 20220704201525.png]]

$\lambda$ is a tuning parameter deciding how much *flexibility* we are affording the model. Therefore to minimize this loss we have to minimize the coefficients. We don't shrink $\beta_0$ which is the intercept, values of our regression when all $x_i=0$. With $\lambda=0$ there will be no penalty but as $\lambda\to\infty$ the impact of the shrinkage penalty grows and the coefficient estimates approach 0. We must therefore select a good coefficient. This method is also called **L2 norm**. In normal regression the coefficients are *scale equivariant* if we multiply the input by some constant $c$ then the coefficients are scaled by a factor 1/c. This way for the multiplication of the coefficients and predictor will always remain the same $(X_j\beta_j)$. This isn't the case the **ridge Regression** therefore the input must be standardized as follows.

![[Pasted image 20220704202856.png]]

##### Weight Decay
When we are performing **l2 regularization** on a neural network model.

### Lasso
This is another variation in which the absolute value/ modulus/ magnitude of the coefficients is minimized instead. This version is known as **L1 norm**.

![[Pasted image 20220704203251.png]]

As with above $\lambda$ scales the effect and the goal is just to minimize the coefficients. 

### Constraint Functions
These two equations for *lasso* and *ridge regression* are also called **constraint functions**. This comes from a perspective where we think of solving them as finding for the case of *ridge regression* an evaluation of all the $\beta_i$ coefficients such that their squared sum is less and sum $i$ and the sum of the moduli is less than $s$ in the case of *lasso*.

$$\sum_{i=1}^n\beta_i^2\le s\hspace{64pt}\sum_{t=1}^n|\beta_i|\le s$$

This will be for a optimal assignment of $\beta_i$ coefficients. This means the coefficients will have the smallest RSS loss for some circle around 0,0 in the case of *ridge regression* and diamond for *lasso* (for 2 coefficients)

![[Pasted image 20220704205656.png]]

The red ellipses show the contours for solo RSS evaluation.  This view has the effect of explaining why *lasso* tends to set coefficient values to 0 as the optimal evaluations for smoothies loss functions will tend to intersect corners at their minima (within the constraint area). But *ridge regression* has a circular area for any given constrain and therefore tends not to set coefficients to 0. This means the model will use all possible input information never reducing a term to 0.

### What does Regularization Achieve
Most least squares model will have some variance in them. Therefore our model won't generalize for a data set different than its training data. **Regularization** significantly reduces the *variance* of the model without a substantial increase in its *bias*. You can keep increasing $\lambda$ which will further reduce variance but at the cost of increasing bias.

[[Regularization Questions]]
Least squares is a method used to get estimate values, we will explore why and how it works. We can start by defining a model. For example $$y=x+v$$where $y$ is a measurement, $x$ is the true value and $v$ is the noise. We can take many measurements and then for each take fine the error as $e_i=y_i-x$. We can use all say $N$ values to define a cost function. $$\mathcal L(x)=\sum_{i=1}^Ne_i^2$$In the **Method of Least Squared** we want to find an $x$ that minimizes this cost function. $$\hat x_{LS}=\arg\max_x\mathcal L(x)=\arg\max_x\left(\sum_{i=1}^Ne_i^2\right)$$This equation is called the **Squared Error Criterion**. In this case since we have multiple $y$ values we have a $\textbf y$ vector of those values. We can also derive this in matrix form using multiple values at once. $$\textbf y=
\begin{bmatrix}y_1\\\vdots\\y_m\end{bmatrix}=
\begin{bmatrix}e_1\\\vdots\\e_m\end{bmatrix}=
\begin{bmatrix}H_{11}&\dots &H_{1n}\\\vdots&&\vdots\\H_{m1}&\dots&H_{mn}\end{bmatrix}
\begin{bmatrix}x_1\\\vdots\\x_n\end{bmatrix}+\begin{bmatrix}v_1\\\vdots\\v_m\end{bmatrix}=
\textbf{Hx}+\textbf v$$In the above definition $\textbf H$ is a **Jacobian Matrix** of partial derivatives of $\textbf y$ with respect to $\textbf x$. This act as coefficients in our model$$
\textbf e=
\begin{bmatrix}e_1\\\vdots\\e_m\end{bmatrix}=
\begin{bmatrix}y_1\\\vdots\\y_m\end{bmatrix}-
\begin{bmatrix}H_{11}&\dots &H_{1n}\\\vdots&&\vdots\\H_{m1}&\dots&H_{mn}\end{bmatrix}
\begin{bmatrix}x_1\\\vdots\\x_n\end{bmatrix}=
\textbf y-\textbf{Hx}$$Now we can write our loss function as $$
\begin{align}\mathcal L(\textbf x)&=\textbf e^T\textbf e\\
&=(\textbf y-\textbf{Hx})^T(\textbf y-\textbf{Hx})\\
&=\textbf y^T\textbf y-\textbf x^T\textbf H^T\textbf y-\textbf y^T\textbf{Hx}+\textbf x^T\textbf H^T\textbf{Hx}\end{align}
$$Then the $\hat{\textbf x}$ becomes $\hat{\textbf x}=\arg\min_x\mathcal L(\textbf x)$ as before.

### Finding x
We can see that our function is essentially a quadratic taking in $\textbf x$. Because of this and the fact that the *residuals* will get large if $x$ is extreme in either direction we know there will be a minima where the derivative of the loss function equals zero. Hence we can take it giving $$\left.\frac{\partial\mathcal L}{\partial \textbf x}\right|_{\textbf x=\hat{\textbf x}}=-2\textbf y^T\textbf H+2\hat{\textbf x}^T\textbf H^T\textbf H=0\implies\hat{\textbf x}_{LS}=(\textbf H^T\textbf H)^{-1}\textbf H\textbf y$$Hence we can find the estimation of a linear system of equations as long as we have its model, we know $\textbf H$ and have a set of measurements $\textbf y$.

# Weighted Least Squares
This is an extension of the least squares method where some measurements are more important than others. This could occur if measurements have a different level of noise. We assume the error has mean 0 and so $$\mathbb E(v_i^2)=\sigma_i^2\hspace{16pt}(i=1,\dots,m)$$We can give noisier measurements less weights by dividing them by their variance. $$\mathcal L(\textbf x)=\frac{e_1^2}{\sigma_1^2}+\frac{e_2^2}{\sigma_2^2}+\dots+\frac{e_m^2}{\sigma_m^2}$$With the requirement that the noise has zero-mean and are all independent we can writ the above as a covariance matrix $\textbf R$ with $\mathcal L(\textbf x)=\textbf e^T\textbf R^{-1}\textbf e$ then $\textbf R$ is defined as:

![[Pasted image 20221024100317.png]]

Hence our loss when expanded our becomes: 

![[Pasted image 20221024100347.png]]

Which we can again solve for an estimate of $\hat x$ as:

![[Pasted image 20221024100418.png]]

# Recursive Least Squares
Here we get data piecemeal (a stream of data) but we cannot recalculate with all our data at once as this will quickly becomes expensive. if we build a model of RLS after $k-1$ recursion we will have some estimate for $\textbf x$ to be $\hat{\textbf x}_{k-1}$. Then we get a new measurement $\textbf y_k$ which still satisfy the linear model $\textbf y_k=\textbf H_k\textbf x+\textbf v_k$. Hence we get the errors as:

![[Pasted image 20221024100913.png]]

We want to update $\hat{\textbf x}_{k-1}\to\hat{\textbf x}_k$. We want to test how well our results match the new measurements this is called the **correction term** equal to $(\textbf y_k-\textbf H_k\hat{\textbf x}_{k-1})$. If this is close to 0 we don't need to update our guess and if its not we do. Therefore we can get the model update as:

![[Pasted image 20221024101215.png]]

Where $\textbf K_k$ is called the **gain matrix** but how do we find this gain matrix? We need to some value that always takes us closer to $\textbf x$ but not too slow or too fast.  Said in maths we want to minimize the variance of the latest estimation:

![[Pasted image 20221024101550.png]]

Now we need to minimize this cost function with respect to $\textbf K_k$ hence we need it in terms of $\textbf K_k$. Subbing in our error function (top) will reach a dead end so we introduce an *estimation-error* as:

![[Pasted image 20221024101850.png]]

This gives us:

![[Pasted image 20221024101906.png]]

### Solve the Optimum Estimation for RLS
We start by taking our recursive model and find a relationship to $\mathbb E(\textbf e_k)$.

![[Pasted image 20221024102158.png]]

We can then take this equation to the definition of $\textbf P_k$ to give a recursive relationship for $\textbf P_k$.

![[Pasted image 20221024102337.png]]

Here $\textbf R_k$ is the $m\times m$ covariance matrix as defined for WLS so represents the Nosie in our different measurements. Here it will be $\textbf I$ the identity matrix.  We take $\textbf P_k$ back to our cost function and calculate the partial derivative with respect to $\textbf K_k$ to get:

![[Pasted image 20221024102705.png]]

Setting this to 0 we can find the optimal $\textbf K_k$ as 

![[Pasted image 20221024102732.png]]

Taking the definition of $\textbf P_k$ back in we reach:

![[Pasted image 20221024102847.png]]

### RLS in action
Putting the above definitions together we get a three step process.

1. **Initialize the estimator** - we manually give the algorithm the first estimator. This requires the values themselves $\hat{\textbf x}_0$ and the covariance matrix $\hat{\textbf P}_0$. This could be estimated from existing measurements for example:

![[Pasted image 20221024103128.png]]

2. **Establish the model** - Now we establish the linear model for the measurements to find the Jacobian matrix $\textbf H_k$. 

![[Pasted image 20221024103237.png]]

3. **Begin recursion** - Now we recursively compute the next estimation based on the new measurements. We first estimate our gain matrix $\textbf K_k$ and then use this to estimates $\hat{\textbf x}_k$. Then we also update our covariance matrix.

![[Pasted image 20221024103408.png]]

[[]]
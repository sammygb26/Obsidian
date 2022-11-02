What is least squares method? #flashcard #MOB #LeastSquares
	The least squares method is a way of estimating a value behind some mode. That is we take some readings $y$ and a model that would produce this $y$ then we predict the $x$ that formed the $y$.

---
What is the squared error criterion? #flashcard #MOB #LeastSquares 
	This is the criterion for the solution to least squares is is $$\hat x_{LS}=\arg\max_x\mathcal L(x)=\arg\max_x\left(\sum_{i=1}^Ne_i^2\right)$$

---
With a linear model what is the form of the model with m measurement and n variables in least squares? #flashcard #MOB #LeastSquares 
	This would be $$\textbf y=
\begin{bmatrix}y_1\\\vdots\\y_m\end{bmatrix}=
\begin{bmatrix}e_1\\\vdots\\e_m\end{bmatrix}=
\begin{bmatrix}H_{11}&\dots &H_{1n}\\\vdots&&\vdots\\H_{m1}&\dots&H_{mn}\end{bmatrix}
\begin{bmatrix}x_1\\\vdots\\x_n\end{bmatrix}+\begin{bmatrix}v_1\\\vdots\\v_m\end{bmatrix}=
\textbf{Hx}+\textbf v$$ Where $\mathbf H$ is the Jacobian matrix of partial derivative of $\mathbf y$ with respect to $\mathbf x$.

---

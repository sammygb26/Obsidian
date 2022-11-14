What is the problem with just fitting a linear binary classifier to data when it comes to generalization? #flashcard #MachineLearningUni #SupportVectorMachines
	The problem is a linear binary classifier can fir the data in many ways that will have the same number of misclassifications; even if the data is linearly separable. Instead we want to maximize the **margin** to make our classifier *generalize* better.

---
What is the margin when it comes to linear classifiers? #flashcard #MachineLearningUni #SupportVectorMachines 
	The margins are shifted versions of the line that are shifted the most to either side of the line but still don't misclassify any labels.

---
How are the margins of a linear classifier defined mathematically? #flashcard #MachineLearningUni #SupportVectorMachines 
	If we have a model defined by $y=w^Tx+w_0$ then our margins can be $$w^Tx+w_0=+1$$ and $$w^Tx+w_0=-1$$ the distance between the two lines/hyperplanes defined by these equations is our margin.

---
What is the formula for the margin r between the decision boundary and one of the margin lines? #flashcard #MachineLearningUni #SupportVectorMachines 
	For a line/hyperplane with the formula $w^Tx+w_0=0$ and lines $w^Tx+w_0=\pm1$ this will be $$r=\frac1{||w||}$$

---
In a support vector machine what are we trying to maximize? #flashcard #MachineLearningUni #SupportVectorMachines 
	We are trying to maximize the **margin** of the linear model. That is we are trying to maximize $1/||w||$. With the condition that our margins are valid. Hence $w^Tx_i+w_0\ge+1$ for all $i$ with $y_i$=+1 and if $w^Tx_i+w_0\le-1$ then $y_i=-1$.

---
What equivalent problem is used to maximize the margins to solve SVM and how do we make it easier to solve? #flashcard #MachineLearningUni #SupportVectorMachines 
	Instead of maximizing $1/||w||$we minimize $\frac12||w||^2$. We add the square to make the problem **convex** so we can get an analytical solution later.

---
What is the form of the solution to SVM? #flashcard #MachineLearningUni #SupportVectorMachines 
	This will be of the form $$w=\sum_{i=1}^n\alpha_iy_ix_i,\text{ }\text{ }\text{ }\alpha_i\ge0$$ where most $\alpha_i=0$ and for the $i$s where this isn't true we say $x_i$ is a **support vector**.

---
What is a support vector? #flashcard #MachineLearningUni #SupportVectorMachines 
	In SVMs the support vector are the vector linearly combined to get $w$. That is in the formula for $w$, $$w=\sum_{i=1}^n\alpha_iy_ix_i,\text{ }\text{ }\text{ }\alpha_i\ge0$$ the support vectors are the $x_i$ values for which $\alpha_i\neq0$

---
How is classification performed with an SVM? #flashcard #MachineLearningUni #SupportVectorMachines 
	We just take the sign of the output that will be $$g(x)=\text{sgn}(w^Tx+w_0)=\text{sgn}\left(\sum_{i=1}^n\alpha_iy_ix_i^Tx+w_0\right)$$

---
What happens in SVMs to the margin r when we choose some other values of +/- instead of 1? #flashcard #MachineLearningUni #SupportVectorMachines 
	The actual values doesn't matter and it only changes the magnitude of the final $w$ found. Working out the math we get $$r=\frac\epsilon{||w||}$$

---
Where do the alpha values come from in the SVM? #flashcard #MachineLearningUni #SupportVectorMachines 
	The $\alpha_i$ values come from the Lagrangians created by the condition that the margins are correct classifiers.

---
What is the lagrangian created when we try to minimize the margin for SVMs? #flashcard #MachineLearningUni #SupportVectorMachines 
	The **margin** is conditioned on the - and + labels being correctly classified by the margin. To work these Lagrangians into the minimization task we use **lagrangian multiplies** of $\alpha_i$ for each $i$ datapoint. This gives $$L(\alpha,w,w_0)=\frac12w^Tw-\sum_{i=1}^n\alpha_i\left(y_i(w^Tx_i+w_0)-1\right)$$for the condition that for all $i$ we have $y_i(w^Tx_i+w_0)\ge1$.

---
What is the Kraush-Kuhn-Tuckert (KKT) condition in SVM? #flashcard #MachineLearningUni #SupportVectorMachines 
	This is the condition that for all $i$ we have in an optimal SVM solution we have $$\alpha_i(y_i(w^Tx_i+w_o)-1)=0$$so either $\alpha_i=0$ or $y_i(w^Tx_i+w_0)=1$.

---
What are the necessary and sufficient conditions for an SVM solution being the optimal one? #flashcard #MachineLearningUni #SupportVectorMachines 
	These are the gradient with respect to $w$ is 0, the gradient with respect to $w_0$ is 0 all the lagrangian $\alpha_i$ values are greater than 0 and $y_i(w^Tx_i+w_0)-1\ge0$ for every $i$.

---
What are soft ad hard margins in SVM? #flashcard #MachineLearningUni #SupportVectorMachines 
	A **hard margin SVM** must satisfy the condition that the margins correctly classify the data. We can relax this to get **soft margin SVMs** where some points can be slightly over the margin and we can have some errors.

---
How is the error function different for soft SVMs as compared to hard SVMs? #flashcard #MachineLearningUni #SupportVectorMachines 
	We relax the condition that all points must be correctly classified and instead allow for each to have some error $\phi_i$ for which it is on the wrong side of the margin. We then minimize the original function and these errors: $$\min_{w,w_0}w^Tw+C(\sum_{i=1}^n\phi_i)$$ where $C>0$ and is usually a **hinge loss**.

---
What is a hinge loss and how is it used for soft margin SVMs? #flashcard #MachineLearningUni #SupportVectorMachines 
	The hinge loss allows us to count negatively only negative errors (ones in the wrong direction). We define it to be $l(t)=\max(0,1-t)$.

---
How are non-linear SVMs created? #flashcard #MachineLearningUni #SupportVectorMachines 
	These are created by **first** projecting the data into higher dimensions (non-linearly) then **second** classifying it in this higher dimension space according to SVM and **thirdly** we project the decision boundary back to our original space.

---
Why do we require the kernel trick in SVM? #flashcard #MachineLearningUni #Boosting 
	When we are using some function function $\phi$ we may require it to output many dimensions in order to fit our boundary well. But the number of dimensions increases the amount of work we need to do in inference and training hence we require a work-around which is *the kernel trick*.

---
What must be true for a kernel to accurately represent some non-linear projection and why is this useful? #flashcard #MachineLearningUni #Boosting 
	It must be true that for all $x_i$ and $x_j$ we have $$k(x_i,x_j)=\phi(x_i)^T\phi(x_j)$$ This is useful from the definition of our SVM function which can be written as within the SVM decision function we only require $\phi(x_i)^T\phi(x)$ where $x_i$ is our weights or support vectors and $x$ is what we are trying to classify.

---
What is the form of the non-linear SVM's decision function? #flashcard #MachineLearningUni #Boosting 
	This is $$f(x)=\sum_{i=1}^n\alpha_iy_i\phi(x_i)^T\phi(x)+w_0$$

---
What is the optimal loss when solving for SVM? #flashcard #MachineLearningUni #Boosting 
	This will be $$L(\alpha,w,w_0)=-\frac12\sum_{i,j=1}^ny)iy_j\alpha_i\alpha_jx^T_ix_j+\sum_{i=1}^n\alpha_i$$

---
Why does the kernel trick in SVM work?b #flashcard #MachineLearningUni #Boosting 
	We only need to calculate $\phi(x_i)^T\phi(x_j)$ for non-linear SVM to work we have $k(x_i,x_j)=\phi(x_i)^T\phi(x_j)$ but $k$ is much easier to calculate. This basically cuts out the number of dimensions by using one $x$ values as a key describing the nonlinearity applied to the other. 

---
What are some popular kernels for SVM? #flashcard #MachineLearningUni #Boosting 
	The **polynomial**, **radial basis** and **hyperbolic tangent** are common.

---
What is the formula for the polynomial kernel in SVM? #flashcard #MachineLearningUni #Boosting 
	This is $$k(a,b)=(1+a^Tb)^2$$

---
What is the formula for the radial basis function kernel (RBF)? #flashcard #MachineLearningUni #Boosting 
	This would be $$k(a,b)=e^{-\gamma||a-b||^2}$$ where $\gamma>0$

---
What is the formula for the hyperbolic tangent kernel? #flashcard #MachineLearningUni #Boosting 
	This is $$k(a,b)=\tanh(k_1a\cdot b+k_2)$$ where $k_1>0$ and $k_2<0$

---
When trying to make a kernel what properties should it satisfy? #flashcard #MachineLearningUni #Boosting 
	It should satisfy $$k(x,z)=x\cdot z=z\cdot x=k(z,x)$$, $$k(x,z)^2\le k(x,x)k(z,z)$$ and $$K=(k(x_i,x_j))$$ which is a $n$-by-$n$ matrix that is positive semi-definite

---
What is Mercer's theorem? #flashcard #MachineLearningUni #Boosting 
	This stats that if $k$ is a continuous symmetric non-negative definite kernel, then $k$ can be expressed as $$k(x,z)=\sum_{i=1}^\infty\lambda_i\phi_i(x)\phi_i(z)$$ where $\{\phi(i)\}$ are eigen-functions, $||\phi_i||=1$ and $\{\lambda_i\}$ are positive eigenvalues $\lambda_i>0$

---
When making new kernels what properties hold? #flashcard #MachineLearningUni #Boosting 
	1. The **sum** of kernels is still a valid kernel 
	2. Some $a>$ times a kernel is still a valid kernel. 
	3. The **product** of two kernels is still valid. 
	4. The product of a function on the input vectors $x$ and $z$ is still a valid kernel. 
	5. Some kernel applied to a non-linear projection of the two input vectors is still valid. 
	6. $k(x,z)=x^TBz$ is valid when $B$ is $n$-by-$n$.

---
How is w0 found in SVM? #flashcard #MachineLearningUni #Boosting 
	We use $y_i(w^Tx_i+w_0)=1$ for support vectors.

---
How is C chosen for soft SVMs? #flashcard #MachineLearningUni #Boosting 
	This is chosen using a validation data set we aren't training on.

---

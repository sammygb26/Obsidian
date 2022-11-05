What problem does regularization hope to solve? #flashcard #MachineLearning #Regularization
	Regularization hopes to solve the problem of overfitting by reducing the **flexibility** of the network.

---
What is overfitting in machine learning? #flashcard #MachineLearning #Regularization 
	This is when our model fits the randomness of our dataset and so doesn't generalize to data outside of our dataset since these random quirks only exist in the dataset.

---
How does basic ridge regression work when regularizing onto of some RSS loss? #flashcard #MachineLearning #Regularization 
	In ridge regression we are regressing a hyperplane into some space. When we add ridge regression we add on top of this a regularizing term.  $$\textit{Loss}+\lambda\sum_{i=1}^p\beta_j^2$$ Here $\beta$s are the coefficients. We add the extra term to cause the learning process to minimize the coefficients as much as possible.

---
What does the lambda term represent in ridge regression and lasso? #flashcard #MachineLearning #Regularization 
	This is a parameter deciding the flexibility of the model. With a higher lambda the model will be less flexible aswell as have reduced variance. This will eventually increase the bias of the network as $\lambda\to\infty$ 

---
What is another name for ridge regression? #flashcard #MachineLearning #Regularization 
	This is also called **l2 norm**.

---
What is l1 and l2 regularization? #flashcard #MachineLearning #Regularization 
	In **l1 regularization** we add a regularization term that is just the sum of the absolute/ modulo of the coefficients to the loss. In **l2 regularization** we add a term that is the sum of the squares of the coefficients.

---
Why is l2 regularization also called weight decay? #flashcard #MachineLearning #Regularization 
	l2 regularization is added onto our loss and our loss is differentiated to get our gradients. However the separate regularization part at least with l2 becomes just $\lambda W$ for gradients W. As we take the gradients of each step we are just taking a fraction of them away hence they are decaying and the name.

---
How does basic lasso regularization work (l1 norm)? #flashcard #MachineLearning #Regularization 
	This works by adding on a sum of the modulus of the coefficients. This way our network's loss is high when the coefficient values are far from 0.

---


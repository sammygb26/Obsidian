What is a common form for generalization bounds? #flashcard #MachineLearningUni #Generalization #Generalization2 
	![[Pasted image 20221024152312.png]]

---
What is C(H) a measure of in generalization? #flashcard #MachineLearningUni #Generalization #Generalization2 
	$C(\mathcal H)$ is a measure of the capacity of $\mathcal H$.

---
What is the sample complexity of a generalization bound? #flashcard #MachineLearningUni #Generalization #Generalization2
	A **generalization bound** gives allow sus to define some $\epsilon$ difference we want from our training data to our test data which we then need to happen $1-\delta$ percent of the time. But this can be rearranged to give the complexity of a function giving the number of **samples needed**
	![[Pasted image 20221024152823.png]]

---
What is VC generalization bounds? #flashcard #MachineLearningUni #Generalization #Generalization2 
	Vapnik-Chernonenkis  generalization bounds
	![[Pasted image 20221024153123.png]]
	Which is independent of learning algorithms and how ERM is done.

---
What is the VC dimension for linear classifiers taking in some p features? #flashcard #MachineLearningUni #Generalization #Generalization2 
	This would be $p-1$ for linear classifiers of the form $$\mathcal H=\{x\mapsto w^T\phi(x):w\in\mathbb R^p\}$$

---
Form multilayer perceptrons with $p$ edges what is the VC-dim? #flashcard #MachineLearningUni #Generalization #Generalization2 
	This would be $$\text{VC-dim}(\mathcal H)=O(p\log p)$$

---
What is the definition of a hypothesis class shattering? #flashcard #MachineLearningUni #Generalization #Generalization2 
	$\mathcal H$ shatters some $n$ if there is some arrangement of $n$ points such that every way of labeling them $\{-1.+1\}$ can be produced by $\mathcal H$.

---
How is the VC dimension of some class defined with respect to shattering? #flashcard #MachineLearningUni #Generalization #Generalization2 
	The VC dimension of some hypothesis class $\mathcal H$ is the max number of points $\mathcal H$ can shatter.

---
What is the capacity generalization trade off? #flashcard #MachineLearningUni #Generalization #Generalization2 
	Given our VC generalization bound we can see that $\mathcal H$ being large makes the minimum we can find for test performance lower hence in theory decreasing loss. But the generalization loss increases as our VC dimension reaches an amount close to being able to memorize our data.

---
How does performing GD or SGD relate to the ERM solution? #flashcard #MachineLearningUni #Generalization #Generalization2 
	We are searching for the ERM solution but it will only give us an approximate solution for this.

---
What are surrogate losses? #flashcard #MachineLearningUni #Generalization #Generalization2 
	This is the idea that we use losses that are easy to optimize but they don't actually describe performance in the task we want called the **task loss**.

---
What is task loss? #flashcard #MachineLearningUni #Generalization #Generalization2 
	Task loss is the performance in the task we actually care about however we usually use other optimizers that are easier to differentiate called surrogate losses.

---
What are the three errors in honest in finding machine learning solutions? #flashcard #MachineLearningUni #Generalization #Generalization2 
	These would be **optimization error**, **estimation error** and **approximation error**.

---
What is optimization error? #flashcard #MachineLearningUni #Generalization #Generalization2 
	This is the error in our machine learning solution given by the mismatch between our surrogate loss (we can optimize with) and our task loss we actually care about when evaluating the program.

---
What is the definition of underfitting? #flashcard #MachineLearningUni #Generalization #Generalization2 
	A model is **underfitting** if there is another model that has lower training error.
	$g$ is underfitting if there exists $f$ such that $L_S(f)<L_S(g)$.

---
What is the definition of overfitting? #flashcard #MachineLearningUni #Generalization #Generalization2 
	A model is **overfitting** if there exists some other model that has higher training loss but lower generalization error. $g$ is overfitting if there exists $f$ such that $L_{\mathcal D}(g)>L_{\mathcal D}(f)$ and $L_S(g)<L_S(f)$.

---
How is overfitting found in practice? #flashcard #MachineLearningUni #Generalization #Generalization2 
	We have access neither to the other program to compare to or the generalization error. Instead the gap between the training and test error is used.

---
Why is a development set needed? #flashcard #MachineLearningUni #Generalization #Generalization2 
	If we continue to use the test set to find hyperparameters to not overfit out network we will end up fitting to the test set. To avoid this we train hyperparameters on a development set and only touch the test set once we have finishes to evaluate performance.

---

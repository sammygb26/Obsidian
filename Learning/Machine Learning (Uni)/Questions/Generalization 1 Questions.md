What problem comes from "programming with data" when it comes to correctness? #flashcard #MachineLearningUni #Generalization
	When **programming with data** we can make a model that fits the data easily but we do not know if this leads to the "correct" solution we want that will perform on real world data and go beyond the dataset.

---
How can the generalization of a network be defined approximately? #flashcard #MachineLearningUni #Generalization 
	Generalization can be defined as being approximately correct on unseen data most of the time. We can measure this as the accuracy of data not used to train the network.

---
What is the idea of the distribution D that formalizes where our training and test data comes from? #flashcard #MachineLearningUni #Generalization 
	The idea is that there is some imaginary dataset $\mathcal D$ which both our testing and training dataset are sampled from therefore they have approximately the same distribution. 

---
How is the training error defined with respect to S? #flashcard #MachineLearningUni #Generalization
	$S$ is our training sample. We define the training error $L_S$ of some program $h$ as $$L_s(h)=\frac1n\sum_{i=1}^nl(y_i,h(x_i))$$Where $y_i$ and $x_i$ are the $i$th $x$ and $y$ values in $S$.

---
Instead of training and test loss what are we trying to minimize in the execution of our program? #flashcard #MachineLearningUni #Generalization 
	We truly want to minimize the loss over the imaginary distribution $\mathcal D$ which both $S$ and $S'$ are drawn from. That is we want to minimize $$L_{\mathcal D}(h)=\mathbb E_{(x, y)\sim\mathcal D}[l(y, h(x))]$$This is called the **generalization error**.

---
What is test set error an estimate of? #flashcard #MachineLearningUni #Generalization 
	The training set error $L_{S'}(h)$ is an estimate of the **generalization error** $L_{\mathcal D}$.

---
What is a hypothesis class with respect to different programs? #flashcard #MachineLearningUni #Generalization 
	The hypothesis class could be the range of a learning algorithm. It is a set of programs and the idea is that we search through this to get our solution when we use a learning algorithm.

---
What is a learning algorithm and its type mathematically? #flashcard #MachineLearningUni #Generalization 
	A **learning algorithm** takes in some set of $S$ of $m$ $(x,y)$ pairs. It then produces some program $h$. The type of this therefore. $$A:(\mathcal X\times\mathcal Y )^m\to\mathcal H$$Where $\mathcal X$ and $\mathcal Y$ are the sets of all possible $x$s and $y$s. Then $\mathcal H$ is the hypothesis class.

---
How can a linear classifier be defined as a hypothesis class? #flashcard #MachineLearningUni #Generalization 
	It will be defined as $$\mathcal H=\{x\mapsto w^T\phi(x):w\in\mathbb R\}$$

---
What does it mean for a hypothesis class to be PAC-learnable with some learning algorithm? #flashcard #MachineLearningUni #Generalization 
	A hypothesis class $\mathcal H$ is **PAC-learnable** with learning algorithm $A$ if for any distribution $\mathcal D$ there exists $\epsilon>0$ and $0\le\delta\le1$ such that $$\mathbb P_{S\sim\mathcal D^m}\left[L_{\mathcal D}(A(S))-\min_{h'\in\mathcal H}L_{\mathcal D}(h')>\epsilon\right]<\delta$$Meaning our loss is only worse than $\epsilon$, $\delta$ percent of the time.

---
What does the no free lunch theorem say? #flashcard #MachineLearningUni #Generalization 
	If we suppose $|\mathcal x|=2m$. For any learning algorithm $A$, there is a distribution $\mathcal D$ and $f:\mathcal x\to0,1$ such that we have $L_{\mathcal D}(f)=0$ but $$\mathbb P_{S\sim\mathcal D^m}\left[L_{\mathcal D}(A(S))\ge\frac1{10}\right]\ge\frac1{10}$$where $2$ and $\frac1{10}$ is arbitrary. So the algorithm can be made to fail on datasets that have a min loss of $0$.

---
What implications does the no free lunch theorem have for model complexity and generalization? #flashcard #MachineLearningUni #Generalization 
	This means when we consider all possible programs we can always find some $f$ that works for a dataset our learning algorithm would fail on. Hence compared to all possible programs our algorithms always fail.

---
How does error decomposition give two parts to our generalization error? #flashcard #MachineLearningUni #Generalization 
	We can decompose our generalization error to give $$L_{\mathcal D}(h)=L_{\mathcal D}(h)-\min_{h'\in\mathcal H}L_{\mathcal D}(h')+\min_{h'\in\mathcal H}L_{\mathcal D}(h')$$The first part $L_{\mathcal D}(h)-\min_{h'\in\mathcal H}L_{\mathcal D}(h')$ is the **estimation error**. While the second part $\min_{h'\in\mathcal H}L_{\mathcal D}(h')$ is the **approximation error**.

---
What is the estimation error of some program? #flashcard #MachineLearningUni #Generalization 
	The **estimation error** of some program is: $$L_{\mathcal D}(h)-\min_{h'\in\mathcal H}L_{\mathcal D}(h')$$ That is the difference from the best program we could get to our programs generalization.

---
What is the approximation error of some program? #flashcard #MachineLearningUni #Generalization 
	The **approximation error** of some program is: $$\min_{h'\in\mathcal H}L_{\mathcal D}(h')$$that is the error that is inherent even in the best solution. So the error is coming from our hypothesis class rather than the our actual specific program.

---
What is empirical risk minimization? #flashcard #MachineLearningUni #Generalization 
	**Empirical Risk Minimization** is when we minimize the loss on the training set to find a good hypothesis (program) $h\in\mathcal H$.

---
What is uniform convergence? #flashcard #MachineLearningUni #Generalization 
	We say $\mathcal H$ has **Uniform Convergence**  if for some $\epsilon>0$ and $0\le\delta\le1$ for every $h\in\mathcal H$ we have: $$\mathbb P_{S\sim\mathcal D^m}\left[|L_S(h)-L_{\mathcal D}(h)|>\epsilon\right]<\delta$$That is $L_S(h)$ is within some $\epsilon$ of $L_{\mathcal D}(h)$.

---
What does uniform convergence imply about some ERM solution? #flashcard #MachineLearningUni #Generalization 
	We know the ERM solution's score over the set it was trained on is at least $\epsilon$ away from its score on the true dataset due to **uniform convergence**. The score on the S dataset is better than or equal to all other programs (definition of **ERM**). But all these programs also have **uniform convergence** hence their generalization score is at most another $\epsilon$ away from their sample score. Since this is true for all programs it is also true for the best generalizer program. Hence $h_{ERM}$ is at most $2\epsilon$ away from the best solution with probability $1-\delta$. Hence it is PAC-learnable.

---

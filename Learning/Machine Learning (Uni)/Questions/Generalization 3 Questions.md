How can switching our a dataset affect performance of many networks? #flashcard #MachineLearningUni #Generalization #Generalization3
	We can recollect the data used to make up a dataset using the same method as before. It is usually found that the performance goes down even through they should come from the same distribution. Luckily the performance on one is correlated with performance in the other so getting better results on the old set gives better results on the new one too.

---
Describe e capacity generalization trade-off? #flashcard #MachineLearningUni #Generalization #Generalization3
	For higher and higher capacities we can find better networks to fit our test set but the error compared to our dataset grows as this does and so we can get better performance but we losses the generalization performance we really want.

---
How can we reduce the VC dimension on an infinite VC dimension class? #flashcard #MachineLearningUni #Generalization #Generalization3
	We can introduce weight decay this limits the possible classes we can have and so improves generalization by decreasing capacity.

---
What is weight decay the lagrangian off? #flashcard #MachineLearningUni #Generalization #Generalization3
	It is the lagrangian of our loss function subject to our weights being bellow a given bound. But as $\lambda$ and $B$ this bound are free their true values don't matter as they depend on one another but are inversely correlated.

---
How does L2 regularization affect the capacity of a hypothesis class it is applied to? #flashcard #MachineLearningUni #Generalization #Generalization3
	It ensures less of that class are viable and so reduces the number of possible programs and so the capacity.
	$$\mathcal H=\{x\mapsto w^T\phi(x):w\in\mathbb R^d\}$$ $$\mathcal H=\{x\mapsto w^T\phi(x):||w||\le B\}$$

---
What is Rademacher complexity for a sample? #flashcard #MachineLearningUni #Generalization #Generalization3 
	Rademacher complexity is a measure of the capacity of a network. It is equal to the the expected best performance of the hypothesis class over all possible labeling of some $n$ points in a sable $S$. $$\mathcal R_S(\mathcal H)=\mathbb E_\sigma\left[\max_{h\in\mathcal H}\frac1n\sum_{i=1}^n\sigma_ih(x_i)\right]$$

---
What is Rademacher complexity over the dataset with n points? #flashcard #MachineLearningUni #Generalization #Generalization3 
	It is the expected Rademacher complexity for a given set drawn from the distribution $\mathcal D$ $$\mathcal R_n(\mathcal H)=\mathbb E_{S\sim\mathcal D^n}[\mathcal R_S(\mathcal H)]$$

---
What are the Rademacher complexity bounds? #flashcard #MachineLearningUni #Generalization #Generalization3 
	With probability $1-\delta$, for all $h\in\mathcal H$ $$L_{\mathcal D}(h)\le L_S(h)+\mathcal R_n(h)+\sqrt{\frac{\log(1/\delta)}{2n}}$$With probability $1-\delta$, for all $h\in\mathcal H$ $$L_{\mathcal D}(h)\le L_S(h)+\mathcal R_S(h)+3\sqrt\frac{\log(2/\delta)}{2n}$$

---
For linear classifiers with bounded norm what is the upper bound for Rademacher complexity? #flashcard #MachineLearningUni #Generalization #Generalization3 
	If $S=\{x:||x||\le r\}$ and $\mathcal H=\{x\mapsto w^Tx:||w||\le B\}$, $$\mathcal R_S(\mathcal H)\le\sqrt\frac{r^2B^2}n$$
	
---
What is the stability of a learning algorithm? #flashcard #MachineLearningUni #Generalization #Generalization3 
	The stability of a learning algorithm is defined as its ability to give similar programs in response to slightly different datasets. Say swapping 1 data point out wont give a completely different dataset.

---
What is the mathematical connection between generalization bounds and stability? #flashcard #MachineLearningUni #Generalization #Generalization3 
	We say for some dataset $S$ when $S^{(i)}$ is the same set but with one point swapped out for the same point from the $\mathcal D$ distribution. We get $$\mathbb E_{S\sim\mathcal D^n}[L_{\mathcal D}(A(S))-L_S(A(S))]=\mathbb E_{i\sim U(n),S\sim\mathcal D^n,(x,y)\sim\mathcal D}[l(A(S^{(i)})(x_i),y_i)-l(A(S)(x_i),y_i)]$$

---
What does the generalization bound for stable algorithms mean? #flashcard #MachineLearningUni #Generalization #Generalization3 
	It means stable learning algorithms don't overfit.

---
If our loss is p-Lipschitz what does that mean in terms of stability? #flashcard #MachineLearningUni #Generalization #Generalization3 
	It means that if we find some difference in our two programs $S$ and $S^{(i)}$ compared on the original dataset. We can find the difference is upper bounded by $p$ times the difference in the programs.

---
If a function is p-Lipschitz and h-strongly convex what does that imply with relation to the minimizer? #flashcard #MachineLearningUni #Generalization #Generalization3 
	It means that $$\frac\lambda2||x-x^\star||^2\le f(x)-f(x^\star)\le p||x-x^\star||$$which further implies $$||x-x^\star||\le\frac{2p}\lambda$$

---
What can L2 regularization allow us to do with a p-Lipschitz loss? #flashcard #MachineLearningUni #Generalization #Generalization3 
 When optimizing over a $p$-Lipschitz loss adding L2 regularization allows us to make what we are minimizing also strongly convex.  Hence we can get and upper bound on the stability score $$||A(S^{(i)}-A(S)||\le\frac{2p}{\lambda n}$$which can be further passes through the Lipschitz definition to give $$\mathbb E_{S\sim\mathcal D^n}[L_{\mathcal D}(A(S))-L_S(A(S))]\le\frac{2p^2}{\lambda n}$$

---

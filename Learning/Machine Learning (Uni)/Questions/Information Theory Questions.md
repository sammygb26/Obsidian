How is information in some event defined? #flashcard #MachineLearningUni #InformationTheory
	We define the information in some event as related to its probability. The exact function for some event $x$ is $$I(x)=\log\left(\frac{1}{p(x)}\right)=-\log(p(x))$$

---
What properties are required for the definition of information? #flashcard #MachineLearningUni #InformationTheory
	We want that the sum of information in two events which are independent is the same as the information in the event where both event happen. $$p(x,y)=p(x)p(y)\implies I(x,y)=I(x)+I(y)$$We also want events that are rarer to be more informative and less rare less informative.

---
What does the base of the logarithm mean for the output of the information function? #flashcard #MachineLearningUni #InformationTheory 
	If the base is $e$ then the units become "nats" and if the base is 2 the units become "bits".

---
What is the definition of entropy of a distribution? #flashcard #MachineLearningUni #InformationTheory 
	This will be the expected information that is the information in each event weighted by how likely that event is. So $H(p)=H(x)=E_{x\sim p(x)}[-\log p(x)]$ 

---
Why is $H(x)$, "entropy of $x$" not a function of $x$? #flashcard #MachineLearningUni #InformationTheory 
	$H(x)$ doesn't give a value for a given value of $x$ as a function but gives a value for the different distributions of $x$. Hence it is a function of them.

---
How does the entropy of a coin change from when the probability of getting heads changes from 0 to 1? #flashcard #MachineLearningUni #InformationTheory 
	The number of bits will be greatest when $u=0.5$ and $0$ when $u=1$ or $u=0$.

---
What is the definition for conditional entropy? #flashcard #MachineLearningUni #InformationTheory 
	Conditional entropy is defined as the entropy of a random variable given some other variable. That is the expected information given some other value.

---
What is conditional entropy of some $x$ given $y$ if the two are independent? #flashcard #MachineLearningUni #Optimization 
	This will just be the entropy of $x$ even if we didn't know $y$. Hence $x$ is "just as random" or we have learned nothing about $x$.

---
What relationship always holds between the conditional entropy of some $x$ and its entropy? #flashcard #MachineLearningUni #Optimization 
	We say $$H(x|y)\le H(x)$$

---
What is the written definition of mutual information? #flashcard #MachineLearningUni #Optimization 
	This is the information shared by two random variables. Or said another way the information gained about $x$ given some $y$ is the mutual information between $x$ and $y$ written $I(x,y)$

---
What is the mathematical definition of mutual information? #flashcard #MachineLearningUni #Optimization 
	The mutual information or shared information is defined as: $$I(x,y)=H(x)-H(x|y)=H(y)-H(y|x)$$$$\hspace{8pt}=E_{x,y\sim p(x,y)}\left[-\log\frac{p(x)p(y)}{p(x,y)}\right]$$

---
What motivates the definition of cross entropy? #flashcard #MachineLearningUni #Optimization 
	If we don't know the distribution of some $x$ random variable we can instead estimate it by using another $q$ distribution.

---
What is the mathematical definition of cross-entropy?#flashcard #MachineLearningUni #Optimization 
	For distributions $p$ and $q$ where $p$ is the true distribution of $x$ we have the cross-entropy $$H(p,q)=E_{x\sim p(x)}\left[-\log q(x)\right]$$That is the expectation information given $q$.

---
If we have $H(p)$ and $H(p,q)$ what do we know about the relation between them? #flashcard #MachineLearningUni #Optimization 
	We know there is never less entropy in $H(p,q)$ that is $$H(p)\le H(p,q)$$

---
What is the definition of Kullback-Leibler divergence? #flashcard #MachineLearningUni #Optimization 
	The difference between the entropy with distribution $p$ and the cross-entropy assuming some variable $q$ is the KL divergence. Hence is defined as $$KL(p||q)=H(p,q)-H(p)=E_{x\sim p(x)}\left[-\log\frac{q(x)}{p(x)}\right]$$

---

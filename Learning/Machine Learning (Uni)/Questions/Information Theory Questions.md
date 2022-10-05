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
	Conditional entropy is defined 
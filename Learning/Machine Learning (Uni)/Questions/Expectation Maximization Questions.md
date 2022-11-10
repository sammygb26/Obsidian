What is the expectation maximization problem in general? #flashcard #MachineLearningUni #ExpectationMaximization
	Expectation Maximization is an algorithm to solve the problem of assigning **distributions** (key features) to fit some data. These features are described by parameters $\theta\in\Theta$ and we are fitting our data $X$. So we are trying to find $$\max_{\theta\in\Theta}p(X|\theta)$$

---
In the solving of EM what alteration is made to the problem to make it solvable? #flashcard #MachineLearningUni #ExpectationMaximization 
	We use a new set of variable $Z$ to represent all unobserved data. This way this and our original dataset $X$ capture all data in the system. Hence now we maximize $$\max_\theta\log p(X,Z|\theta)$$ to solve the problem instead of $$\max_\theta\log p(X|\theta)$$

---
What is the formula for L(q, theta) in the formulation of EM and what property does it have? #flashcard #MachineLearningUni #ExpectationMaximization 
	This would be $$\mathcal L(q,\theta)=\sum_Zq(Z)\log\left(\frac{p(X,Z|\theta)}{q(Z)}\right)$$ this has the property that for all $q$ and $\theta$ it is less than $p(X|\theta)$.

---
How is the formula for L(q, theta) arrived at? #flashcard #MachineLearningUni #ExpectationMaximization 
	We first imagine some distribution of data $Z$ and some discrete distribution over it $q(Z)$. We demarginalize $Z$ from our original equation $p(X|\theta)$ this gives $$\log p(X|\theta)=\log\sum_zp(X,Z|\theta)$$ Then we can times the probability inside the sum by $\frac{q(Z)}{q(Z)}$ and apply **Jensen's inequality** to find $\mathcal L$.

---
What is the evidence and evidence lower bound in EM? #flashcard #MachineLearningUni #ExpectationMaximization 
	The evidence is what we are trying to maximize that is $$\log p(X|\theta)$$the evidence lower bound or ELBO is what we actually maximize.

---
Given the formula describing finding theta with EM given the ELBO? #flashcard #MachineLearningUni #ExpectationMaximization 
	The ELBO would be $\mathcal L(q,\theta)$ hence to find $\hat\theta_{EM}$ we perform $$\hat\theta_{EM}=\arg\max\left(\arg\max\mathcal L(q,\theta)\right)$$

---
What is the understanding how why EM works with respect to maximizing the ELBO in q and theta? #flashcard #MachineLearningUni #ExpectationMaximization 
	We know $\log p(X|\theta)=\mathcal L(q,\theta)+KL[q||p]$. Hence we start with some $\theta$.
	1. We know $p(X|\theta)$ and $q$ don't match at this point. So we match them bringing up $\mathcal L$ to be equal to $\log p(X|\theta)$
	2. This however changes $\mathcal L$ such that $\theta$ is not optimal. So we maximize $\theta$ w.r.t $\mathcal L$ (since we know $\log p(X|\theta)$ is always greater this increases it also)
	3. But this beings us back to step 1 with $q$ not fitting $p(X|\theta)$. Hence we continue monotonically increasing the value of $\log p(X|\theta)$

---
What formula describes the relation between evidence and ELBO given p and q? #flashcard #MachineLearningUni #ExpectationMaximization 
	This would be $$\text{evidence}=\text{ELBO}+KL[q||p]$$ or written another way $$\log p(X|\theta)=\mathcal L(q,\theta)+KL[q||p]$$

---
What are the steps to solving EM? #flashcard #MachineLearningUni #ExpectationMaximization 
	1. We pick some initial $\theta$
	2. **Expectation step** - we let $q^\star(Z)=p(Z|X,\theta)$
	3. **Maximization step** - we let $\theta^{new}=\arg\max_{\theta}J(\theta)$ where $J$ is our ELBO given $q^\star$

---

What is the form of p for a gaussian random variable N(mu, sigma)?  #flashcard #MachineLearningUni #Probability 
	This is $p(x)=\frac1{\sqrt{2\pi\sigma^2}}\exp\left(-\frac1{2\sigma^2}(x-\mu)^2\right)$

---
What is the law of the unicorn statistician?  #flashcard #MachineLearningUni  #Probability
	$E_{x\sim p(x)}[f(x)]=\int_{-\infty}^\infty f(x)p(x)dx$ or when we have discrete probability $E_{x\sim p(x)}[f(x)]=\sum_{x\in\Omega}f(x)p(x)$.

---
If x and y are independent what can be said about E[xy] and E[x+y]? #flashcard #MachineLearningUni #Probability 
	$E[xy]=E[x]E[y]$ and $E[x+y]=E[x]+E[y]$

---
What is the distribution of a linear combination of gaussians? #flashcard #MachineLearningUni #Probability
	A linear combination of gaussians $x_1\sim\mathcal N(\mu_1, \sigma_1^2)$ and $x_2\sim\mathcal N(\mu_2, \sigma_2^2)$ will be $a_1x_1+a_2x_2\sim\mathcal N(a_1\mu_1+a_2\mu_2,a_1^2\sigma_1^2+a_2^2\sigma_2^2)$

---
What is the definition of a moment generating function for some variable? #flashcard #MachineLearningUni #Probability
	The moment generating function for $x$ is $M_x(t)=E[e^{tx}]=\int_{-\infty}^\infty e^{tx}p(x)dx$

---
What is the idea behind moment generating functions? #flashcard #MachineLearningUni #Probability 
	A moment generating function has the form $E[e^{tx}]$ for a random variable $x$ but this is also equal to $1+\frac{t}{1!}E[x]+\frac{t^2}{2!}E[x^2]+...$ hence with $t=0$ the tailor series derivatives will be the expectations on $E[x]$, $E[x^2]$ and so on. The key is if we can prove these are all the same for two variables then they must also have the same distribution.

---

What is a confidence interval? #flashcard #FDS #RandomnessSamplingSimulation 
	A confidence interval specifies a interval of values around a point estimator we expect the true value to be in with a given percentage. For example we can say a average population value is between $(0.1,0.9)$ with a certainty of $95\%$.

---
What is the mathematical meaning of a confidence interval? #flashcard #FDS #RandomnessSamplingSimulation 
	We would say $(\hat\theta-a\hat\sigma_{\hat\theta},\hat\theta+b\hat\sigma_{\hat\theta})$ is our confidence interval with a chance $1-\alpha$ this would mean $P(\hat\theta-a\hat\sigma_{\hat\theta}<\theta<\hat\theta+b\hat\sigma_{\hat\theta})=1-\alpha$ or $P\left(-b<\frac{\hat\theta-\theta}{\hat\sigma_{\hat\theta}}<a\right)=1-\alpha$.

---
How can we get the confidence interval of a normally distributed estimator? #flashcard #FDS #RandomnessSamplingSimulation 
	We can use z critical variables to get $a$ and $b$ for the interval. This can be done for any standardized variable that is normally distributed (which is most all as the number of samples increases).

---
How does the distribution of samples for small confidence intervals change? #flashcard #FDS #RandomnessSamplingSimulation 
	For small number of samples for which we don't know the true variance of the population we will have a t distribution with $n-1$ degrees of freedom.

---

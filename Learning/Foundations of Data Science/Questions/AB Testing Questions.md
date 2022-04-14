What is A/B Testing? #question 
	This is a method for assessing how changes between two groups affect some outcome. We count the number of successes given a change in two groups.

---
What questions does A/B Testing help to answer? #question 
	Does the change in group A significantly affect the outcome. How much does it affect the outcome?

---
How can we estimate the effect of the difference between groups A and B? #question 
	Effect on A and B are both statistics gathered from the actual studies we have done. This means we can make another statistic the difference. We can then use the bootstrap method to gain a confidence interval.

---
What is the large sample theory of A/B Testing? #question 
	If we are only measuring the success and failure of our two groups then we can treat them an binomial distribution for which the probability of success is unknown. Hence we can gather error estimators and so an error estimator for d since it is the difference of the two probabilities times the number of samples. $$\sigma_{\hat d}=\sqrt{\sigma_{n_B}^2+\sigma_{n_B}^2}=\frac{\sqrt{\hat{p_A}(1-\hat{p_A})+\hat{p_B}(1-\hat{p_B})}}{\sqrt{n}}$$
	This will give us our confidence interval $$\textrm{CI}=(\hat d-z_{\frac{\alpha}{2}}\cdot\hat\sigma_{\hat d},\hat d+z_{\frac{\alpha}{2}}\cdot\hat\sigma_{\hat d})$$

---
What are some issues in A/B testing? #question 
	Statistical and practical significance are different we can have a definite effect that still isn't meaningful to us. There are also ethical concerns when A/B testing is done on people without there knowledge.

---

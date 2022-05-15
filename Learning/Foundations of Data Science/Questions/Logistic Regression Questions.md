What are odds? #flashcard #FDS #LogisticRegression
	Odds is a measure of the relative difference in probability between success and failure. It is equal to the Probability of success divided by the probability of failure. That is it is how many time more likely success is than failure. It is also then the difference in the relative population sizes or regular population sizes (counts)

---
What is the odds ratio? #flashcard #FDS #LogisticRegression
	The odds ratio is a measure of how much a random variable changes the relative odds of success of failure. So it is equal to the Odds of success given the random variable is true over the odds of success given that random variable is false.

---
What is effect size? #flashcard #FDS #LogisticRegression
	This is a measure of how much a change to a random variable affects the odds of success and failure for another. It is equal to 1 - OR(x) where x is the random variable. It is a percentage change for a change in the random variable x defined as having an effect on some other random variable.

---
What are the principles of logistic regression? #flashcard #FDS #LogisticRegression
	The idea is that we can fit a logistic curve to a linear regression logistic model to get a probability function instead. We can fit is using Principle of Maximum Likelihood where we fit a curve maximizing the likelihood of the results we are looking at.

---
What is a logistic curve? #flashcard #FDS #LogisticRegression
	A logistic curve is given by the logistic function. It is useful because it can fit a linear regression well to be able to match probability instead in helps fit using the principle of maximum likelihood. And is equal to $$\frac{e^x}{1+e^x}=\frac{1}{1+e^{-x}}$$

---
What is the logistic regression model and how can it be used to find predicted probability? #flashcard #FDS #LogisticRegression
	The logistic regression model is simply a regular linear regression model passed through the logistic function which fixes it values between 0 and 1 so they can function as probabilities. If the model is then fit correctly it can give a accurate prediction with a probability given by the linear model passed into the logistic function. Here $f$ is a logistic function. $$f(B_0 + B_1\cdot x) =\frac{1}{1-e^{-B_0 - B_1}}$$

---
What are log odds? #flashcard #FDS #LogisticRegression
	These are just the log of the odds. They shift the values so that negative log odds refer to odds between 0 and 1 and positive log odds refer to odds between 1 and infinity.

---
How can the coefficients of a logistic regression be interpreted? #flashcard #FDS #LogisticRegression
	We can see that the **log odds** and **logistic function** are inverses. If we interpret the output of our linear model to be in log odds the two functions will cancel out and the probability behind log odds will becomes out output. Therefore we can interpret $\beta_0$ as the log odds when $x=0$ and we can interpret $\beta_1$ as the change in log odds corresponding to a change in $x$ of $1$.

---
How might $\beta_1$and $\beta_0$ be interpreted in light of their connection to log odds? #flashcard #FDS #LogisticRegression
	Since if we interpret the output of the linear regression function to be in log odds then output of the function becomes probability. Hence we have $$Odds=e^{\hat\beta_0}\cdot e^{\hat\beta_1x}$$
	This means a change $x$ by $1$ corresponds to an $e$ increase in $Odds$.

---
Given $\beta_1$ is in log odds what is $OR(x)$? #flashcard #FDS #LogisticRegression
	We are taking $\beta_1$ to be log odds, the odds ratio is the amount the odds will change when $x=1$ vs $x=0$ since this is the exact change in log odds $\beta_1$ captures hence $e^{\beta_1}$ will be the change in odds, we can say $OR(x)=e^{\beta_1}$

---
How can we interpret multiple $\beta_i$ coefficients in multiple logistic regression? #flashcard #FDS #LogisticRegression
	They are just the corresponding odds ratio for the independent variable they are capturing the effect of.

---
How can logistic regression be used as a classifier? #flashcard #FDS #LogisticRegression
	Logistic regression gives us a predicted probability for an outcome we can pick a threshold probability to turn this into a classifier.
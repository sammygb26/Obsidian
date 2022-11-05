# P-values
A P-value is defined for a [[Statistic]] given a [[Statistical Model]]. It is used for [[Hypothesis Testing]] to confirm or deny the null hypothesis as well as give a measure of how well the observed data fits it. It is defined as the *percentage probability mass more extreme that the statistic in the mass distribution*. So for example with a [[Binomial Distribution]] you would have
$$
P(T_0\le t_0)=B(t_0;n,p)=\sum_{t=0}^{t_0}b(t;n,p)
$$
*where $B$ is the  [[Cumulative Distribution Function]] of the binomial distribution and $b$ is the [[Probability Mass Function]] of the binomial distribution*.

We use the CDF instead of 1-CDF in this case since we are taking $t_0$ to be an value at the small end of the extremes. In this case if the binomial was a representation of the number of black people in a jury of size $n$ where the population has a $p$ proportion of black people. Our alternative hypothesis could be black people are under represented in the jury.

Another way to calculate a P-value for a binomial distribution with lark $n$ would be to use a [[Normal Distribution]] to approximate it (with $\mu=np$ and $\sigma=\sqrt{np(1-p)}$). We can then use Z [[Critical Values]]. Where our $z$ value would be
$$
z=\frac{t_0-\mu}{\sigma}
$$
We can then use the standard [[Normal Distribution]]'s [[Cumulative Distribution Function]] $\phi(z)$ to find our p-value.

## Interpretation of P-values and Statistical Significance
The **smaller** a p-value the **less compatible** the statistic is with the [[Statistical Model]] is is being used to confirm or deny. We can set a threshold value under which we will reject the null hypothesis. A standard usually used is $p<0.05$ would mean we have **statistical significance** and this is simply scientific convention. Asterisks are also used to denote significance

* means significant at least at the p < 0.05 level
** means significant at least at the p < 0.01 level
*** means significant at least at the p < 0.001 level

#### Choosing the right level of significance
There is no correct way to choose the level of significance and it will depend on the application. For example for a drug safety level you would probably want a very small p-value to reject the null hypothesis that the patients risk of death would be increased by the drug.

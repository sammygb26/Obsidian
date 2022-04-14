# A/B Testing
This is a method for assessing how changes between two groups affect some outcome. We can give one group (the A group) one outcome and another group (the B group) the other. We want to answer two questions:

1. Is A *significantly* better?
2. How much worse or better is B?

This is quite often used in web design to give users two version of a website n see what the effect is of a design change. There are **ethical** problems however with A/B testing.

## [[Bootstrap Method]] for A/B Testing
If we have a A/B test with $n=1000$ for samples per group. Then $n_A=700$ and $n_B=720$ for the numbers for each site. We are estimating the parameters $p_A$ and $p_B$ and the difference $d=p_A-p_B$. The estimators for these are $\hat{p_A}=\frac{n_A}{n}$, $\hat{p_B}=\frac{n_B}{n}$ and $\hat{d}=\frac{\hat{p_A}}{\hat{p_B}}$. We can have $B$ bootstrap repetitions. We can sample $n_A^*$ for $\textrm{binom}(n,\hat{p_A})$ and sample $n_B^*$ from $\textrm{binom}(n,\hat{p_B})$. We can also compute the difference $d^*$ at this time and store them all. From this we can find a confidence interval for difference and so find the confidence A or B has a positive effect. So in this case we will have 15% chance of A and 85% chance for B being better.

## Increasing Certainty
We can get a distribution for the difference but we may want to get a more sure estimate and distributions. We can increase the number of samples and the variance should go down.

![[Pasted image 20220124181310.png]]

We are however assuming the **time-period** we have picked isn't biased. We have to be careful on what sample we are using and if it has a good spread of the demographic.

## Large Sample Theory A/B testing
This allows us to get a confidence interval from the observed proportions rather than using the estimator form the bootstrap method. We know our two groups will have binomial distributions. So the standard error for the numbers will be  $\sigma_{n_A}=\sqrt{np_A(1-p_A)}$ and $\sigma_{n_B}=\sqrt{np_B(1-p_B)}$ (for $n_A$ and $n_B$) with $\mu_{n_A}=np_A$ and $\mu_{n_B}=np_B$.  The standard error in these estimators will be $\hat\sigma_{\hat{p_A}}=\sqrt{\frac{\hat{p_A}(1-\hat{p_A})}{n}}$ and $\hat\sigma_{\hat{p_B}}=\sqrt{\frac{\hat{p_B}(1-\hat{p_B})}{n}}$. Then we can find the standard error in $\hat d$ to be 
$$
\sigma_{\hat d}=\sqrt{\sigma_{n_B}^2+\sigma_{n_B}^2}=\frac{\sqrt{\hat{p_A}(1-\hat{p_A})+\hat{p_B}(1-\hat{p_B})}}{\sqrt{n}}
$$
As we make $n$ larger we can use a normal distribution to model this. So
$$
\textrm{CI}=(\hat d-z_{\frac{\alpha}{2}}\cdot\hat\sigma_{\hat d},\hat d+z_{\frac{\alpha}{2}}\cdot\hat\sigma_{\hat d})
$$

## Issues
**Statistical and practical significance are different** we can have a definite affect that still doesn't mean a lot to us. **Ethical**, users don't have informed consent so they can't choose whether or not to take part. For example with the mood A/B testing at Facebook. Then there is **data protection** users have the right to their data and if these tests are done without knowledge its hard to do.

[[AB Testing Questions]]
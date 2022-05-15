# Estimation
Estimation is the attempt to discern some statistic for a population for a sample. We call these statistics like mean and variance *parameters*. As they can be used a parameters to build a distribution of our estimator. There are two different parts of an estimator we can consider. A *point estimator* which gives a singular value. Then there is a confidence interval which indicates how a accurate we expect the point estimator to be.

The notation used for estimators is for some statistic $\theta$ the same symbol with a hat $\hat\theta$. Some of course have their own symbols $\bar X=\hat\mu$

## Bias and Variance
Estimators how two properties we car about primarily. Their *bias* and *variance*. 

1. *Bias* is the difference we expect form our estimator with the true value in out population. That is $$\text{Bias}=E[\hat\theta-\theta]=E[\hat\theta]-\theta$$When this is 0 we say the estimator is *unbiased*
2. The variance is used just a statistic for a normal distribution but describes how spread out out estimator is.$$\text{varience}=V[\hat\theta]$$
3. The *mean squared error* of an estimator tells us about how wrong are estimator may be. This is defined as $$MSE=E[(\hat\theta-\theta)^2]=V[\hat\theta]+(E[\hat\theta]-\theta)^2=\text{variance}+(\text{bias})^2$$

These results can be summarized visually as follows

![[Pasted image 20220511141352.png]]

We also have *standard error*. This is defined simply as the square root of the variance of the estimator. If we know the standard deviation of our population then we can also give the standard error as $$\sigma_{\bar X}=\frac\sigma{\sqrt{n}}$$
If we don't know the true variance we can use $S$ as an estimator for $\sigma$. But in this case both are distributions so the central limit theorem doesn't apply. In general however this can be used with $n>100$.

![[Pasted image 20220511151330.png]]

[[Estimation Questions]]
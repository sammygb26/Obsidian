# Confidence Intervals
The idea with confidence intervals is to get a sense of what range of value we are confidence in and so how likely our value is to be different form our point estimate. We can use *critical values* to give the range of values for a given certainty. This means when we have a normal distribution we can use *z critical values* multiplied by out variance and added onto our average.

![[Pasted image 20220511160136.png]]

The confidence interval itself is defined for some estimator $\hat\theta$ as $(\hat\theta-a\hat\sigma_{\hat\theta},\hat\theta+b\hat\sigma_{\hat\theta})$ has a $1-\alpha$ probability of holding the true value. We write this as $$P(\hat\theta-a\hat\sigma_{\hat\theta}<\theta<\hat\theta+b\hat\sigma_{\hat\theta})=1-\alpha$$This has the same meaning as $$P\left(-b<\frac{\hat\theta-\theta}{\hat\sigma_{\hat\theta}}<a\right)=1-\alpha$$We can extend this to an actual statistic for example the mean value as $$\frac{\hat\theta-\theta}{\hat\sigma_{\hat\theta}}=\frac{\bar X-\mu}{\sigma/\sqrt n}$$Then how do we actual fin the values for $a$ and $b$. These of course will be the *z-critical values* for a normal distribution. The values we want will be $z_{\alpha/2}$ and $z_{1-\alpha/2}$. We can also use the [[Bootstrap Method]] to find confidence intervals.

## Interpretation of confidence intervals
The values given for our confidence intervals and what values for $\alpha$ we give will depend on our situation. Things that don't matter too much may be ok with a low trust however critical things may not and we may also require a smaller interval.

## Small sample confidence intervals
When we are working with $n<40$ or around about there we can consider the sample to be small. Our estimate for the standardized variable will contain two random variables the estimate and the standard error. This is fine for a large number of samples but with less the distribution will no longer be normal and so we cannot use a z distribution. Instead we get a t distribution. In fact we always had a t distribution but with large $n$ this is almost the same as a z distribution. We then use t critical values instead which give a larger rand for larger values.

![[Pasted image 20220511162353.png]]

We count the degrees of freedom as $n-1$ so the green t-distribution has 4 samples.

[[Confidence Intervals Questions]]
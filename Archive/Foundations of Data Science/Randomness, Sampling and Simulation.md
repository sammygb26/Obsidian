# Randomness, Sampling and Simulation

A *statistic* is a number calculated from some sample or population. It therefore partially describes the characteristics of the population.

In *inferential statistics* we want to estimate (with confidence intervals) the true value of statistics in a population form a sample of that population. When we *estimate* we are looking for one of two things either a *point estimate* (an expected values for the true population statistic) and a *confidence interval* (which is a range of values we expect the true value to be in with a given probability).

There are two approaches to statistical inference:
1. *Statistical Simulations* - this is where we use a repeated random sampling to get approximate answers to complex distributions without actually having to analyze the distributions mathematically.
2. *Statistical theory* here we use the properties of well known distributions to infer value for true data.

We want to know the distribution of a variable we measure in a population. We can look at the shape given by our sample.

![[Pasted image 20220511125933.png]]

## Sampling and Simulations
To perform statistical inference we need to be able to *sample* our distributions. A *random sample* will have a size $n$ elements taken from a finite population or a continuous probability distribution. We have simulations of uniform probability distributions these can then be used to get any other distribution.

When sampling from a probability distribution we can take many sample and plot a histogram to get an idea of the true distribution.

When we sample form a set of discrete items we have two options either we can sample *with replacement* or *without replacement*. The second a lows us to take far more sample and allows for more intuitive estimation of the values. 

Sometimes our sample aren't truly random that is there is some part of our process that biases the results to not be representative of the true population. One of these is a *sample of convenience* where taking the easiest route to sampling some distribution may lead to an unrepresentative sample.

## Simulations
In a simulation we will generate a number of sample $n$. This will give one sample of the population and so one statistic. But since we are considering what other values could have made out statistic we see that is to is distributed. To get this distribution we can take $k$ replications. This way we can gather a distribution for some statistic.

This can also be used for *hypothesis testing* if the distribution given by our simulation suggests a true statistic or value is extremely unlikely we can conclude out model is in someway wrong.

When we perform estimating this way we can get a confidence interval for any percentage we want without having to determining mathematically the exact distribution of the real distribution.

## Distribution of small samples statistics from probability distributions
The distribution of the mean of a sample will depend on the original sample. For example a normal distribution's mean will also be normally distributed. In fact many different distributions will have different statistical distributions for different statistics.

![[Pasted image 20220511133426.png]]

As sample get larger all these distributions become tighter and the variance decreases. All the statistic themselves also become normally distributed.

![[Pasted image 20220511133607.png]]

This comes down to two key facts about samples and distributions.

1. *Central Limit Theorem* - The distribution of the mean (or sum) of any distribution will converge to a normal distribution as the number of samples increases. For the mean the variance will be a factor of $n$ smaller than the true population variance. ![[Pasted image 20220511134505.png]]
2. *Law of large numbers* - In the limit of $n$ to infinity the sample mean $\bar X$ tends towards the true population mean $\mu$ ![[Pasted image 20220511134446.png]]

[[Randomness, Sampling and Simulation Questions]]
# Statistical Preliminaries
This will introduce the notation used for statistic for the whole of the [[Foundations of Data Science - Overview]] course.
## Samples and Populations
There is a difference between **populations** and **samples**. A **population** is the actual group in the world. For example if we are studying some animal. The real instances of that animal in the world are the **population**. A **sample** is a subset of that **population** which we have collected data on.
* $N$ is the size of the **population**
* $n$ is the size of our **sample** (of the *population*)

*Note: this means $n\le N$*

#### Sample Mean and Population Mean
The sample mean is the average of some variable $x$ with $n$ **samples** from the population, $x_1$, $x_2$, $x_3$ … $x_n$ the **sample mean** is defined as:
$$
\bar{x}=\frac{1}{n}\sum_{i=1}^nx_i
$$
The population mean is the *true average* in the actual population so it cannot be known unless we have a sample of the whole population. It is defined as for a numeric variable $x$ with $N$ instances $x_1$, $x_2$, $x_3$ … $x_N$  as:
$$
\mu_x=\frac{1}{N}\sum_{i=0}^Nx_i
$$
The **sample mean** is an [[Estimator]] of the population mean.

#### Sample and Population Median
The **sample median** $\tilde{x}$ of a variable $x$ is the *middle* value of the sample. That is if we order all instances in the sample $x_1$, $x_2$, $x_3$ … $x_n$ such that for two adjacent $x_a$ and $x_b$ $x_a<x_b$. Then then $x_\frac{n+1}{2}$ instance will be the median if $n$ is odd. If $n$ is even then it will be the the average of the two values closes to the middle so the mean of the$(\frac{n}{2})^{\textrm{th}}$ value and the $(\frac{n}{2}+1)^{\textrm{th}}$ value . In the same way the **population median** is just this for the whole population $x_1$, $x_2$, $x_3$ … $x_N$ median.

## Skew and Symmetry
Skew and Symmetry tell us about the *shape* of a variable in the population. What the distribution of values *looks* like. If we sample randomly from a population like this we get a [[Probability Distribution]].
* If a distribution is **symmetric** then $\bar{x}=\tilde{x}$
* If a distribution is **positively skewed** then $\bar{x}>\tilde{x}$
* If a distribution is **negatively skewed** then $\bar{x}<\tilde{x}$

## Variance and Standard Deviation
The **variance** of a sample is a measure of how much the values in the sample vary from the sample mean. For a numeric variable with $n$ observations and instances $x_1$, $x_2$, $x_3$ … $x_n$ the **sample variance** is defined as:
$$
s^2=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2
$$
Then from this the **sample standard deviation** is defined as
$$
s=\sqrt{s^2}=\sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2}
$$
We have to square the **deviations** $x_i-\bar{x}$ since they will just sum to zero. We don't use **magnitudes** $|x_i-\bar{x}$ since they don't behave well mathematically. The **units** for $s^2$ are the ${(\textrm{units for }x})^2$ then the units for $s$ are the $\textrm{units for }x$.

The **population variance** for a variable $x$ for a population with $N$ instances $x_1$, $x_2$, $x_3$ … $x_N$ is:
$$
\sigma^2=\frac{1}{N}\sum_{i=1}^{N}(x_i-\mu_x)^2
$$
Then for the same population **population standard deviation** is defined as:
$$
\sigma=\sqrt{\sigma^2}=\sqrt{\frac{1}{N}\sum_{i=1}^{N}(x_i-\mu_x)^2}
$$
The devisor for **sample variance** is $n-1$ instead of $n$ since we know the deviations will sum to zero $\sum_{i=1}^{n}(\bar{x}-x_i)=0$ so the last $x_i$ is always defined by all the other so there are only $n-1$ **degrees of freedom**.

#### Scaling variance and standard deviation
If we scale the instances what happens to the **variance** and **standard deviation**? Take a sample of $x_1$, $x_2$, $x_3$ … $x_n$ then a scaled version of $x$ call it $y=cx$ for some scalar $c$ then
* *$\bar{y} = c\bar{x}$
* $s_y^2=c^2s_x^2$
* $s_y=cs_x$

#### Variance Shortcut Formula
Another way of writing variance is the mean of the $x^2$ variable minus the mean of the $x$s squared ($\bar{x}^2)$ that is:
$$
s_x^2=\frac{1}{n-1}\sum_{i=1}^{n}\left(x^2-\bar{(x^2)}\right) -(\bar x)^2
$$

[[Statistical Preliminaries Questions]]


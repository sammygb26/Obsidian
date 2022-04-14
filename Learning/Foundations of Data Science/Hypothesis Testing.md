# Hypothesis Testing
The aims of hypothesis testing are to decide if a hypothesis or model is compatible with some observed data then if it is do fully test if it is a good hypothesis we need to investigate and describe a mechanism specific to the data that explains why it is true.

## Method of Hypothesis testing
For this we need two hypotheses. The null hypothesis and the alternative hypothesis. The null hypothesis (or $H_0$) the claim that we initial assume to be true formalized as a [[Statistical Model]]. E.g., a jury panel is chosen randomly. The alternative hypothesis (or $H_a$) the claim that is contradictory to $H_0$, typically not formalized as a statistical model. E.g., a jury isn’t chosen randomly.

#### Procedure for a hypothesis test    
1) Decide a test statistic which is a function on some sample data (e.g., number of black people)
2) Determine the distribution of that statistic would be if it arose from the null hypothesis model
3) Either A) Deciding on a rejection region i.e., region of the distribution of the test statistic under H0 in which we should reject H0. Typically, these are the extremities of the distribution if our test statistic falls in this region, we reject H0 and otherwise we don’t reject it. B) Return [[P-values]] which tells us how compatible the test statistic is with the data.

#### Rejection Regions
Here we specify a region to be some percentage amount of probability mass (5% and so on). Then depending on our alternative hypothesis relying on the value either being smaller, greater than or either of the mean of the null hypothesis’s statistical description. We will have a lower tailed, higher tailed or two-tailed region (the first two being one tailed rejection regions)
![[Pasted image 20220119112744.png]]
We can then find the **_boundaries_** of this region by finding the [[Critical Values]] for the given rejection percentage. These boundaries define the region we then reject the null hypothesis if the test statistic falls in this region.

An example of a **lower tailed** rejection region with the statistic being the number of black people on a jury could come from the alternative hypothesis the jury is biased agonized black people then this could be true if the value is much smaller than what is expected and so we reject the null hypothesis if the test statistic is much smaller. Then an example of a **higher tailed** rejection region would be the jury is based to have more black people than random. Then it would be **two-tailed** for the alternative hypothesis that the jury selection is simple not random.

## P-values
Another way to validate or invalidate a hypothesis is with [[P-values]]. They are a measure of how well a given test statistic confirms or rejects a given hypothesis (captured as a [[Statistical Model]])

## Multiple Categories
We can also perform hypothesis testing on multiple categories for example with jury selection for multiple ethnic groups. Given the null hypothesis for example "ethnic groups have no effect on jury selection rates" we can get expected values for our values we can then compare the the observed values. 

![[Pasted image 20220119122647.png]]

We want a measure of how well our observed values match our expected values. We can take the squared sum of the differences similar to [[Principle of Least Squares]].  *Here $n_i$ is the observed number in an ethnic group and $p_i$ is the proportion of that ethnic group in the population with $n$ being the total size of the population*
$$
\sum_{i=1}^{k}(n_i-np_i)
$$
This is an **absolute** measure however and we would like a **relative** measure instead. This gives us a statistic called the **chi-squared** statistic written as
$$
\chi^2=\sum_{i=1}^{k}\frac{(n_i-np_i)^2}{np_i}
$$
Or said another way
$$
\chi^2=\sum^k\frac{\textrm{(observed - expected)}^2}{\textrm{expected}}
$$
#### Calculating Chi-squared from [[Statistical Simulation]]
We can use the [[Bootstrap Method]] and sample from a multinomial population with the total $n$ and the proportion in the population defined as $p_i$ and number $k$ times calculating $\chi^2$ each time. This will give us a chi-squared distribution
![[Pasted image 20220119121938.png]]
*The orange line is a chi-squared distribution with 4 degrees of freedom*

The number of degrees of freedom is the number of datapoints that actually define the distribution. In this case is is 4 since even through there are 5 ethnic groups they always sum to the same total $n$ so the 5th doesn't matter.

#### Goodness-of-fit
Now that we have a statistic to measure how well multiple categories fit an expected we can find [[P-values]] from this statistic. Large $\chi^2$ values therefore indicate poor **goodness-of-fit** while small ones may indicate that the data has been doctored in some way (a different type of extreme).

#### Two-way contingency tables
If we have a two-way contingency table as below, how can we find the estimated values say if we expect both groups to be equally proportioned.
![[Pasted image 20220119122903.png]]
We can note this means in this case that the proportions will $p_{ij}=p_{i*}p_{*j}$ where $p_{i*}$ and $p_{*j}$ are the marginal probabilities given by
$$
p_{i*}=\frac{n_{i*}}{n_{**}} \textrm{ and } p_{*j}=\frac{n_{*j}}{n_{**}}
$$
Where $n_{**}$ is the total population and $n_{i*}$ and $n_{*j}$ are the totals in the categories given the value $i$ and $j$ respectively.
$$
\hat{e_{ij}}=n_{**}p_{ij}=\frac{n_{i*}n_{*j}}{n_{**}}
$$
![[Pasted image 20220119124223.png]]

We can see that since the two groups (*depressed vs not depressed* and *male vs female*) both sum to the same total $n_{**}$ then one if we know the number in 1 group we know the other 3. This means we will get a chi-squared distribution with 1 degree of freedom. We can calculate our own observed chi-squared statistic as
$$
\chi^2=\frac{(\textrm{observed - expected})^2}{\textrm{expected}}=\sum_i\sum_j\frac{(n_{ij}-\hat{e}_{ij})^2}{\hat{e}_{ij}}
$$
This can be compared to the chi-squared distribution to get [[P-values]]

## Issues in hypothesis testing
#### **Type I** and **Type II** errors
There are two types of errors in hypothesis testing **Type I** and **Type II**. A **Type I** error is when even though the null hypothesis $H_0$ is true you get a p-value in the 0.05% range which can happen. To reduce the likely hood of this the $\alpha$ rejection area range can be made smaller. A **Type II** error is when the null hypothesis $H_0$ is false yet we still get a statistic in the accepted range despite it coming about not from the model we expect.

#### Decisions based on confidence intervals
Scientific conclusions and business policy decisions shouldn't be based on if [[P-values]] pass a specific threshold. $p \le 0.05$ is often seen as complete evidence in science however it doesn't mean $H_0$ is false it is on a spectrum instead.

#### Data snooping, Multiple Testing and p-value hacking
When you run an experiment many times until you get a p-value less than 0.05 and only report that even if $H_0$ hold up in most cases in this case you would be reporting **Type I** errors, this is called **Multiple Testing**. The chance of running into this is quite high say you do 20 experiment then the chance of running into a **Type I** error is $1-0.95^{20}=0.64$. You have to make sure not to only report shocking results.

It is tempting to only report shocking findings however this can slant the truth we actually receive. **Data snooping** and **p-value hacking** is the practice of running many experiments and selecting only a subset to report. This is common for example with sponsored science done for drug companies. To overcome this proper inference requires reporting and transparency and it may be important to monitor conflicts of interest.

[[Hypothesis Testing Questions]]
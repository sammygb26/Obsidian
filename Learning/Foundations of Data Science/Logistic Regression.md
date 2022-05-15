# Logistic Regression
This is to do with the classification problem (where a solution is [[K Nearest Neighbors]] for example) where you are trying to find the class of a data point given a number of attributes say fruit size and color. In logistic regression the task is to predict the probability that an unseen datapoint belongs to a given category given the independent variables. As the name suggests this is based on [[Linear Regression]]

## Principles of Logistic Regression
Take a binary classification for a bank where we have to predict if a load is approved or not. We can see that for in the following example an age increase increases the approval chance so we want some line going from low with low age and high with high age for probability of approval.
![[Pasted image 20220118185223.png]]
This isn't very useful however so instead we can use a contingency table showing the empirical probability (relative frequency) of having credit approved or not approved based on employment status. Below we are plotting (P(X=x, Y=y) where X is employment and Y is approval)
![[Pasted image 20220118190241.png]]
In logistic regression we use odds which is calculated as follows.
$$
\textrm{Odds(Sucess)}=\frac{\textrm{P(Sucess)}}{\textrm{P(Failure)}}=\frac{\textrm{P(Sucess)}}{1-\textrm{P(Sucess)}}
$$
So the odds of being approved given you are not employed is 0.34 (you are three more times likely to be not approved) and if you are employed it is 2.42 (you are around two and a half times more likely to be approved). We then also have the odds ratio which is 
$$
OR(x)=\frac{\textrm{Odds(Sucess|x=True)}}{\textrm{Odds(Sucess|x=False)}}
$$
$OR(x)$ means is how many times more likely you are to be successful in this case given that x is false compared to it bring true. That is the effect of being employed in this case increases your change of getting approved by 7.09 times. We say that the effect size if $OR(x)-1)$ (6.09 in this case).

If we use a regression for the case above we will get a line that goes above 1 and below zero but this is impossible for or a probability so we need to modify this to make since. We do this with a logistic curve.
![[Pasted image 20220118192148.png]]
This curve is $f(x)=\frac{e^x}{1+e^x}=\frac{1}{1+e^{-x}}$  hence $f(B_0 + B_1\cdot x) =\frac{1}{1-e^{-B_0 - B_1}}$ the following is what we get when we apply this to the above example
![[Pasted image 20220118192657.png]]

## Interpretation of Logistic Regression
##### Interpretation of $B_0$ and $B_1$ 
In linear regression $B_0$ is the y intercept of the regression line and $B_1$ is the gradient of the line. For $x=0$ we have $f(B_0+0\cdot B_1)=f(B_0)=\frac{1}{1+e^{-B_0}}$ hence this is the probability of success when $x=0$.

#### Log Odds
We can define the log odds of success as
$$
\textrm{Log Odds(Success)}=ln\frac{\textrm{P(Sucess)}}{\textrm{P(Failure)}}=ln\frac{\textrm{P(Sucess)}}{1-\textrm{P(Sucess)}}
$$
This means that for $\textrm{Odds}=1$ we have $\textrm{Log Odds}=0$ meaning equal probability of success and failure. If $\textrm{Odds}>1$ then $\textrm{Log Odds}>0$ meaning success is more likely than failure. Finally if $\textrm{Odds}<1$ then $\textrm{Log Odds}<0$ meaning failure is more likely than success. We should noy also that if $P$ is probability of success then $P=\frac{1}{2}$ implies $\textrm{Odds}=1$. Then $P>\frac{1}{2}$ means $\textrm{Odds}>1$ and $P<\frac{1}{2}$ means $\textrm{Odds}<1$.

When the $\textrm{Log odds}$ increase by 1 then the $\textrm{Log odds}$ will increase by $e$. When we refer to probability in terms of log odds we will then use logits (logistic units). We might might also see logistic regression written as $f(\hat{B_0})=x$ and $\hat{B_0}=z$ this just means $f(z)=\frac{1}{1+e^{-z}}=x$ when we have this $x$ is in logits and $z$ is normal. Hence also $z=ln\frac{x}{1-x}$ so we have
$$
\textrm{logit}(p)=ln\frac{p}{1-p}
$$
This is just the inverse of the logistic function. Hence the change in log odds in our regular regression function. $\beta_0$ and $\beta_1$ are both measured in logits. This means a change in the dependent variable will increase the log odds by $\beta_1$ and so increase the odds by $e^{\beta_1}$. Then the odds ratio will just leave change factor for a unit increase hence the odds ratio is $e^{\beta_1}$ for the dependent variable.

When we are using logits they are what is given by a regular [[Linear Regression]] where as our probability is given by the logistic function on the prediction from the regression. This is why $\hat{B_0}$ is measured in logits. 

### Logistic regression model in terms of log odds
Success is $P(\textrm{Y=1|x})=f(\hat{B_0})+\hat{B_1}\cdot x)=\frac{1}{1+e^{-\hat{B_0}-\hat{B_1}\cdot x}}$ 

Failure is $P(\textrm{Y=0|x})=1-f(\hat{B_0})+\hat{B_1}\cdot x)=1-\frac{1}{1+e^{-\hat{B_0}-\hat{B_1}\cdot x}}=\frac{e^{-\hat{B_0}-\hat{B_1}\cdot x}}{1+e^{-\hat{B_0}-\hat{B_1}\cdot x}}$ 

Hence odds is $\textrm{Odds}=\frac{P(\textrm{Y=1|x})}{P(\textrm{Y=0|x})}=\frac{1}{e^{-\hat{B_0}-\hat{B_1}\cdot x}}=e^{\hat{B_0}+\hat{B_1}\cdot x}$ 

Therefore $\textrm{Log odds}$ is $ln\frac{P(\textrm{Y=1|x})}{P(\textrm{Y=0|x})}$ which is just $\hat{B_0}+\hat{B_1}\cdot x = \textrm{logit}(P(\textrm{Y=1|x})$  also meaning that $\hat{B_0}$ is log odds when the independent variable is equal to 0.

### Interpretation of $\hat{B_1}$
We have from the above equations that $\textrm{Odds}=e^{\hat{B_0}+\hat{B_1}\cdot x}=e^\hat{B_0}\cdot e^{\hat{B_1}\cdot x}$ this means when we increase x by 1 we increase the Odds by a factor of $e^{\hat{B_1}}$. For a binary variable this would be the average change in probability for a single extra unit on the independent variable. This means
$$
OR(x)=e^{\hat{B_1}}
$$
This would mean for every increase of x by one you will be $e^\hat{B_1}$ times more likely for the category we are trying to guess to be 1.

## Multiple Logistic Regression
This will allow us to deal with more independent variables as in [[Multiple Regression]]. We will have many independent variables say $x^{(1)}$ - age, $x^{(2)}$ - employment … then we have 
$$
P(\textrm{Y=1}|x^{(1)},x^{(2)}$,...)=f(B_0+B_1x^{(1)}+B_2x^{(1)}+...)
$$
We can then fit our multiple regression model to the training data giving us our coefficient $\hat{B_0}$, $\hat{B_1}$, $\hat{B_2}$ and so on now these are in log odds (logits) so we have to convert them to Odds or OR
![[Pasted image 20220118223941.png]]
So this means the log odds increase by 1.881 when a person in employed vs not employed. Then the Odds or receiving a load goes up by a factor of 6.562 for a person we is employed bs not employed.

### Bootstrap [[Foundations of Data Science/Confidence Intervals]] for coefficients
![[Pasted image 20220118224429.png]]
*Note: These are really the distributions of $e^\hat{B_i}$* not just $\hat{B_i}$

Since the coefficients are from the data they are statistic therefore we can use the bootstrap method to derive confidence intervals for them. So as with the regular [[Bootstrap Method]] we can pick a number of repetitions and we will have a sample size equal to our population. We can then plot the distributions above and find the intercepts by indexing into the sorted array of the calculated coefficients.

Note this can also be used for [[Hypothesis Testing]] since these coefficients tell us if some independent variable has an effect on the likelihood of some other. For example if $H_0$ is age doesn't affect credit approval this would mean $e^{B_1}=1$. However we can see that the p value for this value of $e^\hat{B_1}$ is 0 (or a very small probability) so we can reject the null hypothesis.

## Logistic Regression Classifier
Up until now we have taken the output of logistic regression to be a probability, an odds ration or a log odds ratio. The equation for the log odds ratio is when $\underline{x}=(x^{(1)},x^{(2)}...x^{(k)})$ 
$$
ln \frac{P(\textrm{Y}=1|\underline{x})}{1-P(\textrm{Y}=1|\underline{x})}=B_0+B_1x^{(1)}+B_2x^{(2)}+...
$$
To turn logistic regression into a classifier all we need to to find a threshold value that in terms of the log odds. Then below this value we predict Y=0 and if log odds is smaller we predict Y=1. So
$$
B_0+B_1x^{(1)}+B_2x^{(2)}+...\ge c
$$
Implies Y = 1 while
$$
B_0+B_1x^{(1)}+B_2x^{(2)}+...< c
$$
Implies Y = 0. C can be anything we like if C = 0 then our  Odds must be 1 ($ln0$) at the boundary that is the chance for either $P_y(1)$ and$ $P_y(0)$ are both $\frac{1}{2}$.

![[Pasted image 20220119000545.png]]
*This is a variety of choices applies to c for a logistical regression classifier of approval for Income and Age*

Here like in [[Linear Regression]] Income has been take log base 10 so just as in linear regression we can change bases to get a more accurate result.

Another reason why logistic regression is useful is it works simple as a scoring system where the value we compare against c is a linear combination of say a persons data relating to their credit score. We can therefore if we want tell them these values so they can understand how to change it.

#### Comparison to [[K Nearest Neighbors]] classifier
![[Pasted image 20220119002913.png]]
KNN differs from logistic regression in a number of key ways

1. The Logistic regression decision boundary is a straight line while the KNN boundary is very nonlinear
2. The KNN gives more flexibility to fit the data however this also allows overfitting.
3. The logistic regression algorithm is much more transparent
4. KNN classifiers benefit from having standardized independent variables as inputs; logistic regression doesn't need this, though it can help if we are regularizing a logistic regression classifier.

*Transparent* meaning it can be easily understood why a data point was placed in a given category. This is since the score that determines log odds is a simple linear combination of the data points attributes $\underline{x}$ 

### Finding the Logistic Regression Coefficients with [[Principle of Maximum Likelihood]]
In [[Linear Regression]] we estimated the $\hat{B_0}$ and $\hat{B_1}$ by the [[Principle of Least Squares]]. Finding the coefficient by minimizing the least squares function. With logistic regression we can use the principle of least squares. So the [[Principle of Maximum Likelihood]] will be used instead. In this we will adjust the coefficient to maximize the likelihood. These coefficient will then be called the **maximum likelihood estimators**.  We need an expression for the maximum loverhood to do this then we optimize with respect to our parameters. However we will have to use [[Numerical Optimization]] to do this instead of solving like in principle of least squares.

First to help we will redefine success and failure from $y_i=0$ for failure and $y_i=1$ for success. We will change this to $y_i=-1$ for failure and $y_i=1$ for success. This them makes
$$
P(Y=y_i|X=x_i)=\frac{y_i+1}{2}f(B_0+B_1x)+\frac{-y_i+1}{2}(1-f(B_0+B_1x))
$$
The reason this works is since we have redefined $y_i$ as either $-1$ or $1$ so thee two parts $\frac{y_i+1}{2}...$ are either 1 or 0 if success and failure. This allows us to switch which probability we are using depending on the $y_i$ value.  The whole idea is that this function is largest when we have a high probability for the correct value and low if not. We therefore want to maximize it over all $i$ to find **maximum likelihood estimators** that give the highest likelihood to the results we have. The second part is our logistic regression function but with the first fraction correcting form out change from 0, 1 to -1, 1.
$$
1-f(B_0+B_1x)=f(-B_0-B_1x)
$$
So we can rewrite $P(Y=y_i|X=x_i)$ as
$$
P(Y=y_i|X=x_i)=\frac{y_i+1}{2}f(B_0+B_1x)+\frac{-y_i+1}{2}f(-B_0-B_1x)
$$
But we know that the fist part will only be selected when $y_i=1$ and the second part will only be selected when $y_i=-1$ so we can take $y_i$ into the f function in both cases giving us this
$$
P(Y=y_i|X=x_i)=\frac{y_i+1}{2}f(y_i(B_0+B_1x))+\frac{-y_i+1}{2}f(yi(B_0+B_1x))
$$
Finally since $\frac{y_i+1}{2}+\frac{-y_i+1}{2}=\frac{2}{2}=1$ we can combine the two parts to get the following
$$
P(Y=y_i|X=x_i)=f(yi(B_0+B_1x))
$$
We can then look at all datapoints together with a $n$ dimensional vectors $\underline{y}$ and $\underline{x}$ giving us
$$
P(Y=\underline{y}|X=\underline{x})=P(Y=y_1|X=x_1)P(Y=y_2|X=x_2)=\prod_{i=1}^nP(Y=y_i|X=x_i)
$$
So from the above equation we the the bellow expression which is the **likelihood of the dataset given the model**/
$$
P(Y=\underline{y}|X=\underline{x})=\prod_{i=1}^nf(y_i(B_0+B_1x))
$$
The problem now is that this is hard to differentiate so we can take a log of the product making it a sum since $ln(ab)=ln(a)+ln(b)$  this makes $ln\prod_{i=1}^nai=\sum_{i=1}^nln(a_i)$ so
$$
lnP(Y=\underline{y}|X=\underline{x})=\sum_{i=1}^nln(f(y_i(B_0+B_1x)))
$$
Now we have a log likelihood which we can differentiate. Then with those derivatives we can perform numerical operation to find $\hat{B_0}$ and $\hat{B_1}$.

[[Logistic Regression Questions]]
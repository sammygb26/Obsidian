# Linear Models
In linear models we want to predict some variable $y$ from some other variable(s) $x$. Here $y$ is the **dependent variable** and $x$ is the **independent variable(s)** also called the **regressor(s)**. We will use concepts from [[Statistical Preliminaries]] to understand this. We are "regressing $y$ from $x$" in this case where regressing just means predicting.

## Covariance
This is a measure of how much two variables values vary on the same gradient. It is equal to 
$$
S_{xy}=\frac{1}{n-1}\sum_{i=1}^n(x_i-\bar x)(y_i-\bar y)
$$
The way this works out is if two variables have a positive then when one's difference from its mean is negative or positive the others will be making the sum positive overall. The opposite is then true if there is a negative relation. This is however a unit dependent measure so its value depends on the variance of the choice variables. The units of this measure will therefore be the units of $x$ times the units of $y$.

## Correlation
This is not a unit dependent measure of how linearly related two variables are. It is equal to
$$
r_{xy}=\frac{S_{xy}}{S_xS_y}=\frac{\sum_{i=1}^{n}(x_i-\bar x)(y_i -\bar y)}{\sqrt{\sum_{i=1}^{n}(x_i-\bar x)^2\sum_{i=1}^{n}(y_i-\bar y)^2}}
$$
This measure has no units and always sits between on the interval $[-1,1]$ it is equal to -1 when the two variables relationship is a perfect straight line sloping down (sloping up if it is 1).

## Standardized Variables
Standardizing variables is a useful way of removing the specifics of the unit used to describe the variable and it also simplifies many processes. To standardize a variable for all values we subtract the mean and divide by the variance.
$$
z_i=\frac{x_i-\bar x}{S_X}
$$

## Simple Regression Method
One simple way of regressing y from x is we split the range of values of x into sections and for each section calculate a mean. We can then predict that for every new x its y value is the average of its bin.
![[Pasted image 20220131104353.png]]
This can work however it doesn't work well for bins with little data and also for bins with no data values cannot be predicted. This leads to another method [[Foundations of Data Science/Linear Regression]]

## Linear Regression
This is a method where we build a linear model that is a function on the x value we give it. Linear function meaning it has the form $y=mx+c$. In specific we want $y=\beta_0+\beta_1x$ where $\beta_0$ and $\beta_1$ are the regression coefficients. This is covered in [[Foundations of Data Science/Linear Regression]]
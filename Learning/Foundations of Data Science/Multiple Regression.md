# Multiple Regression
[[Linear Regression]] can be expanded to work with not just single independent variables, we can use **multiple regression** to do this. We can do this with categorical variables as well by transforming them into numbers. For example a binary number can be transformed into a variables who's values are 0 and 1. As **multiple regression** is just an extension of linear regression the model used is similar. A basic multiple regression model for $k$ variables would look like
$$
y=\beta_0+\beta_1x_1+\beta_2x_2+...+\beta_nx_k
$$
The idea behind multiple regression is we are instead of working in a 2 dimensional space as with simple linear regression we are working in a higher $k+1$ dimensional space. 

## Fitting a Multiple Regression
We use the same **principle of least squares** to do this except with more variables in the function. This would give us
$$
f(\beta_0, \beta_1, ... \beta_k)=\sum_{i=1}^{n}(y_i-(\beta_0+\beta_1x_{i1}+...\beta_k+x_{ik}))^2
$$
We then want to minimize this function giving us our prediction values
$$
\hat y=\hat\beta_0+\hat\beta_1x_1+...\hat\beta_kx_k
$$
The details of the mathematics behind this are given in [[Mathematics Of Multiple Regression]]

## Interpreting Multiple Regression Coefficients
The $\beta_0$ coefficient will be the prediction for the dependent variable $y$ if all other independent $x_i$ variables are 0. Often this doesn't make actual sense. The units for $\beta_0$ will be the units of $y$. The understanding of the $\beta_i$ coefficients is that for every unit increase in $x_i$ we expect a $\beta_i$ increase in $y$. We do also note that for binary values whose use in the model differs form 0 to 1 $\beta_i$ shows the effect of that variable on average compared to the average of if it isn't used.

We can still compute **mean squared error** and **root mean squared error** as they just depend on $\hat y$ and a particular instance of $\bar x$ (input vector).

## Numerical Diagnostics
There are many ways to measure how good a regression fits our data.

**(Root) Mean Squared Error** -> This is just the average of the mean squared error so
$$
\textrm{MSE}=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat y_i)^2
$$
Then the Root Mean Squared Error is simple $\textrm{RMSE}=\sqrt{\textrm{MSE}}$.

**Coefficient of Determination** -> We want a measure of how well our line fits our data that is the portion of the variance in y explained by our line. Variance is captured by the **Total Sum of Squares** defined as the sum of squared distances from the mean of $y$
$$
\textrm{SST}=\sum(y_i-\bar y)^2=(n-1)s_y^2
$$
To capture how much of this isn't explain by our line we use **Sum of Squared Errors** defined as the sum of squared distances from the prediction.
$$
\textrm{SSE}=\sum(y_i-\hat y_i)^2
$$
The **Coefficient of Determination** is therefore
$$
R^2=\frac{\textrm{SST}-\textrm{SSE}}{\textrm{SST}}=1-\frac{\textrm{SSE}}{\textrm{SST}}
$$
We can compare these diagnostics when using multiple regression on all data vs regression on just single independent variables or collections of variables. 

**Interpreting Coefficient of Determination** -> One problem with splitting up regression for example with binary variables is that our individual SST will be as the binary variable is perfectly controlled for. But this will mean that $R^2$ is much larger than is reasonable if we are comparing into the individual split up regressions. 

**Lurking Variables** -> This is when we have some variable that explains much of the variation in a sample. When we don't include this it becomes a **lurking variable** that if included could reduce the error in our estimate.

## Interaction Terms and Non-linear Fits
We we wanted to have the effect of one variable in our model modulated by another we could include an **interaction term** to take this into account. The interaction term is basically a new independent variable defined as the product of some other independent variables. Our model becomes with two independent variables $x_1$ and $x_2$ and their interaction ($x_3=x_1x_2$)
$$
y=\beta_0+\beta_1x_1+\beta_2x_2+\beta_3x_1x_2
$$
We can also have a **non-linear** model where we also include terms that are for example polynomial functions on other variables ($x_2=x_1^2$)
$$
y=\beta_0x_1+\beta_2x_1^2
$$
This can all lead to a problem called **overfitting** where our regression fits our training data so well that it fails to generalize to our real world data. This motivates the use of **adjusted R-squared** to measure our performance.

## Adjusted R-squared
As we increase the number of coefficients we take our regression into higher and higher dimensions but if we are doing this then how can we be sure we aren't overfitting and just memorizing the data while not generalizing.
$$
R_a^2=1-\frac{n-1}{n-(k+1)}\frac{SEE}{SST}
$$
So its basically a version of $R^2$ scaled down by the number of coefficient used in the regression compared to the number of variables. The $\frac{n-1}{n-(k+1)}$ is always greater than 1 hence $R_a^2<R^2$ always.

## Correlated Independent Variables
Some of our independent variables can be correlated. This means a change in 1 can predict a change in another. If we have correlated variables in our model it can lead to strange effects like for example a variable that is positively correlated with our dependent having a negative coefficient as all the growth can be explained by some other variable that is correlated with our independent variable.
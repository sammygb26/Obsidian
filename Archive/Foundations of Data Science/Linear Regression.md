## Linear Regression
Linear regression is a method for building a **linear model** where we use a linear function on some **independent variables** to predict some other variable's (the **dependent variable**) value. This will use many part from [[Statistical Preliminaries]]. The independent variables are therefore called the **regressors**. We predict y using a linear function of x. If $x$ is the regressor and $y$ is the dependent then we are "regressing $y$ on $x$". Linear function meaning it has the form $y=mx+c$. In specific we want $y=\beta_0+\beta_1x$ where $\beta_0$ and $\beta_1$ are the regression coefficients.

## Principle of Least Squares
We can describe how bad our choice of $\beta_0$ and $\beta_1$ is by an error function. A good way is the SSE of Sum of Squared Errors function. That is for all our data we have $\hat y=\hat\beta_1x + \hat\beta_0$ where $\hat\beta_0$ and $\hat\beta_1$ are estimates for $\beta_0$ and $\beta_1$. Then $\hat y$ is out predicted value for $y$ given $x$. The sum or squared errors function is then described for a choice of $\beta_0$ and $\beta_1$.
$$
f(\beta_0,\beta_1)=\sum_{i=1}^{n}(y_i-(\beta_0+\beta_1 x))^2
$$
Our search for the values of $\beta_0$ and $\beta_1$ will give us the estimates $\hat\beta_0$ and $\hat\beta_1$. We do this by applying [[Calculus]] specifically [[Multivariable Calculus]]. We first take partial derivatives for each variable we are solving for and set them to 0
$$
\frac{\delta f}{\delta \beta_0}=\sum_{i=1}^{n}(-2)(y_i-\beta_0-\beta_1x_i)=0
$$
$$
\frac{\delta f}{\delta\beta_1}=\sum_{i=1}^n(-2x_i)(y_i-\beta_0-\beta_1x_i)=0
$$
We can change around these formulas to get the following
$$
n\beta_0+\left(\sum x_i\right)\beta_1=\sum y_i
$$
$$
\left(\sum x_i\right)\beta_0+\left(\sum x_i^2\right)\beta_1=\sum x_i y_i
$$
We can remove $\beta_0$ and note that $\sum_{i=1}^{n}(x-\bar x)^2=\sum_{i=1}^{n}x_i^2-n\bar x^2$ to give us
$$
\hat\beta_1=\frac{\sum x_i y_i-n\bar x\bar y}{\sum x_i^2-n\bar x^2}=\frac{\sum(x_i-\bar x)(y_i-\bar y)}{\sum(x_i-\bar x)^2}
$$
If we solve for $\beta_0$ we can also get
$$
\hat\beta_0=\bar y-\hat\beta_1\bar x
$$
These are the formulas for our regression line.

## Properties of Regression Line
We know the line passes through $(\bar x, \bar y)$ from the equation for $\hat\beta_0$ which gives us
$$
y=\hat\beta_0+\hat\beta_1 x=\bar y-\hat\beta_1\bar x+\hat\beta_1 x=\bar y+\hat\beta_1(x-\bar x)
$$
Hence when $x=\bar x$, $y=\bar y$. We can also note that the regression lines for $y$ on $x$ and $x$ on $y$ will be different. 
![[Pasted image 20220131112402.png]]
The would be the same if the correlation coefficient was 1 or -1 but due to the being points spread around the center this line is sloped so that the predictions are closer to the mean. This is called **regression to the mean** and makes sense since more average variables are infract more likely.

## Diagnostics
We can also show a residual plot where we subtract $\hat y$ from all $y$ values giving the part of $y$ not captured by our line. These new points will have a linear correlation coefficient of 0 and a mean of $(0,0)$.
![[Pasted image 20220131112724.png]]
If we can see some pattern in the remaining data it can be a sign there is some part of our data not explained by our regression and we may need another prediction tool this is called **nonlinearity**.
![[Pasted image 20220131112911.png]]
One way of dealing with exponential type **nonlinearity** and still use linear regression is to **transform** the data. We can do this by applying functions to it before we run our prediction. For example with population growth we can instead predict log population since population often grows exponentially.

Another problem transforming can solve partially is **heteroscedasticity** which is when the variance of our dependent variable changes with our independent variable. Since a logarithm would make larger value smaller to a greater level than smaller ones this could help in some cases with heteroscedasticity.
![[Pasted image 20220131113253.png]]

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

[[Linear regression Questions]]





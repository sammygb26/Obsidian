**Gaussian filters** are an important family of recursive state estimators. This were historically the first tractable implementations of the Bayes filter for continuous spaces. Here our **belief** is represented by a multivariable normal distribution. This normal distribution is given by the equation $$p(x)=\det(2\pi\Sigma)^{\frac12}\exp\{-\frac12(x-\mu)^T\Sigma^{-1}(x-\mu)\}$$ Here $\mu$ is the mean (vector) and $\Sigma$ is the covariance (matrix). The covariance will will be symmetric and positive semidefinite.  There are ramifications to this choice mainly that gaussians are unimodal. This is generally good for robotics but bad in general for problem where there may be multiple solutions. The **parameterization** of the above is called the *moments parameterization*. 

### The Kalman Filter
This filter uses the **moments parameterization** each belief is represented with a mean $\mu_t$ and a covariance $\Sigma_t$ for a gaussian distribution. The posterior probabilities will also be gaussian if the Markov assumptions are made as well as three properties.

1. **Linear Gaussian** - The state transition probability $p(x_t|u_t,x_{t-1})$ must be a *linear* function in its arguments with added Gaussian noise. This is expressed as $$x_t=A_tx_{t-1}+B_tu_t+\epsilon_t$$ Here $x_{t-1}$ and $x_t$ are state vectors, and $u_t$ is the control vector at time $t$. $A_t$ and $B_t$ are matrices. $A$ is square in the size of $x_t$/$x_{t-1}$ while $B$ takes in a vector the size of $u_t$ making a vector of $x_t$. This function is always **linear** in its arguments. This is a condition for the Kalman filter. The random variable $\epsilon_t$ is a gaussian random vector that models the uncertainty introduced by the state transition. It will have a mean of $0$ and its covariance will be $R_t$. The equation above gives our probability distribution ![[Pasted image 20221217102726.png]]
2. **Measurement probability us linear in its arguments with Gaussian noise**. When We say measurement probability we mean $p(z_t|x_t)$ is a gaussian linear in its arguments with added gaussian noise. $$z_t=C_tx_t+\delta_t$$ Here $C_t$ takes in a vector the size of $x_t$ and gives a predicted vector the size of our measurement. $\delta_t$ is a multivariate Gaussian with zero mean and covariance $Q_t$. The measurement probability is thus given by the following distribution ![[Pasted image 20221217103106.png]]
3. The initial belief is also a normal distribution with mean $x_0$ and covariance $\Sigma_0$ ![[Pasted image 20221217103201.png]]

These assumptions ensure the posterior $bel(x_t)$ is always a Gaussian for any point in time $t$.

##### Algorithm
The **Kalman Filter** represent the belief at tie $t$ by the mean $\mu_t$ and covariance $\Sigma_t$. The input to the algorithm is the previous mean and covariance along with the control vector and measurement vector. The mean is updated first using a deterministic version of the state transition function then the covariance is updated to incorporate added randomness. We then have our belief before we incorporate our measurement $z_t$. The **Kalman Gain** is $K_t$ and it encodes how much of the measurement it incorporate into the new state estimate. The remaining lines then manipulate the mean and covariance to be inline with this gain. The term $z_t-C_t\bar\mu_t$ is called the **innovation**. This is the difference between the actual measurement and the expected measurement.

![[Pasted image 20221217104910.png]]

### The Extended Kalman Filter
Any non-linear dynamic cannot be captured by the standard Kalman filter so instead we relax the assumption requiring that our update and measurement models are linear in our previous state. Instead we allow for non-linear function but we **linearize** them to allow us to use the Kalman filter. In the **extended Kalman Filter** we have our model as $$x_t=g(_t,x_{t-1})+\epsilon_t\hspace{64pt}z_t=h(x_t)+\delta_t$$$g$ replaces the $A_t$ and $B_t$ matrices from the Kalman filter while $h$ replaces the $C_t$ matrix. With arbitrary function however this means the belief is no longer Gaussian. Infact performing a belief update in these circumstances has no closed form solution. So instead EKF predicts an approximation of the true belief given these states.

##### Linearization Via Taylor Expansion
We approximate $g$ with a linear function which it the tangent of $g$ at the mean $\mu_t$. Still an error is given by this approximation. We linearize using the **Taylor expansion** at the point most likely to be our true value. Again this will be the mean. We get the following when linearizing at $\mu_{t-1}$ (previous best guess) as well as the new mean $\mu_t$. This linearization is given as the matrix $G_t$.

![[Pasted image 20221217122021.png]]

If we write this as a Gaussian we get

![[Pasted image 20221217122319.png]]

$G_t$ is called the **Jacobian matrix**. It depends on $\mu_t$ and $\mu_{t-1}$ and so differs as time passes.

This same technique is used for the measurement function $h$. But this time the expansion is taken around $\bar\mu_t$ (most likely state).

![[Pasted image 20221217122546.png]]

with $h'(x_t)=\frac{\partial h(x_t)}{\partial x_t}$. If we write this as a gaussian we get

![[Pasted image 20221217122645.png]]

##### EKF Algorithm
The EKF algorithm is similar to the standard KF algorithm. The most important difference in the replacement of $A_t$ and $B_t$ with $g$ and the replacement of $C_t$ with $h$. EKFs use Jacobians $G_t$ and $H_t$ instead of the corresponding linear system matrices $A_t$, $B_t$ and $C_t$

![[Pasted image 20221217122839.png]]

##### Practical
The EKF has become the most popular tool for state estimation. It is simple and computationally efficient. How well the approximation performs depends on two factors. The degree of uncertainty and the degree of non-linearity. 

EKF is commonly extended to take a sum of gaussians between each state. This allows the filter to pursue multiple distinct hypothesis. This can be represented as $$\text{bel}(x_t)=\frac1{\sum_t\psi_{t,l}}\sum_l\psi_{t,l}\det\left(2\pi\sum_{t,l}\right)^{-\frac12}\exp\left\{\frac12(x_t-\mu_{t,l})^T\Sigma_{t,l}^{-1}(x_t-u_{t,l})\right\}$$Here $\psi_{t,l}$ are mixture parameters with $\psi_{t,l}\ge0$ These serve as weights for the different gaussian mixtures.
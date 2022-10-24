This filter was created by **Rudolf Kalman** (given national medal of science for it). This was a key *weapon* behind the apollo lunar module (used in the lunar computer). This model allows us to estimate the **state** of some robot that is continuously changing over time. It does this by comparing a model of how the state should evolve with an observed state. Both are uncertain but together we can get a more accurate reading.

![[Pasted image 20221020112148.png]]

### States of Mobile Robot
The **state** of a robot is a set of quantities such as position, orientation and velocity (though it could be anything). A **motion model** can be used to predict the robots future state after some period of time. We predict $\check{\textbf x}_k$ (guess) from $\hat{\textbf x}_{k-1}$ (estimate for previous state) which is itself a combination of $\check{\textbf x}_{k-1}$ and $\textbf y_{k-1}$ (measured state). The calculation of the $\textbf y_k$ values is our **measurement model**.

![[Pasted image 20221020111648.png]]

An example is *integration* of the velocity to give us the displacement and next position based on the current position and orientation. **State estimation** is the core to the localization problem as direct localization can fail to provide accurate results.

##### Urban Canyons

Problems with localization can occur here when satellites aren't in line of sight. Multiple positions can be given. The key idea is to combine where we guess we are with observations. We **predict and correct**.
![[Pasted image 20221020111857.png]]

### Overall model
1. **Predict next state** with some uncertainty
2. **Measure** the experimental position with some uncertainty
3. The we **combine** to increase certainty of our prediction.

![[Pasted image 20221020112108.png]]

### Model
The **Kalman filter** requires the following motion and measurement models:

![[Pasted image 20221020112333.png]]

$\mu$ can be through of as the input in the case of a car it may be acceleration. The $F$ and $G$ are matrices that  parse our input into the form of $x$. We assume both the noise variables are **gaussian**:

![[Pasted image 20221020112614.png]]

Because of the noise this means both $\textbf x_k$ and $\textbf y_k$ are random variables. Now $\textbf F_{k}$ (**prediction matrix**) is our prediction step matrix. This can represent a system of linear equations that describe how the state of our system evolves over time. Say if we have $\hat{\textbf x}_k$ as our predicted position of the form $[p, v]$ for position and velocity. Then we would have the equations: $$p_k=p_{k-1}+\Delta t\cdot v_{k-1}$$ $$v_k=v_{k-1}$$ Then our transition matric would be $\textbf F_k=[1 \hspace{6pt}\Delta t, 0\hspace{6pt}1]$.  Hence we have $\check{\textbf {x}_k}=\textbf F_{k-1}\hat{\textbf x_{k-1}}$ (where the check just means its our guess). We also have a covariance matrix $\hat{\textbf P}_k$ for $\hat{\textbf x}_k$ as we aren't sure about our state. We need to update this the same as $\textbf x$ itself. 

![[Pasted image 20221020165637.png]]

Hence we get an update for $\textbf x$ and $\textbf P$ that is: $$\check{\textbf x}_k=\textbf F_{k-1}\hat{\textbf{x}}_{k-1}$$$$\check{\textbf P}_k=\textbf F_{k-1}\hat{\textbf P}_{k-1}\textbf F_{k-1}^T$$
We keep track of changes we know are happening that affect our current model with some vector of changes $\textbf u_k$ and some matrix $\textbf B_k$. We also need to keep track of **external uncertainty** this mean that things we cannot predict as part of our model like random wind or slipping can occur (in the example of a car or robot). We add onto this model the uncertainty of $\textbf Q_k$ which is a covariance matrix.  Hence at this point: $$\check{\textbf x}_k=\textbf F_{k-1}\hat{\textbf{x}}_{k-1}+\textbf G_{k-1}\textbf u_{k-1} $$$$\check{\textbf P}_k=\textbf F_{k-1}\hat{\textbf P}_{k-1}\textbf F_{k-1}^T+\textbf Q_{k-1}$$
### Updating with Measurements
Now we have our model but we also get **readings** from our sensors. These may not be in the same units as our state $\textbf x_k$ so we convert with a matrix $\textbf H_k$ this transfers our state $\textbf x_k$ into the units of our readings. From these we can get our expected sensor readings:

![[Pasted image 20221020171457.png]]


Now this is simple however instead we have a random of states a sensor reading could refer to as our sensors aren't perfect. We need to compare the state we are likely to be in from our model to the likelihood given our sensor readings. This gives us the **sensor noise** $\textbf R_k$. The mean of our sensor distribution is just the reading we observe written as $\textbf y_k$. 

This defines for every possible sensor state two probabilities. The probability of it being right and we have  measured with noise some $\textbf y_k$ value. And the probability is right and we are however far away from our $\hat{\textbf x}_k$ state. The overall probability is the both are true. Hence we multiple the two together and infect get another gaussian distributed vector wit a mean and covariance matrix.

### Kalman Gain
Now we have two **Gaussians** we want to multiple them together. That is we want to find the blue distribution from the green and pink ones bellow. We know also these gaussian have the form in 1D at least as $$p_{x\sim\mathcal N(\mu,\sigma^2)}(x)=\frac1{\sigma\sqrt{2\pi}}\exp\left(-{\frac1{2\sigma^2}}(\mu-x)^2\right)$$
![[Pasted image 20221020180356.png]]

Multiplying multiple equations like this together we get:

![[Pasted image 20221020180336.png]]

We can take a factor $k$ out to makes these simpler.

![[Pasted image 20221020180423.png]]

But this is just single values so in matrix form it becomes.

![[Pasted image 20221020180505.png]]

Now we call $\textbf K$ the **Kalman Gain**. In our example it becomes $$\textbf K_k=\textbf H_k\check{\textbf P}_k\textbf H_k^T(\textbf H_k\check{\textbf{P}}\textbf H_k^T+\textbf R_k)^{-1}$$Now we simply the equations by removing $\textbf H_k$ of the front giving us:

![[Pasted image 20221020112723.png]]

Optimal gain also called **Kalman Gain**. $K_k$ the *optimal gain* can be through of as our confidence in our prediction. It changes all the time and allows our model to be updated over time.

![[Pasted image 20221020113031.png]]

# Extended Kalman Filter
We are assuming everything is **linear** however sometimes processes are *non-linear*. We example we may want to use *non-linearities* if we need to use trigonometry.

![[Pasted image 20221020113933.png]]

But we can only use linear function in any KF as without this our gaussian functions will be destroyed. We do this by using **Taylor Series** expansion. $$f(x)=f(a)+\frac{f'(a)}{1!}(x-a)+\frac{f''(a)}{2!}(x-a)+...$$With just a linear model we cannot get too good enough result; we will use a expansion to estimate our non-linear model. In **EKF** we only expand the 1st order terms hence still "use" a set of linear equations each time we run the filter.

![[Pasted image 20221020114122.png]]

We need to choose a point to **linearize over**. For this we pick the most recent state estimate. We need to rely on the most recent state we use our quests state and add on our first and second order derivatives as $\textbf F_k$ and $\textbf L_k$.

![[Pasted image 20221020114333.png]]

### Jacobian Matrix
A **Jacobian matrix** is  matrix composed of the first-order partial derivates of a multivariable function. Where the output of that function can be multiple variables.  That is 

![[Pasted image 20221020122110.png]]
It will always have an many rows as vector components $(f_1, f_2,...,f_m)$ and as many columns as variables $(x_1,x_2,...,x_n)$.


### Putting it all together
![[Pasted image 20221021194523.png]]
![[Pasted image 20221021194538.png]]
Is the reason the prediction equation bellow does have the F and L terms because we are linearizing at the $\hat{\textbf x}_{k-1}$ value?
![[Pasted image 20221021194557.png]]

### Working Example
If we imaging some car it will have a position $p$ and a velocity $\dot p$ so we measure its state with $\textbf x=[p\hspace{6pt}\dot p]^T$ then we also have $\textbf u$ our known changes which will be our acceleration $\textbf u =\ddot p$. With this we can build a simple *motion/process model* as $$\textbf x_k=f(\textbf x_{k-1},\textbf u_{k-1},\textbf w_{k-1})=[1\hspace{6pt} \Delta t, 0\hspace{6pt} 1]\textbf x_{k-1}+[0\hspace{6pt} \Delta t]^Tu_{k-1}+\textbf w_{k-1}$$Now our **measurement model** will be more complicated as the observed values is connected via a non-linear function: $$y_k=\phi_k=h(p_k,v_k)=\tan^{-1}\left(\frac{S}{D-p_k}\right)+v_k$$We also have the noise densities $v_k\sim\mathcal N(0,0.01)$ and $\textbf w_k\sim\mathcal N(\textbf0,(0.1)\textbf1_{2\times2})$. Now we need to find the **Jacobians** which is done by differentiating our $\textbf f$ and $h$ functions. $$\textbf F_{k-1}=
\left.
\frac
{\partial \textbf f}
{\partial \textbf x_{k-1}}
\right|
_{\hat{\textbf x}_{k-1},\textbf u_{k-1},\textbf 0}
=
\begin{bmatrix}  
1 & \Delta t \\  
0 & 1  
\end{bmatrix}
\hspace{16pt}

\textbf L_{k-1}
=
\left.
\frac
{\partial \textbf f}
{\partial \textbf w_{k-1}}
\right|
_{\hat{\textbf x}_{k-1},\textbf u_{k-1},\textbf 0}
=
\textbf 1_{2\times 2}$$Now for the $h$ function $$
\textbf H_k=\left.
\frac
{\partial h}
{\partial \textbf x_k}
\right|
_{\check{\textbf x}_{k},\textbf 0}
=
\begin{bmatrix}
\frac{S}{(D-\check{\textbf p}_k)^2+S^2} & 0
\end{bmatrix}
\hspace{16pt}
\textbf M_k=
\left.
\frac
{\partial h}
{\partial v_k}
\right|
_{\check x_k, \textbf 0}
=
1
$$


![[Pasted image 20221020115025.png]]

![[Pasted image 20221020115040.png]]

![[Pasted image 20221020115050.png]]

### Limitations of EKF
The EKF works by linearizing the non-linear motion and measurement models to update the mean and covariance state. The difference between the linear approximation and the nonlinear function is called **linearization error** this depends on :

1. How non-linear the function is
2. How **far away** from the operating point the linear approximation is being used.

##### Linearization Error example
Take two coordinate systems polar and Cartesian. We take some **non-linear** function form one to the other.  When using a **linearized-model** the mean and covariance will be completely different.

![[Pasted image 20221020115453.png]]

Hence we have to ensure the system dynamic are not highly nonlinear and the sensor sampling time is slow relative to how fast the system is evolving (points move far form the estimation in the model). This can lead to:

1. The estimated mean state can become very different form the true state
2. The estimated state covariance can fail to capture the true uncertainty - *overconfident*

The Jacobian matrices can also be a source of error in EKF implementations as: 

1. They can be prone to error when calculated by humans
2. Numerical differentiation can be slow and unstable
3. Automatic differentiation can also be *unpredictable*

[[Kalman Filter Questions]]



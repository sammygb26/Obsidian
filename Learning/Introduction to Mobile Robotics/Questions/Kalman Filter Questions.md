What does the Kalman filter allow? #flashcard #MOB #KalmanFilter
	The **Kalman Filter** allows a distribution of possible states to be combined/checked against measurements. This allows us to get a far more accurate estimation of current state.

---
What is the state of some system (Kalman)? #flashcard #MOB #KalmanFilter 
	The **state** of some system is a set of quantities that describe "state" of said system for some point in time.

---
In the Kalman filter what different values are combined (symbols) for a given step? #flashcard #MOB #KalmanFilter 
	For the step from $k-1$ to $k$ we start with the variable $\hat{\textbf x}_{k-1}$ (with covariance $\hat{\textbf P}_{k-1}$) which is our estimate for our state in the previous timestep. We then use this to predict $\check{\textbf x}_k$ which is our guess for the next state (with covariance $\check{\textbf P}_k$). We then use our sensors to find our measured state $\textbf y_k$. We then combine $\check{\textbf x}_k$ and $\textbf y_k$ to find our new estimated state $\hat{\textbf x}_k$.

---
What is an example covered in the Kalman lecture for unreliable sensors? #flashcard #MOB #KalmanFilter 
	An example is GPS in a city where reflections of buildings can cause times to be slightly different leading to error in GPS localization.

---
What two models are needed for the Kalman filter? #flashcard #MOB #KalmanFilter 
	We need a **motion model** and a **measurement model**.

---
What is the form of the motion model is the Kalman filter and what are the parts? #flashcard #MOB #KalmanFilter 
	In the linear case it has the form $$\textbf x_f=\textbf F_{k-1}\textbf x_k+\textbf G_{k-1}\textbf u_{k-1}+\textbf w_{k-1}$$Where $\textbf F$ is a matrix describing a set of linear equations taking one state of the system to another. Then $\textbf G$ is the same just taking in known changes to the system. $\textbf w$ is a random term taking into account unknown changes (process or motion noise).

---
What is the form of the measurement model of the Kalman filter and what are the parts? #flashcard #MOB #KalmanFilter 
	In the linear case it has the from $$\textbf y_k=\textbf H_k\textbf x_k+\textbf v_k$$Here $\textbf H$ is a matrix describing the relation between the sensors and the current state then $\textbf v$ is random term (measurement noise) taking part in errors in the readings.

---
What are the two types of noise in the Kalman filter system? #flashcard #MOB #KalmanFilter 
	There is the **measurement noise** and the **process motion noise**.

---
What is the distribution of the measurement noise in the Kalan filter? #flashcard #MOB #KalmanFilter 
	This will be $$\textbf v_k\sim\mathcal N(0,\textbf R_k)\hspace{16pt}\textbf w_k\sim\mathcal N(0,\textbf Q_k)$$ So $\textbf R$ is the covariance in $\textbf v$  (measurement noise) and $\textbf Q$ is the covariance in $\textbf w$.

---
How can we encode a simple position and acceleration system into the Kalman filter model's F matrix? #flashcard #MOB #KalmanFilter 
	This system will have two variables $p$ position and $v$ velocity. Hence we can have two equations also: $$p_k=p_{k-1}+\Delta t\cdot v_{k-1}\hspace{16pt}v_k=v_{k-1}$$ Hence the rows of $\textbf F$ will be $[1\hspace{6pt}\Delta t]$ and the second row will be $[0\hspace{6pt}1]$.

---
When applying a matrix multiplication to a random vector variable what operation happens to its covariance matrix? #flashcard #MOB #KalmanFilter 
	If we have $Cov(x)=\Sigma$ then $Cov(\textbf A x)=\textbf A\Sigma\textbf A^T$ 

---
What are the equations to update x with our motion model? #flashcard #MOB #KalmanFilter 
	We have $$\check{\textbf x}_k=\textbf F_{k-1}\hat{\textbf{x}}_{k-1}+\textbf G_{k-1}\textbf u_{k-1} \hspace{16pt}\check{\textbf P}_k=\textbf F_{k-1}\hat{\textbf P}_{k-1}\textbf F_{k-1}^T+\textbf Q_{k-1}$$

---
What is the Kalman gain? #flashcard #MOB #KalmanFilter 
	The Kalman gain comes from the multiplication of our two distributions for sensor states coming together (multiplication). This describes a thirds distribution where the Kalman gain is a figure taking our to scale between the two.

---
What is H in the Kalman Filter model? #flashcard #MOB #KalmanFilter 
	This is a matrix describing the sensor date we would get given some state. Hence it allows us to translate our predicted state into the same space as our sensor readings.

---
What is the formula for Kalman gain? #flashcard #MOB #KalmanFilter 
	The formula is: $$\textbf K_k=\check{\textbf P}_k\textbf H_k^T(\textbf H_k\check{\textbf{P}}\textbf H_k^T+\textbf R_k)^{-1}$$

---
What is the formula for the corrected prediction x hat in the Kalman filter? #flashcard #MOB #KalmanFilter 
	This formula is: $$\hat{\textbf x}_k=\check{\textbf x}_k+\textbf K_k(\textbf y_k-\textbf H_k\check{\textbf x}_k)$$
	
---
What is the formula for the corrected prediction correlation matrix? #flashcard #MOB #KalmanFilter 
	This would be: $$\hat{\textbf P}_k=(1-\textbf K_k\textbf H_k)\check{\textbf P}_k$$

---
What is the term (yk-Hkxk) often called? #flashcard #MOB #KalmanFilter 
	The formula $(\textbf y_k-\textbf H_k\check{\textbf x}_k)$ is often called the **innovation**.

---
What is the extended Kalman filter? #flashcard #MOB #KalmanFilter 
	This is an extension on the regular Kalman filter that allows it to approximate non-linear functions.

---
What is the tailor series expansion of some function at a point a? #flashcard #MOB #KalmanFilter 
	This will be:
		$$f(x)=f(a)+\frac{f'(a)}{1!}(x-a)+\frac{f''(a)}{2!}(x-a)+...$$

---
How does EKF approximate non-linear functions? #flashcard #MOB #KalmanFilter 
	EKF uses the tailor series expansion to create an approximate linear function which we can then use in the Kalman equations.

---
How would we linearize a motion model in EKF? #flashcard #MOB #KalmanFilter 
	We take some function giving $\textbf x$ values $\textbf x_k=\textbf f_{k-1}(\textbf x_{k-1},\textbf u_{k-1},\textbf 0)$ this can be approximated form our estimate value. That is: $$\textbf x_k=\textbf f_{k-1}(\textbf x_{k-1},\textbf u_{k-1},\textbf 0)$$$$\approx\textbf f_{k-1}(\hat{\textbf x}_{k-1},\textbf u_{k-1},\textbf 0) $$$$= \textbf f_{k-1}(\hat{\textbf x}_{k-1},\textbf u_{k-1},\textbf 0)+ \left. \frac {\partial\textbf f_{k-1}} {\partial\textbf x_{k-1}} \right| _{\hat{\textbf x}_{k-1},\textbf u_{k-1},\textbf 0} (\textbf x_{k-1}-\hat{\textbf x}_{k-1})+\left.\frac{\partial\textbf f_{k-1}}{\partial\textbf w_{k-1}}\right|_{\hat{\textbf x}_{k-1},\textbf u_{k-1},\textbf 0}\textbf w_{k-1}$$Where the first partial derivative becomes $\textbf F_{k-1}$ and the second becomes $L_{k-1}$.

---
How would we linearize a measurement model? #flashcard #MOB #KalmanFilter 
	We take some function giving $\textbf y$ values $\textbf y_k=\textbf h_{k}(\textbf x_{k},\textbf v_k)$ this can be approximated form our estimate value. That is: $$\textbf y_k=\textbf h_{k}(\textbf x_{k},\textbf v_k)$$$$\approx\textbf h_{k}(\hat{\textbf x}_{k-1},\textbf 0)$$$$\left. \frac {\partial\textbf h_{k}} {\partial\textbf x_{k}} \right| _{\hat{\textbf x}_{k},\textbf 0} (\textbf x_{k}-\hat{\textbf x}_{k}) + \left. \frac {\partial\textbf h_{k}} {\partial\textbf v_{k}} \right| _{\hat{\textbf x}_{k},\textbf 0} \textbf v_k$$Where the first partial derivative becomes $\textbf F_{k-1}$ and the second becomes $L_{k-1}$.

---
What is a Jacobian matrix? #flashcard #MOB #KalmanFilter 
	A **Jacobian Matrix** is a matrix made our of first order partial derivatives of a multivariable function. For $n$ inputs and $m$ outputs it is an $m\times n$ matrix. So if $f$ is of the form $f(x_1,x_2,...,x_n)=(f_1,f_2,...,f_m)$ then we have  the Jacobian matrix $J_f=[j_{il}]$ where $$j_{il}=\frac{\partial f_i}{\partial x_l}$$

---
What is the form of the linearized motion model for EKF? #flashcard #MOB #KalmanFilter 
	This will be $$\textbf x_k=\textbf f_{k-1}(\hat{\textbf x}_{k-1},\textbf u_{k-1},0)+\textbf F_{k-1}(\textbf x_{k-1}-\hat{\textbf x}_k)+\textbf L_{k-1}\textbf w_{k-1}$$Remembering that in fact $\textbf F$ and $\textbf L$ are partial derivatives of the underlying model.

---
What is the form of the linearized measurement model for EKF? #flashcard #MOB #KalmanFilter 
	This will be $$\textbf y_k=\textbf h_k(\check{\textbf x}_k,0)+\textbf H_k(\textbf x_k-\check{\textbf x}_k)+\textbf M_k\textbf v_k$$Remembering that in fact $\textbf H$ and $\textbf M$ are partial derivatives of the underlying model.

---
What is the prediction step in EKF? #flashcard #MOB #KalmanFilter 
	The prediction step is $$\check{\textbf x}_k=f_{k-1}(\hat{\textbf x}_{k-1},u_{k-1},0)$$and then for the covariance matrix$$\check{\textbf P}_k=\textbf F_{k-1}\hat{\textbf P}_{k-1}\textbf F_{k-1}^T+\textbf L_{k-1}\textbf Q_{k-1}\textbf L_{k-1}^T$$

---
What is the Kalman gain for the EKF? #flashcard #MOB #KalmanFilter 
	This would be $$\textbf K_k=\check{\textbf P}_k\textbf H_k^T(\textbf H_k\check{\textbf P}_k\textbf H_{k}^T+\textbf M_k\textbf R_k\textbf M_k^T)^{-1}$$

---
What is the correction step for the EKF? #flashcard #MOB #KalmanFilter 
	The correction step is $$\hat{\textbf x}_k=\check{\textbf x}_k+\textbf K_k(\textbf y_k-\textbf h_k(\check{\textbf x}_k,0))$$and then for the covariance matrix $$\hat{\textbf P}_k=(1-\textbf K_k\textbf H_k)\check{\textbf P}_k$$

---
What is the linearization error with EKF? #flashcard #MOB #KalmanFilter 
	This is the difference between the linear approximation the the non-linear underlying function we are modeling.

---
What does the linearization error in EKF depend on? #flashcard #MOB #KalmanFilter 
	This depends on how non-linear the function is and how far away form the operating point the linear approximation is being used.

---
What are the two failure states linearization error can lead to? #flashcard #MOB #KalmanFilter 
	Either the estimated mean is very different form the true state or the state covariance doesn't capture uncertainty and we are overconfident.

---
Why are Jacobian matrices a source of EKF error? #flashcard #MOB #KalmanFilter 
	They are a source of EKF error due to error calculating them aswell and numerical and automatic differentiation to find them being unstable and the former also being slow.

---

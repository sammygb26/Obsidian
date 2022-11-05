# Optimizers
There are many optimizers that are names after the algorithms they implement. The choice of the optimizer can affect how long it takes to train from hours to days.

### Stochastic Gradient Descent
This is the simplest optimizer. We can think of an assignment of values to the network as an input to a function. This function returns the **loss** which describes how badly we solve our problem. For $i$ weights we will be in a $i$ dimensional space and can calculate an $i$ dimensional vector in this space pointing in the direction that will reduce. So for this algorithm we take a small step in that direction hoping to reduce loss. Our *learning rate* will be the fraction of this gradient we use to move our point by. This **LR** parameter highly affects the convergence with higher learning rates in some cases descending faster although they can also miss the minimum and get a higher values or be incapable of finding a minimum without chance on their side. 

Standard **gradient descent** requires we take a true loss calculated over the entire dataset. However this is expensive computationally for very large datasets. **SGD** randomly picks just one sample to descend over. This work especially well when we have lost of very similar data. This way it's not needed for us to use all the data to get accurate results. The *redundant* data wouldn't be needed and is just making computation harder. The strict definition only has one data point being used however it is more common to use a *mini-batch* for each step.

### Mini Batch Gradient Descent
*Gradient descent* can already be sped up using batching where we stack examples into a larger data structure $X$. We can process all $m$ examples quicker but with very large $m$ we must process our entire training step before taking a small step. A better solution is to take some steps before we even finish our entire set. We split out training set into smaller parts called **mini batches** these may have 1000 examples instead of say 5000000. So we split our $X$ into many batches $X^{\{1\}}..X{\{2\}}...X^{\{s\}}$.Them we have a similar case for $Y$ giving $Y^{\{1\}}..Y{\{2\}}...Y^{\{s\}}$. Where $s$ is the number of mini batches. Some *mini batch* $t$ is made out of $X^{\{t\}},Y^{\{t\}}$. Then $X^{\{t\}}$ will have dimension $(n_x,m/s)$ and $Y^{\{t\}}$ similarly. We simply implement 1 step of gradient descent for each batch. Each pass though all mini-batched is called an **epoch**.

##### Understanding
With batch gradient descent we go through every example on each run of gradient descent. We expect the *cost* to go down on each generation. But in mini-batch gradient descent we are training trying to minimize a different batch each time. This will cause the function to be noisier.

![[Pasted image 20220715211412.png]]

It should still train downwards thought. But some mini-batches may by change perform worse or better. One parameter we need to choose in the *mini-batch size*. With this equal to $m$ we get batch gradient descent. The *mini-batch* size could also be equal to 1 making this **Stochastic Gradient Descent** where each example is a minibatch. For this we look at a example then take a step and repeat. We can compare the two strategies. With SGD in purple and BGD in blue.

![[Pasted image 20220715211917.png]]

BGD converges smoothly to a minima however SGD doesn't and instead oscillates and takes a more random path where some examples can mislead and other can improve. The proper value to use will be somewhere in between. Using pure *batch gradient descent* ($m$) it will take too long to train each iteration. But *stochastic gradient descent* will make lots of progress after one and the randomness isn't a problem but there will be no speed up form **vectorization**. *BGD* is fine for small sets of data ~2000. Typical sizes may be 64, 128, 256 or 512. We must ensure that our minibatches fit in CPU or GPU memory otherwise the performance will fall of massively.

### Exponentially Weighted Averages
To understand more sophisticated *optimization algorithms* it can be important to understand **exponentially weighted averages** also called *exponentially weighted moving averages* in statistics. We can look at the daily temperature over time for example in London. Say in the form $\theta_1, \theta_2,...$ we can create a moving average by initializing some $U_0=0$ then $U_1=0.9U_0+0.1*\theta_1$. This is generalized to $U_t=0.9U_{t-1}+0.1\theta_t$. The $\theta$ are plotted in blue and the $U$ in red.

![[Pasted image 20220715213709.png]]

We generalize this to $V_t=\beta V_{t-1}+(1-\beta)\theta_t$. This will be approximate the average of $\frac1{1-\beta}$ so ~10 days in the case above. With $\beta$ = 0.98 we will average of 50 (green line). This gives a smoother average but the curve shifts to the rights. We ca decrease $\beta$ to average over a smaller range and so we adapt to weight changes more and are more random. This formula implements an **exponentially weighted average** (*exponential weighted moving average*).

##### Understand
We can expand a large term like say $V_{100}$ this may give an expansion like :$$
V_{100}=0.1\theta_{100}+0.9*0.1\theta_{99}+0.9*0.9*\theta_{98}+...
$$$$
V_t=0.1\sum_{i=1}^t0.9^{t-i}\theta_t
$$The form of this can be through of as an exponentially decaying function that is multiplies by the average temperature.

##### Bias Correction
When we initialize our average we initialize to 0. This causes our average to lag behind for the first part. The way we can do this is instead of taking just $V_t$ we take $\frac{V_t}{1-\beta^t}$. When $t$ is larger $\beta^t$ is small and this will make no difference. Otherwise it will scale the values of $V_t$ so that they better match the $\theta$ values.

### Gradient Descent With Momentum 
This algorithm also called **momentum** is almost always faster than standard GD. It works by taking a *exponential weighted average* of the gradients instead of the true gradients. If you look at the blue line below we can see that we bounce form one side to the other of the valley the minima is in. This bouncing prevents us form using a larger learning rate which may destabilize our results (pupil). We can look at this by our learning needs to be greater on the horizontal axis but less on the vertical. On each iteration ($t$) we compute the usual derivatives computing $dw$, $db$ etc. Then we calculate $V_{dw}$ to be $\beta V_{dw}+(1-\beta)dw$ aswell as a similar operation for $db$. We then update with $V_{dw}$ instead of $dw$. This smooths out the steps of gradient descent. In our example he vertical ones will cancel out and the horizontal ones will add up to keep the average high. Allowing for a more stable gradient (red).

![[Pasted image 20220715220518.png]]

This can be through of as momentum. Where $d\theta$ adds acceleration $V_{d\theta}$ is the velocity (going down due to drag prevent massive speed ups).  Now with *momentum* we will have two hyperparameters $\alpha$ and $\beta$ one to control the fraction of the gradients added and the other to control our *momentum*. The *bias correction* isn't usually used as the initialization process takes such a small number of iterations. Often $(1-\beta)$ term is left our but this usually just scales the corresponding value by a factor of $\frac1{1-\beta}$. But this can be confusing as $\alpha$ will need to be retuned for different $\beta$ values.

### RMSprop
This stand for *root mean squared prop* and like *momentum* it can speed up learning. The way it works is we compute $d\theta$ same a usual. Then we set some $S_{d\theta}=\beta S_{d\theta}+(1-\beta)d\theta^2$ where the squaring is element wise. We then have the update step $$\theta=\theta-\alpha\frac{d\theta}{\sqrt{S_{d\theta}}}$$The idea is this scales down large oscillating movements as negatives and positives will join together in the squaring operation. Then small values will be scaled up. This will scale down oscillations. Hence this will give a similar effect to *momentum*. In practice a small term is added to $\sqrt{S_{d\theta}}$ to ensure numerical stability ($\epsilon$).

### Adam
Many algorithms have been supposed but then shown not to generalize well to other problems. Both **RMSprop** and **Adam** have shown to work far better than standard gradient descend. We initialize to start $V_{d\theta}$ and $S_{d\theta}$ to 0. Then on each iteration $t$ we compute $d\theta$ as normal. We then calculate the *momentum average* using $\beta_1$.$$V_{d\theta}=\beta_1V_{d\theta}+(1-\beta_1)d\theta$$Then we calculate the *RMSprop average* using $\beta_2$ $$S_{d\theta}=\beta_2S_{d\theta}+(1-\beta_2)d\theta^2$$*Bias* correction is typically implemented in **Adam**. Hence we get$$V_{d\theta}^{\text{Corrected}}=\frac{V_{d\theta}}{1-\beta_1^t}\hspace{64pt}S_{d\theta}^{\text{Corrected}}=\frac{S_{d\theta}}{(1-\beta_2^t)}$$Then we perform out update$$\theta:=w-\alpha\frac{V_{d\theta}^{\text{Corrected}}}{\sqrt{S_{d\theta}^{\text{Corrected}}}+\epsilon}$$Hence combining the gradient descent form *momentum* and *RMSprop*. The **hyperparameters** are $\alpha$ which needs to be tuned. $\beta_1$ controlling momentum ($d\theta$) is usually 0.9. $\beta_2$ controlling ($d\theta^2$) is recommended to be 0.999. $\epsilon$ is usually $10^{-8}$ but this doesn't change the algorithm much. *Adam* stands for *Adaptive moment estimation* where $d\theta$ is the first moment and $d\theta^2$ is the second.

### Learning Rate Decay
Here we slowly decay the learning rate over time.  This solves a problem we may have where our algorithm doesn't converge to a minima. But if we slowly reduce $\alpha$ we can learn quickly but as we take smaller and smaller steps we oscillate less and less. When we are first learning we learn roughly and work out the fine details later.

![[Pasted image 20220716000954.png]]

One *epoch* is one pass through the data. We can set $$\alpha=\frac1{1+\text{decay rate $*$ epoch-num}}\alpha_0$$ Here $decay-rate$ and $\alpha_0$ are other hyperparameters. The learning rate gradually will decrease. Other implementations are also used like $\alpha=0.95^{epoch-num}$ or $\alpha=\frac1{\sqrt{epoch-num}}$ or$\alpha=\frac1{\sqrt t}$ where $t$ is the minibatch number. Or a custom function that say decreases by a half every number of epochs. Manual decay can also work where over the days a model trains we tune it to keep the model moving. 

### Local Optima Problem
In the early days of machine learning many people worried about algorithms getting stuck in *local optima*. Such as bellow in the where there are many place son a 3D gradient landscape

![[Pasted image 20220716002120.png]]

However in reality this is only easy because it 3D. Points with 0 gradients in the true landscape are often saddle points like on the right. This is as for a minima all gradients must be 0. Then also the curvature must all be convex (not concave) hence it is very unlikely to actually find a local minima. Having some convex and some concave make a saddle. *Local optima* aren't a problem instead *plateaus* are. This is a region where the derivative is close to 0 for a large area. This will cause the parameters to move very slowly along the plateau.

![[Pasted image 20220716002544.png]]

[[Optimizers Questions]]


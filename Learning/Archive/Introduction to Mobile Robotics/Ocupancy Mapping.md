**Occupancy Grid Mapping** refers to a family of computer algorithms in probabilistic robotics for mobile robots which address the problem of generating maps from noisy and uncertain sensor measurement data. This is done with the assumption the robot pose is known.

The map is commonly represented as a grid of evenly spaced random variables each representing the presence of some obstacle. This is somewhat the opposite of the localization problem we are given the position of the robot and our task is to build a map of the world.

We further assume there is no motion model for these maps and so they do not change with time (**static objects only**). Our **measurement model** defines $p(z_t|m,l_t)$ which is the probability of making observation $z_t$ given a map $m$ and a location on the map $l_t$.

### Initial Solution
We can partition the world into cells, each one in in one of two states; filled or empty. The individual grid cells are $m_i$ and $\vec m$ is the vector of all grid cells. We want to calculate $$p(m|z_{t:t},x_{1:t})$$Unfortunately we cannot filter $\vec m$ since there are $2^{|\vec m|}$ possible states. So instead we need to filter each state independently and we need to **assume they are independent** to do this. We can instead reduce the complexity to $2|\vec m|$ by reconstruction the map from a product of marginal probabilities. $$p(m|z_{1:t},x_{1:t})=\prod_ip(m_i|z_{1:t},x_{1:t})$$This is a **poor assumption** since obstacles usually span multiple cells however it does make the problem tractable. We do not assume the cells are independent we know they aren't but we approximate them as such.

### Derivation
We say $X^i$ is the state of a grid cell $m_i$. The state is either $x$ meaning filled or $\bar x$ meaning empty. We look for the probability a cell is filled filled given the measurements $p(z_t|x,z_{1:t-1})$. We use a Bayesian filter $$p(x|z_{1:t})=\frac{p(z_t|x,z_{1:t-1})p(x|z_{1:t-1})}{p(z_t|z_{1:t-1})}=\frac{p(z_t|x)p(x|z_{t:t-1})}{p(z_t|z_{1:t-1})}$$Where the second quotient is given by the **Markov assumption** meaning $p(z_t|x,z_{1:t-1})=p(z_t|x)$. This doesn't hold for a single cell map. We expand the above equation using bayes rule to get $$p(x|z_{1:t})=\frac{p(x|z_t)p(z_t)}{p(x)}\frac{p(x|z_{1:t-1})}{p(z_t|z_{1:t-1})}$$Now $p(x|z_{1:t})$ is based on the **inverse sensor model** $p(x|z_t)$ instead of the forward model $p(z_t|x)$. The inverse sensor model specified a distribution over the binary state variable as a function of the measurement $z_t$. We can define this for a grid of squares for a given measurement like a laser beam.

![[Pasted image 20221217131738.png]]

Similarly we can use Bayes' rule to get $$p(\bar x|z_{1:t})=\frac{p(\bar x|z_t)p(z_t)}{p(\bar x)}\frac{p(\bar x|z_{1:t-1})}{p(z_t|z_{1:t-1})}$$This allows us to derive two update rules 

![[Pasted image 20221217132237.png]]

Finally given our recursive update rule. IF the probability $p(\bar x)>p(\bar x|z_t)$ then the update add $z_t$ in decreases the probability of $p(\bar x|z_{1:t})$. We take the log of this update rule to give the update in terms of log odds. This reduces the prevalence of **floating point errors**.

![[Pasted image 20221217133206.png]]

Now we only need to specify $p(x|z_t)$ the inverse sensor model and $p(x)$ the prior.

### Problems with Markov Assumption
We use the **Markov Assumption** to claim that $p(z_t|x,z_{1:t-1})=p(z_t|x)$. This is reasonable if $x$ represents the state of the complete map. However, $x$ is the state of a single cell. The Markov assumption in  this context doesn't make sense. We cannot say the observation $z_t$ is independent of all prior observations given only the state of a *single cell* as the bean model couples observations by passing through multiple cells.

![[Pasted image 20221217133724.png]]

This is an example of what can happen with a wide beam. This is reduced by narrow bean measurement tools such as LiDAR.

### Limitations of Occupancy Mapping
In our system cells are either filled or empty however it makes sense for cell to be on a spectrum. For example foliage may fill a cell less than a wall.

**Semi-Transparent Obstacles** - Classical occupancy grids have trouble with semi-transparent observes such as glass and vegetation. These obstacles may return hits to a laser only about half the time. The grid map will eventually converge to filled or not filled both of which are wrong. We could treat these cell as biased coins either. Then we keep track of three number probability light reflects, probability light passes through and probability cell is empty given by the remaining probability mass.
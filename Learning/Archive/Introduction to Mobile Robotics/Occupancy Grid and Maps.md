Occupancy Grid Mapping refers to a family of computer algorithms in probabilistic robotics for mobile robots which address the problem of generating maps from noisy and uncertain sensor measurement data, with the assumption that the robot pose is known. **Why Mapping** we have performed localization but we need to localize to something to build up an image of the world.

![[Pasted image 20221031130814.png]]

An **occupancy grid** describes is a given cell is occupied or not in the scene. This allows the car to decide what areas it can't move over/through.

1. We discretize the cell size.
2. We **like** occupancy to static objects such as trees buildings and road railings.
3. Each cell is given a binary value (filled or not)

Only static objects are used as we don't have to worry about them changing too fast and se we can reuse the map much later.

![[Pasted image 20221031130908.png]]

### Assumptions
We can only use **static**environments so we need to identify static and dynamic objects. We assume cells are **independent** of each other. We need to know the vehicle stat at each time step otherwise we can't transform our measurements between the different time steps (3 assumptions).

### Range Sensor
We can use many range sensor to find the distance in many directions to objects. We want to use this range info to build our occupancy grid. 

### Belief and Noise

![[Pasted image 20221031131013.png]]

One problem with this is **measurement Nosie** this may be due to reelections of the beam. So how can we make binary decision with all this Nosie. We may instead use a **probabilistic occupancy grid**. In this belief map we give the belief in some sell $m_i$ is equal to the probability of $m$ given the sensor reading $z$ and the car position $x$. Then we can use a **threshold** to give a binary map.

![[Pasted image 20221031131036.png]]

$$\text{bel}_t(m)=p(m|(z,x))$$

To improve the robustness, multiple timesteps are used to produce the grid map *Baye's theorem* is applied recursively 

$$\text{bel}_t(m)=n*p(z_i|m)\text{bel}_{t-1}(m)$$

Here $n$ is a normalization factor to keep our belief in a good range of values.

### Problems

![[Pasted image 20221031131122.png]]

If our probabilities start of very small we can get very small outputs which can be hard for computers to store. Instead we can **store the log odds ration** (logits) which collapses the space of values to be far smaller $$\log\frac p{=-1}$$This gives more room as we map $0\to1$ to $-\infty\to\infty$. We can even perform an update purely on log odds.

### Inverse Measurement Model
We need to take out points from the world to reading we might get. These taking in the world points and give ranges. For example the range will be th Euclidian distance. But many of the point don't land in cells directly or there are cell that aren't bit by a point. Instead we take $\alpha$ and $\beta$ to be our range noise and $\beta$ define the same for angles. Hence instead we take a box defined by $\alpha$ and $\beta$ to give a block of points we can activate. Hence each beam can be responsible for large area of pixels.

![[Pasted image 20221107094920.png]]

### Not all LIDAR points are useful to mapping
This happens partly due to the large amount of points hence we can apply don sampling to make the processes happen faster. We also **remove overhanging objects** as then don't affect deriving too much. We also need to **remove the ground plane**. Which is just all the noise coming from the floor. We can generate a plane mesh and then any sensor overlapping with it I should be removed.

### Removal of Dynamic Objects
Here we need to perform **object detection** and remove them from our occupancy map.

### Hi-Def road map
We also want other maps then just occupancy maps such tat we can plan mor what that. 

![[Pasted image 20221107100221.png]]

**Lanelets** Are defied by the following *left and right boundaries, regulations, connectivity to other Lanelets* 

Regulations - Elements (stop line, pedestrian crossing), Attributes (speed limit).

![[Pasted image 20221107100338.png]]



### Topological 
This is a graph like map that is simplified to only the essential information like connectivity and distance along edges.

![[Pasted image 20221107100630.png]]

### Semantic Map
A semantic map is a map describing what makes up a given space. For example it could describe a house with different areas labeled for different rooms.

![[Pasted image 20221107100953.png]]

### Feature/ Mandark Map
Feature/Landmark Map  
Easily observable parts or features of static objects in the environment, e.g., yellow cones. Widely used for odometry and SLAM systems.
![[Pasted image 20221107101215.png]]

### Mathematically
In **occupancy grid mapping** we are trying to estimate $p(z_t|m,l_t)$ using a *measurement model* where $m$ is our grid map $l_t$ is a cell and $z_t$ is some observation. We need to apply *filtering* to estimate the state each frame. We cannot estimate the state as one large vector $\mathbf m$ so we approximate cells as independent and so $$p(\mathbf m|z_{1:t},x_{1:t})=\prod_ip(m_i|z_{1:t},x_{1:t})$$

### Derivation
We are working with a random variable $X^i$ the state of cell $i$. We want to model $$p(x|z_{1:t})=\frac{p(z_t|x)p(x|z_{1:t-1})}{p(z_t|z_{1:t-1})}$$To update our estimation of our cells state. We take a Markov assumption that previous observations don't tell us about cells (this is wrong will come back later). Hence $p(z_t|x,z_{1:t-1})=p(z_t|x)$  $$p(x|z_{1:t})=\frac{p(z_t|x)p(x|z_{1:t-1})}{p(z_t|z_{1:t-1})}$$ We then expand this equation using **bayes rule** to get $$p(x|z_{1:t})=\frac{p(x|z_t)p(z_t)}{p(x)}\frac{p(x|z_{1:t-1})}{p(z_t|z_{1_t-1})}$$

$p(x|z_{1:t})$ is base don the inverse sensor model $p(x|z_t)$ instead of the familiar forward model $p(z_t|x)$. This specified a distribution of the *binary* state variable as a function o the measurement $z_t$. This may be described by a pass through and hit mode like below

![[Pasted image 20221107103612.png]]
1) probability equal to prior, 2) Low probability 3) high probability

The binary nature allows us to derive where $\bar x$ is the cell being empty as apposed to occupied.

![[Pasted image 20221107103833.png]]

This gives the update rules

![[Pasted image 20221107104005.png]]

That is if $p(x|z_{1:t})$ is increasing or decreasing after an update is relative to if $p(x|z_t)>p(x)$ which make sense. We can take the log prob so we aren't using tiny floating point numbers to get

![[Pasted image 20221107104331.png]]

Where we only care about the probability in the previous state $l_{t-1}(x)$, initial state $\log\frac{p(x)}{p(\bar x)}$ the measurement. Hence this also means if our measurement didn't change the chance of $x$ it will remain the same as in the previous state.

### Problems with Markov Assumption
We made a Markov Assumption $p(z_t|x,z_{1:t-1})=p(z_t|x)$ . This makes sense if $x$ was the whole map but not if $x$ is a single cell. This is since the beam model means cell affect one another.

![[Pasted image 20221107105230.png]]

### Limitations of Occupancy Mapping
In OGM cells are filled or not but it makes sense in some situation for them to be partially filled. Hence we may describe how filled a cell is like for example a wall being more filling than a bush.

**Semi-transparent objects and Mitigation** - These grids maps have trouble dealing with semi-transparent obstacles like glass and vegetation as beams can pass through them. Can measure density instead.

[[Occupancy Grid Maps Questions]]
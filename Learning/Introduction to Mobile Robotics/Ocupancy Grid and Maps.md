**Why Mapping** we have performed localization but we need to localize to something to build up an image of the world.

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

### Not all LIDAR points are useful to mapping
This happens partly due to the large amount of points hence we can apply don sampling to make the processes happen faster. We also **remove overhanging objects** as then don't affect deriving too much. We also need to **remove the ground plane**. Which is just all the noise coming from the floor. We can generate a plane mesh and then any sensor overlapping with it I should be removed.

### Removal of Dynamic Objects
Here we need to perform **object detection** and remove them from our occupancy map.

### Hi-Def road map
We also want other maps then just occupancy maps such tat we can plan mor what that. **Lanelets** Are defied by the following *left and right boundaries, *regulation, *attribute

### Topological 
This is a simpler way to look at grips maps.

### Feature/ Mandark Map
We can store a grip map and then send our biult up information to other cars moving about.
What is the need for mapping in mobile robotics? #flashcard #MOB #OcupancyGridMaps
	We need maps in order to build up an image of the world we can then operate within and use to predict future states.

---
How does a occupancy grid map describe the world? #flashcard #MOB #OcupancyGridMaps 
	An occupancy grid map describe the world though cells taking up space either in 2D or 3D. These cell then have a binary values describing if they are filled or not. This allows us to know what area we cannot enter.

---
What are the three features a occupancy grid map has? #flashcard #MOB #OcupancyGridMaps 
	1) The cells have a discrete size 2) We want occupancy of static objects but not necessarily dynamic objects 3) We want a cell to have a binary value describing if it is filled or not.

---
Why might we only want to use static objects in occupancy grid maps? #flashcard #MOB #OcupancyGridMaps 
	This is so we know our grid map isn't changing too fast this way we can reuse it over time.

---
What 3 assumptions are made to work with the occupancy grid map? #flashcard #MOB #OcupancyGridMaps 
	1) Objects are Static (environment), 2) Cells are independent of each other, 3) The state f the robot is known for each state.

---
What is the main sensor used to create an occupancy grid map and why? #flashcard #MOB #OcupancyGridMaps 
	We need some sort of range sensor to build an occupancy grid map, this is since it give directions to objects in many different direction so we can simply these hit boxes to get our grid map.

---
What are the problems with range sensor and what approach is good to solve these? #flashcard #MOB #OcupancyGridMaps 
	A problem is the **measurement noise** in our sensor which can cause object to appear which aren't there.  A **probabilistic occupancy grid map** is used to solve this.

---
What is a probabilistic occupancy grid map? #flashcard #MOB #OcupancyGridMaps 
	A **belief map** describes cell by their belief $m_i$ which is the probability of $m$ given our sensor reading $z$ and position $x$. It describes how confident we are some cell is filled. Occupies ~0.9 empty~0.1

---
How is a belief map converted into a regular binary occupancy grid map? #flashcard #MOB #OcupancyGridMaps 
	We can use a threshold value and set any cells we are overly confident in to be occupied.

---
Mathematical what is the belief of some cell in a belief map? #flashcard #MOB #OcupancyGridMaps 
	This is the probability of some cell being occupied given sensor reading and current state. $$\text{bel}_i=p(m|(z,x))$$

---
How can we improve the robustness of our occupancy grid map? #flashcard #MOB #OcupancyGridMaps 
	We can apply **bayes rule** recursively this way we can  a more stable belief. 
	

---
What is the update rule for occupancy grid maps using bayes rule? #flashcard #MOB #OcupancyGridMaps With belief at time $t$ $\text{bel}(m^i)$ current measurement $p(z_t|m^i)$ and normalizing constant $n$ we get:  $$\text{bel}_t=np(z_t|m^i)\text{bel}_{t-1}(m^i)$$

---
What is a problem with using probabilities for our belief map? #flashcard #MOB #OcupancyGridMaps
	very small number can give floating point errors making our results inaccurate. Instead we would use logits which map probability space to the whole number range.

---
What is the update rule for occupancy grid maps using bayes rule and log odds? #flashcard #MOB #OcupancyGridMaps
	This would be $$l_{t,i}=logit(p(m^i|z_t))-l_{t-1,i}-l_{0,i}$$ where $l_{t,i}$ is our logit belief at time step $t$ for cell $i$ and $p(m^i|z_t)$ is our measurement.

---
What measurements are taken by a range scanner sensor? #flashcard #MOB #OcupancyGridMaps 
	We would measure an list of bearing $\phi$ and ranges $r$ each able to describe some line and a point along it.

---
What is the inverse measurement model of the range in a scanner sensor? #flashcard #MOB #OcupancyGridMaps 
	This would be $$r^i_s=\sqrt{(x_o^i-x_o^s)^2+(y^i_o-y^s_o)^2}$$ where $\__s$ means relative to $s$ our robot. Hence $x_o^s$ is our robots global position and $x_0^i$ is our cell's global position.

---
What is the invers measurement model for a bearing to a vehicle? #flashcard #MOB #OcupancyGridMaps 
	This would be  $$\phi_s^i=\tan^{-1}\left(\frac{y_o^i-y_o^s}{x_o^i-x_o^s}\right)-\theta_o^s=\phi_o^i-\theta_o^s$$ where $\phi_s^i$ is the   bearing from our object to the forward direction of our robot, $\phi_o^i$ global bearing to the object from our robot. Then $\theta_o^s$ is the relative bearing of our robot's forward direction.

---
For each cell in an occupancy grid map how is it associate to some range beam? #flashcard #MOB #OcupancyGridMaps 
	We just take the beam with the smallest angle away form it. That is for a beam $k$ we get $$k=\arg\min(|\phi_s^i-\phi_s^k|)$$

---
What is the affected region for a given range beam for an occupancy grid map? #flashcard #MOB #OcupancyGridMaps
	This is a section described for each beam and range where we use $\alpha$ to describe the affected range for particular beam and $\beta$ to describe the affected angle for a measurement.

---
Why is Lidar filtering important? #flashcard #MOB #OcupancyGridMaps 
	LiDAR produces so much data every frame we cannot use all this data and so need to downs sample it to the most useful.

---
What three things are mainly removed in LiDAR filtering? #flashcard #MOB #OcupancyGridMaps 
	We remove **overhanging objects**, **ground plane** and **dynamic objects**.

---
Why ado we remove overhanging objects in LiDAR filtering? #flashcard #MOB #OcupancyGridMaps 
	We remove overhanging objects in LiDAR filtering as we can't come into contact with the any way so maintaining where they are isn't import ant to us.

---
Why do we remove the ground plan in LiDAR filtering? #flashcard #MOB #OcupancyGridMaps 
	The ground plan uses a lot of lidar points but all these points are fine to driver over and so we can discount the data as it won't help with building an occupancy grid map.

---
Why do we remove dynamic objects in LiDAR filtering? #flashcard #MOB #OcupancyGridMaps 
	We remove dynamic objects as they will change over time and so we cannot reuse the data we create described by them.

---
What makes detecting dynamic obejcts hard for LiDAR? #flashcard #MOB #OcupancyGridMaps 
	Even if its clear what the object is we cannot know if its dynamic or not. Instead we need to look over multiple frames to see if it is changing.

---
What are other types of maps other than an occupancy grid map? #flashcard #MOB #OcupancyGridMaps
	High definition road map, topological map, semantic map, feature/ landmark map.

---
What is a high definition road map? #flashcard #MOB #OcupancyGridMaps 
	This is a type of map that describes road features to a high degree of accuracy and is designed for path and behavior planning.

---
What are lanelets? #flashcard #MOB #OcupancyGridMaps 
	Lanelets are elements used to describe HD road maps. They are made our of left and right boundaries, regulations and connection to other lanelets. They can describe things like **intersections** or **sections of road**.

---
Whare is a topological map? #flashcard #MOB #OcupancyGridMaps 
	This is a graph like map that is simplified to only the essential information like connectivity and distance along edges.

---
What is a semantic map? #flashcard #MOB #OcupancyGridMaps 
	A semantic map is a map describing what makes up a given space. For example it could describe a house with different areas labeled for different rooms.

---
What is a feature/landmark map? #flashcard #MOB #OcupancyGridMaps 
	This is a type of map that describes static feature that are easily identifiable and can be used for odometry and SLAM systems.

---
What is the Logits update for each cell when we have a inverse measurement model? #flashcard #MOB #OcupancyGridMaps 
	This will be $$l_t(x)=\log\frac{p(x|z_t)}{p(\bar x|z_t)}+\log\frac{p(\bar x)}{p(x)}+l_{t-1}(x)$$ where the random variable $X$ is for a single cell. Then $l_t(x)$ is logits for a given timestep $t$ and $p(x|z_t)$ is found form our inverse measurement model.

---
What problems can making a Markov Assumption when we update our occupancy grid give? #flashcard #MOB #OcupancyGridMaps 
	The problem is that it isn't true since a beam can be cut of by many different cells. Hence we can get conflicts where a range finder gives cell where there aren't any. Then we also assume our sensor readings are constant.

---
What are the limitations of occupancy mapping? #flashcard #MOB #OcupancyGridMaps 
	Cell's state is binary which doesn't always make sense. It also doesn't work when we consider objects that are semi transparent and so may be not there are time and there at other time depending on how our range finder detects them.

---

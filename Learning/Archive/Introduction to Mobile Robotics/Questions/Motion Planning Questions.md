What is the task and goal in mission planning? #flashcard #MOB #MotionPlanning
	The task is to navigate the robot form its current position to a final **destination**. To do this our **goal** is to find a path in terms of time and distance traveled.

---
How does different scenarios make motion planning for robots harder? #flashcard #MOB #MotionPlanning 
	We cannot plan in detail enough for all the minutia. Our robot therefore has to be able to adapt and take into account the feature of these different scenarios.

---
What must a motion planner consider when it comes to road structure? #flashcard #MOB #MotionPlanning 
	There are many situation the robot could find itself in. **Road structure** means the robot has to adapt its movement to different turn, bends and overall road topology.

---
What must a motion planner consider when it comes to intersections and traffic interactions? #flashcard #MOB #MotionPlanning 
	We need to maintain our goal turning or moving to a location but we need to take into account the rules of the road, other cars movement and how rules affect them. As well as pedestrians and other agents.

---
What must a motion planner do when it comes to static objects? #flashcard #MOB #MotionPlanning 
	It needs to ensure the objects are avoided. We need to take this into consideration when planning our motion as these objects constrain our movement.

---
Wat must a motion planner do when it comes to dynamic objects? #flashcard #MOB #MotionPlanning 
	A motion planner must avoid these objects and ensure collisions don't occur. This will restrict our movement over time as dynamic obstacles move. To do this it is also useful to predict the motion of these objects into the future.

---
What are the 5 behaviors in a robots common behaviors set? #flashcard #MOB #MotionPlanning
	These are behaviors the robot stiches together into its overall movement and plan in the world:
	1. Speed tracking
	2. Deceleration to stop
	3. Stay stopped
	4. Yield
	5. Emergency stop

---
What does a mobile robot have to take into account when yielding? #flashcard #MOB #MotionPlanning 
	It has to take into account the motion of other agents waiting until there is space to continue.

---
When does a mobile robot need to perform an emergency stop? #flashcard #MOB #MotionPlanning 
	A mobile robot need to perform an emergency stop when there is an unexpected or unforeseen event that could hurt or kill someone or damage something.

---
What is the hierarchy in motion planning? #flashcard #MOB #MotionPlanning 
	A the top is the **mission planner** then we have the **behavioral planner**, then the **local planner** made our of the path planner and velocity profile generator. Finally we have the vehicle control.

---
What is the bicycle model? #flashcard #MOB #MotionPlanning 
	This is a model of a cars kinematics which represents the car s a beam with two wheels one of which can turn like a bike. 

---
What restriction does a vehicle corresponding to a bicycle model give? #flashcard #MOB #MotionPlanning
	This restricts the **curvature** the robot can with its path. This is due to the robot only being able to turn while moving and an amount corresponding to its movement.

---
What is curvature of a path? #flashcard #MOB #MotionPlanning 
	Curvature describes how much a path is "curving". If we fit a sphere to the curve the curvature will be the inverse of the radius $$K=\frac1r$$

---
When it comes to  what a friction ellipse and comfortable rectangle? #flashcard #MOB #MotionPlanning
	Our robot can only accelerate a certain amount without loosing friction. The **friction ellipse** describes the space of accelerations lateral and longitudinal we can take without loosing control. The **comfortable rectangle** is more restrictive and is the region of acceleration our passengers would feel comfortable in hence we need to ensure we don't constantly exceed this.

---
When we are turning as a speed v and radius r what is our lateral acceleration equal to? #flashcard #MOB #MotionPlanning
	This will be $$a_{lat}=\frac{v^2}r$$

---
Given we have a maximum latera acceleration what is the limit on our speed for a given curvature in our path? #flashcard #MOB #MotionPlanning
	We know $a_{lat}=\frac{v^2}r$  hence if we have some max $a_{lat\max}\ge a_{lat}$ we get $$v^2\le\frac{a_{lat\max}}k$$

---
How do static objects constrain our path as a robot? #flashcard #MOB #MotionPlanning 
	As we move about our robot cuts a swath in the world which is the space it needs to be free in order to move. Hence static objects in this area constrain what paths we can take.

---
How can we ensure to avoid static objects as a robot? #flashcard #MOB #MotionPlanning
	We can find for different path a **swath** all the space that must be free in order to allow us to complete the path. To avoid objects we can just ensure there is no occupancy in our swath.

---
When it comes to motion planning how can dynamic objects be hard to deal with? #flashcard #MOB #MotionPlanning 
	We need to ensure there are not collisions. This is hard as we cannot 100% predicts the path of these objects. Hence we need to **track** and **predict** their movement and continually update this prediction.

---
What is a simple way to track if a collision will occur with some dynamic object? #flashcard #MOB #MotionPlanning 
	We can track the **angle** between our trajectory and theirs. If this angle isn't changing we will **collide** with the other agent.

---
What is the leading vehicle constrain in motion planning? #flashcard #MOB #MotionPlanning 
	We need to ensure our speed doesn't outpace and car in front of us. As if this happen eventually we will collide

---
What are road rule constraints in motion planning? #flashcard #MOB #MotionPlanning 
	We need to ensure we follow the rules of the road. Hence following these rules constrains our path.

---
What are objective functions in motion  planning? #flashcard #MOB #MotionPlanning 
	Objective functions are measurement we try to optimize in order to perform well and not just complete the task.

---
How can the path length be calculated for a robot? #flashcard #MOB #MotionPlanning 
	This will be $$S_f=\int_{x_i}^{x_f}\sqrt{1+\left(\frac{dy}{dx}\right)^2}dx$$

---
How can the travel time be calculated for a robot? #flashcard #MOB #MotionPlanning 
	This will be $$T_f=\int_0^{S_f}\frac1{v(s)}ds$$

---
What is reference tracking when it come to object functions in motion planning? #flashcard #MOB #MotionPlanning 
	We want to penalize deviation from our path or speed limit but we don't want to penalize reducing the length or sticking to our original path. Hence we use a **hinge loss** $$f(x)=\min(0,x-c)$$

---
What is jerk? #flashcard #MOB #MotionPlanning 
	Jerk is a measure of the change in acceleration of our robot. We want to minimize this as it can be uncomfortable for passengers.

---
What constrains should be optimize to minimize jerk? #flashcard #MOB #MotionPlanning 
	We want to minimize $$\int_0^{S_f}||\overset{\dots}x(s)||^2ds$$

---
What constrain should we optimize to minimize curvature and what is the reason to do this? #flashcard #MOB #MotionPlanning 
	Minimizing curvature minimizes acceleration making the ride more comfortable. We would optimize $$\int_0^{S_f}||k(s)||^2ds$$

---
what does the mission planner use to operate? #flashcard #MOB #MotionPlanning 
	The mission planner plans our the overall path using pathfinding algorithms such as A* and Dijkstra.

---

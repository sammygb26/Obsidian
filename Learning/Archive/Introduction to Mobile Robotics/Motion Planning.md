### Missions, Scenarios and Behaviors
In *mission* planning we want the problem to navigate from its current position to a final destination on the map. Hence our **goal** is to find a path (trajectory) in terms of time or distances traveled. This is **high level**.

![[Pasted image 20221110111545.png]]

This will generate **motion todo**. But we need to take into consideration the specific shape of the road and acceleration constraints.

In complex environment we also need to take into account road network, traffic rules and other agents (cars humans etc.).

We also need to avoid **static** and **dynamic** objects. We can avoid static objects with occupancy grid mapping. With **dynamic objects** it gets more complicated as even if there are traffic rules we do not know if they will follow them. We need to plan for this kind of violations but not become too timid to not work well.

### Common Behavior Set
We only need a limited number of classes of behaviors in order to perform well.

1. **Speed tracking** - we need to track max allowed speeds
2. **Deceleration to stop** - here we need to decelerate to make the car stop (like for example when there is a red light)
3. **Stay stopped** - simple waiting
4. **Yield** - here we have to wait for dynamic objects to change (cars, people)
5. **Emergency stop** - when we need to stop in order to avoid the consequences of a traffic violation (people or cars)

### Hierarchical Planning Approach
To perform this planning we break it into a **hierarchy** of optimizing problems. each optimization problem is tailored to the **correct scope level of abstraction**. Each optimization problem will have its own constraints and object functions.
We may not get an optimal solution but the problem is tractable and we will get a good solution.

![[Pasted image 20221110112350.png]]

### Motion Planning Constraints

**Bicycle Model** this is a model of a car we represent a car as a simple model as a bike. With a front and back tire.

![[Pasted image 20221110112533.png]]

This has a **rolling constrain** (curvature) where we can more forwards and backwards but not sideways. We need to change the front wheels direction to achieve lateral movement.

**Curvature** limits the direction a mobile robot can travel. Motion planning is challenging due to this rolling constraints of this model.

Curvature describes how much a function is changing where the curvature $k$ is the inverse of the radius of that circled.

![[Pasted image 20221110112819.png]]

The curvature can also be calculated using the first order and second order derivatives if we have the function itself.

**Vehicles Dynamics** - we may have a **friction ellipse** which describes the hind of lateral and longitudinal acceleration the car can take.  We will have a **comfortable rectangle** which is actually comfortable for passengers and drivers.

![[Pasted image 20221110113049.png]]

These constraints limit the acceleration (lateral and longitudinal). When we are turning the lateral acceleration can be defined as $$a_{lat}=\frac{v^2}r$$where $r$ is the radius of the turning circle. We want to ensure $a_{lat}$ is always within range.

We can combine curvature and the above equation to get $$v^2\le\frac{a_{\text{lat max}}}k$$That is our velocity is constrained by our curvature. Hence the maximum allowed velocity is not fixed.

### Static Objects
Static obstacles **constrain** the location that a car can occupy along its path. Static obstacles constraints satisfied by performing **collision checking**. This is done using **swath** for the vehicle's path. **Swath** is th union of all the grid cell occupied by the body of the ego vehicle as the ego vehicle traverses the path. We need to check the swath isn't occupied everywhere. We need checking as we have already planned our path in the higher levels of the planning hierarchy.

![[Pasted image 20221110113839.png]]

### Dynamic Obstacles
Dynamic vehicles / pedestrian also impose more challenging constraints. Constraining our motion plan based on the behaviors f these moving agents will often involve tracking and predication of their dynamics. This is subject to **uncertainty**.

**Intersection Vehicle Constraints** - this is when we track the angle between the paht of the ego vehicle and the other agents vehicle. We want there to not be a collision in these paths.

**Leading Vehicle Constraint** - A leading vehicle in front places an **upper constraint** on the vehicles longitudinal velocity. If we exceed their speed we will eventually crash.

**Road Rules** - here there are many rules we must follow, signs etc.

### Objecting Functions for motion Planning

**Efficiency** - we want to measure **path length** and **travel time**. Where $S_f$ is our displacement. We can then calculate travel time by integrating again with the velocity.

![[Pasted image 20221110114240.png]]

![[Pasted image 20221110114415.png]]

**Reference Tracking** - we want to penalize deviation from the reference path or speed limit. For velocity we usually use **hinge loss** to penalize speed exceeding violations. Where we only penalize going over a speed limit (positive side).

![[Pasted image 20221110114523.png]]

**Smoothness** - we want to ensure changes in acceleration don't change too much. For example we constrain **jerk** the rate in change in acceleration.

![[Pasted image 20221110114735.png]]

**Curvature** - we want to constrain curvature to ensure the care smoothly turns both for the wheels and for the passenger experience.

![[Pasted image 20221110114908.png]]

### Hierarchical Planner
Mission planner is the highest level focusing on **map-level-navigation**. We can use algorithms like A* and Dijkstra to solve this ang get the best path. The behavior planner focuses on other agents and *rules of the road, driving behaviors*. Then **local planner**

[[Motion Planning Questions]]

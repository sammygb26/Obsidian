An example of how **behavior planning** might work is information about the road state and value functions can be combined to find which behavior should be followed in a probabilistic way. Different movement sets are decided over for different applications. A **state machine** is used to do this. **Behavioral planner** takes place after the **mission planner**. This focuses on different agents, the rules of the road and driving behaviors.  This sends details on the the **local planner**.

The definition is it plans a set of high level driving action or maneuvers to **safely** achieve the driving mission under various driving situations. It considers

* Rules of the road
* Static objects
* Dynamic objects

The planned path must be **efficient** and **safe**.

### Driving Maneuvers (non exhaustive)
**Track speed** - maintain current speed on the road
**Follow leader** - match the speed of the leading vehicle and maintain a safe distance
**Deceleration to stop** - begin decelerating and stop before a given space
**Stop** - remain stopped in the current position
**Merge** joint or switch onto a new drive lane.

![[Pasted image 20221123190410.png]]

### Outputs
The **primary output** is a driving maneuver that should be executed by the local planner. 

The **secondary outputs** prepares the problem for the local planner. It dives a set of constrain which must be obeyed. For example

* Ideal path
* Speed limit
* Lane boundaries
* Stop locations
* Set of objects of interest

### Inputs

* High definition road map and traffic rules
* Mission path (**from mission planner**)
* Localization information
	Where we are in the scene.
* Perception information
	All observed **dynamic** objects and the prediction of their future movement plus **time to collision**.  This is given by object perception. IT will also give observed **static objects** like road signs and traffic lights. We may also need local occupancy grid to ensure we are moving through the world safely.

### Finite State Machine
We need a system to translate the many inputs into a useful output behavior for our local planner. In the FSM each **state** is a driving maneuver. each state is associated with an **entry action** specifying the constrains sent to the local planner (this can be through of as the arguments to the movement). **Transitions** define movements from one maneuver to another. **Transition conditions** are monitored in the machine and define a rule that needs to be med before the transition to another behavior occurs.

![[Pasted image 20221123191208.png]]

### Advantages of FSM
This is a **direct** implementation of the definitions of behavior planning, hence it requires use to define maneuvers or state and local planning constraints or entry actions. This acts as a decomposition on the whole problem as in each state we only need to check the conditions relating to that state. This **limits** the rule checking and improve the speed of our computation.

There are also **disadvantages** for example uncertainty isn't modeled so we can get stuck in states that don't match the true state we are in.

### Case Study: Intersection without dynamic objects
We will look at a scenario with 2 lanes so 4 way. There is stop sign for every direction. There are different things we want to do. 

* Travel through intersection
* Travel left at intersection
* Travel right at intersection

We consider this without dynamic objects. We **discretize** the intersection into different regions.

![[Pasted image 20221123191840.png]]

**Red** - approaching an intersection
**Greed** - at the intersection
**Orange** - on an intersection

We determine the size for each zone based on the ego vehicle velocity and the size of the intersection. It changes with the velocity and we need more time to slow down in this case. We can already get information for this from **high definition road-maps**. We consider three mauves for this case

* Track speed
* Decelerate to stop
* Stop

**Before entering the zone** - here we want to track our speed and transition to **decelerate to stop** once we are approaching.

![[Pasted image 20221123192151.png]]

**Selecting a decelerate to stop location** - once we are stopping we need to keep decelerating till the stop point is reached. The stop point is an **entry action** for the state.

![[Pasted image 20221123192407.png]]

**Stay stopped** we also need to wait once we have stopped and then continue.

![[Pasted image 20221123192511.png]]

There can also be **measurement noise**. A way we can mitigate this problem is to set a threshold we instead we can use a threshold instead of 0.

![[Pasted image 20221123192659.png]]

### Case 2 intersection with dynamic objects
We will still consider a 4 way intersection as above. The size of the zones are defined by the *ego velocity* and *size of intersection* in the static case. 

##### Time to Collision
This is an important concept where we measure how long it will take till we hit another objects. This takes an **advanced perception module** tracking and predicting another vehicles movement. All of this gives TTC and the DTC (distance to collision).

![[Pasted image 20221123193013.png]]

Now we know **where** and **when** we will hit. We assume this is given by some other module to our behavior planner.

**State machine states** - we introduce a new behavior to allow us to interact with dynamic objects **follow leader**.

![[Pasted image 20221123193228.png]]

**Track speed** - if we have no other vehicles we will keep moving then decelerate to stop once we are approaching. But if there is a dynamic object we will track **TTC** and if this TTC is below a given level we instead **track speed**.

![[Pasted image 20221123193457.png]]

**Follow leader** - once we are in this state we are limited to follow the leader until our paths diverge. For example if the vehicle drives away TTC will get larger than a threshold we can go into **track speed** if we aren't approaching. The ego vehicle can also leave the approaching's zone at which point we decelerate to stop as we would before. If they leader stops in the approaching zone then we also stop in that zone.

![[Pasted image 20221123193846.png]]

**Decelerate to stop** and **stop** we remain the same as before.

This state machine cannot manage all possible states. For example other kinds of dynamic objects.

### Time to Collision (Expanded)
To calculate this we consider **where the collision points is** and **how long it will take to get there**. To calculate this we need accurate predicted paths and accrete geometry of these vehicles. There are two approaches to calculate this:

**Simulation approach** - where we simulate the movement of each vehicle as time passes. This moves the vehicle model over time. We check if any part of the two dynamic objects has collided at any time. This requires very fine grained geometry model and is hard to get in the real world.

![[Pasted image 20221123194244.png]]

**Estimation approach** - here we approximate both vehicles for example using bounding boxes and moving the swaths over time. This give the collision estimation over time. Exact collision part is often ignored as the model is simple and instead the time and rough position is more important. In extreme cases only a point for each vehicle is used.

![[Pasted image 20221123194627.png]]

There are advantages and disadvantages. For example simulation is more computationally expensive but it is higher accuracy and so gives good results. This is mainly used for offline applications where are estimation is used in real time prediction.

### Planner Testing
We need to test our planners to ensure they are safe to use.
1. **Modular** tests
2. Simulation tests (e.g. help of the CARLA simulator)
3. Controlled private track tests (a lab environment)
4. On road tests with close supervision e.g. experienced driver for quick intervention.

[[Behavior Planning Questions]]
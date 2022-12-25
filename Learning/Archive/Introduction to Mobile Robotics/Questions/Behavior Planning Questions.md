What does the mission planner focus on? #flashcard #MOB #BehaviorPlanning 
	The mission planner focuses on map-level navigation.

---
What does the bahaviour planner focus on? #flashcard #MOB #BehaviorPlanning
	The behavior planner focuses on other agents, rules of the road and driving behaviors. This is used to generate a planned path.

---
What does the local planner focus on? #flashcard #MOB #BehaviorPlanning 
	The local planner focuses on collision avoidance in the path vicinity.

---
What does the bahaviour planner get as its input, what does it consider and what does it output? #flashcard #MOB #BehaviorPlanning 
	A behavior planner gets a get an overall mission of where it needs to go. It plans the set of **high level** deriving actions or maneuvers that would safely achieve this mission. It considers rules of the road, static objects and dynamic objects (both close to the vehicle).

---
What ae the 5 main driving maneuvers? #flashcard #MOB #BehaviorPlanning 
	1) Track speed
	2) Follow leader
	3) Decelerate to stop
	4) Stop
	5) Merge

---
What is involved in the track speed maneuver? #flashcard #MOB #BehaviorPlanning
	In track speed the car must maintain is speed at some constant level.

---
What is involved in the follow leader maneuver? #flashcard #MOB #BehaviorPlanning
	Here the car must ensure it doesn't exceed the speed of some leader car it is behind in order t ensure a collision doesn't occur.

---
What is involved in the decelerate to stop maneuver? #flashcard #MOB #BehaviorPlanning
	Here the car breaks to bring itself to a stop.

---
What is involved in the stop maneuver? #flashcard #MOB #BehaviorPlanning
	Here the car remains stopped waiting for the situation to change.

---
What is involved in the merge maneuver? #flashcard #MOB #BehaviorPlanning
	Here a car must plan to move from one lane to another. It must plan to ensure it doesn't hit any cars while achieving this.

---
What are primary and secondary output of bahaviour form the behavior planner? #flashcard #MOB #BehaviorPlanning
	The primary outputs are the driving maneuvers to be executed. The secondary outputs are constrains that must be obeyed by the local planner. For example the ideal path, speed limit, lane boundaries, stop locations and set of objects of interest.

---
What inputs might the behavior planner require? #flashcard #MOB #BehaviorPlanning 
	High definition road map, mission path (from mission planner), localization information. Perception information:
		1) All observed **dynamic objects** and prediction of their future movements and TTI.
		2) All observed **static objects** including road signs and traffic lights.
		3) Local **occupancy grid** for safe movement.

---
How can a behavior planner be modeled as a FSM? #flashcard #MOB #BehaviorPlanning 
	each state can be a **maneuver** each state has an **entry action** which supplies constraints to local planner. **Transitions** define movement from one maneuver to another. **Transition conditions** are monitored in state  and define the rules that need to be met for a transition from one state to another.

---
Overall how might an FSM represent coming to an intersection with no dynamic objects? #flashcard #MOB #BehaviorPlanning
	We would have three states **decelerate to stop**, **stop** and **track speed**. While we are not in the **approaching's zone** we **track speed**. Then once we are we **decelerate to stop**. This is maintained until our speed is lower than some threshold (require due to inaccurate sensors). Then we stop. We hold stop for some prior of time then once this is acceded we **track speed again**.

---
Overall how might an FSM deal with an intersection situation with dynamic objects? #flashcard #MOB #BehaviorPlanning
	Here we might have four states. **Stop**, **Track speed**, **follow leader** and **decelerate to stop**. 
	1. The **track speed** might transition to decelerate to stop if its in approaching the intersection. Then it might transition to follow leader if TTC with some object is smaller than some threshold.  
	2. The **follow leader** might be maintained while TTC is smaller than some threshold and  we aren't approaching which would transfer us to decelerate to stop. If this wasn't the case and TTC grew too large we might transition back to track speed.
	3. The **decelerate to stop** might be maintained while speed is high then transition to stop once speed is low.
	4. **Stop** might just wait then transition to track speed again after this.

---
What is TTC? #flashcard #MOB #BehaviorPlanning 
	This is time to collision and is an important metric used to avoid colliding with dynamic objects. The idea is that if TTC is decreasing we may collide But if it is over a given level we don't need to worry about colliding at least for the time being.

---
What are the two approach to TTC? #flashcard #MOB #BehaviorPlanning 
	There is the **simulated approach** and the **estimation approach**.

---
What is the simulated approach to TTC (pros and cons)? #flashcard #MOB #BehaviorPlanning 
	Here we simulate the movement of the dynamic objects and check at each instant if they have collided. This gives a very accurate TTC however it requires very accurate geometry and modeling which is hard to get and expensive/slow to compute.

---
What is the estimation approach to TTC (pros and cons)? #flashcard #MOB #BehaviorPlanning 
	In th estimation approach the geometries of the vehicles over time are approximated. Collision points are then estimated based on the predicted position. The exact part of the car colliding is ignored and simplifies geometry for the vehicle issued. For example a car might even be represented as a single point. This doesn't give hugely accurate results but is cheap and quick to compute.

---

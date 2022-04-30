What are the two types of non-determinacy that depend on the number of states and how do we describe them? #flashcard #RA #PlanningAndActingInTheRealWorld
	*Bounded* non-determinacy where there is a limited (finite) number of states we could end up in (describes by ranges)
	*Unbounded* non-determinacy where there is a infinite number of states we could end up in (described by exact values), this also allows for unforeseen outcomes as there may be infinite

---
What are the three types of planning for acting in non-deterministic environments? #flashcard #RA #PlanningAndActingInTheRealWorld 
	*Sensorless planning* - also called conformant planning where we don't get any knowledge of what state we are in.
	*Contingency planning* - where we get some update and so must change our actions based on what we observe but we still follow a plan
	*Online planning* where we may have to replan if we end up in a state we couldn't have predicted

---
What is the aim when solving a Sensorless planning problem? #flashcard #RA #PlanningAndActingInTheRealWorld 
	The aim when solving a Sensorless planning problem is the reason it is called a conformant planning problem. We aim to start with a set of possible states and through some sequence of actions ensure all of the states have lead to some goal state.

---
What is the aim when solving a contingency planning problem? #flashcard #RA #PlanningAndActingInTheRealWorld 
	The aim in to produce a contingency plan. This is a plan that changes the action sequence depending on what is observed. It however only account for foreseen percepts that fit into the agents model. If something happens the plan isn't prepared for it may fail.

---
What is the aim when solving an online planning problem? #flashcard #RA #PlanningAndActingInTheRealWorld 
	The idea here is to produce a plan that is likely to work. We keep checking how the progress is going however if we find things aren't going according to plan we can  to find a solution. This can solve problems where we may end up in states our model of the world doesn't predict to be possible as we just ignore our old plan and try to formulate another. This doesn't ensure the agent will solve the problem just that it will at least have something to try.

---
What adaptation is needed for PDDL to take in percepts? #flashcard #RA #PlanningAndActingInTheRealWorld 
	We need to maintain a belief state about the world. We can take perception actions to refine this state and ensure we reach our goal state. This is done with a percept schema that gives us is value for some unknown value.

---
How does the way we represent out current state change when we incorporate percepts into PDDL? #flashcard #RA #PlanningAndActingInTheRealWorld 
	Our state instead of being a conjunction of positive literals will be a conjunction of positive and negative literals with anything not mentioned being unknown. That is we have a belief state instead of a normal, simple state.

---
What assumption can be made about the world to simplify the belief state for use in PDDL? #flashcard #RA #PlanningAndActingInTheRealWorld 
	We can assume there are no exogenous events. That is the world only changes when we know. This way if we perceive some value we can assume it's state will not change with time and so can leave percepts in our belief state as long as we like, not worrying about any change.

---
How can Skolemization help us plan using PDDL in a Sensorless environment? #flashcard #RA #PlanningAndActingInTheRealWorld 
	Skolemization allows us to state with some universal existential statement and create Skolem constants. These constants show for example that every object has a color by defining a constant representing the color for each object. Our actions can then build up relations between these constants possibly allowing us to satisfy our goal.

---
How can we solve a Sensorless planning problem in PDDL? #flashcard #RA #PlanningAndActingInTheRealWorld 
	We use a belief based PDDL where our state a a collection of variable we know the value of. Our goal is then to conform these values given our action schema to a goal state. The value we do know can be given to us from the start either through pure addition to our belief state or inference based on universal quantification.

---
How can we perform action in a belief based PDDL problem if the actions preconditions may not be met? #flashcard #RA #PlanningAndActingInTheRealWorld 
	If the actions may not be met then the result may or may nor happen. We cannot however allow actions which may do more than happen fully or not at all. This is as doing this will increase the complexity of out belief state our of being a simple CNF formula to a full logical formula with many more states.

---
How do action effects work in a belief based PDDL problem? #flashcard #RA #PlanningAndActingInTheRealWorld
	The effects update the belief state in a similar way to a normal PDDL state. If we make something true we add it as true. If we make something false we add it as false (instead of removing it) and if we don't change something then we leave it in or out. But this only works if our actions always have the same consequences assuming their preconditions are met.

---
How does contingent planning work in PDDL? #flashcard #RA #PlanningAndActingInTheRealWorld 
	This works in a similar way to usual we can use an AND-OR search as usual where the AND nodes are created when we perceive the world. This will produce an contingent plan contain if else branches.

---
What are the types of monitoring that allow for online planning? #flashcard #RA #PlanningAndActingInTheRealWorld 
	Action monitoring - ensure that the preconditions for an action hold before we execute it
	Plan monitoring - before we execute an action we verify that the remaining plan will still work
	Goal monitoring - before executing an action we check if there is a better goal we could be trying to achieve
	Any of these may find our plan will fail or we have a better option in any case we will replan.

---
What problems can online planning not solve? #flashcard #RA #PlanningAndActingInTheRealWorld 
	Online planning cannot solve problems where something unknow is required to be understood to complete a task. For example if an agent runs out of power and can no longer perform some required action no amount of replanning will allow it to solve a problem if it doesn't understand how to recharge.

---
What is a high level action? #flashcard #RA #PlanningAndActingInTheRealWorld 
	A high level action is an abstract action. It can be refined later in a sequence of more HLAs or primitive actions, eventually refining to a sequence of primitive actions. This is called an implementation.

---
What are primitive actions in the context of HLAs (high level actions)? #flashcard #RA #PlanningAndActingInTheRealWorld 
	Primitive actions are just standard actions. They cannot be broken down further into more simpler actions. That is they are where our actions hierarchy bottoms out.

---
What is an implementation of a HLA and what is a refinement of a HLA? #flashcard #RA #PlanningAndActingInTheRealWorld 
	An refinement of a HLA is a sequence of HLAs or primitive actions. An implementation is a refinement that is made up of only primitive actions.

---
When is a HLA said to achieve some goal? #flashcard #RA #PlanningAndActingInTheRealWorld 
	A HLA can be said to achieve some goal then at least one of its implementations would achieve the goal.

---
How is a hierarchical search performed in a planning setting using HLAs? #flashcard #RA #PlanningAndActingInTheRealWorld 
	A hierarchical search is performed by dividing some HLA plan for a problem. Then we continue to refine each part; finding a refinement that matches what each HLA should do until we have devised the whole solution.

---
What does it mean to search for an abstract problem? #flashcard #RA #PlanningAndActingInTheRealWorld 
	This means we search for a partial solution made up of unrefined HLAs. The details of how the plan will  be implemented isn't concrete however we ensure the HLAs all do their job to fulfill the overall plan.

---
What is the reachable set for a hierarchical plan and a sequence of hierarchical plans? #flashcard #RA #PlanningAndActingInTheRealWorld 
	The reachable set for a single HLA $h$ from a state $s$ is the set of states the HLA could possibly terminate at. The reachable set for a sequence will just be the union of every state reachable from given the final HLA from any state reachable from the rest of the plan. Denoted $Reach(s,h)$ or $Reach(s,[h_1,...h_n])$

---
What are the three ways a HLA can describe its effect on a variable other than how a standard action would effect it? #flashcard #RA #PlanningAndActingInTheRealWorld 
	1. $\tilde+$ can choose to make it true or leave it unchanged
	2. $\tilde-$ can choose to make it false or leave it unchanged
	3. $\tilde\pm$ can choose to make it true or false or leave it unchanged

---
What is the optimistic set of states reachable from some HLA? #flashcard #RA #PlanningAndActingInTheRealWorld 
	The optimistic set of states assumes that we can always choose fully between the states we can affect and there is no case where one choice in variable value make another impossible. Denoted $Reach^+(s,h)$

---
What is the pessimistic set of states reachable from some HLA? #flashcard #RA #PlanningAndActingInTheRealWorld 
	This pessimistic set of states assumes that we can only choose one variables value freely at once. So we can at most ensure the value of one variable when we expand. Denoted $Reach^-(s,h)$

---
Given the optimistic and pessimistic sets of reachable states for some HLA what can we conclude about some set of goal states? #flashcard #RA #PlanningAndActingInTheRealWorld 
	If the pessimistic set intersects with the goal set then our HLA is guaranteed to fulfil our goal. If the optimistic set doesn't intersect then our HLA is guaranteed to not be able to fulfill our goal. And if the optimistic set does intersect but the pessimistic set doesn't then we need to refine our HLA to understand if it can reach a goal state.

---
What does it mean for a HLA to have the downward refinement property of some goal? #flashcard #RA #PlanningAndActingInTheRealWorld 
	It means at least one of the implementations of the HLA achieves the goal.

---

# Planning in the Real World
We have looked at basic logical planning in [[Classical Planning]] but in the real world we need to be more pragmatic and we need to relax the assumptions we have made about the world we are working in. We will also look at *hierarchical planning* which allows planning to be more efficient by solving a problem abstractly and then diving into details.

## Time, Schedules and Resources

## Hierarchical Planning
We cannot hope to plan down to the lowest possible detail and for all actions, this is just too hard a problem. Instead we need to plan at a higher level and using abstraction we can do this. This all comes from *hierarchical task networks* that is HTN planning.

#### High Level Actions
The lowest level set of actions are called *primitive actions* (these are the same as regular PDDL actions). High level actions can be *refined* to one or more a sets of these primitive actions called *refinements*. They themselves may be treated as their own planning problem for later. Seen below is a definitions of many possible refinements for an action.

![[Pasted image 20220429165722.png]]

HLA refinements can also contain other HLAs and have preconditions just like normal actions. A HLA refinements that doesn't contain further HLAs is called an *implementation*. The implementation of any HLA is a sequence made by adding together all the primitive actions gathered by expanding the HLA's sub-actions. We can say a HLA achieves a goal if one of its implementations does. When a HLA has one solution hence only one implementation we can easily find it's preconditions and effects. Otherwise we can either search through implementations to find one that works or we can use just the abstract HLA and reason about it on its own.

#### Searching for Primative Solutions
We can define a HLA recursively. To do this for example to refine the HLA $Act$ we get for any action $a_1$ which can be part of our refinement $[a_1,Act]$. We can then add a refinement to $[]$ which has the preconditions that the effect of $Act$ is already completed. This means once we have completed our action we can stop there. Expanding these HLAs it a search problem solved by a Hierarchical search. We can use any of the standard search techniques to do this.

![[Pasted image 20220429173202.png]]

#### Searhing for Abstract Solutions
Here we must ensure for any HLA in a sequence at least one of its implementations does achieve what we need the HLA to do. We can then work the precise details out later. A HLA achieving this' description is said to have the *downward refinement property* hence all that is needed is for the HLAs to have this then we can reason about them. The problem comes when we can't know without expanding some HLA if it will achieve a goal as we have to inspect all its refinements to ensure this. But this can never be ensured if we don't know if the preconditions for any action action is satisfied. Instead we work with the *reachable set* of a HLA. Written as $Reach(s,h)$ for state $s$ and HLA $h$. Is the set of states that are reachable by any implementation of the HLA. The reachable set of a sequence is all the states reachable from any state reachable from the subsequence. Hence

![[Pasted image 20220429175449.png]]

We can say a HLA achieves a goal if its reachable set intersects with the set of goal states. This is *angelic semantics*. Where as with *demonic semantics* all reachable states must be goal states. The angelic comes from the agent choosing the eventual refinement. This way of defining a HLA means the effects can have many states for variables. Either it becomes negative, positive or we choose (positive, negative or both).

1. $\tilde+$ means we can make something positive or leave it the same if we want to
2. $\tilde-$ means we can make something negative (false) or leave it the same 
3. $\tilde\pm$ means we can make something negative or positive or leave it the same

We cannot capture the different combinations of these however for example a state may allow us to choose $\tilde\pm A$ and $\tilde\pm B$ individually but may to be able to ensure they are both positive. We can give two estimates of the true set $Reach$ therefore. $Reach^-$ the pessimistic set where we may only be able to ensure one variable at a time or $Reach^+$ the optimistic set where we choose for all variables.

![[Pasted image 20220429181347.png]]

If our optimistic set intersects with a goal but the pessimistic set doesn't then we cannot tell if a HLA will reach our goal. In this case we need to refine further to know for sure if we can reach the goal. Angelic search is the strategy used to solve these problems

![[Pasted image 20220429182917.png]]

The idea is to solve a problem we will begin by checking if the optimistic set of reachable states contains our goal state if not we have failed. We check if out plan pessimistically intersects with out solutions and if it does we expand it. If not then we will try to refine our plan to make the pessimistic option match out goal state.

## Planning and Acting in Nondeterministic Domains
We aim to extend planning to handle partially observable, observable, nondeterministic and unknown environment. There are three types of planning that we can incorporate to deal with these states.

There are two types of non-determinacy which depend on how we describe states
	-> *bounded* - fixed number of possible  (described by ranges)
	-> *unbounded* - possibly infinite number of states (described by exact values)
		This also allows for unforeseen outcomes.
	

*Sensorless planning (conformant planning)* - for environments with no observations. Solution from all possible states.

*Contingency planning* - for partially observable and non-deterministic environments. Here we have separate conditions to take care of what we may observe. The plan describes what to do in any outcome. Can be used in *bounded* state space.

*Online planning* - which is used for unknown environments. We devise a plan if it wont work anymore we replan. This is for when we can't anticipate all contingencies. Can be used in *unbounded* state space.

Planners deal with *factored representations* meaning states are described by sets of variables that describe the world and can be broken apart in some way (unlike atomic representations). This lead to differences in how we plan as comparted to [[Beyond Classical Search]]. This changes how we define the agents ability to act and sense and their *belief state*. The **Belief State** is a set of possible states the agent may be in.

(Search Heuristics??)
(Resolving actions??)

We need to update our *belief state* based on what we observe. We may start in some state but we don't know the values of that state. Hence we need to observe and collect information to act (unless we want to take a Sensorless approach). The way this takes form in *PDDL* is actions are allowed to have precondition and effects with variables not in the actions variable list. That is we can use a kind of anonymous action from our belief state the resolves to a true action when applied to our true state. So the action
$$
Paint(can,x)
$$
no longer has a color $c$. The color will be part of the hidden state and may be inferred but isn't guaranteed by the action itself. The hidden variable $c$ will be *universally quantified* and will gain a value form a predicate tying it to a defined variable like $Color(can, c)$.

![[Pasted image 20220407213240.png]]

To get past the limitations of this the agent now has to perceive using percepts. The percept is given to the agent through its sensors and it must maintain a model of this when it is actually acting. The is encoded into PDDL with a *percept schema*.

![[Pasted image 20220407213458.png]]

The first one means when the object is in view we can perceive its color. The second one means if a can is open and in view we can perceive its color. We have a precondition that once met allows us to add a predicate and restrict our belief state. The agent learns the *truth*. **(** We can still describe a *fully observable* environment this way where every variable can be perceived without any preconditions, then a *Sensorless* planner just has no percept schema. **)** Without any exogenous events in the world these variables will not change so we know them for certain and can reason about them. An *online* replanning agent may have to check variables over to make sure things are going to plan.

In the real world we use a combination of *online* and *contingency*. We plan contingently for things that have a real change of happening and have results we care about and we use online/replanning when unexpected things happen. What we incorporate into our plans therefore depends on the situation goal / what we care about.

### 1. Sensorless Planning
In [[Beyond Classical Search]] we introduced planning for Sensorless problems. Now we expand for planning problems. We represent the physical transition model as a collection of action schemas and the belief state as a logical formula instead of a set of states (as before *BCS*). This belief state is similar to the goal state search used in *backwards planning*. We don't need fluents like *inView* as we cannot perceive ): We also take some unchanging facts as given for example $Object(table)$, $Can(C_1)$ etc. This is as they hold in every belief state. We may not know which predicates are true but may know some predicate in a collection may be true. Like all object and cans have colors. $\forall x. \exists c. \hspace{4pt} Color(x,c)$. We *Skolemize* these to obtain our belief state.

![[Pasted image 20220407215619.png]]

In classical planning we take a *closed world* approach and define any predicate not mentioned as false. But in this kind of planning *and partially observable planning* we use a *open-world assumption*. Here states can contain both positive and negative fluents (like backwards planning). A fluent not mentioned is unknown! The belief state is the set of possible worlds satisficing the formula. This can be solved by a sequence of actions

![[Pasted image 20220407220001.png]]

The agent can consider any action whose preconditions are satisfied by $b$. We cannot use the other action as our transition model will not define the *effects* if the preconditions may or may not be unsatisfied.

The rule for updating a belief state $b$ with an applicable action $a$ to a new belief state $b'$ is

![[Pasted image 20220407220412.png]]

$RESULT_P$ will be defined by our *transition model* in this case. Each of the $s$s are states defined by a 1-CNF formula. In our case we need to construct a new belief state from the $l$ literals in our $s$. If we know a literals value then we compute the new value form the current value and the delete list of the action. So if it isn't change we leave it but if it changes we update and delete. We consider 3 cases if we don't know the value

1. The action adds $l$ then $l$ will be true in $b'$ regardless of initial value.
2. If the action deletes $l$ then $l$ will be false in $b'$ regardless of its initial value.
3. If the actin doesn't affect $l$ then $l$ will retain its initial value (unknown) and will not be part of $b$.

This all comes from the above formula! We just need to make sure $b'$ never contains opposite literals. We start with $b$ then we add any true literals to true and false ones to false and keep any other the same (set or unset). This also means then all states if we start with a conjunction of literals will be a conjunction of literals hances for n fluents there are $O(n)$ states., better than $O(2^n)$ seen wit h FOL. This effect can only be maintained if our actions have the same effects no matter what state then are taken in when the conditions at least are met. These would be conditional with $when$ keywork like.

![[Pasted image 20220408200602.png]]

These lead to disjunctions hence we no longer have 1-CNF. The conditions are similar to precondition the difference being with preconditions if conditions aren't met the state stays the *same* as before hence no disjunction is needed. We can reduce FOL to 1-CNF by only considering fluents who's value we know for certain and keeping the rest out of the loop. But this limits our capacity to reason. This is *sound* all plans will work but not *complete* as it cannot find all solutions. We can also focus on keeping the belief state small that is maintaining a 1-CNF through our action sequence. We do this too when we check the time and pat our pockets (connection to neurobiology). Another option is to represent the belief as the initial belief state then the actions taken but this requires a lot of computation when we want to check if we satisfy our belief state. We can also tread these actions as literals themselves then we can sat solve to find a solution and understand what combination of actions are needed that way. This may or may not be more efficient depending on the situation.

**Heuristics** - Like in search we want heuristics to make out planning more efficient, that may be *admissible* ideally. We also know that if a belief stat $b_1$ is a subset of another belief state $b_0$ then $h(b_1)\le h(b_0)$ as solving $b_0$ also solves $b_1$ so any action relative to $b_1$ must be no worse.

This way if we calculate a heuristic for some superset of our belief state then we will have an admissible heuristic for it. Hence we can take a random collection of states that satisfy our belief state apply any admissible heuristic and take the max.

![[Pasted image 20220409113719.png]]

### 2. Contingent Planning
Contingents plans are worked out with if then else statements and describe how to solve a non-deterministic or partially observable problem.

![[Pasted image 20220409120553.png]]

Any variable in the plan is existentially quantified. As our percepts have preconditions what we percept may depend on the actual state we are in hence as with conditional effects we get disjunctions are are removed form 1-CNF with the same solutions as in the previous section.

### 3. Online Replanning
To replan we need *execution monitoring* which tells us when to replan. We can use **online replanning** when eighter we can't anticipate all outcomes or don't want to calculate every possible branch. For branches that are sufficiently unlikely we simple say $replan$.

Replanning may also mean our model of the world is incorrect, for example the model of some action may have a *missing precondition* for example if we miss that we need a screwdriver to open a can. We can also have *missing effects* for example we may get the floor painted while painting an object and we can have *missing state variable* like we aren't modeling what how much paint is in the can for example. There may also be *exogenous events* where outside forces interfere in our plan, this could also be some new requirement being added to our goal.

![[Pasted image 20220409122556.png]]

Without replanning our plans will therefore be fragile as our models must wok with the real world perfectly to not fail. The agent has a choice of how carefully it monitors the environment.

*Action monitoring* -> before executing an action the agent verifies that all the preconditions still hold.

*Plan monitoring* -> before executing an action the agent verifies that the remaining plan will still succeed. 

*Goal monitoring* -> before executing an action the agent checks to see fi there is a better set of goals it could be trying to achieve.

In the above diagram we see an agent who starts in $S$ and attempts to reach $G$ with $wholeplan$ this leaves it at state $S$ where it realizes it is in state $O$. From here the plan is *repaired* and then continues from $P$.

The runs into problems if we find our self in a dead end like running out of power. But also when the outcome of our actions isn't non-deterministic but just depends on a value not measured like for example the can being empty. We can just retry to get it to work eventually it will never work to paint with an empty can. We can either *randomly* select form possible plans then or **learn**.

[[Planning and Acting in the Real World Questions]]
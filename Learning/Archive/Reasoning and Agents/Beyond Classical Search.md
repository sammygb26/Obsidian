# Beyond Classical Search
We have looked at **classical** search algorithms in [[Search]] and [[Informed Search]] but these are only for problems that are **deterministic**, **observable** and **discrete** where the solution is a sequence of actions. We can get to more real world solutions if we look past this however.

## Local Search
So far the algorithms have has a **system**/**systematic way** to find a sequence. The sequence has mattered to the solution however for many problems such as [[Constraint Satisfaction Problems]] this order doesn't matter simply finding the solution is the trouble. **Local Search** algorithms don't care about pathing and operate at the level of a single, **current node**. Hence the name **local**. They have two main advantages

1. They can use very little space
2. They can find solutions to large (or infinite continuous) state spaces traditional **systematic** searches would fail in.

These type of searches can also be good for problems that don't have defined goals where instead a goal function is attempted to be optimized purely like with **genetic algorithms**.

We can consider the state space as a function with minima and maxima. The values here are given by our **heuristic function** or an **objective function**. A local search is **complete** if it always find a goal state. But it is **optimal** if it always find the global minima/maxima for the objective function.

![[Pasted image 20220211233648.png]]

## Hill-Climber Search
A **Hill-Climber-Search** is a simple search that attempts to maximize or minimize a value function. We just find the max value of all our successors and make that the next current state.

![[Pasted image 20220211234237.png]]

This is a **greedy** local search we just take the best neighbor state without looking ahead at all. These will make rapid progress towards an optimal state however they can easily get stuck at three main obstacles

1. **Local Maxima** -> Values which are greater than all their neighbors so the hill climber will remain stuck here
2. **Ridges** -> a sequence of local maxima that is hard to escape.
3. **Plateaus** -> a flat area in state space, it can either be a flat maxima or a shoulder which can lead to new maxima but our search can get lost.

There are alterations to this such as **stochastic hill climbing** where we choose randomly from the top max states. Or **Fist-Choice hill climbing** where we send out many stochastic hill climbers in all direction hoping one will stumble on a solution. **random restart hill climbing** just puts us in a random state and tries to find a solution. The success will depend on the **topology** of the state space the more local maxima the harder the problem.

## Simulated Annealing
If we just perform hill climbing and never go down it is easy to get stuck at maxima instead we could so random movement but then we will only find a solution randomly. The idea is we start with high randomness (temperature) and slowly cool until we settle on a solution. Similar to when metal is **annealed** heated and cooled slowly to increase strength. The way this works is we pick a random move and if it improves the situation we take it. The probability we pick it decreases exponentially with the 'badness' of the move, and the temperature. If the slowing down happens slow enough the probability of finding a solution approaches 1.

## Searching with Nondeterministic Actions
If we have a partially observable or non-deterministic environment or both we need to make use of *percepts* to narrow down the possible set of states we are in and can also tell us what outcomes of actions actually happened (for partially observable or nondeterministic respectively).

If we want to incorporate non-determinism we need to expand our transition model to define not just a result form an action in a state but a set of results.

![[Pasted image 20220409132019.png]]

If we don't know our state then we could be in any of the possible states of the world. When we start to take action we reduce and expand this state depending on the outcomes of that state. Our solution will then also contain if then else solution to give the flexibility needed to solve non-deterministic problems. These are *contingent solutions*

### AND-OR Search Trees
How do we find these *contingents solutions* though. We need to have a search tree as in [[Informed Search]] but we need more detail to give our solution. OR nodes have branching come from the agents choices while AND nodes the difference in outcomes comes from the environment.

![[Pasted image 20220409132711.png]]

For example here $suck$ in state 1 can lead to 5 or 7 randomly (environment AND). While in state 1 itself we can choose to go $right$ or $suck$ (choice OR). We can therefore get an and or search tree with the following algorithm.

![[Pasted image 20220409132932.png]]

Here we discard any reoccurring states as if that was a solution we could also have reached it earlier when we first found it in the search tree.

## Try, try again
It may be that our actions sometimes fail leaving us no closer to our goal. To take account of this we need looping and se we add labels which control our flow through the plan.

![[Pasted image 20220409133638.png]]

Again whether this actually works depends of if the all outcomes will happen or if there is a hidden state which means what we need to happen will never happen. We may need to **learn** to overcome this.

## Searching with Partial Observations
This is the case where we don't precisely know the state we are in instead we can make observations which narrow down what state we are in. This gives a *belief state* which is a set of possible states the agent may be in. Through further. If we have no percepts we are *Sensorless* and the problem becomes a Sensorless or *conformant* problem, where we attempt to coral all states to be the same through some sequence of actions. For example there are methods for orientating parts in a factory without knowledge of their initial orientation. This may be impossible if our actions are also non-deterministic as we cannot ensure we have completed any of the steps. Still the idea is to search in a belief state space to ensure we reach some goal state.

When we have a partially observable state we have to say how the environment generates percepts for the agent. We might for example have a local dirt sensor and a positions sensor but not a sensor for surrounding dirt as in the vacuum bot example. The problem specification will include a $Percept(s)$ function that define the percept that will be achieved in some state $s$. If this is also non-deterministic then this will return a set of possible percepts. With partial observations the states that could have lead to a percept will be a set. A three step solution is given for integrating belief onto the Sensorless version.

1. *Prediction* this is the same as the Sensorless problem where we predict a set of states from our current belief state given some action with will be $$\hat b=\text{Predict($b,a$)}$$
2. *Observation prediction* here we determine a set of percepts $o$ that could be observed in the belief state. $$\text{Possible-Percepts($\hat b$)}=\{s:o=\text{Percept($s$) and $s\in\hat b$}\}$$
3. *Update* stage is where we determine for each possible percept the belief state that would result form the percept. This will be a new belief state $b_o$ which is the set of states that could have given the percept.$$b_0=\text{Update($\hat b,o$)}=\{s:o=\text{Percept(s) and $s\in \hat b$}\}$$
So we update our belief state given our action then we find what percepts we could observe then we reduce our belief state to be only those states that could have produced the action. If we combine this with the possible percepts we can get the $Results$ which is a list of possible results we could have obtained $$\text{Results}(b,a)=\{b_o:b_o=\text{Update}(\text{Predict}(b,a),o)\text{ and }$$$$o\in\text{Possible-Percepts}(\text{Predict}(b,a))\}$$


[[Beyond Classical Search Questions]]
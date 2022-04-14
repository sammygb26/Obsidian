# Problems
These are what our [[Agents]] solve. A problem is similar to a Task [[Environment]]. The problem is defined by many different [[Environment]]al states. These states are connected by actions our agent can perform. Our agent needs to find solutions to these problems.

## Problem Types
**Deterministic, fully observable** -> this means we know our current state and we know from every state what state our actions will brig us to.
**Non-observable** -> This means we know for all actions in all states what state they will lead to is but we don't know for suer our state. The trick here is to find a way of ensuring we are in the goal.
**Nondeterministic and/or partially observable** -> Here we know our state or there about but we can't be sure what our actions will do. Therefore we need to use our senses to **check** and so we need to have a path that can change so we need a **contingency** plan (which can be found through [[Reasoning and Agents/Search/Search]] intermixed with execution) so this is called a **contingency problem**.
**Unknown state space** -> exploration problem

## Well-defined Problem Formulation
A problem can be formulated with an **initial state** an **action successor function** a **goal state** and a **path cost**. We formulate problems to abstract away from the real world.
* **Initial State** -> The state of the environment we start in
* **Action successor function** -> $S(\underline{x},a)\to \underline{y}$ where $\underline{x}$ and $\underline{y}$ are states and $a$ is an action. This defines the edges of the graph that we can visualize or problem as.
* **Path cost** -> function taking in current state and action and giving a cost (may be important if part of our problem is to minimize a cost)
* **Goal state/test** -> the state our agent has to reach to complete the problem.

## State Space and the Real world
The space of all possible states and the actions moving us between them can be thought of as a **state space**. The real world is far more complex than this state space so **abstraction** allows us to actually solve the problem. When we compare the abstract to the real we so the following patter
* *Abstract* state -> {set of real states}
* *Abstract* action -> {complex combination of real actions}
* *Abstract* solution -> {set of real path leading to a real goal}
**Abstraction** is useful since it allows us to reduce the problem to one that is easier to solve.

![[Pasted image 20220120173048.png]]
*State space for a vacuum robot*

For real world problems the states may be a combination of many variables the states spaces and their actions are therefore very complicated hence why we need **abstraction**.
![[Pasted image 20220120173144.png]]

[[Problems Questions]]
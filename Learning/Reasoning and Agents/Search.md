# Search
This is a **problem-solving** strategy that has the world represented in **atomic** states that have no structure unto themselves. Search requires a **goal** so this strategy is employed by a type of *goal-based agent* called a **problem-solving agent**. These agents will concern themselves with fully observable, deterministic worlds. We will set the goal to maximize the performance of the agent.

## Idea
So we have **atomic** states and we know what actions get us to what other states. This is from the world being **discrete**, **deterministic** and **fully-observable**. So the solution will be a sequence of action that will send us through a series of states finishing with us in a goal state. So once we have **formulated** our problem in terms of states and actions connecting them we can then **search** possible sequences of actions to find a solution. We would then **execute** this solution to solve the problem.
				**Formulate** -> **Search** -> **Execute**

![[Pasted image 20220211193244.png]]

So we perceive, we use this to update our state, then if we don't have a plan we figure out what we are aiming for then we construct a problem out of this and our current state. We can then search this to get a solution sequence.

## Well Defined Problem
In order to use search our problem needs to be **well defined**. For this it will need ->
1. **Initial State** where our search will try to reach the *goal* from
2. **Actions** what we can do in each state
3. **Model** (reactions) what our actions will do to our state(s) (transitions $\{s,a,s'\}$)
4. **Goal test** a way of determining if we have reached the goal state
5. (Opt)**Path Cost** a cost for each action so we might find the 'best' solution

All this will give our problem in terms of a state space we can represent this with a **graph**

![[Pasted image 20220211195332.png]]

## Searching For Solutions
Now that we have a problem we can search for solutions to it this is done my **expanding** nodes where a node is a state given a sequence of actions. We keep track of all the **frontier** nodes that are reachable from ones we have already explored, we know some sequence of actions reaching these states. We can then ideally find a goal node then the path of actions we have taken to this will be a solution. If we have no goal node we can expand another so our frontier is bigger. This gives us **Tree Search**

![[Pasted image 20220211194929.png]]

We can see that we can go from *Arad* to *Sibiu* to *Arad* again this would make a loop in our actual *state space* and is a **redundant path** since any solution containing this part of the sequence would have a simpler solution where we didn't do the loop. We can keep track of the explored nodes so we can keep track of the **explored** nodes (meaning we have added all their child nodes to the frontier) and so make sure not to explore them again, This gives us **Graph Search**

![[Pasted image 20220211200015.png]]

## Implementing Search Algorithms
We will need a **node** which is a *data-structure* that allows us to keep track of where we are in the tree. The difference between **nodes** and **states** is nodes make up the search tree while states make up the problem state space formulation.

A **node** has four parts
1. **State** -> The state in the state space the node represents
2. **Parent** -> The node that was explored to reach this one
3. **Action** -> That action that was applied to the parents state to reach here
4. **Path-Cost** -> The cost to reach this node from the initial state. 

![[Pasted image 20220211200606.png]]

We can simple then generate a **child node** from a **parent node** with the simple function below

![[Pasted image 20220211200718.png]]

We simply use our problem formulation to get the next state from our parent's state. Then assign the parent and the action. The path cost is then calculated form the current path cost and the action cost.

We will also need some sort of ordering for our *frontier* to give us nodes in an order as we will have to do one at once. This simple choice gives us our first two **search-strategies**. A **strategy** just being the order we expand the *frontier* in. We can either use a **stack** or a **queue**. If we use a *queue* we will get **Breadth-First Search** and if we use a stack we will get **Depth-First Search**.

When we are comparing these different algorithms we want to measure how well they perform. For this we measure four things:

1. **Completeness** -> Is the algorithm guaranteed to find a solution
2. **Optimality** -> Does the strategy find the most optimal solution having the total lowest cost.
3. **Time Complexity** -> How does the time taken behave in the limit
4. **Space Complexity** -> How does the space taken to compute behave in the limit

The **Complexity** features are asymptotic values and are measured in accordance with the size of the problem. There are 3 characteristics of a problem we will concern ourselves with

1. $b$ the **branching** factor -> on average how many possible actions can be taken from a node
2. $d$ the **depth** -> how deep is the shallowest goal we can hope to find.
3. $m$ the **maximum** -> how deep is the deepest node (could be $\infty$)

## Breadth-First Search
This has the effect of going 'wide' first. We explore all the nodes accessible in 1 step before exploring all the nodes accessible in 2 steps and so on. 

![[Pasted image 20220211215908.png]]

This behavior is ensure by the use of a **queue** which gives **FIFO** (First In First Out) behavior. So the nodes we first find will be first explored.

![[Pasted image 20220211214314.png]]

This is **Breath-First-Search** algorithm. It is very much a **graph-search** implemented with a **FIFO** scheme for the frontier nodes' exploration order.

#### Properties
**Completeness** -> This will always find a solution if one exists as it will explore radially out form the start state
**Optimality** -> It will find the solution taking the least actions. This may not be the most optimal if we have a cost function but without this is optimal
**Time-complexity** -> In the worst case we have to explore every node down to the solution at depth $d$ if each time the number of nodes multiplies by $b$ this will be $O(b^d)$
**Space-complexity** -> We will have to store the frontier nodes in this will always at least be the number of nodes at the solution depth which $b$ times larger for every level down so is $O(b^d)$

## Depth-First Search
This has the effect of going 'deep' first. We explore the nodes we have most recently found first. So we 'dive' down into the tree. Once we find a dead end we **back-track** using the parent of the dead end node.

![[Pasted image 20220211215954.png]]

This behavior is ensured by the use of a **stack** which return the last element that was added to it a so called **LIFO** (Last In First Out) scheme. The implementation is the same as **depth-first-search** algorithm accept with a stack instead of queue.

#### Properties
**Completeness** -> This will find the solution if the depth is finite and **graph-search** is used however if it can get in loops or there is no limit on the depth it will have to stumble upon the solution.
**Optimality** -> Its not optimal since it just finds whatever solution it ends up across.
**Time-Complexity** -> On average the since half the time it will have to explore half the tree at least all the way to $m$ the time complexity is a fraction of the time to explore the whole tree so it $O(b^m)$ 
**Space-Complexity** -> It will only have to store the branches for one shot down to the max depth at worst so is $O(bd)$

**Depth-First-Search** and **Breadth-First-Search** have slightly varying characteristics but which his better. They differ on hey performance measures. The key idea is that even though **BFS** is better in terms of time, completeness and optimality it has terrible space complexity making it infeasible for large problems. But **DFS** is still bad in terms of completeness and may also take a very long time to find even shallow solutions. There is a solution however.

## Depth-Limited-Search
This is a partial solution, how do we make sure **DFS** doesn't get stuck in a loop of go on forever. We just limit the depth it can go to. This way if there is a shallow solution it will find it. We just keep track of the depth and stop exploring at this point.

![[Pasted image 20220211221159.png]]

We have a **cutoff** value that determines this. This is a limited algorithm however. Its time complexity is similar to **DFS** accept we replace $m$ with this $l$ for the limit. Then it is still incomplete as there might be no solutions at our given depth. But we could just keep increasing the depth...

## Iterative-Deepening-Search
Here we perform a **DLS** to a depth of 1. Then we go for 2 and so on. It is really a wrapper around **DLS** that gives it desirable properties. Here is the algorithm.

![[Pasted image 20220211221617.png]]

Very simple but the key is it maintains the asymptotic properties of **DFS** while gaining completeness and optimality if we don't have a cost function.

### Uniform-Cost Search
This is a more basic one similar to **BFS** the way it works is we instead of expanding the shallowest node we expand the node with least cost. This is enforced by a **heap** where we keep a list ordered so that we can always pop of the element with some min value. In this case the cost.

![[Pasted image 20220211222107.png]]

The great thing here is it becomes **optimal** even for problems with cost functions.

## Bidirectional Search
The idea here is we search from a goals state and a start state at the same time in hopes of running into each other.  We do have to know the goal states before hand however. This works best if we have 1 goal state, like in a pathfinding problem.

![[Pasted image 20220211222356.png]]

## Summary
![[Pasted image 20220211222420.png]]

These are alright but we can get better results by instead of using these **uninformed** searches using [[Reasoning and Agents/Search/Informed Search]]
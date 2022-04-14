# Adversarial Search
**Adversarial Search** is concerned with how an agent should act in a **game**. Where in AI a game is usually a **zero-sum**, **perfect-information** (observable) game (like chess). **Zero-Sum** is the condition where one agent is against another, so one winning means the other looses. This is enforced by their utility functions being opposites so they come into conflict. Most games worth studying can't be solved due to their high branching factors. Being slower in these cases means the algorithms can't perform as well. We will look at **pruning** to allow us to discount moves we wont make. **Evaluation functions** so we can limit the depth of our searches and actually get a solution.

## Formulation
We consider games between two players, **Min** and **Max**. **Max** moves first and points are awarded for winning and subtracted for loosing. This makes this a search problem with the following elements.

1. **Initial State** -> $S_0$ how the games is set up at the start
2. **Player**(s) -> which says which player has the next move in a given state
3. **Actions** -> the set of legal moves that can be made from a state
4. **Terminal-test** -> says if a terminal makes the came over (**terminal states**) or if the game continues
5. **Utility** -> this describes if the agent wishes to get to some terminal state or not. So it will be positive for a win and negative for a loss.

The **Initial State**, **Actions** and **Results** define a game tree as below. Nodes are states and actions are moves. The **Utility** is given at the leaf **terminal states**. For simple games there are few states so the tree is possible to compute but for larger games this is more theory as it would be impossible to actual use it in a game like chess with $10^{40}$ states.

![[Pasted image 20220212115712.png]]


## Minimax Algorithm
In previous searches we would just need a sequence of action to get to the goal. But we are competing against **Min** so we need to find a **strategy** that brings us to the goal. It will have **Max**'s move then the moves resulting from the different choices **Min** can take. The **optimal** strategy will leave **Max** in the best move after **Min** has moved. Then each move is determined by how good the options it will lead to given that **Min** will act in the best way. If we consider a trivial game where each player makes two moves then the **terminal states** are reached we get the following tree.

![[Pasted image 20220212121300.png]]

The **minimax** value for a given node is the value of the best action the opponent will take

![[Pasted image 20220212121357.png]]

The value depends on the current player, this defines weather the expected choice will be for the player in that node. The **minimax decision** is the action (above $a_1$) that leads to the state with the highest minimax value for **Max**. This is all assuming **both players are moving optimally**. So it maximizes the worst case outcome for **Max** leaving **Min** with the worst subset of choices.

The basic **minimax** algorithm explores down to the end states *recursively* then backs up to give the minimax values for all nodes. This will take $O(b^m)$ time for branching factor $b$ and max-depth $m$. It uses a depth first search so space complexity is $O(bm)$ or $O(m)$ if we create actions one at a time. This is impractical for real games due to the time complexity.

![[Pasted image 20220212123006.png]]

So this is the basic algorithm.

## Alpha-Beta Pruning
The number of nodes expanded is exponential in the size of the tree. This needs to be cut down to make this feasible. Alpha-eta pruning allows us to find optimal solutions without exploring all nodes. They key idea can be seen bellow

![[Pasted image 20220212123943.png]]

If we even find some node $n$ such that **Player** has a choice to go there. Then if at have found a choice $m$ for which $v(m)>v(n)$ in some parent of $n$. Then we will never reach $n$ as either there is some greater node on the current path that would cause us to not choose $m$ or the value that will be propagated up will be worse than $v(m)$ so we will choose $m$. We then keep track of these values $\alpha$ for the best move for **Max** that has been found for any choice point along the path to the current node. Then $\beta$ is the value for the best move for **Min** that has been found along the path to the current node.

![[Pasted image 20220212132638.png]]

The reason the best along the current path is used is if we have found a better node while going down it could propagate up and we may pick it instead of our previous $\alpha$. But if we can't beat the new $\alpha$ it will be chosen ahead of us instead. The effect his have is exploring high value nodes first makes our algorithm cut out more and more work. In the best case we get $O(b^{m/2})$ when picking perfect moves (reducing our branching factor to $\sqrt b$. But when we select random moves it is about $O(b^{3m/4})$.

## Dealing with Reality
Even with adversarial search and alpha beta pruning we have to explore all the way to **terminal states**. This isn't feasible for games like chess even with our pruning. Instead we have to explore to a given depth and stop. We still need some value to propagate up however. An option is to use a heuristic function called an **Evaluation function** this alters the recursion seen bellow

![[Pasted image 20220212134550.png]]

This **Evaluation function** is an estimate of the expected utility we will achieve from a given position, so is an estimate of the minimax value. For many games however this is context dependent so in chess the estimates were given by evaluations of how good moves were developed by human players. But later neural networks were used to do this. A simple way to do this is summing up a collection of features for each position

![[Pasted image 20220212140000.png]]

The features are just values calculated from the state. Like number of pawns in chess etc. This assumes the value of a feature is **independent** from the other ones. Otherwise we would have a complex functions (like that created by a neural network or more simple non-linear functions). A problem is if the evaluation function will change wildly after the current move. In this case we an measure the **quiescence** of a terminal state. Low quiescence means the evaluation function is not likely to change soon. In this situation the evaluation function makes sense to use but otherwise it may cause poor performance. There is also the **horizon effect** where an AI will attempt to mov pieces capture over the horizon it will explore to at the expense of other pieces. But it doesn't have enough long planning to realize this was always inevitable.

## Optimizations
We want to try find best moves with a heuristic. An approach that makes sense is remembering the tree exploration from out previous search. This works since the next state out opponent chooses will be one we have already explored a great deal of. So we can use our previously calculated best choices to inform us this time. We can also use an iterative deepening approach where we explore 1 ply deep then 2 ply and so on. We can use the best moves from the last search to cut out much of the work in the new one hence this actually doesn't take too much effort. Then when the opponent makes a move we just restrict our search to a subtree.

We can also store **transposition** where we arrive at the same position by multiple routs. We can store minimax values in a hash table in case they come up again. Then we can use this table to guide our search at the same time.


# Making Complex Decisions
This will focus instead of one-shot stochastic environments instead long term *sequential decision problems*. Here the agents utility depends on its performance in a sequence of actions.

## Sequential Decision Problems
We will look at a simple example of an agent moving on a grid. There is a goal and a pit. The agent ending a the goal has a utility of 1 and the pit -1. The agent can move $Up$, $Down$, $Left$ and $Right$. But in a stochastic manor such that for example when attempting to move up it has a certain change to move left or right instead. The environment is fully observable.

![[Pasted image 20220414133949.png]]

Of course the deterministic solution is easy. We will have a *transition model* which describes the outcomes of any action in each state or $P(s'|s,a)$. The transitions will also be *Markovian* (Markov assumption). We also need to define a utility function, which will depend on the sequence of states and *environment history*. This will for now be just a reward for reaching each state. 1 and -1 for the states labeled and -0.04 for all other (to make the agent prefer shorter paths). We will make the utility of the environment history just the sum of these rewards when the agents reaches the end. This whole set up is called a *Markov decision process* (sequential decision problem, fully observable, stochastic with Markovian transition model and additive rewards). All this plus a set of $Actions(s)$ which we can take in state $s$.

A solution to this problem will be a *policy*. A description of what action should be taken in any state. This will be denotes $\pi$. The quality of the policy is the expected utility as a policy can have a range of eventual utilities. The *optimal policy* will give the highest expected utility $\pi^*$. The policy describes what the agent should just do it is therefore a simple reflex agent that is made by a utility-based agent.

![[Pasted image 20220425104334.png]]

This gives the optimal policy for various path costs. For example in a the path cost is low enough that the optimal choice is to move the long war around form 3,1 and not risk ending up in (-1). We can also see in b some options for how different path coasts affect the policy. For example with a positive path reward we will attempt to take as many actions as possible and avoid both +1 and -1.

### Utilities over time
In the *Markov Decision Process* above we used a sum of rewards of the states visited to calculate the performance of the agent. This isn't the only way and we will use *multi-attribute utility theory* to define this. We write this as $U_h([s_0,s_1,...,s_n])$. To analyze this we need to decide whether there is a *finite horizon* or *infinite horizon*. For a *finite horizon* there is some fixed $N$ after which we do not count any more utilities. That is for all $k>0$ we have $U_h([s_0,s_1,...s_{N+k}])=U_h([s_0,s_1,...,s_N])$. For example if $N=3$ for the above example an agent in (3,1) can't look far enough ahead to consider taking the long way around and therefore must head directly to (+1). With $N=100$ however the long term path can be considered and therefore we can take the longer safer path. This means with a finite horizon the optimal action in a given state could change over time. We say the optimal policy is *nonstationary*.

With an *infinite horizon* however there is not change in the assessment of a state given the time. Hence it will have a *stationary policy*. It should also be noted that infinite horizon doesn't mean the sequence in infinite just there is no fixed deadline $N$. For example a sequence may not be infinite with terminal states.

We now need to define the utility of the state sequences. In the terminology of multi-attribute utility theory each state $s_i$ can be viewed as an *attribute* of the sequence $[s_0,s_1,...]$. To obtain a simple expression in terms of the attributes we some sort of preference-independence assumption. We assume the preferences between sequences are *stationary*. That is the preference between two sequences $[s_0,s_1,s_2,...]$ and $[s'_0,s'_1,s'_2,...]$. Is that same as $[s_1,s_2,...]$ and $[s'_1,s'_2,...]$ if the sequences begin with the same state $s_0=s'_0$. This means that if you preferred some future starting from tomorrow then you should also prefer it starting from today. With a stationary assumption there are just two ways to assign utilities tosequences.

1. *Additive rewards* that is the utility of a state sequence is $$U_h([s_0,s_1,s_2,...])=R(s_0)+R(s_1)+R(s_2)+...$$
2. *Discounted rewards* that is the utility of the state sequence is $$U_h[s_0,s_1,s_2,...]=R(s_0)+\gamma R(s_1)+\gamma^2R(s_2)+...$$ where $\gamma$ is the *discount factor* in the range $(0,1)$. This describes the agents preference for current reward over future rewards.

If we choose *infinite horizon* however if a terminal state is never reached or if the agent never reaches ones then all the environment histories will be infinitely long. If we also have additive, undiscounted rewards then our utility will be some infinite value. That is $+\infty$ or $-\infty$ we can agree the former is better but how can we compare $+\infty$ to itself? There are three solutions to this.

1. With *discounted rewards* the utility of a sequence is *finite* even if the sequence is infinite. Then every value is bounded by some $\pm R_{max}$ such that $$U_h(s_0,s_1,s_2,...])=\sum_{t=0}^\infty \gamma^tR(s_t)\le\sum_{t=0}^\infty\gamma^tR_{max}=\frac{R_{max}}{1-\gamma}$$ this results comes from the infinite sum of a geometric series.

2.  If the environment contains terminal states and the agent is *guaranteed* to get to one eventually then we don't need to compare infinite sequences . A policy guaranteed to reach a terminal states is called a *proper policy*. We can use $\gamma=1$ for this (additive rewards). Improper policies can cause standard MDP solving tequniques to fail.
3. We can compare infinite sequences in terms of *average reward* obtained per timestep. A sequence that on average stays around 0.5 will be better than one that stays around 0.1.

### Optimal Policies and utilities of states
We will use the sum of discounted rewards to give the utilities of a state sequence.  We can compare the policies by comparing the *expected* utilities found when executing them. We assume the agent is in some initial state $s$ and define $S_t$ to be a random variable that is the state reached at $t$. When executing some policy $\pi$. Hence $S_0=s$. The distribution over the remaining $S_t$ values is therefore defined by $s$, $\pi$ and the transition model for the environment. The expected utility obtained for executing $\pi$ starting in $s$ is given by $$U^\pi(s)=E\left[\sum_{t=0}^\infty\gamma^tR(S_t)\right]$$ Here the expectation is with respect to the distribution over state sequences determined by $s$ and $\pi$. Out of all the policies starting in $s$ there will be one (or more) will have the highest expected utility $\pi_s^*$ will denote this. Hence $$\pi_s^*=\mathop{\text{argmax}}_\pi U^\pi(s)$$
Since we use discounted utilities with an infinite horizon the optimal policy is *independent* of the starting state. Hence $\pi_{s}^*=\pi_{s^*}^*$ for all starting states $s$ and $s^*$. The action sequence itself won't be independent of course but the overall best policy will be. This means it doesn't matter what state we start in if two sequences converge to the same state they don't disagree on what to do and this makes intuitive sense. Given this we can say the true utility of a states is just $U^{\pi^*}(s)$ that is the expected sum of discounted rewards if the agent executes an optimal policy, we can just write $U$ for this. For the above example we will therefore get

![[Pasted image 20220425115851.png]]

Given this we can define equally $\pi^*(s)$ as $$\pi^*(s)=\mathop{\text{argmax}}_{a\in A(s)}\sum_{s'}P(s'|s,a)U(s')$$Hence it is the action we can take in $s$ that will maximize the expected utility of the state we land in. But how can we find this policy?

## Value Iteration
This is an algorithm for calculating an optimal policy. We attempt to calculate the utility of each state and then use the state utilities to select an optimal action in each state.

### The Bellman equations for utilities
We have previously defined the utility of a state as being the expected sum of discounted rewards from that state onwards. Hence there is a relationship between the utility for one state and its neighbors. That is the utility of one state is the intermediate rewards $R(s)$ and the expected discounted utility of the next state. That is $$U(s)=R(s)+\gamma\mathop{\text{max}}_{a\in A(s)}\sum_{s'}P(s'|s,a)U(s')$$ This is called a *Bellman equation*. A set of bellman equations is defined for all sets then the $U(s)$ values are the solution to these equations and there is only one unique solution. The maxed action is also the optimal policy.

### The value iteration algorithm
The bellman equations are the basis of value iteration. If we have $n$ possible states then there are $n$ equations containing for each $n$ unknowns. We can try solve these simultaneously therefore. The problem is the equations are *nonlinear* due to the use of the "max" operator. Hence this will be harder to solve than simple linear algebra techniques. An *iterative approach* can be attempted.  We can start with arbitrary initial values for the utilities we calculate the right hand side of the equation and use it as a new estimate for the left hand side. We can continue this until an equilibrium is reached. We let $U_i(s)$ be the utility for the state $s$ at the $i$th iteration. The iteration step is called a *bellman update* and looks like $$U_{i+1}(s)\leftarrow R(s)+\gamma \mathop{\text{max}}_{a\in A(s)}\sum_{s'}P(s'|s,a)U_i(s')$$
Hence this gives the following algorithm

![[Pasted image 20220425122352.png]]

The values over time for a number of states is given bellow aswell as the number of iteration required to get bellow a given error for different discount factors.

![[Pasted image 20220425122724.png]]

### Convergence of value iteration


## Policy Iteration
We can see that it is possible to get an optimal policy even when the utility function estimate is inaccurate. If one action is clearly better than the others then the exact size of the utilities really doesn't matter. This suggests another way to find optimal policy called *policy iteration*. It has two basic steps

1. *Policy evaluation* where given a policy $\pi_i$ we calculate $U_i=U^{\pi_i}$, the utilities of each state if $\pi_i$ where to be executed.
2. *Policy improvement* calculate a new MEU policy $\pi_{i+1}$ using one-step look-ahead based on $U_i$.

This algorithm will terminate when the policy improvement step yields no change in the utilities. At this point $U_i$ will be the fixed point of the bellman update. Then $\pi_i$ will be the optimal policy The *policy improvement* step is trivial but how can *policy evaluation* be implemented. Since the action at each step us fixed by the policy this is actually far simpler than solving the bellman equations as in value iteration. This removed the "max" operator essentially as the action is fixed. We can therefore solve for $U_i$ using linear algebra. This can be solved in time $O(n^3)$. Hence for small state spaces this can work the best but can become expensive for large state spaces. However exact policy evaluation isn't needed. We can instead perform simplified value iteration as the policy is fixed. $$U_{i+1}(s)\leftarrow R(s)+\gamma\sum_{s'}P(s'|s,\pi_i(s))U_i(s')$$, this algorithm is then called *modified policy iteration*.

![[Pasted image 20220425130245.png]]

[[Making Complex Decisions Questions]]
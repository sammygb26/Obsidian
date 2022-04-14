# Making Complex Decisions
This will focus instead of one-shot stochastic environments instead long term *sequential decision problems*. Here the agents utility depends on its performance in a sequence of actions.

## Sequential Decision Problems
We will look at a simple example of an agent moving on a grid. There is a goal and a pit. The agent ending a the goal has a utility of 1 and the pit -1. The agent can move $Up$, $Down$, $Left$ and $Right$. But in a stochastic manor such that for example when attempting to move up it has a certain change to move left or right instead. The environment is fully observable.

![[Pasted image 20220414133949.png]]

Of course the deterministic solution is easy. We will have a *transition model* which describes the outcomes of any action in each state or $P(s'|s,a)$. The transitions will also be *Markovian* (Markov assumption). We also need to define a utility function, which will depend on the sequence of states and *environment history*. This will for now be just a reward for reaching each state. 1 and -1 for the states labeled and -0.04 for all other (to make the agent prefer shorter paths). We will make the utility of the environment history just the sum of these rewards when the agents reaches the end. This whole set up is called a *Markov decision process* (sequential decision problem, fully observable, stochastic with Markovian transition model and additive rewards). All this plus a set of $Actions(s)$ which we can take in state $s$.

A solution to this problem will be a *policy*. A description of what action should be taken in any state. This will be denotes $\pi$. The quality of the policy is the expected utility as a policy can have a range of eventual utilities. The *optimal policy* will give the highest expected utility $\pi^*$. The policy describes what the agent should just do it is therefore a simple reflex agent that is made by a utility-based agent.


17.1,2,3
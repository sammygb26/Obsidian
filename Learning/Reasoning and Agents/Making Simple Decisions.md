# Making Simple Decisions
Now we can combine *utility theory* with *probability theory* to yield *decision theory*. This will give us a *decision-theoretic agent* which can make rational decisions based on what it believes and wants.

## Combining Beliefs and Desires Under Uncertainty
The basic idea of *decision theory* is it deals with choosing among actions based on the desirability of their *immediate outcomes*. We are assuming the environment is episodic therefore. We define $Result(a)$ as a random variable whose values are the possible outcomes states $s'$ our our actions. From this we get

![[Pasted image 20220412184303.png]]

The $a$ is the event where the action $a$ is executed or chosen by the agent. We define how good a state is with a *utility function* $U(s)$ is the utility of $s$. The *expected utility* of an action is the average utility of the outcomes weighted by the probability of those outcomes call it $EU(a|e)$. The principle *maximum expected utility* says a rational agents should attempt to maximize this utility

![[Pasted image 20220412184611.png]]

## The Basis of Utility Theory
We may wounder why the MEU principle is the one to choose why not attempt to minimize loss over gain (like humans do in many circumstances). We can lay out constrains on how preferences should function for a rational agent then from this show that MEU must hold. The following notation is used 

![[Pasted image 20220412185352.png]]

$A$ and $B$ can be through of as representing something the agent gets. We may not know what is is in that case it can be thought of as a *lottery*. The outcomes of a lottery may be another lottery or an atomic state. We want to understand how our preference between the lotteries come form our preferences for the underlying states. This gives constraints that our preferences must obey

1. *Orderability* two things are either greater, lesser or equal in preference, we have to decide.
2. *Transitivity* if we have three lotteries $A$ $B$ and $C$ and $A\succ B$ and $B\succ C$ then $A\succ C$
3. *Continuity* if some lottery $B$ is between $A$ and $B$ in preference then there is some probability of getting $A$ or $C$ in another lottery which we would be indifferent to $B$ from.
4. *Substitutability* If an agent is indifferent to two lotteries $A$ and $B$ then it is also indifferent to a more complex lottery with $A$ or $B$ subbed in
5. *Monotonicity* if we prefer $A$ to $B$ then we will prefer a lottery that gives a higher change of $A$ and $B$ otherwise
6. *Decomposability* this means we can combine any sequence of lotteries into a larger lottery where each final outcomes has a summed probability form the outcomes of the more complex lottery

These *axioms of utility theory* only describe preference not the utility function. But we can conclude there must be a *utility function* with these axioms. We called it $U$ and it is defined such that $U(A)>U(B)\iff A\succ B$ , $U(B)<U(A)\iff B\succ A$ and $U(A)=U(B)\iff A\sim B$. This means from the above axioms also that the *expected utility of a lottery* is the sum of the probabilities of each outcome times the utility of that outcomes.

![[Pasted image 20220412190953.png]]

Hence if we define the utility of states and the change of each for every action the utility of the actions is defined.

## Utility Functions
We can use *preference elicitation* to work out an agents utility function. For this we present different choices to the agent and given the outcomes we want for each choice we can build up a utility function. There is not absolute scale but this is usually done by fixing the worst and best cases. The others must fit between and the axioms define their positions. These are called *Normalized utilities* if the worst is at 0 and the best at 1. We asses the values for any other state by letting the agent choose between it and a *standard lottery* $[p,a;(1-p);b]$ were $a$ is the best state and $b$ is the worst. Hence this lottery has utility $p$.

## Utility of Money
This is a part of human utility that is studies in economics where much of this agent theorizing has come from. If an agent prefers more money to less all other things being equal it has *monotonic preferences* for money. Money may not act as a utility function as an agent may have different preferences between lotteries.

An example is if we are going to win a million pounds and we are given the choose between keeping this and flipping a coin and having 50% chance of loosing all our money and 50% change of getting 2.5 million. The *expected monetary value* will be 1.25 million for the coin flip. More than if we just keep the money  but this doesn't seem like the better decision. This doesn't mean our utility method has failed. We want to define the utility of two actions.

![[Pasted image 20220412192943.png]]

If utility isn't directly proportional to the monetary value then we can solve this problem as below.

![[Pasted image 20220412193053.png]]

In the real world we find the utility of money is treated as a logarithmic function on the amount of money (a). We may also not care as much about going more into debt see in (b). An agent with a curve like this is *risk-averse*. The opposite case is *risk-seeking*.

## Decision Networks
This is a generation mechanism for making rational decisions called an *influence diagram*. We combine Bayesian networks with additional nodes for actions and utilities.

![[Pasted image 20220412194209.png]]

This is an example of a *decision network* it has three types of nodes

1. *Chance nodes* these are the ovals and are random variables that act just the same as in Bayesian networks.
2. *Decision nodes* these are rectangles and represent a choice of action the agent has. We choose the value that goes into these nodes.
3. *Utility nodes* these are the diamonds and represent the agents utility function

We can also connect the utility directly to the random variables in this case it will be the expected utility instead as the random variables have a distribution that defines expected utility.

![[Pasted image 20220412194809.png]]

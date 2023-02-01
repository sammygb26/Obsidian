What is a decision theoretic agent? #flashcard #RA #MakingSimpleDecisions
	A decision theoretic agent models the probability of different outcomes from different actions. It combines this with a utility model for the different outcomes to weight up its actions.

---
How is the the result of an action modeled probabilistically? #flashcard #RA #MakingSimpleDecisions 
	The result of an action can be defines as a random variable. Or possibly split up into multiple RVs if that is simpler. This means our agent can reason about $P(Result(a)=s'|a,e)$

---
How is an action chosen by a rational decision theoretic agent? #flashcard #RA #MakingSimpleDecisions
	A rational agent will attempt to maximize expected utility. Therefore the actions it will choose will that that which maximizes the utility of the possible states weighted by their probability.

---
What are the three operators that describes preference between outcomes in utility theory? #flashcard #RA #MakingSimpleDecisions 
	These are $\succ$, $\sim$ and $\succsim$ meaning for arguments $A$ and $B$. $A$ is preferred to $B$. The agents is indifferent to $A$ and $B$. The agent is prefers $A$ to $B$ or is indifferent from $A$ to $B$.

---
What are the properties of preferences or axioms or utility? #flashcard #RA #MakingSimpleDecisions 
	1. *Orderability* the preference between two events must be equal, greater or lesser. The agents cannot not choose.
	2. *Transitivity* if $A$ is preferred to $B$ and $B$ to $C$ then $A$ is preferred to $C$.
	3. *Continuity* if the preference of something $B$ is between $A$ and $C$. Then there is a probability of getting $A$ or $C$ that makes the agents indifferent between than and $B$.
	4. *Substitutability* if an agent is indifferent to two events $A$ and $B$ then some more complex sequence of events that will lead to $A$ or $B$ that agent will also be indifferent to.
	5. *Monotonicity* if we prefer some event $A$ to $B$ then we prefer some event that leads to $A$ more often than $B$.
	6. *Decomposability* a sequence of events leading eventually to some states is equivalent so a single event leading to the states with the same probability.

---
How can preference elicitation be used to find an agents utility function? #flashcard #RA #MakingSimpleDecisions
	We need to find the relative unity of an event for an agent. For this we can find some worst event and make it 0. Then some best event and make it 1. We find  for any event the probability of getting 1 or 0 in utility for which the agent is indifferent to that and some event. That probability can be the utility of the event. If the axioms of utility hold this will yield a utility function will place each event in the correct order and with the correct relative weighting.

---
What is a decision network used for? #flashcard #RA #MakingSimpleDecisions 
	A decision network can be used for one-shot short term decisions. It only takes into account a single slice of time or just a fixed section of a Bayesian network for which we can control some values (the actions). Some of the random variables can be weighted together to give our utility. The expected utility for each action can therefore be compared.

---
What are the parts of a decision network? #flashcard #RA #MakingSimpleDecisions 
	The parts of a decision network are the chance nodes which are random variables just as in a BN.
	Decision nodes that represent values we can choose.
	Utility nodes are the outcomes node we care about.

---
How can a decision network be simplified? #flashcard #RA #MakingSimpleDecisions 
	We can remove intermediate utility measures and just show how possible random variables direct influence on the utility function.

---

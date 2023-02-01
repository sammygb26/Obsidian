What constraint classical search have the we may want to get past? #flashcard #RA #BeyondClassicalSearch
	Classical search takes place in deterministic, observable and discrete environments where the solutions is a sequence of actions. If we want to work with CSP solutions where the order of actions doesn't matter or more chaotic environments we will need more search techniques.

---
What is local search? #flashcard #RA #BeyondClassicalSearch 
	This is a search techniques that doesn't take into account pathing. It instead works just to find some next node given the current node. Hence it only cares about the local space.

---
What are the advantages of local search? #flashcard #RA #BeyondClassicalSearch 
	It can use very little space to operate as only the current node needs to be stored between steps. Then can also find solutions to large or infinite continuous state spaces which tradition systematic searches found fail in.

---
What does complete and optimal mean for a local search algorithm? #flashcard #RA #BeyondClassicalSearch 
	A complete local search algorithm always finds some goal state. An optimal local search algorithm always finds the state with the global maxima/minima for the objective function. 

---
How does hill-climber-search work? #flashcard #RA #BeyondClassicalSearch 
	This is the simplest approach and just attempts to maximize or minimize the value function. We just loop over all neighbors than can be reached through some action. If the best one is better we move our local state to it and continue and if not we return our current value. This is a greedy local search as it always makes the best short term choice rather than looking ahead. This means it makes rapid progress but quickly gets stuck.

---
Where can hill climber search get stuck? #flashcard #RA #BeyondClassicalSearch 
	1) Local maxima where all values that can be reached are less desirable.
	2) Ridge - a sequence of local maxima that is hard to escape
	3) Plateau - a flat area in state space, it can either be a flat maxima or a shoulder either way our search can get lost here.

---
What is simulated annealing? #flashcard #RA #BeyondClassicalSearch 
	This is similar to hill climbing but we may note if we never go down it is easy to get stuck at maxima. Instead we could move randomly but this isn't an efficient way to find a solution. The idea is we start with high randomness (temperature) and slowly cool until we settle on a solution. If we find an improving move we take it but if we don't we may also take it depending on how bad and the current temperature.

---
How can a transition model be expanded to define nondeterministic transitions? #flashcard #RA #BeyondClassicalSearch 
	We can use a set of states as the output and input for our transition model instead.

---
What are contingent plans? #flashcard #RA #BeyondClassicalSearch 
	Contingent solutions work in fully observable non-deterministic environments and describe what to do in a given state aswell as what to do in all the possible states reached after that action. 

---
How can searching be done with limited observations? #flashcard #RA #BeyondClassicalSearch 
	To do this we maintain a *belief state* which is a set of possible states we could be in. We may also reduce with with percepts lining up with the possible percepts we could achieve.

---
How does AND OR search work? #flashcard #RA #BeyondClassicalSearch 
	The idea is we have two cases that can change our action path, either we make a decision or some random event happens we can perceive. So for each split case in an AND node (that is the environment make the decision). We can then explore from the OR nodes to find paths to a solution.

---

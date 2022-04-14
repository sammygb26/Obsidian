What is a probabilistic FSM? #question 
	A probabilistic FSM is a type of non-deterministic FSM where instead of us 'choosing' where we go every time there are multiple possibilities we have a probability of going down each path. This way each string isn't accepted or rejected but has a probability of being accepted or rejected.

---
What are the parts of a probabilistic FSM? #question 
	A probabilistic FSM is made out of 5 parts.
	Q the set of all states in the FSM
	$\Sigma$ the set of all symbols in the language of the FSM
	q0 the starting state of the FSM
	F the accepted end states.
	$\Delta$ the transition function taking a set of states for a given symbol in the alphabet to another set of states.
	We then also have $p_{q,a,q'}$ which is the probability for the symbol $a$ in the state $q$ taking us to the state $q'$

---
What are hidden Markov Models (HMMs)? #question 
	These are FSM transducers rather than inducers meaning they output symbols at every state instead of taking them in.

---
What are the parts of a hidden Markov model? #question 
	The parts of a hidden Markov model are similar to a PFSM. There is a set of states Q. Then there is a probability of moving from one state to any other $p_{q,q'}$. Then in each state there is a probability of generating any given symbol in the alphabet. So the chance of generating symbol $a$ in state $q$ would be $b_{a,q}$.

What is the most likely path problem? #question 
	The idea is we want to find the path through the states of the HMM that was most likely to generate the string we got.

---
How does the Viterbi Algorithm work?
	This works in a dynamic programming way the idea is for any symbol in the sequence the most likely state it came from is the one that has the most likely chance of generating the previous part of the sequence multiplies by the chance of getting to the current state and the chance of generating the current symbol. This gives us a recursion that can be modeled in a 3D data structure. Hence we can dynamically build up our answer from this level.

---

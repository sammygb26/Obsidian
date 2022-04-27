What problem does complex decision describe? #flashcard #RA #MakingComplexDecsions
	Complex decisions describes sequential decision problems where past choice may affect future ones. The utility the agent cares about depends on a sequence of actions.

---
What parts of a Markov decision process? #flashcard #RA #MakingComplexDecsions 
	A sequential decision problem is describes by a transition model which gives the distribution of possible states given some action in a state. For the transition model we can also make a Markov assumption that the transition only depends on the last current state.
	A utility function which takes in a state and gives a number reward for that state.

---
What is the solution to a Markov decision process? #flashcard #RA #MakingComplexDecsions 
	The solution is a policy that describes what the agent should do to maximize long-term utility in each state.

---
What problem is needs to be solved when we consider utilities over time? #flashcard #RA #MakingComplexDecsions 
	We need a way to get from the rewards of a sequence of states the long term utility of those states. This is complicated when there may be infinitely long sequences of states.

---
What are the two ways to deal with the utility of a sequence of actions that could be infinite? #flashcard #RA #MakingComplexDecsions 
	We can have a finite horizon where we only count the rewards up to a certain point in the future. Or we can have an infinite horizon.

---
What is the problem with a finite horizon when comparing the utility of sequences of states? #flashcard #RA #MakingComplexDecsions 
	With finite horizons our plan may change depending on our starting state. This means as we replan in the future updating our current state our plan can change. That is it is non-stationary.

---
What are the two ways to deal with infinitely long sequences of states given we make a stationary assumption? #flashcard #RA #MakingComplexDecsions 
	We can either have additive rewards or discounted rewards. For additive rewards we count a sum over the rewards in all states as the utility. For discounted rewards we discount for each timestep in the future some factor of the reward is discounted such that even for a infinite sequence some finite utility value is approached.

---
What is the problem with an infinite horizon additive rewards model? #flashcard #RA #MakingComplexDecsions 
	This means any overall negative or positive sequence the utility will tend to infinity. But we cannot compare infinities hence our agents cannot compare these utilities. Only if they are negative or positive. This is solved by a discounted reward as the utility approaches some finite number.

---
What are the three ways to compare infinite reward sequences? #flashcard #RA #MakingComplexDecsions 
	1. *Discounted rewards* where our reward is a sum over all rewards from our sequence but we discount the future rewards based on some discount factor.
	2. We only compare *proper sequences* that reach terminal states and therefore aren't infinite.
	3. *Average rewards* where we scale down the utility based on the length of the sequence. But this more highly weight strategies that end sooner

---
How can we give the utility of a policy in a Markov decision process? #flashcard #RA #MakingComplexDecsions 
	The utility of a a policy will be the expected utility achieved if we follow that policy over all the states. The same policy will be optimal for all states in a MDP.

---
How can we define the utility of a state for a Markov Decision Process? #flashcard #RA #MakingComplexDecsions 
	This will be the expected discounted reward reward (utility) achieved if we follow out policy from that state.

---
How can we find the optimal policy if we already know the utility of the states in a MDP? #flashcard #RA #MakingComplexDecsions 
	This will be for each state the action the maximizes the expected utility of the next state.$$\pi^*(s)=\mathop{\text{argmax}}_{a\in A(s)}\sum_{s'}P(s'|s,a)U(s')$$

---
What are the parts of a Bellman utility equation and what is it? #flashcard #RA #MakingComplexDecsions 
	A bellman utility equation gives the utility for some state. This is calculated by adding the rewards for said state to the maximum expected utility for some action in that state. $$U(s)=R(s)+\gamma\mathop{\text{max}}_{a\in A(s)}\sum_{s'}P(s'|s,a)U(s')$$

---
How does the value iteration algorithm for the Markov Chain process work? #flashcard #RA #MakingComplexDecsions 
	We can see that the bellman equations describe for $n$ states $n$ equations with $n$ unknowns. If they were linear equations this could be solved as a matrix however the $max$ operator is nonlinear. Value iteration instead treats these equations as a contraction on some state utility vector object. We repeat a bellman update step where a new utility value for each state is calculated using the previous utilities (which can initially be random). This will overtime cause the utility vector to approach a stationary point which is the true utility of the states.

---
How does policy iteration work to solve a Markov Chain Process? #flashcard #RA #MakingComplexDecsions 
	Policy evaluation updates a policy in two steps. It evaluates it, generating utilities for the states in the process given the current policy. Then it improves it by generating a new optimal policy for those new state utilities. The improvement stage can be found by using the state utilities to find for each state the action the maximizes the expected next utility. The utilities themselves can be found by noting that since the policy is fixed the bellman equations become linear. Hence since there are $n$ equations and $n$ unknowns we can solve the linear equations to get the exact utility for the states.

---
How does modified policy iteration work and why is it needed? #flashcard #RA #MakingComplexDecsions 
	Modified policy iteration is needed if we can't perform complete policy evaluation due to limited resources. Instead we can estimate using the same techniques as value iteration accept without the max step as the policy is fixed.

---

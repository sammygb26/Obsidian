
What are the four different problem types and what is their solution described as? #flashcard #RA #Problems
	Deterministic, fully observable -> This is when our agent know the state of the world and how it will change with the actions the agent takes. The solution to this problem is a sequence of actions .
	Deterministic, Non-observable -> This means we know how our actions will affect the state of the environment but not what state we are in. The solution here is again a sequence of actions (this time it must ensure we somehow complete the goal)
	Nondeterministic and/or partially observable -> Here we can't be sure what our actions we cannot be sure what our actions will do so we need a contingency plan to change what actions we take depending on what we perceive.
	Unknown State space -> We need to explore to understand the environment better.

---
What are the parts of a formulated problem? #flashcard  #RA #Problems
	Initial state -> the state the environment starts in.
	Action successor function -> function describing what state the actions will take us to for a given state.
	Path cost -> defines the cost of an action in a given state important depending on goal and if we require optimum solutions
	Goal state -> the state we have to reach to complete the problem

---
How do state spaces help us solve real world problems? #flashcard  #RA #Problems
	This is through abstraction. The real world is far to complex for us to design agent programs to solve instead we create simplified state spaces with abstract actions and abstract state. These we can then solve.

---
How do abstract states compare to the real counterparts? #flashcard  #RA #Problems
	*Abstract* state -> {set of real states}
	*Abstract* action -> {complex combination of real actions}

---

	
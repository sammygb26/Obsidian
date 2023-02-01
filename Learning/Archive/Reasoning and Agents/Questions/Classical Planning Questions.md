What problem does classical planning solve? #flashcard #RA #ClassicalPlanning
	Logic cannot be solved for larger problems and becomes intractable while search can be hard to implement without a numerical evaluation of our goal.

---
What is PDDL? #flashcard #RA #ClassicalPlanning 
	PDDL is a language representation that is simpler although less expressive than FOL. We can describe planning problems with it and avoid problems with inference in FOL.

---
What are the parts of a PDDL description of a problem? #flashcard #RA #ClassicalPlanning 
	The *initial state* which we start in. The *Actions* which are the possible actions we can take in any state $Actions(s)$. The *Result* which is the out come of any action in any state $Results(s,a)$. Then then have the goal which describes the states we want to reach $Goal(s)$.

---
What are states in PDDL? #flashcard #RA #ClassicalPlanning 
	A state is represented as a conjunction of positive fluents that are ground (no variables). We make the closed world assumption hence any fluent not mentioned is false. We can also have predicated on constants which act just like regular fluents but give a way to label them.

---
How are actions and results represented in PDDL? #flashcard #RA #ClassicalPlanning
	Actions and results are given via an action schemas. These have three parts; the arguments, the precondition and the effect. The arguments are variable which can be assigned to any constant which gives an instance of the action. If the preconditions are met in the state we are in we can therefore perform the action. The effect describes what the action changes. So what it adds and removes to form the next state.

---
How are the precondition and effect described in PDDL? #flashcard #RA #ClassicalPlanning 
	The precondition and effect are both conjunctions of literals both positive and negative. As we have the closed world assumption, all the positive literals in the precondition must be in the current state and the negatives must not be. Then the effect works as an add delete list. Any negative literals in the effect are removed from the current state if they are in and any positives not already in are added.

---
How is a goal represented in PDDL? #flashcard #RA #ClassicalPlanning 
	The goal in PDDL is represented as a conjunction of positive and negative literals. This defines a function returning true or false when applied to a state. That is if our goal is satisfied in a given state. This will be true if none of the negative literals exist in our state and all of the positives ones do. Any not mentioned literal is ignored.

---
What is state-space search? #flashcard #RA #ClassicalPlanning 
	In state space search we try to find a path of action that modify the initial or goal state, revealing a path between both. It is called state space as each node in our search is a state.

---
How does forward (propagation) search work? #flashcard #RA #ClassicalPlanning
	In forward planning we start from the initial state and perform actions getting to new states. We can use domain independent heuristics with this however and apply A* to find a solution.

---
How does backward (regression) search work? #flashcard #RA #ClassicalPlanning 
	In backward planning we start from the goal and apply actions. As we start with a conjunction of positive and negative laterals we continue with this. We can apply an action in reverse to get a subgoal from a goal. If a subgoal matches our initial state we have found a path to our goal.

---
What are partially uninstantiated actions? #flashcard #RA #ClassicalPlanning 
	This is a type of action used in backward planning. We perform an action with a variable instead of a constant leaving the instantiation to later allows us to simulate if we had performed many actions in one stroke. Hence we have less subgoal but the same coverage making backward search more efficient.

---
What is plan space search? #flashcard #RA #ClassicalPlanning 
	The idea is instead of searching for a sequence of actions we instead treat the initial state and finial goal as constraints that must be matched by actions. This means the exact order doesn't matter but instead only if we can find a connection match.

---
What is a partially ordered plan? #flashcard #RA #ClassicalPlanning 
	A partially ordered plan is a collection of actions that match the start initial state to the goal state through action however the order isn't fixed instead constraints are added to ensure actions don't interfere with each other.

---
How is a partially ordered plan found? #flashcard #RA #ClassicalPlanning 
	We find a flaw in the plan then add an action to take care of this. This may lead to more or less open conditions. If we can resolve these to our start state by adding more actions we have found a POP.

---
What parts are needed to describe a partially ordered plan? #flashcard #RA #ClassicalPlanning 
	To describe a partially ordered plan we need a list of actions in the plan. A list of orderings that describe the constraints on the plan. A list of links that describe why the plan has the constraints.

---
What is the benefit of partially ordered plans? #flashcard #RA #ClassicalPlanning 
	Partially ordered plans search through a space of possible plans rather than simply what possible final plans exist. They allow for flexibility and choice when the plan is being executed while reducing the search space as search POP represents many actual plans.

---

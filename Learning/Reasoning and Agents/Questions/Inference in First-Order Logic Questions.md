What is a *substitution*? #flashcard #RA #InferenceInFOL
	A *substitution* is an assignment of variable to ground terms.

---
What is universal installation? #flashcard #RA #InferenceInFOL
	This means if we know a universal statement is true then every possible substitution of ground terms in place of the variables is a also true for a given model.

---
What is existential instantiation? #flashcard #RA #InferenceInFOL
	The rule is that if we have n existential statement we can perform *existential instantiation* by replacing the variable that is quantified by a new constant symbol that isn't used elsewhere. This could always be proved to be equivalent to some symbols that is used else where but for the time is different. This new symbol is called a *Skolem constant

---
What is *reduction to propositional inference* and how do functions give a problem with this? #flashcard #RA #InferenceInFOL
	The idea is that we can just remove quantifiers and treat the problem as a simple propositional one that we already know how to solve. We can  use *universal installation* and *existential instantiation* to do this. The problem is if we have functions we have infinite *ground terms*. However there is a theorem saying that if some sentence is entailed it can be shown with only a finite number of propositionalized knowledge base. So we can do a deepening search were each time we increase the number of functions we can apply to constants.

---
What is *reduction to propositional inference* semidecidable? #flashcard #RA #InferenceInFOL
	The problem is as we use an iterative deepening approach to solve if we find a level for which our sentence is entailed then we know it is entailed in general. But if we never find this level we can't know if there is some level we haven't reached or if our sentence is false. This makes *RPI* semidecidable it can tell us if something is entailed but not if it isn't.

---
What is *unification*? #flashcard #RA #InferenceInFOL
	Unification is when we have two sentences and we try to find a substitution that makes them equivalent. For example $\forall x. P(x)$ can be unified with $P(Jack)$ udder the substitution $\alpha=\{x/Jack\}$.

---
How can *unification* be used with *generalized modus ponens*? #flashcard #RA #InferenceInFOL
	*GMP* says if we have a statement of the form $p_1\land p_2\land ... p_n \implies q$ then if we have some $p_1^*, p_2^*...p_n^*$ that unifies with $p_1\land p_2\land ... p_n$ under some substitution $\alpha$ then we can imply $q$ with the substitution $\alpha$. So we can use unification to find this substitution and then infer the result.

---
What must we always do to our variables when *unifying*? #flashcard #RA #InferenceInFOL
	We must *standardize apart* this means we give every variable a different name so that we aren't trying to unify so that two variable are the same when they shouldn't be.

---
What are the 7 steps to simple unification? #flashcard #RA #InferenceInFOL
	1. *Decomposition* where if we are trying to unify two predicates that are the same we switch to unifying their terms.
	2. *Conflict* if we are trying to unify two predicates that aren't the same, or constants that aren't the same we *fail*.
	3. *Eliminate* if we are trying to unify some $x$ to some non variable term $t$ (that passes occurs check) then we just add $\{x/t\}$ to the substitution and replace all $x$ with $t$.
	4. *Delete* if we try to unify something to itself we just try to unify whatever is left.
	5. *Switch* if we are trying to unify some ground term to a variable we switch the order so that it is the same form as needed for *eliminate*.
	6. *Coalesce* if we are trying to unify two variables together we can just replace all the references with one to the other in our remaining unification and add the substitution $\{x/y\}$
	7. *Occurs check* if we are trying to unify $x$ with some non variable term that contains $x$ we have *fail* as this will cuasse an infinite loop.
	
---
What is *forward chaining*? #flashcard #RA #InferenceInFOL
	*Forward chaining* is a method of inference where we start from our ground truths and continue to use *GMP* and *unification* to infer new sentences until we can infer some sentence we are trying to infer. All of our knowledge base must be made our of *definite clauses* of the form $A\land B\to C$ where $A$, $B$ and $C$ are literals. Where *literals* are atomic sentences.

---
What are the properties of *forward chaining*? #flashcard #RA #InferenceInFOL
	It is *sound* and *complete* meaning something is only inferred when it is entailed and anything that is entailed is inferred. The problem is if we have function symbols then an infinite number of new facts can be generated. In this case *forward chaining* is semidecidable.

What is *backward chaining*? #flashcard #RA #InferenceInFOL
	This is the opposite of *forward chaining* the idea here is instead of starting with our known facts and building up we start with what we want to prove and branch down. Filled out our what must be inferred to infer our conclusion.

---
What are the properties of *backward chaining*? #flashcard #RA #InferenceInFOL
	Backward chaining will find solutions and is *sound*. But cannot infer all due to getting stuck infinite loops where it will continue to try to imply some truth but never manage.

---
What is *non-ground term binary resolution*? #flashcard #RA #InferenceInFOL
	Here the idea is that if we have two literals what we unify under sam $\theta$ then if they are negations of each other we can infer that they can't both be true. Hence if they are part of two disjunctions then we can take the matching literals our and combine into one large disjunction.
	
	![[Pasted image 20220215200304.png]]

---
What is *resolution*? #flashcard #RA #InferenceInFOL
	Resolution is a technique where we reduce our *FOL* to *CNF* then we use *Non-ground Binary Resolution* to infer a contradiction with the negation of the statement we are trying to prove hence proving the whole thing. If all our $KB$ is in *CNF* then all the disjunctions can be used as parts of *non-ground binary resolution* we can continue to match to conjunctions until either we reach no remaining clauses in our disjunction (contradiction we can infer the opposite of what we were trying to resolve) or we can no longer apply rules hence we know under the substitution $\theta$ we have built up the statement we were trying to resolve can be true. 

---

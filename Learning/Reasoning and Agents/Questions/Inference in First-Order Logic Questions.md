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
In what form must sentences be to be used by generalized modus ponens? #flashcard #RA #InferenceInFOL 
	To be used in generalize modus ponens the statements must be in the form of a con


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
What are the three main ways to improve the efficiency of forward? #flashcard #RA #InferenceInFOL 
	The main types are 
	*Incremental forward chaining* - new facts must be derived form rules unifying with a set of conjuncts containing at least one conjunct not present the in the last loop.
	*Matching rules against known facts* - need to find a variable to unify into a rule. Can order which variables we look for by which predicate has the least objects in it.
	*Irrelevant facts* - sections of rules may be left out if they aren't relevant to our query. Equally variable bindings can be restricted to a set that fit our goal.

---
How can incremental forward chaining improve the efficiency of forward chaining? #flashcard #RA #InferenceInFOL
	Incremental forward chaining comes from the observations that with a standard forward chaining algorithm everything that can be inferred is inferred for each time step. So only a unification containing a conjunct from the last timestep has the potential of generating some new fact, so we don't need to evaluate any other. We can also index rules so that we only check ones matching conjunct types generated in the last timestep.

---
What is matching when it comes to forward chaining? #flashcard #RA #InferenceInFOL 
	Matching in forward chaining is the task of finding sets of conjuncts to match into the premise of a rule.

---

How can matching in forward chaining be improved from a standard forward chaining algorithm? #flashcard #RA #InferenceInFOL 
	Matching can be improved reducing the size of the set of variable substitutions we check. We can do this by storing possible variable bindings for conjuncts by the conjunct type they fulfill. This way to fill out all possible unifications with a conjugation we start with the conjunct with the fewest possible unifiers. If some variable is bound to multiple conjuncts then we can also start with the one that yields the fewest options. This way we have the least to check.

---
What is the problem of irrelevant facts in forward chaining? #flashcard #RA #InferenceInFOL 
	The problem of irrelevant facts in forward chaining is the general problem that we may infer many statements and use entire rules that have nothing to do with the statement we are trying to entail.

---
How can we get past the problem of irrelevant facts in forward chaining? #flashcard #RA #InferenceInFOL 
	To get around this problem we can use only a subset of rules that relate to our query. We can also restrict what variables can be used in some rule allowing us to restrict the values allow to a set of "magic" variables.

---
What is Logic Programming? #flashcard #RA #InferenceInFOL 
	Logic Programming a technique for describing some knowledge to a compute so it can infer facts on it. The Logic Programmers give the computer rules in a language like Prolog for example. Then we can query the compute with statements we want it to find answers to.

---
What are three ways to improve the speed of Logic Programs within backward chaining? #flashcard #RA #InferenceInFOL 
	We can instead of running a recursive program use a more dynamic approach where our path is stored in a stack; this makes it easier to find errors and can make other improvements easier to implement.
	We can keep track of variable bindings at all times. Combined with using a stack instead of recursion this allows for simpler code that saves on space and time. Each path of bindings is called a *trial*.
	We can compile our logic program so that the knowledge base is instilled into it and for each rule it can more efficiently find solution bindings.

---

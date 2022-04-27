What is a Bayesian network? #flashcard #RA #ProbabilisticReasoning
	A Bayesian network is a compact representation of a JDP that exploits conditional independence. It has a graph structure that describes the conditional independence of RVs (which are nodes in the graph). The edges are the relations and are directional flowing from parents (causes usually) to children. The graph is also acyclic.

---
What are the parts of a BN (Bayesian network)? #flashcard #RA #QuantifyingUncertainty
	A BN has a collection of RVs it models which are the nodes of a graph. The directed edges of a graph (pointing from parents to children) describe the conditional independence relations for a variable. That is a child is conditionally independent of all non-decedents given its parents. The CPD is also defined for each variable witch is the probability of each value given the parents. Then due to the conditional independence this is an efficient compression of a JPD.

---
How can the CPT values be used to find any JPD entry? #flashcard #RA #ProbabilisticReasoning 
	The CPT values represent the values probability given the parents, so we can multiply all the CPT entries corresponding to some assignment, as all the parents will be given to get the final probability for that assignment as would have been assigned in the JPT. This comes from if we expand using some order that is maintained in the parent child structure of the graph. This way using bayes law we can expand and remove irrelevant parents from each entry.

---
What is the chain rule in CPT expansion? #flashcard #RA #ProbabilisticReasoning 
	Since we can choose the order we expand such that we don't include any non-decedents in an expansion of a probability in many cases this is useful. $$P(X_i|X_{i-1},...,X_1)=P(X_i|Parents(X_i))$$Note this only works if none of $X_{i-1}...X_1$ are decedents of $X_i$
	
---
What is a Markov blanket and what properties does it have? #flashcard #RA #ProbabilisticReasoning 
	The Markov blanket of a variable in a bayes network is a nodes parents, children and children's parents. Any variable will be conditionally independent of everything else given the values for these nodes.

---
How can we represent efficiently conditional distribution? #flashcard #RA #ProbabilisticReasoning 
	The idea is to use efficient representations of common conditional connections between nodes. Some examples are Deterministic nodes where the values of the parents define the child completely, noisy-or which is part of the noisy class of relations but describes the cases where many causes could cause some values to shift but all in a noisy unsure way that is independent of each other. Continuous distributions can also be described by few values and therefore efficiently stored and describes despite infinite values.

---
Describes noisy or and how it works? #flashcard #RA #ProbabilisticReasoning 
	Noisy or is a noisy relations that describes when some values may be caused by many or variables. If we assume that if this effect is show or inhibited is independent we can use noisy or. We only need store for each parent the probability of inhibition. That is only the parent is true but the child is still false. The chance of any combination of parents providing a inhibited child is just the product of the individual probabilities.

---
What is the aim of inference in a Bayesian network? #flashcard #RA #ProbabilisticReasoning 
	The aim of inference in a Bayesian network is to find the probability of some value given some observed values. We therefore need to *marginalize* over the variables that we don't know. Hence we get $$P(X|e)=\alpha\sum_yP(X,e,y)$$For RV we care about X, evidence $e$ and other $y$. We apply the chain rule to this in order get our final equations we want to expand. We can then evaluate this statement to find our original query given the CPT entries.

---
How is inference by enumeration done in a Bayesian network? #flashcard #RA #ProbabilisticReasoning 
	To perform inference by enumeration we need to expand the following formula $$P(X|e)=\alpha\sum_yP(X,e,y)$$where $P(X,e,y)$ can be given by the CPT. We choose the order we marginalize over the values in $y$ as best we can to minimize the number of calculations. But then just split at each sum and multiple at each step expanded with the *chain rule*. 

---
What is the chain rule in Bayesian networks? #flashcard #RA #ProbabilisticReasoning 
	The chain rule comes when we repeatedly apply the product rule in a certain order to reduce a single probability to a product of conditional probabilities given by the CPT.

---
What is the main problem with value enumeration in a BN? #flashcard #RA #ProbabilisticReasoning 
	The main problem is continuous branching with the sum splits in value enumeration will lead to repeated multiplication of the same probabilities. This can be solved through variable enumeration where the repeated values are packed into a matrix which is processed to give the final answer.

---
How does variable elimination work? #flashcard #RA #ProbabilisticReasoning 
	Variable elimination works by splitting the sum created in variable enumeration into factors. The factors are given by the individual CPT values we are summing to begin with. Each entry into a CPT can be represented as a matrix that can be indexed by the changing elements of the probability. Hence we only store the CPT probabilities once. There matrices are multiplies pointwise and marginalized just as before.

---
How is marginalization and point wise factorization performed with variable elimination factors? #flashcard #RA #ProbabilisticReasoning 
	Marginalization is performed when we have a sum of probabilities all values of a RV. We start with a matrix who has a dimension described by this RV and we want to know what the probability of the other RV combinations is without considering the marginalized RV. So for each entry indexed by the other RVs we sum over all possible values for the marginalized RV.
	Point wise factor is done simply. From two matrices with RVs indexing into them we make a new matrix which has the union of the RVs from each indexing into it. Then for each cell in this matrix to find the new matrix we take th values for the RVs describing that cell plug them into the original matrices and multiply giving the new value.

---
How does direct sampling work? #flashcard #RA #ProbabilisticReasoning 
	Direct sampling is the simples approximate method for inference in a BN. The way it works is we generate sample states of the network distributed by how likely they are. We can then calculate anything we want from just the sample we have obtained. 

---
Describes the direct sampling algorithm for BNs. #flashcard #RA #ProbabilisticReasoning 
	For a prior probability for some conjunction of RV values. We start at the top of the BN and sample the values for the nodes with no parents first as their distribution depends on nothing. This allows us to sample the next nodes in the topological order as their parents give us their conditional probabilities. This continues until we have sampled every node we care about.

---
How are posterior probabilities calculates with direct sampling method? #flashcard #RA #ProbabilisticReasoning 
	Posterior probabilities are calculated either by rejection sampling or likelihood weighting. In rejection sampling we simply ignore every sample that does fit out conditional RVs and only sample from the remaining RVs. In likelihood weighting we fix the conditional RVs and weights each sample based on how likely it would have been to generate those RVs.

---
What are the downsides of each direct sampling posterior probability method? #flashcard #RA #ProbabilisticReasoning 
	*Rejection Sampling* can lead to throwing away many samples if we have unlikely conditions. This will mean we have to sample far more despite it not helping our final result.
	*Likelihood weighting* can lead to repeated multiplication of small numbers (less than 1) which will quickly approach 0 giving inaccurate results if we have many unlikely conditions. This problem can be reduced through the use of negative logs.

---
How does Markov chain simulation work? #flashcard #RA #ProbabilisticReasoning 
	The way this works is we generate uniformly some random sample of the RVs in the BN (fixing conditional RVs in place if we have them). Then we randomly pick some RV (that isn't a conditional one) and resample it. Its distribution can be given by its *Markov blanket* (parents, childing and children's parents). Each instance of the BN can be counted as a sample so by summing up the values for an RV we can approximate the distribution (with or without the conditional variables).

---

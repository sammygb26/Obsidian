What are hidden Markov Models? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies2
	Hidden Markov models is a system where we have $T$ observations ($x_1,...,x_T$) and $T$ model states ($z_1,...,z_T$).  We want to predict these **hidden states**.

---
What is the Markov assumption made in a HMM? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies2 
	We assume $z_t$ is independent of all $z_1,...z_{t-2}$ given $z_{t-1}$.

---
What does the HMM jpdf factorize according to? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies2 
	It factorizes according to $$p(x_1,...,x_T,z_1,...,z_T)=p(z_1)p(x|z_1)\prod_{t=2}^Tp(z_t|z_{t-1})p(x_t|z_t)$$

---
How can a probability distribution be represented by an undirected graph? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies2
	A probability distribution can be represented by an undirected graph where every vertex is a variable then the edges just exist if there is dependency between variables. No edge=independent.

---
When is a path blocked and variables separated in an undirected graph? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies2 
	A path is blocked if any vertex on the path is given. Two variables are separated if al paths between them are blocked.

---
When are two sets of variables independent given a thirds in an undirected graph? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies2 
	Two sets of variables X and Y are independent given a third Z if all paths between X and Y are **blocked** given Z that is all variables pairs are **separated** given Z.

---
When is a distribution said to factorize according to an undirected graph and what is the partition function? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies2 
	A distribution is said to factorize according to an undirected graph if $$p(x_1,...,x_n)=\frac1Z\prod_{i=1}^K\phi_i(C_i)$$ where $$Z=\sum_{x_1,...,x_n}\prod_{i=1}^K\phi_i(C_i)$$ is the **partition function** not depending on the assignment of $Z$ in this case.

---
What is a clique in an undirected graph? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies2 
	A clique is a set of vertices such that every vertex in the set has an edge learning to every other vertex in the set.

---
What is a maximal clique in an undirected graph? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies2 
	A maximal clique is a set of fully connected vertices such that there is no other vertex in the graph that can be added to the set to make it have more vertices and still be a clique.

---
When a probability distribution factorizes according to an undirected graph what are the factors? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies2 
	The factors are the $\phi_i$ components of the signature $\phi_i:\mathcal C_i\to\mathbb R$ where $\mathcal C_i$ is a set of all the possible assignments of the clique $C_i$.

---
When what implies independence in a jpdf that factorizes according to an undirected graph? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies2 
	Separation of variables implies independence however not always the other way around*.

---
What is a Bayesian Network? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies2 
	A Bayesian network is a combination of a directed graph along with a distribution that factorizes according to the graph.

---
What is a Markov Random Field? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies2
	A Markov Random field is an undirected graph combined with a distribution that factorizes according to the graph.

---
What is the difference between the Conditional Random Field and a Markov Random field? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies2
	When we have an undirected graph and probability distribution that factorizes according to that graph it will be a MRF generally if we are modeling joint distribution and a CRF when we are modeling conditional distributions.

---
What is the Ising Model? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies2 
	This is a undirected graph model where we have grid of random variables only dependent on their top, bottom, left and right neighbors.

---
What is a linear-chain conditional random field? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies2 
	A linear-chain conditional random field is a sequence of $T$ random variables all connected in a chain $$...-y_{i-1}-y_i-y_{i+1}-...$$ where each $y_i-x_i$. Where the graph is an undirected graph.

---
What is the conditional pdf of a linear chain conditional random field and how is the partition function different here? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies2 
	This will be $$p(y_1,...,y_T|x_1,...,x_T)=\frac1{Z(x_1,...,x_T)}\phi(x_1,y_1)\prod_{t=2}^T\phi(y_{t-1},y_t)\phi(x_t,y_t)$$ where the **partition function** $Z$ now depends on the assignment of the $x$ values instead of being constant (as this is a conditional distribution).

---
When can we say a distribution factorizes according to a graph? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies2 
	We can say this when all independencies on the graph are also in the distribution.

---
What does the Hammersley Clifford theorem say? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies2 
	This says that if a distribution matches all the independencies on an undirected graph and the distribution is strictly positive (not equal to 0) then the distribution factorizes according to the graph.

---

What is the definition of independence? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1
	We say $X$ and $Y$ (random variables) are independent if $$p(x,y)=p(x)p(y)$$ which is equivalent to $p(x|y)=p(x)$ or $p(y|x)=p(y)$.

---
How can say two sets of RVs are independent of each other? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	We can say two sets $\{x_1,...,x_n\}$ and $\{y_1,...,y_m\}$ are independent if $$p(x_1,...,x_n,y_1,...,y_m)=p(x_1,...,x_n)p(y_1,...,y_m)$$

---
Why is it important that independence allow us to factorize large probability statements? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	We can factorize for two independent elements $X$ and $Y$ into $p(x,y)=p(x)p(y)$. Now the domain $X\times Y$ is larger than $X+Y$ hence the function we create which is equivalent is much smaller hence more computationally efficient to model.

---
What is mutual independence and what other form of independence does this imply? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	Var variables $X_1,X_2,X_3$ are mutually independent if $p(x_1,x_2,x_3)=p(x_1)p(x_2)p(x_3)$. This implies **pairwise** independence between elements. But this **doesn't go the other way**.

---
What does it mean for variables to be conditionally independent? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1
	Variables $X$ and $Y$ are conditional independent given $Z$ if $$p(x,y|z)=p(x|z)p(y|z)$$

---
How can independence be tested for? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	Given our joint pdf we say $p(x,y)$ we know that we can get $p(x)$ and $p(y)$ by marginalizing our $y$ and $x$ respectively. Then we check these marginalized pdfs times together equal the original for every $x$ and $y$. That this this condition holds $$p(x,y)=p(x)p(y)$$

---
What is the probabilities chain rule? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	This comes from the idea that $p(x_1,...x_n)=p(x_i)p(x_1,...x_{i-1},x_{i+1},...,x_n|x_i)$. We can repeatedly apply this rule to expand some joint pdf of $n$ RVs into $n$ PDFs with more and more conditional variables. The **chain rule** states this can be done in any order.

---
How can we represent independence with a graph structure? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	Each vertex can be a random variable. We make this graph direction with the edges leading from "parents" to "children". A childs probability is independent of all other variable if we are given its parents' values.

---
If a probability space factorized according to some independence graph how can we write its JPDF? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	For a DAG of the vertices $x_1,x_2,...,x_n$ where a child is conditionally independent of all other variables given its parents. we can write $$p(x_1,x_2,...,x_n)=\prod_{i=1}^np(x_i|Pa(x_i)$$

---
If we have some factorization graph of a probability space is this the only way to represent the probability spaces structure? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	No the graph is just one way describing one way of factorizing this JPDF it hold no other say over the structure of the space.

---
What are the three most common structure in the independence graph? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	These are the **chain** (x->y->z), the **common cause** (x<-y->z) and the **v-structure** (or common effect) (x->y<-z).

---
If we have a chain structure in our independence graph what does this imply about the independence of the variables? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	If we have a chain $x\to y\to z$ then $(x\perp z )| y$.

---
If we have a common clause structure in an independence graph what does this imply about the independence of the variables? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	If we have $x\leftarrow y\rightarrow z$ then $(x\perp z)|y$.

---
If we have a v-structure in an conditional independence graph what does this imply about the independence of the variables? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	For $x\to y\leftarrow z$ this makes $x\perp z$ however if we are given $y$ then $(x\not\perp z)|y$.

---
How would we state that a graph reparents some probability space? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	This will be the case if the JPDF factorizes according to the graph.

---
With a v-structure how is the independence of the parents affected by knowledge of the child's descendants? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	The **v-structure** that is $x\to y\leftarrow z$ means that if we are given $y$ or any of its decedents $d$, then $(x\not\perp y)|d$ however if we don't know any of these then $x\perp y$.

---
What is blocking in a dependency graph? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	Some connection in the graph between $x$ and $z$ is blocked if $x\perp z$. 

---
When is a chain blocked in a dependency graph? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	The chain a->b->c is blocked given b.

---
When is common cause structure blocked in a dependency graph? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	The common cause structure a<-b->c is blocked in a dependency graph when b is given.

---
When is a v-structure in a dependency graph blocked? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	The v-structure a->b<-c in a dependency graph is blocked when b isn't given.

---
When is a path blocked in a dependency graph? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	A path is blocked if any of the basic structures making one up are blocked.

---
When are two variables separated in a dependency graph? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	Two variables are separated if all paths between them are blocked.

---
If we know the separation of variables in a dependency graph what does this tell us about their independence in the probability distribution that factorizes according to the graph? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	If two variables are separated then they are independent in the probability distribution that factorizes according to the graph.

---
Given a dependency graph what implies the independence of two sets X and Y given a third Z? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	X and Y will be independent if all pairs $X\times Y$ re separated given $Z$.

---
What is the task in naïve bayes? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	In naive bayes we are given $d$ features (as in a feature vector $\textbf x$) and we want to predict some $y$ values.

---
What does naive bayes assume for its variables? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	It assumes that all $x_i$ features are independent given $y$.

---
How does the jpdf factorize in naive bayes? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	The jpdf factorizes as $$p(x_1,x_2,...,x_d,y)=p(y)\prod_{i=1}^dp(x_i|y)$$

---
For naive bayes what is the conditional probability of y given x? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	This will be $$p(y|x_1,...,x_d)=\frac{p(y)\prod_{i=1}^dp(x_i|y)}{\sum_{y'}p(y')\prod_{i=1}^dp(x_i|y')}$$

---
What do we need to find in order to perform naive bayes? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	We need to find the bas probability for each $y$ not given $x$ and we need to find the probability of each $x$ given each $y$. That is $p(y)$ pdf and $p(x_i|y)$ conditional pdf.

---
How is a naive classifier bayes net trained? #flashcard #MachineLearningUni #StatisticalDependencies #StatisticalDependencies1 
	This is trained with the equation $$L=-\log\prod_{i=1}^np(y_i|\textbf x_i)$$where $\textbf x_i$ is a vector of $x_i$ features.

---

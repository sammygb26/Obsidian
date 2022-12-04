### Hidden Markov Models
For a sequence of observations $x_1, x_2, ...x_T$ we ass um there is a hidden sequence $z_1,x_2,...z_T$. The first assumption is that $x_t$ is independent of everything else given $z_t$ (Markov assumption). The second assumption is that $z_t$ is independent of $z_1,z_2,...z_{t-2}$ given $z_{t-1}$.  This will have the form:

![[Pasted image 20221117153720.png]]

The probability distribution that factorizes over the graph is

![[Pasted image 20221117153756.png]]

### An Undirected Graph Representation
The problem with the **directed graph** is we have to worry about mapping dependencies and we have to be careful with them.  Instead we use an **undirected graph**. Here

1. Each vertex is a variables
2. Each edge signals a dependency
3. The graph is undirected

We don't know the causal relationship between two objects and instead just state whether they are dependent or not. There are no child-parent relationships. A path is **blocked** if any vertex on the path is given. Two variables are **separated** if all paths between the two variables are blocked. Two sets of variables $X$ and $Y$ are independent given a third set $Z$ if $X$ and $Y$ are separated given $Z$. The problem is **factorization is harder**!

### Undirected Factorization
A distribution is said to factorizing to an undirected graph if

![[Pasted image 20221117154512.png]]

where 

![[Pasted image 20221117154544.png]]

The $Z$ is required as $\phi_i$ isn't always a probability and hence we sum over all values to ensure the result is a probability. We call $Z$ the **partition function**. Note $Z$ doesn't depend on any assignment of $x_1...x_n$ as we just go over every possible combination of $x$s.

**Clique** is a set of vertices all connected to each other.

The set $C_i\subset\{x_1,...,x_n\}$ is a **maximal clique** if there is no vertex we can add to its that would give a larger clique. The function $\phi_i:\to\mathcal C_i\to\mathbb R$ is called a factor, where $\mathcal C_i$ is all the possible values that can be assigned to $C_i$.

![[Pasted image 20221117155100.png]]

Hence the above class gives two cliques.

Similar to the directed case **separation** on undirected graph implies independences in the distribution that factorizes according to the graph. Technically, separation does not necessarily include all independencies in the distribution that factorizes according to the graph (but this is a technicality).

* A **Bayesian network** is a graph and distribution that factorizes according to that graph.

* An undirected graph and a distribution that factorizes according to the graph is called a **Markov random field**.

* An undirected graph and a distribution that factorizes according to the graph is typically a Markov random field (MRF) when modeling joint distributions, but typically called a conditional random field (CRF) when modeling conditional distributions.

### Ising Model

![[Pasted image 20221117155611.png]]

### Linear-chain conditional random field

![[Pasted image 20221117155634.png]]

Finding the cliques and expanding gives

![[Pasted image 20221117155729.png]]

Here $Z$ becomes a function as this is a conditional probability and so we must normalize with respect to the $x$s.

### Independencies to Factorization
If a distribution matches all the independencies on a directed graph then the distribution factorizes according to the graph. But we have to test **many** dependencies to make this happen.

(Hammersley-Clifford) if a distribution matches all the independencies on a undirected graph the distribution is **strictly positive** (not equal to 0), then the distribution factorizes according to the graph.

[[Statistical Dependencies 2 Questions]]
# Probabilistic Reasoning
Here we will introduce and use *Bayesian networks*, these allow us to exploit bayes rule to do useful inference within a model we hold. They are also natural to the world we live in and allow for an efficient representation of our world knowledge.

## Representing Knowledge in Uncertain Domain
*JPDs* can be used to fully describe the world so that we can reason about it probabilistically but they are inefficient in the way they store information. **Bayesian Networks** are data structures that describe relationships between objects so that by exploiting conditional independence they can store fare less than a usual JPD.

A *Bayesian network* is defined as a directed graph. Each node in the graph is a *Random Variable* (discrete or continuous), a set of directed links connects pairs of nodes. If an arrow points from RV $X$ to RV $Y$ then $X$ is the *parent* of $Y$. The graph s acyclic (overall is a DAG). Then for each node $X_i$ has a conditional probability distribution $\textbf{P}(X_i|Parents(X_i))$ and is conditional independent given $Parents(X_i)$ of all other RVs. The intuitive meaning of some connection is that the parent has an influence on the child.

![[Pasted image 20220411172556.png]]

This is one example of a Bayesian network another is given bellow with more layer of RVs and with the conditional probabilities aswell.

![[Pasted image 20220411172810.png]]

The *conditional probabilities* are in *conditional probability table*s which shows the probability distribution given the different values of the parent (with the false cases left out in this case as they are trivial to calculate given the true cases). Each of the cases is called a *conditioning case* (combination of parent values). Just as before these scaled as $O(2^k)$ where $k=$ the number of parents. But $k$ is usually much smaller than $n$ as before in [[Quantifying Uncertainty]]. If a node has no parents then there is only one conditioning case hence only one row. There are many extra things we could add but they are rolled into the probability tables which is a benefit of this technique. Hence we don't need to observe extra information or model it.

## The Semantics Of Bayesian Networks
The semantics of the network define what the edges and the number attached to each node mean. If we remember the *JPD* has each entry corresponding to the probability of a particular set of observed variable and we take the conditional independence statement about parents. For nay probability in the JPD
$$
P(x_1,...,x_n)=\prod_{i=1}^n\theta(x_i|parents(X_i))
$$
Here $P(x_1,...x_n)=P(X_1=x_1,...X_n=x_m)$ for brevity. The numbers $\theta$ are the values described in the network. Each *JPD* entry can therefore be represented as a product of appropriate *CPT* entries from the network. This means $\theta=P$ for the conditional probabilities hence.
$$
P(x_1,...,x_n)=\prod_{i=1}^nP(x_i|parents(X_i))
$$
If we read the *CPT* entries in a specific way we can extract the *JPD* entry.

![[Pasted image 20220411174654.png]]

This comes from repeated application of the product rule from [[Quantifying Uncertainty]] Done in a specific order allowing us to exploit the conditional independence eventually giving us our probability. This is called the *chain rule* it is equivalent to

![[Pasted image 20220411175130.png]]

If $Parents(X_i)\subseteq \{X_i-1,...X_1\}$ hence a Bayesian network is only true if a variable is conditionally independent of its other predecessors in the node ordering giving its parents. This gives a method of defining a network

1. *Nodes* first define the set of variables required to model the domain. Then order them $\{X_1,...X_n\}$ any order will work but the resulting network will be more compact if the variables are ordered such that causes precede effects.
2. *Links* for $i=1$ to $n$ do: *Choose* from $X_1,...X_{i-1}$ a minimal set of parents for $X_i$ such that the (14.3) is satisfied. Then we add a link from the parent to $X_i$. Then we write doe the CPT for $X_i$ ($\textbf P(X_i|Parents(X_i))$)

For the above network we must for $MaryCall$ believe the following statement

![[Pasted image 20220411180223.png]]

Otherwise the node would have different parents.

Now that we have defined how we build a *Bayesian Network* we can note due to the *chain rule* expansion it functions a a compact representation of a JPD that can be written given some conditional independence statements are true. We can also choose how many connections we want to model if we keep this below a fixed number we can achieved linear complexity rather than exponential! But in general we want to find the middle ground between storing many probabilities and having an accurate network and this can be decided based on our circumstances. The order of our graphs can determine how compact the representation is hence why choosing a good order is important

![[Pasted image 20220411181002.png]]

We also find that the *CPT*s describe strange probabilities if we have a *diagnostic* order. Instead we want a *causal* order that will be easier to find the probabilities to encode into our network.

*Topologically* we can say a node is independent of its non-*descendants* given its parents. This also lead to another independence property called a *Markov blanket*. That is a nodes is independent of all other nodes given its parents, children and children's parents.

![[Pasted image 20220411181931.png]]

## Efficient Representation of Conditional Distributions
We can make the *CPT* smaller by limiting the number of nodes in one to $k$ but we still have to fill a number of $O(2^k)$ but this is actually the worst case when the relationship is arbitrary instead we can use *canonical distributions* that fit a pattern to compress our representations.

#### Deterministic Nodes
A deterministic nodes value is given by its parents hence each of the rows in the *CPT* has all 0s accept one 1. This could also be a numerical relationship like minimum value (this could work for continuous parents).

#### Noisy-OR
*Noisy* relationships can categories logical relationships. This one generalizes the logical OR. We might say a $Fever$ is true if $Cold$, $Flue$ or $Malaria$ is true.  With *noisy-OR* we can add uncertainty about the value of each parent's effect on the child ($feveer$). For example $Cold$'s effect on $Fever$ could be *inhibited*. 

With this relation we assume all the possible causes are listed (and can add a catch all *leak node* if we don't know them all) and we assume the inhibitors for the different parents are independent which may be the case for many parents. Then the child is false iff all its parents are inhibited. Then in this case we only need 3 probabilities.

![[Pasted image 20220411183625.png]]

We we have the following rule to calculate the probabilities of the full *JPT* hence we have a linear time.

![[Pasted image 20220411184245.png]]

#### Continous Variables
A continuous variable has an infinite number of variables so we can't specify the probability for all. We can perform *discretization* and assign each value instead to a range/interval. But we loose accuracy and may end up with a large domain to account for this. Or we can use a function that is defined by *parameters* these describe a standard family of functions. Like for example the *normal distribution* or a *uniform distribution* but we can also define *probability density functions* for this and add our own parameters to affect them. We can also use a *nonparametric* solution where we defined these distributions individually for each conditional case.

A network with both discrete and continuous variable is called a *hybrid Bayesian network*. We need to define the continuous distributions with continuous parents, discrete distributions with continuous parents and continuous distributions with discrete parents.

## Exact Inference In Bayesian Networks
In *inference* we have a basic task. We want the posterior probabilities of some *query variables* given some observed *event*, which is some assignment of values to *evidence variables*. We have the query variable $X$ the evidence variable $E$, the event $e$ and the other variable $Y$ (*hidden variables*). Then all the variables are $\{X\cup E\cup Y\}$. We then want $\textbf P(X|e)$. We will cover an exact algorithm to calculate this but it becomes intractable so there are approximate inference methods latter on.

**Inference By Enumeration** - This is one approach. Any query can be computed give the JPD values. That is $\textbf P(X|e)$ can be calculated as
$$
\textbf P(X|e)=\alpha\textbf P(X,e)=\alpha\sum_y\textbf P(X,e,y)
$$
All the $\text P(X,e,y)$ terms can be given as products of the CPT entries hence we can calculate them. Hence with the burglary example we may want the following

![[Pasted image 20220411191115.png]]

Which becomes this after the *chain rule*

![[Pasted image 20220411191142.png]]

Here we also move parts around such that we are multiplying the least number of times. We can show this structure in a graph where each split is for a sum over different values.

![[Pasted image 20220411191314.png]]

We can also give the **enumeration ask** algorithm that work following this equation.

![[Pasted image 20220411191607.png]]

**Variable Elimination Algorithm** - This improves on enumeration by eliminating repeated calculations. We split our equation into a series of matrix multiplications turning this into a dynamic programming method for solving the problem.

![[Pasted image 20220411192101.png]]

This is as we reuse the later factors $f_5$ and $f_4$ many times. The arguments into the matrix are how we index into it. So $f_3$ is indexed by 3 variables and $f_4$ and $f_5$ are indeed by 1 (so they are vectors).

![[Pasted image 20220411192405.png]]

We rewrite the equation as follows where $\times$ means pointwise product and not matrix multiplication.

![[Pasted image 20220411192438.png]]

We can some over some values to remove it form a combination of factor. This yields a new factor. We continue like this until we get our final factor which is normalized to get our result.

![[Pasted image 20220411192847.png]]

This shows one such expansion.

To perform a *pointwise factor* we just need to have two matrices that are indexed into by some combination of variables. The variables indexing into the new matrix is the *union* of the original two. 

![[Pasted image 20220411194139.png]]

The number of entries is the product of the size of the domain for each variable. So if they're binary its $2^m$ where $m$ is the number of variables. For each combination giving an entry the value in the entry is the product of the corresponding entries in the original matrix.

![[Pasted image 20220411194359.png]]

To perform *summing out* of a variable we just split the matrix into $m$ matrices for a domain size $m$. Then these matrices each correspond to a given value in the domain of the variable being summed out. We then reduce this variable from being able to index into the matrix.

The final algorithm is given as

![[Pasted image 20220411194813.png]]

The ordering we eliminate the variables in determines the size of the matrices we need to keep track of. To find the best order is intractable but we can do well with heuristics. Like for example by always eliminating the variable that will reduce the size the most (greedy method). We may also find ourselves summing out to a nonindexed matrix which is just 1. In this case we can remove this as the result will be the same.

The *efficiency* of a network depends on the structure of the network. For example in a *singly connected network* or *polytree* where there is only one path between any two nodes. Has complexity that grown linearly with the size of the network where the size of the network is the size of the CPT entries. We can also have *multiply connected networks*
where there are multiple paths. Inference in these networks is $\#P-hard$ problem an order above NP-hard.

If we want the posterior probabilities for $n$ variables it will take $nO(n)$ time. This can be reduced to just $O(n)$ time with *clustering algorithms* also called *join tree* algorithms. These are used in commercial Bayesian network tools. We join nodes in the network together so that the final network is a polytree. Hence we will have to calculate all posterior probabilities on the path to some final node hence it grown in time $O(n)$ if a polytree does.

## Approximate Inference in Bayesian Networks
Now that we have looked at how to do true inference we see that is it intractable so instead we require approximate methods to give good enough results. Here *Monte Carlo* or randomized sampling algorithms are used to give approximate answers, the accuracy depends on the number of samples generated hence scales with compute.

**Direct Sampling** 
If we generate samples for each variable in topological order we can for each variable take in its parents (which are already generated) and generate the next value given the distribution described in the CPD.  This gives the following algorithm for one sample.

![[Pasted image 20220411201458.png]]

These samples will be as likely as their corresponding entries in the JPD as we increase the number of samples. The correctness can be seen easily as the probability as sample is generated is

![[Pasted image 20220411201743.png]]

 Since this is true we say this algorithm generates *consistent* samples: any estimate of probability will approach the true probability for large samples. The probability of some value in the output we can count the number of times each value appears in our samples the divide this by the number of samples to get our final value.  Here $N_{PS}$ is the number of times the given sample was generated ($X_1=x_1,...X_n=x_n$)

![[Pasted image 20220411201931.png]]
 
**Rejection Sampling**
Here we use the *direct sampling* method given above to generate samples. We however want conditional probabilities this time. So we throw away any sample that doesn't match our preconditions. We can then find an estimate of the probability our value occurs by dividing the number of times we observe it by the number of restricted samples.

![[Pasted image 20220411202708.png]]

The standard deviation in the answer with both these methods will be $1/\sqrt n$ where $n$ is the number of samples used (after restriction). This is the problem with rejection sampling, if we get very rare preconditions we will need to generate fare more samples as we need to make up for rejecting so many.

**Likelihood weighting** 
This avoids the inefficiencies of rejection sampling by generating only event which fit our preconditions. It is a generalization of *importance sampling* which is in general used for statistics. We weight each sample based on the probability we would have observed the evidence variable given our current working sample values. 

![[Pasted image 20220411203820.png]]

The problem here is that the values will become vanishingly small with rare events. Instead we can encode with negative logs and add the corresponding value instead of multiplying small numbers. The weighting gives the following formula for the probability of getting some sample.

![[Pasted image 20220411204430.png]]

This gives the correct estimates we want for when we weight up all the sample we generate, hence it is *consistent*.

**Markov Chain Simulation**
*Markov chain Monte Carlo* works differently to the other techniques above. Here we generate some new sample by making random changes to our previous sample. We therefore things of the algorithm as having a state for the network it is working with. We will look at *Gibbs sampling* which is designed to suite Bayesian networks. We start with some random but we can fix evidence variables to whatever value we want. The next state is done by randomly sampling for the non-evidence variables. The distribution is calculated form the *Markov Blanket* which we have since all variables are given. We then continue to sample over and over again.

![[Pasted image 20220411210449.png]]


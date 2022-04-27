# Quantifying Uncertainty
Since we cannot actually know for sure the outcome of any action or even what state we are in we need to incorporate ways to act under this uncertainty and to represent it. In [[Beyond Classical Search]] we used a *belief state* for this. The drawbacks of this are

1. We have to consider *every* possible state given inputs
2. Our plan can grow to any size if we consider any number if contingencies (which may be very unlikely, meteorite)
3. We still need to act even if we can't ensure we meet the goal.

If there are things we can't deduce for sure that our plan depends on then its success cannot be inferred this is the **qualification problem**.

## Acting Under Uncertainty
If we want to act under uncertainty we need to get over the qualification problem can work with a *likelihood* that some plan will work. The plan may have a change of affecting and feature we care about in the environment and so our performance measure. The *rational* thing depends on the importance of the features and how likely they are given our plan.

We can try to quantify uncertainty with FOL if we do this say something causes pain. Then we may write
$$
Pain\implies Thing
$$ But this isn't true as many things cause pain. So maybe we write 
$$
Pain\implies Thing_1 \lor Thing_2\lor Thing_3...
$$
But this will go on for ages we cannot quantify the number of things that *could* cause pain. We could flip it around and say
$$
Thing \implies Pain
$$
But what if it only sometimes causes pain? Again we need all the things that cause pain. We cant use this as it is too much work, we may not know all the causes it could be and in a given situation we may not have the state of all the causes. To deal with degrees of belief we will use *probability theory*. We can instead describe how likely something is to cause another with a probability between 0 and 1. We can use a probability if we reason with respect to a *knowledge state* and not the real world as in the real world things are either true or false. We ask what is the probability of $this$ *given* $that$.

### Rational Decisions
We have have different plans that have a high likelihood of succeeding. We need to weight them up with both how likely they are and how much we *prefer* the plan. Our agent therefore needs **preferences** between the different possible **outcomes** of our plans. The outcome are true states with definite values describing them. **Utility Theory** is used to for our preferences and to reason about them, where the utility is the degree of usefulness of a state. Both *utility theory* and *probability theory* are combined to give **Decision theory**.

![[Pasted image 20220410214505.png]]

---

*A **rational** agent is **rational** iff it choses the action that yields the highest expected utility, averaged over all the possible outcomes of the action*

---

## Basic Probability Notation
In probability theory the set of all possible worlds is called the *sample space* all the worlds in it are mutually exclusive and exhaustive. Then $\Omega$ is all the worlds and $\omega$ is a single world.

A *probability model* associates a numerical probability $P(\omega)$ with each possible world. Then we have the basic axioms of probability theory which says that the total probability of all worlds is 1 and every probability is between 0 and 1. So $0\le P(\omega)\le 1$ and
$$
\sum_{\omega\in\Omega}P(\omega)=1
$$
We don't just care about single worlds but *events* which is a set of possible worlds we can give a probability that is for us ending up in any of these worlds. That is for an event $\phi$ its probability is defined as
$$
P(\phi)=\sum_{\omega\in\phi}P(\omega)
$$
A probability that isn't conditioned on something like $P(doubles)$ is called a *unconditional* or *prior* probability. If we incorporate evidence we get a *conditional* or *posterior* probability. They are defined mathematically as

![[Pasted image 20220410220020.png]]

This can also be written as the *product rule*

![[Pasted image 20220410220105.png]]

We will use states described by sets of elements as in [[Beyond Classical Search]] etc. a *factored representation* and not a *atomic one*. Hence we have variables in *probability theory* these are called *random variables* as they change in the possible worlds. Every RV has a *domain* the set of values it can take. We then define the probability the RV takes a given value $x$ for RV $X$ as $P(X=x)$ and for logical variables $P(X)=P(X=true)$ and $P(¬X)=P(X=false)$. We can also factor a probability into a vector as for a $weather$ state.

![[Pasted image 20220410220913.png]]

Can be written as

![[Pasted image 20220410220926.png]]

A variable holds in a world if as we defined the world as a matching of variables to values, there is a higher order match to our random variable. We define a *joint probability distribution* as the probability of any combination of random variables. So the JDP of $X$ and $Y$ defines the probability of each combination of the two. A *full joint probability distribution* is this for all variables so therefore defines how probable every state of the world is.

## Inferences Using Full Joint Distributions
We will go over a simple method for *probabilistic inference*, that is the computation of posterior probabilities for queries propositions given observed evidence. The joint distribution then describes our knowledge about the functioning of the world. A simple way to do this is to find all the probabilities that are our query is true in and sum them together. A *marginal probability* can be extracted and gives the probability distribution for a single variable. When we do this we sum up the probabilities for every value of the variable in question. This process it called *marginalization*.

Another for of this rule is called *conditioning*. Here we what the probability distribution of a variable given some other variable is already true. In this we consider only the worlds in which the conditioning variable has its assigned value. Then we scale up all the probabilities proportional as this will take up some fraction of the overall probability. Since it is a constant and also always scales up the probabilities left to sum to one we can leave the calculation out and just sum later to make all probabilities 1 this is called *normalization*. We use $\alpha$ as this factor. This gives our overall inference.

![[Pasted image 20220410224711.png]]

Here $X$ is our query variable $e$ is our evidence and $y$ is the other variables. We sum over all the $y$ to pull them all together into one probability that gives the distribution if they weren't modeled. Since $X\cup e\cup y$ is all the variables $\textbf{P}(X,e,y)$ is just defined by the **JPD**. The problem is with more variables the size of the JPD grows at $O(2^n)$ 

## Independence
Independence describes a special case of the probability distribution where the value of a query variable stays the same no matter the value of another it is conditioned on. It could be something like

![[Pasted image 20220410225350.png]]

The weather doesn't depend on dental health. Using relationships like this we can decompose the JPD into smaller pieces then the size will not grow as fast asymptotically. If $a$ is independent of $b$ then

![[Pasted image 20220410225529.png]]

And equally for $X$ and $Y$

![[Pasted image 20220410225547.png]]

These decompose larger JDPs the most striking example would be fully independent RVs where we could fully decompose. The only issue is this breaks with the sliest interference so can be hard to maintain in the real world.

![[Pasted image 20220410225715.png]]

## Bayes' Rule
Bayes' rule can be derived from the product rule and is written as follows.

![[Pasted image 20220410230004.png]]

This rule underlies most of AI systems probabilistic inference. This can be expanded to a multivariable for with evidence and other variables.

![[Pasted image 20220410230120.png]]

The idea is that this can be used to switch the direction of inference. That is if we have $P(cause|effect)$ if we know the probability of cause and effect we can get $P(effect|cause)$ so we can get from a *causal* relation a *diagnostic* relation.

[[Quantifying Uncertainty Questions]]
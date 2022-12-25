We already know the definition of independence $x$ and $y$ are independent if $p(x,y)=p(x)p(y)$. This is equivalent to $p(x|y)=p(x)$. This is denotes as $x\perp y$. Many variables can be independent together in which case we write $\{x_1,\dots,x_n\}\mathrel{\unicode{x2AEB}}\{y_1,\dots,y_m\}$ then

![[Pasted image 20221114151703.png]]

So its just the same but with sets. Independence implies that probability can be **factorized**. For example supposing we have $x\in\mathcal X$, $y\in\mathcal Y$ and $z\in\mathcal Z$. If $\{x,y\}\_z$ then

![[Pasted image 20221114151911.png]]

We can say we want to to make expressions simpler. This is as the **domains** are smaller, combinatorically. That is $\mathcal X\times\mathcal Y\times\mathcal Z$ is much smaller than $\mathcal X\times\mathcal Y$ and $\mathcal Z$.

### Mutual independence
Variables $x_1$, $x_2,x_3$ are mutually independent if

![[Pasted image 20221114152105.png]]

This implies pairwise independence that is $x_1$ is independent of $x_2$ (1 to 3, 2 to 3) but this doesn't imply **mutual independence**. Mutual independence implies pairwise independence but not the other way around!

### Conditional Independence
We say $x$ and $y$ are conditionally independent given $z$ if

![[Pasted image 20221114152259.png]]

We say $x\_|y|z$. This can also happen with sets of variables giving  

![[Pasted image 20221114152341.png]]

### Testing Independence
We can test for independence by using **marginalization**, to test the first equation above we would test

![[Pasted image 20221114152605.png]]

(where sums are replaced by integrals for continuous $x$ and $y$) Then we check if 

![[Pasted image 20221114152630.png]]

We could check all of the triplets of the variables but this would be slow. Hence in general it is hard to test for independence.

## "Chain rule" of conditional probabilities
Any joint probability $p(x_1,x_2,...,x_n)$ can be favorized in any order for example

![[Pasted image 20221114152815.png]]

or 

![[Pasted image 20221114152845.png]]

We can pick whatever order of $x_i$ variables we want to unroll giving the sequence of probabilities above.

### Applying independence (Scenario)

1. Every Thursday there is a alarm testing (t)
2. The alarm (a) goes of when there is fire (f)
3. If the alarm goes off, people in the building meet at the front door (g) on the ground floor
4. People gather in the building if there is a strike (s)

We can see there is independence conceptually.  The alarm testing is independent of the fire (t and f). A strike is independent of what happens in the building (s is independent of {a, f, t}). People gathering is independent of fire and alarm testing if we know whether there is a strike (as we know people with gather anyways) that is g is independent of {f, t} given s and a. Combining this we get

![[Pasted image 20221114153413.png]]

### A (directed)  graph representation
We could represent the above as

![[Pasted image 20221114153907.png]]

Each vertex is a variables, a parent has edges pointing from children to itself. The graph is directed (giving the children, arrows from parents to children) an acyclic. The probabilities are for the child given the parents. We can go down the graph to get the distribution as

![[Pasted image 20221114153940.png]]

A distribution **factorizes according to the graph** if

![[Pasted image 20221114154010.png]]

That is we can write the joint probability in the form described by the graph. The graph describes a **factorization** not the actual variables.

The two objects the **distribution** and the **graph** only interact when we factorize the distribution. But they are not the same.

### Basic structures
We want to understand how the structure of the graph affects the probability space the graph describes. So will will look at basic cases in hopes of budling up to more complicated graphs.

![[Pasted image 20221114154540.png]]

**Chain** just points to the next variable we can show that $x$ is independent of $z$ if we know $y$.

![[Pasted image 20221114154651.png]]

**Common cause**  means that a variable is parent to two others. This causes $x$ and $z$ to be independent if we know $y$

![[Pasted image 20221114154755.png]]

**v-structure** (common effect) means some RV is caused by two other RVs. If this is true then $x$ is independent of $z$, but if we know $y$ they aren't independent.

![[Pasted image 20221114155052.png]]

The other part can be proven by contradiction. We assume $x\_|z|y$ we say if that is true then

![[Pasted image 20221114155819.png]]

But if we take $x$ and $y$ to be independent then

![[Pasted image 20221114155842.png]]

Within the sum we are given $y$. All triplets must be the same so $p(x)$ and $p(x|y)$ must be the same. But this would mean $x$ and $y$ are independent which contradicts our graph in the first place.

### Descendants v-structure
We can have the case in our graph that

![[Pasted image 20221117123321.png]]

Where $d$ is a descendent of $y$ at some points. This structure means $x$ and $z$ aren't independent if we are given any descendent of $y$.

### Separation
From the structure above we can derive the idea of **blocking**. For example in the case

1. $x\to y\to z$ we say is **blocked** given $y$.
2. $x\leftarrow y\to z$ is **blocked** given $y$.
3. $x\to y\leftarrow z$ is **blocked** if $y$ and its descendants are not given.

The idea of blocking means dependence is blocked.  Hence the flow of dependencies is blocked. Two variables are **separated** if all paths connecting the two variables are blocked. This extends to sets as well. 

* Two sets of variables $X$ and $Y$ are independent given a third $Z$ if all pairs in $X\times Y$ are separated given $Z$.

The graph doesn't imply anything directly about the probability distribution.

### Independencies in the two objects
**Separation** on the graph implies *independence* in the distribution that factorizes according to a graph. However separation doesn't necessarily include all independencies in the distribution that factorizes according to the graph. But usually this doesn't happen.

### Naïve Bayes
Here our task is to predict $y$ given $d$ features $x_1$, $x_2$, ... , $x_d$ ($\textbf x$ vector). We suppose $x_1,x_2,...,x_d$ are **mutually independent** given $y$ (key assumption). $$p(x_1,x_2,\dots,d_d,y)=p(y)p(x_1,\dots,x_d|y)=p(y)\prod_{i=1}^dp(x_i|y)$$ With the final step occurring due to our key assumption. Using bayes rule we can get the probability of $y$ given the features

![[Pasted image 20221117152632.png]]
When we have a data set ($\{(x_1,y_1),...,(x_n,y_n\}$) we train the naïve Bayes classifier with the log loss

![[Pasted image 20221117153358.png]]

Hence we maximize the likelihood of our data given our probabilities ($p(x_i|y)$ and $p(y)$).

[[Statistical Dependencies 1 Questions]]
### Long Range Dependencies
Often in language the form of words depends on words that are arbitrarily far away.

![[Pasted image 20230303121617.png]]

Generally it isn't massive but still much further than the shortest dependencies.

### Phrase Categories
We can think of the **categories** of phrases. We look at the **substitutability** as we would with phrase level tags. With POS categories for example **adjectives**:

![[Pasted image 20230303121851.png]]

**Phrasal categories** act in the same way but over entire **phrases** are substitutable. For example **noun phrases**:

![[Pasted image 20230303121939.png]]

This is one example of a **constituency test**.

##### Coordination
This is another test for constituency. We use this to identify phrases. The idea here is if we can combine a phrase with a conjunction we have identified that phrase as the same category as the other phrase

![[Pasted image 20230303122147.png]]

A failure case would look like

![[Pasted image 20230303122213.png]]

We conjoin with a phrase that could be substituted in the same place while making sense.

##### Clefting
Here we use a template "__ is/are who/what/where/when/why/how"/ We takes our phrase and rearrange this to come before the template.

![[Pasted image 20230303122443.png]]

A failure would look like

![[Pasted image 20230303122455.png]]

### Theories of Syntax
A **theory of syntax** should explain which sentences are *well-formed* and which are not. A well formed sentence is **district form meaningful**. A famous example of a well-formed by not meaning full sentence is

![[Pasted image 20230303122759.png]]

But syntax can help interpret meaning.

The two theories we will look are are CS and DS.

### Constituency (aka phrase) structures
Here the first layer will be **words** then the second layer is **POS** tags. Beyond this we have *phrasal categories*.

![[Pasted image 20230303122954.png]]

![[Pasted image 20230303123011.png]]

### Context-Free Grammar
Context-free grammar is a tuple of 4 elements. We have $V$ as non-terminals, $\Sigma$ is the set of terminals. $R$ is the set of rules from $X\to Y_1,Y_2,\dots Y_n$ where $n\ge0$ Then $X\in V,Y_i\in V\cup \Sigma$ so a terminal to a sequence of terminals and non-terminals. $S$ is defined as the dedicated start-symbol.

##### Example Grammar
We can have **inner rules** which take non-terminals to non-terminals. Then **preterminal rules** which are like emission rules and take non-terminals to terminals.

The CFG defines are set of strings (a language of well formed sequences). It also defines the structures used to represent sentences (constituent trees)

##### Structural Ambiguity
Some sentences have more than one parse: this gives **structural ambiguity**.

![[Pasted image 20230303123713.png]]

Here this is caused by PoS ambiguity but many cases done even come from this but instead are **attachment ambiguity**. Here this depending on where the different phrases attack in the tree. Different attachments give different meanings.

![[Pasted image 20230303123836.png]]

##### Prepositional Phrases (PP-) Attachment Ambiguity![[Pasted image 20230303123932.png]]

##### Why Context-Free
In a context-free grammar what can be in a sub-tree is only affect by what the phrase type is (VP for example) but not the **context**.

Context free grammars also allow us to build up possible syntax trees for the grammar in a simple way.

### Key Problem
Once we have defined the grammar we can look at

**Recognition problem** which defines if the sentences belongs to the language which is defined by a CFG.

**Parsing problem** what is the most plausible derivation corresponding to a sentence (this encompasses recognition)

# Parsing Algorithms
Here we want to compute the structure for an input string give a grammar. This can then help us get meaning but we have to get around ambiguity.

**For correctness** - we need to find the right structures to get the right meaning
**For efficiency** - we cannot search all possible structure as this can be very slow.

![[Pasted image 20230303124412.png]]

### Parser Properties
All parsers have two fundamental properties:

**Directionality**: the sequence in which the structure are constructed this could be 
	1. **Top-down** - start with $S$ and choose expansions to get to words
	2. **Bottom-up** - start with words and built up to $S$
	3. **Mixed** - also possible and can give more complex. We can start with *left-corner* which goes the same way humans parse sentences.

**Search strategy** - the order in which the search space of possible analyses is explored.

##### Top Down Parser
Here we start with $S$ and look for different possible way to expand giving a sentence

![[Pasted image 20230303124709.png]]

This will be our **search space**, then we can look at different search strategies like **depth-first search**, where we build out sentence as far as possible if this branch doesn't work out we go back. **Breadth-first** we simulate all possible parses are once (can require a lot of memory). [[Search]] 

*Note:* these two are generally combined with pruning to get cut the number of possibilities.

**Best-first search** if we we also have a score we can use this to search some cases first.

# CYK algorithm
This is a **bottom up** parsing algorithm for CFGs. This was very popular and in fact is generalizable to probabilistic modeling.

The basic CKY algorithm support only rules in the Chomsky Normal Form (CNF), these must be either **preterminal rules** (emissions) or **binary inner** rules. But every grammar can be converted to CNF. That is they define the same language, but the trees will look different. But we can later reverse this transformation on the final tree.

##### Convert to CNF
ere we get rid of empty ($\epsilon$) productions, then we remove unary rules. These are both simple. We also need to remove $n-ary$ rules. For example with the expansion

![[Pasted image 20230303125519.png]]

We break this down so we gradually apply the rule with intermediate states. For example

![[Pasted image 20230303125608.png]]

Generall more structure forms are used like:

![[Pasted image 20230303125640.png]]

But we can undo this transformation once we have a final tree. This conversion is known as **lossless Markovization** in the context of PCFGs.

# Syntax Part 2
in **parsing** we are given a grammar $G=(V,\Sigma,R,S)$ and a sentence of words $\mathbf w=(w_1,w_2,\dots,w_n)$. Our goal is to produce a parse tree for $\mathbf w$. We need an easy way to prefer to strings. The sequences are given by offset sequences as in

![[Pasted image 20230307121715.png]]

So $span(i,j)$ refers to the words between $i$ and $j$.

### Key problems
The **recognition problem** checks if a sentence belongs to the languages defined by the CFG. Then the parsing problem also gives the (tree). The simplest case would be parsing **one word**. Here the rules $C\to w_i$ will allow any word to be parsed to a non-terminal (which is required for CNF)

![[Pasted image 20230307121946.png]]

Now we want to parse larger sentences $C\to C_1 C_2$. We look for a rule in this form, if there is such a rule we can apply it. But there are many parsing for the subtrees (we can split them differently)

![[Pasted image 20230307122122.png]]

### Signatures
Applications of rules are independent of inner structure of a parse tree. We only need to know the corresponding span and root label of the tree.

### CYK idea
Here we compare for every span a set of admissible labeles. These are give by some midpoint for the lower span. We start with small threes and build up to larger ones. When done we check if $S$ is among the admissible labels of the whole sentence if it is the sentence belongs to the language.

![[Pasted image 20230307122543.png]]

Different squares give the tree bellow them. Hence the order we full it in starts with subsentences of length 1 and then 2 and so on.

![[Pasted image 20230307122658.png]]

### Starting with words
First we can parse the single length sentences with emission rules then **unary rules**.

![[Pasted image 20230307122848.png]]

### Moving up
First we apply binary rules, checking all possible rules.

![[Pasted image 20230307123104.png]]

### Finishing
With more complicated rules we check the possible **midpoints** that give the two subtrees we would break the sentence down to. For example 4 and 3 or 1 and 5. Infact we can get $S$ multiple ways giving multiple **ambiguous** interpretations

![[Pasted image 20230307123247.png]]

The interpretations can be seen as 

![[Pasted image 20230307123308.png]]

### CKY Formally
In genera we will build a chart $chart[\min][\max][c]$. The relevant entries have $0\le\min<\max\le n$.

##### Preterminal rules are simple
![[Pasted image 20230307123446.png]]

##### Binary rules: more complicated
These are more complicated as we have to check possible midpoints

![[Pasted image 20230307123528.png]]

##### Unary Rules
We can also integrate unary rules into this.  Simply after applying unary and then binary rules we add unary rules.

![[Pasted image 20230307123646.png]]

This misses out **unary closure** as unary rules can lead to new unary rules. In general we compute a closure of these rules, where we add in new rules that would skip out any intermediate states.

![[Pasted image 20230307123836.png]]

But this can mess with **probability** parsing and we must also keep track of which rules work this way.

### Skeleton Implementation
![[Pasted image 20230307123939.png]]

In general this will have time complexity $O(n^3c)$. For a sentence of length $n$ and grammar size $c$. These can also be run faster using a matrix implementation on GPUs.

## Dealing with Ambiguity
There are exponentially many derivation for a typical sentence.

![[Pasted image 20230307124356.png]]

We want to **score all derivations** to encode how plausible they are. For this we need a **probabilistic CFG**. We associate probabilities with the rules $p(X\to\alpha)$. We need to ensure the axioms of probability apply and so we want all rules for a given non-terminal to sum to one. 

$$\forall X\to \alpha\in R: 0\le p(X\to\alpha)$$ $$\forall X\in N: \sum_{\alpha:X\to\alpha\in R}p(X\to\alpha)=1$$
This simple addition allow scoring of trees. 

![[Pasted image 20230307124619.png]]

### Distribution over trees
We define a distribution over **production rules for each nonterminal**. Our goal was to define a **distribution over parse trees**. 

![[Pasted image 20230307124733.png]]

But luckily with maximum likelihood procedure they are always proper.

We say $G(x)$ is the set of derivation for the sentence $x$. The probability distribution defines the scoring $P(T)$ over the trees. $T\in G(x)$. Finding the best parse for the sentence according to PCFG

![[Pasted image 20230307124918.png]]

### ML estimation
Here we have a **treebank** a collection of sentences annotated with constituent trees

![[Pasted image 20230307125204.png]]

For this we apply the rule

![[Pasted image 20230307125237.png]]

Smoothing may also be applied to get around sparsity in the data.

##### Examples
As an example we can take the **toy treebank** as follows:

![[Pasted image 20230309165454.png]]

Then the differen't rule's probabilities are given as

![[Pasted image 20230309165527.png]]

##### Penn Treebank
Penn Treebank is a treebank for the WSJ is contain around 40,000 annotated sentences with 1,000,000 words. It has **fine grain** POS tags (45) for example with verbs

![[Pasted image 20230309165736.png]]

Then it also have flat NPs like

![[Pasted image 20230309165755.png]]

### Probabilistic Parsing
We discussed the recognition problem, checking if a sentence is parse able with a CFG. Now we can look how how we may recognize what is the probability of the most probably parse tree. Now we perform a similar to performing Viterbi. We look in each subtree for the most probable parse for each non-terminal. So $chart[0][n][S]$ will store the best probability for a given node.

![[Pasted image 20230307125638.png]]

##### Preterminal rules

![[Pasted image 20230307125659.png]]

##### Binary Rules

![[Pasted image 20230307125725.png]]

### Unary Rules
Similarly to CFGs: after producing score for signatures $(c,i,j)$, we try applying unary rules (and rule chains).

![[Pasted image 20230307125840.png]]

Technically this breaks this being a PCFG but for CKY this doesn't matter.

### Recovery of the tree
For tree recovery for each signature we store a back pointer to show the best (most probably node) it came from. But this can get complicated with unary rules.

### Speeding up the algorithm (approximate search)
We can perform **basic pruning** where for each span (i,j) store only labels which have the probability most $N$ times smaller than the probability of the most probable label for this span.

We can check not all rules but only rules yielding subtree labeles having non-zero probability

We can also perform **coarse-to-fine-pruning** where we parse with a smaller (simpler) grammar and precompute posteriors probabilities for each span. Then we only use the ones with non-negligible probability from the previous grammar.

This basically rules out the worst possible nodes.

[[Syntax and Parsing Questions]]
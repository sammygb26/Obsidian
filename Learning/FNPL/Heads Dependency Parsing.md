A problem with standard PCFGs is there is no lexical dependencies. For example the following are treated the same. As the POS tags given are the same.

![[Pasted image 20230310121330.png]]

We can produce splits of POS tags but this is often not enough as per the above examples. For example here we would add a information about kinds of objects to POS tags.

# Lexicalization
Here we create new categories this time by adding the **lexical head** of the phrase.

![[Pasted image 20230310121539.png]]

Then if we consider 

![[Pasted image 20230310121559.png]]

And we see that we can now discriminate between rules makes sense and those that don't.

### Practical Issues
All this category-splitting makes the grammar much more **specific** but this leads to huge grammar blowup and very *sparse data*. Lost of effort on how to balance these two issues has been made. 

- Complex smoothing schemes (similar to N-gram interpolation/backoff)
- More recently, increasing emphasis on automatically learned subcategories.

### Lexicalization Constituency Parse

![[Pasted image 20230310122035.png]]

We can remove phrasal categories from the tree as follows

![[Pasted image 20230310122058.png]]

We can also remove duplicate terminals

![[Pasted image 20230310122122.png]]

Then collapsing duplicates gives

![[Pasted image 20230310122147.png]]

This is called a **dependency parse**.

## Dependency Parse
![[Pasted image 20230310122230.png]]

Linguists have observed that the meaning of words within a sentence depend on another, mostly in asymmetric, binary relations. Some construction don't clearly fit this patters like *coordination* and *relative clauses*. The tree structure shows how these relations are applied.

Equivalently, but showing the word order (head -> modifier)

![[Pasted image 20230310122447.png]]

### Content vs. Functional Heads
Some treebanks prefer **content heads**. Here the head is a noun.

![[Pasted image 20230310122515.png]]

While some prefer **functional heads**. Here the functional work is the head so here with is the head.

![[Pasted image 20230310122530.png]]

So we can create structures in different ways.

### Edge Labeles
It is often useful to distinguish different kinds of head -> modifier **relations** by labeling the edges.

![[Pasted image 20230310122700.png]]

Important relations for English include *subject*, *direct object*, *determiner*, *adjective*, *modifier*, *adverbial modifier* etc.

### Dependency Paths
For **informational extraction** tasks involving real-world relationships between entities, chains of dependencies can provide good features.

![[Pasted image 20230310122836.png]]

### Projectivity
A sentence's dependency parse is said to be **projective** if every subtree (node and all its descendants) occupies a contiguous span of the sentence. This is the same as the dependency parse being drown on top of the sentence without any crossing edges.

![[Pasted image 20230310123010.png]]

Other sentences are **non-projective** like

![[Pasted image 20230310123034.png]]

Non-projectivity is rare in English but common in many languages. This can also be called **planarity**.

# Transformations
We saw how the **lexical head** of the phrase can be used to collapse down to a dependency tree.

![[Pasted image 20230310123253.png]]

But how can we find each phrase's head in the first place.

The standard solution is **head rules**. For every non-unary (P)CFG production we designate one RHS nonterminal as containing the head. This would give

![[Pasted image 20230310123418.png]]

Heuristics to scale this to large grammars e.g. with an NP immediate N child is the head. After the rules are found we propagate the head up the tree.

![[Pasted image 20230310123526.png]]

We assume the **head rules** are given.

# Direct Parsing
Some algorithms you have seen for PCFGs can be adapted to dependency parsing. This skips out making constituency trees then converting.

- **CYK** can be adapted through efficiency is a concert one way takes $O(Gn^5)$ while Eisner algorithm brings it down to $O(Gn^3)$.
- **Shift-reduce** - a more efficient and doesn't require a grammar.

## Transition Based Parsing: Shift Reduce Parser
![[Pasted image 20230310123852.png]]

There are different version of **transition based parsing algorithms**. We always have a **stack** and a **buffer**. The stack contains elements we have already started to parse. The input buffer contains words we haven't started to parse. The algorithm moves inputs from the buffer to the stack and outputs dependency relations in the process. There are three possible actions that can be taken.

1. **Left arc** - This assigns head-dependent relation between $s_1$ and $s_2$ then $s_2$ is pop
2. **Right arc** - Assign head-dependent relations between $s_2$ and $s_1$ then we pop $s_1$.
3. **Shift** Here we put $w_1$ on top of the stack.

This is enough to parse all **projective trees** but this cannot deal with non-projective trees.

### Example
![[Pasted image 20230310124340.png]]

So if we follow this order of action we would get the above tree.

### Transition-Based Parsing
We have a model that could give the dependency parse. But we need a model. We train a **classifier** to predict the next action ($Shift,\space LeftArc,\space RightArc$), an proceed left-to-right through the sentence in $O(n)$ time complexity!

This can only fine **projective** trees (without special extensions). For this new actions are added but this performs poorly.

### Graphs-Based Parsing
The idea here is the from the full connected directed graph of all possible edges choose the best ones that form a tree. 

**Edge-factored** models: Classifier assigns a nonnegative score to each possible edge **maximum spanning tree** algorithms find the spanning tree with highest total score in $O(n^2)$ time.

![[Pasted image 20230310125038.png]]

This doesn't make assumptions about projectivity.

### Graph-based vs. Transition-based vs. Conversion-based
**Transition based** - Feature in scoring function can be looked at in any part of the stack; no optimality guarantees for search; linear-time (classically) projective only.

**Graph based** - Features in scoring function limited by factorization; optimal search within that model; quadratic-time; no projective constraint. 

**Conversion based** - In terms of accuracy, sometimes best to first constituency-parse, then convert to dependencies. This doesn't take exponential time as human language is structured in a natural way that reduces the complexity.

### Choosing a Parser: Criteria
![[Pasted image 20230310125521.png]]


Statistical parsing is required to deal with the problem of **ambiguity** in the syntax trees for grammar. Dynamic programing algorithms can successfully compute grammars syntax trees over sentences but can't resolve them.

## Probabilistic Context-free Grammars
This is an augmentation of a CFG. It has parameters

- $N$ - a set of **non-terminals** (or variables)
- $\Sigma$ - a set of **terminal symbols** (disjoint form $N$)
- $R$ - a set of **rules** or productions, each of the form $A\to\beta[p]$, where $A$ is a nonterminal $\beta$ is a sequence of terminals and non-terminals then $p\in[0,1]$ is a number expressing $P(\beta\mid A)$.
- $S$ - a designated **start-symbol**

The probability $p$ just describes when we see $A$ what the chance is it will be expanded to $\beta$. So for all possible expansion of $A$ we will have $$\sum_\beta P(A\to\beta)=1$$A PCFG is **consistent** if the probabilities of all the sentences in that language are 1. This may not be the case if there are looping productions (for example $X\to X$ with a probability 1).

#### PCFGs for Disambiguation
The PCFG assigns a probability to the overall sentence which we can use to disambiguate between interpretations. We want to define our probabilities so the interpretations we expect are more likely. The definition of the probabilities $p$ tells us that for a given parse tree $T$ and sentence $S$ the probability of both $S$ being generated and $T$ being the tree is $$P(T,S)=\prod_{i=1}^nP(RHS_i\mid LHS_i)$$Now a given parse tree can only have one sentence and so $P(T,S)=P(T)P(S\mid T)=P(T)$. If we want to find the most likely tree we are trying to find $$\hat T(S)=\underset{T\text{s.t.}=\text{yield}(S)}{\arg\max}P(T\mid S)$$But $P(T|S)=P(T,S)/P(S)=P(T)/P(S)$ but $P(S) is constant in the argmax and so $$\hat T(S)=\underset{T\text{s.t.}=\text{yield}(S)}{\arg\max}P(T)$$

#### PCFGs for Language Modeling
We can also use a PCFG to give a probability to a sentence. We want the probability that the sentence could have arisen from any possible syntax tree. That is $$P(S)=\sum_{T\text{s.t.}S=\text{yield}(S)}P(T,S)=\sum_{T\text{s.t.}S=\text{yield}(S)}P(T)$$

## Probabilistic CKY Parsing of PCFGs
We can parse the best tree with CKY with only minor alterations. The basic idea is that we will always use the most probable parse for a given subtree non-terminal, if we didn't we wouldn't have the most probable tree. So we can use our upper triangle as with regular CKY (upper triangle of a matrix $(n+1)\times(n+1)$), then each element $[i,j]$ were $i>j$ will be the parse for the span $i$ to $j$. 

For each $|V|$ non-terminal we have an entry in each of the $[i,j]$ cells. If there are multiple rules which lead to the same non-terminal for $[i,j]$ then we use the most probable one.

## Ways to Learn PCFG Rule Probabilities
We still need to find the actual probabilities for this tree. We can use a **treebank** to start with and learn the probabilities from the rule $$P(\alpha\to\beta\mid \alpha)=\frac{\text{Count}(\alpha\to\beta)}{\sum_\gamma\text{Count}(\alpha\to\gamma)}=\frac{\text{Count}(\alpha\to\beta)}{\text{Count}(\alpha)}$$. We can get a treebank if we don't have one by using a parser. But to get the best parse (as the sentence will be ambiguous) we need a probabilistic parser. For this we will need the probabilities which brings us back to where we started. Hence **expectation maximization** is used as often happens with these problems. A special case called the **inside-outside** algorithm (related for forward-backward algorithm) is used.

## Problems with PCFGs
There are two major problems with using standard PCFGs to model and parse language. **Poor independence assumptions** - PCFGs make restrictive independence assumption about the productivity of  non-terminals being independent on the rest of the tree. **Lack of lexical conditioning** -the word content informs the semantic structure not just the other way around! So PCFGs fit to common structures rather than the actual language being used (words).

#### Independence Assumptions Miss Structural Dependencies
When we find the joint probability of a tree and sentence we multiply the probability for each expansion together. This implicitly makes the assumption that the expansions are independent given their non-terminal (left hand side $A\to\beta$). But this actually isn't true. For example **subject** and **object** positions for NP are far more likely to use *pronouns* and *non-pronouns* respectively. The PCFG has no way to represent this discrepancy. **Parent annotation** is one way to do this.

#### Lack of Sensitivity to Lexical Dependencies
The tree is dependent on the letters but only at the leaf productions. We can look at two parses for the sentence "Workers dumped sacks into a bin", one Dumped(sacks, into a bin) the action of dumping results in the sacks being in the bin. The other parse is Dumped(sacks into a bin) where we are dumping the noun "sacks into a bin". This doesn't make much sense so why can't the grammar just resolve it one way or the other. Well this comes down to whether the PP is NP or VP attacked.

In the end this comes down to replacing $$VP\to VBD\space NP\space PP$$with $$VP\to VBD\space NP\hspace{16pt}\text{ and }\hspace{16pt}NP\to NP\space PP$$so depending on the language probabilities either one will always be preferred or the other. The problem is a sentence like "fishermen caught tons of herring" basically has the same attackmen problem VP(caught) or NP(tons) for the PP. In English the correct NP attachment is more likely.

The change comes down to the relation between the verb and the head of the PP. So it could be resolved by having different probabilities based on the head verb and PP head. That is we add in **lexical dependencies**.

This also happens in **coordination ambiguities** for example "dogs in houses and cats" it makes more sense to have the dogs in the houses separate from cats rather than the dogs both in the houses and cats. Of course this is informed by the match between dogs in houses vs dogs in cats. So we need to incorporated the word meaning to get past this.

## Improving PCFGs by Splitting Non-terminals
We can first look at how to incorporate information about position in the syntax tree to get past the poor independence assumptions. One way is **parent annotation** for example $NP$ with a parent $S$ (likely pronoun) can the label $S\hat\space NP$ giving

![[Pasted image 20230422132016.png]]

Now we can have two sets of probabilities for each situation.
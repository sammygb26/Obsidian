In parsing we want to construct a **constituent tree** that matches a given sentence. This can be used to check if a sentence is *grammatical* or for **semantic analysis** of the sentence. For example "Book that flight" we might want this tree 

![[Pasted image 20230420210832.png]]

So in parsing we will be given a **grammar** and will have to find out if a sentence is grammatical and also its parse tree.

## Parsing as Search
We are taking the grammar and using it to guide our search. We could start with the $S$ node and expand until we find a configuration that matches. This would be a **top-down**, goal directed search. Where we are searching to fit some "data" (words). The other options is **bottom-up** where we start with the "data" (words) and search for what fits it. These correspond to **rationalist** (emphasizing prior knowledge) and **empiricist** (emphasizing data).

#### Top-Down Parsing
We can treat each partial derivation of the final tree as a node in this search. We expand nodes by picking the leftmost node (arbitrarily) and expanding it with all possible rules. This gives the next set of nodes. We eventually get POS tags and if they can't match the sentence we can reject this leaf. Of course heuristics can be used and trees that are getting too big to ever generate a sentence can also be thrown away.

![[Pasted image 20230420213347.png]]

The **right** hand side is matched to create the possible expansions.

#### Bottom-up Parsing
Here we start with the bottom level nodes and apply rules, expanding with the possible rule applications as our edges in parsing. This continues until we have reached a rule that comes from the $S$ tag. Unlike top-down parsing we are matching the descendants on the **left** hand side of the rule to our node.

![[Pasted image 20230420214203.png]]

## Ambiguity
When there is ambiguity in the syntax tree for a sentence it is called **structural ambiguity**. There are many sources of it like **attachment ambiguity** for example "I ran over to the man with my ball" the PP "with my ball" can either attack to the VP(ran) or the NP(man) so either the man has my ball or I have my ball.

There are also **coordination ambiguities** for example "the old men and women" is it old men and all different ages of women or old men and women.

Ambiguities can also work their way up from **POS tags**. For example a word might be Noun vs Verb ambiguous leading to multiple parse trees.

The problem this leaves for top-down and bottom up parsers is they must select between many interpretations. But it can be computationally expensive to find all possible parses via search. The number grows exponentially with the size of the sentence! 

**Search** generally can't run in parallel due to memory limitations so a depth first search must be used. This leads to lots of repeated work as failed interpretations of initial words may lead to failure later on. This requires lots of backtracking and is inherent in the grammar (made even words with full larger grammars).

## Dynamic Programming Parsing Methods
Here we construct tables which describe sub-parses of the entire tree. Each possible sub-parse points to its constituents and so from the final $S$ node we can work out way back to reconstruct the tree.

#### CKY parsing
We restrict the grammars to be in **Chomsky Normal Form** (which every grammar can be converted into) as this allows for simplicity in the table leading to efficient computation.

**Conversion to CNF** - So CNF has only two types of rules $A\to BC$ where $A,B$ and $C$ are non-terminals. Then $A\to a$ where $A$ is a non-terminal and $a$ is a terminal. So we 1) Copy all rules to the new grammar 2) Convert terminals within rules to dummy non-terminals, so this basically  removes any mixing of terminals a non-terminals within a production. 3) Collapse any unit productions to their eventual expansions or collapse to their terminal productions. 4) Make all rules binary (binarization) and add them to the new grammar.

To turn this into a parser we can keep track of pointers to the nodes that made up a given sub node. We can then use these pointer to retrace our steps.

## Evaluating Parsers
When we evaluate parsers we don't just evaluate if the parse tree was correct or wrong. Instead we parse the proportion of the **constituents** that are correct or incorrect. We can imagine that parsing a longer sentence give more places to fail. This way of measuring ensures we get more fine grained errors on these longer trees and so can better evaluate the models that parse them against each other. Generally parser are evaluated as compared to **gold labeled** versions. In this case we can compute *precision* and *recall* as 

![[Pasted image 20230422141050.png]]

We say a constituent is correct if the same constituent exists in the gold label parse with the same start point, end point and label. So the correct constituents correctly labels a part of a sentence.

We can then compute the **F-measure** as $$F_\beta=\frac{(\beta^2+1)PR}{\beta^2P+R}$$with $\beta>1$ weighting $R$ more and $\beta<1$ weighting $P$ more. Where this is basically an extension on a weighted harmonic mean.

## Probabilistic Lexicalized CFGs
When we lexicalize we give different probabilities based on the head words of the constituents we generate. We can add in **head words** and **head tags**. Both of these are inherited from child nodes based on the **head rules**.

![[Pasted image 20230422172207.png]]

and entire parse tree for this would look like this

![[Pasted image 20230422172242.png]]

In this case the **lexical rules** will have probability 1 as $VBD(dumped, VBD)\to dumped$ is inevitable. We could then try to estimate these probabilities. For example we could perform

![[Pasted image 20230422172549.png]]

But for many such rules the chance we will actually run into them is very small. One way around this is to have a model generate the rules themselves this way we estimate the parts of the generative model rather than the rules. One example is the **Collin's Parser**. In it we generate constituent from our rule our from the main head constituent $H$. $$LHS\to L_nL_{n-1}\dots L_1HR_1\dots R_{n-1}R_n$$So we begin with the estimate of the **head constituent** then we generate each individual $L_i$ term in order. Then we generate the $R_i$ terms in order. We condition on the head word $hw$, the head tag $ht$, $P$ the parent non-terminal and $H$ the head terminal which we generated first. We will have 3 different probabilities $P_H$ for the head $P_L$ for the left hand expansions and $P_R$ for the right hand expansions.

![[Pasted image 20230422173158.png]]

In general we have a 3 stage sequence to get a probability for a rule as follows. 

1. Generate the head of the phrase $H(hw, ht)$ with probability $$P_H(H(hw,ht)\mid P,H,hw,ht)$$
2. Generate modifier to the left head with total probability $$\prod_{i=1
   }^{n+1}P_L(L_i(lw_i,lt_i)\mid P, H, hw, ht)$$such that $L_{n+1}(lw_{n+1},lt_{n+1})=STOP$. So we stop once we've generated a stop token.

3. Generate modifier to the right of the head with total probability $$\prod_{i=1}^{n+1}P_R(R_i(rw_i,rt_i)\mid H,P,hw,ht)$$such that $R_{n+1}(rw_i,rt_i)=STOP$. So we stop once we've generated a stop token.
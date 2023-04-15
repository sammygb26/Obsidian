This is the most commonly used mathematical system for constituent structure in English. These **Context-Free-Grammars** are also called **Phrase-Structure Grammars**. This is made out of **rules** or **productions** which express the ways that symbols of the language can be grouped and ordered together. There is also a **lexicon** of words and symbols. The following productions express that a Noun Phrase can be a determiner followed by a Nominal or a ProperNoun.

![[Pasted image 20230408131752.png]]

These rules are hierarchically embedded so we combine the following rules with the above.

![[Pasted image 20230408131841.png]]

There are two categories of symbols in the language. There are the *words* in the language called **Terminals** and the symbols that express cluster or generalizations which are called **non-terminals**. In each rule the item to the right of the ($\to$) is an order list of one or more terminals and non-terminals. The left of the arrow is a single *non-terminal*. 

CFGs can be used to generate and parse language. During generation we stats with a given start symbols and the rule $\to$ means we can rewrite the non-terminal to the left as the sequence of terminals and non-terminals to the right. This expansion rule being applied is called a **derivation**. We can get a tree of these

![[Pasted image 20230408132340.png]]

Here we would also say $NP$ **immediately dominates** $Det$ and $Noun$ and **dominates** all nodes below it in the tree. Different rules exist for expanding all non-terminals. For example $PP\to\text{Preposition } NP$ becomes "from Aberdeen". Some other example are

![[Pasted image 20230408151825.png]]

A **lexicon** can therefore be given as

![[Pasted image 20230408151914.png]]

Then the grammar rules can be listed as:

![[Pasted image 20230408152001.png]]

The $\mid$ or symbol is used to denote different possible expansions. To generate a sentence we start with $S$ and pick an expansion rule for it. We then progressively expand the non-terminals until only terminals remain. For example in **bracketed notation** we get\

![[Pasted image 20230408152239.png]]

Then the **constituent tree** would be

![[Pasted image 20230408152322.png]]

These language rules define a **formal language**. This will be the set of string that can be generated in by the language. A sentence is **grammatical** if it can be generated by the language and it is **ungrammatical** if it cannot be. This notion or grammaticality that is binary is quite limited as in reality sentences don't always have to follow the same rules at different time or in general. In linguistics this type of formal language model is called a **generative grammar**, since the language is defined by the set of possible sentences "generated" by the grammar.

### Formal Definition of CFG
A CFG $G$ is defined by four parameters $N$, $\Sigma$, $P$, $S$ (and is a four-tuple).

- $N$ - a set of **non-terminal symbols** (or **variables**)
- $\Sigma$ - a set of **terminal symbols** (disjoint from $N$)
- $R$ - a set of **rules** or production, each of the form $A\to \beta$ where $A$ is a non-terminal, $\beta$ is a string of symbols from the infinite set of strings $(\Sigma\cup N)^*$ 
- $S$ - a designated **start symbol**

A language is defined via the concept of **derivation**. One string is **derived** from another if a sequence of rules can be applied expanding non-terminals in the first to give the second. If this is done by one rule then we have a **direct derivation**. The language is formally describes as the set of string composed of terminal symbols which can be derived from $S$. $$\mathscr{L}_G=\{w\mid w\text{ is in }\Sigma*\text{ and }S\Rightarrow^* w\}$$Mapping a string to the parse tree is called **parsing**.
These are an extension of **Context Free Grammars**. A **CFG** is defined by ($N,\Sigma,P,S$) but a PCFG is extended with a conditional probability for each rule $P$. A **PCFG** is defined with 

1. $N$ - a set of **non-terminal symbols** (or variables)
2. $\Sigma$ - a set of **terminal symbols** (disjoint from $N$)
3. $R$ - a set of **rules** or productions, each of the form $A\to\beta[p]$, where $A$ is a non-terminal, $\beta$ is a string of symbols from the infinite set of strings $(\Sigma\cup N)*$, and $p$ is a number between 0 and 1 expressing $P(\beta\mid A)$.
4. $S$ - a designated **start symbol**

We can also write the probability as $P(A\to B$) or $P(A\to B\mid A)$. All the possible expansion of a terminal must sum to 1 and so we get the property $$\sum_{\beta}P(A\to\beta)=1$$If this is true for all probabilities in the **PCFG** then it is **consistent**. Recursive rules can cause this not not the case if there are infinite loops!

### PCFGs for Disambiguation
Each tree $T$ can be given a probability by a PCFG. Each tree can be a **derivation** for a given sentence and so we can use the probability to **disambiguate** between the trees. The probability for a given tree is the product of all the probabilities for each non-terminal in the parse tree $T$. So $$P(T,S)=\prod_{i=1}^nP(RHS_i\mid LHS_i)$$This will be the JPD of the parse tree and the sentence but since the parse tree contains all the words in the sentence $P(S|T)=1$ and so$$P(T,S)=P(T)P(S\mid T)=P(T)$$This disambiguation algorithm can be formalized as follows, where the **yield** is defined as the string of words a tree gives. $$\hat T(S)=\underset{T.s.t.S=\textbf{yield}(T)}{\arg\max}P(T\mid S)$$Now we can rewrite $P(T\mid S)$ as $P(T,S)/P(S)$ but $P(S)$ is constant so we just want the argmax of $P(T,S)=P(T)$. And so we get $$\hat T(S)=\underset{T.s.t.S=\textbf{yield}(T)}{\arg\max}P(T)$$We just select the parse with the highest probability.

### PCFGs for Language Modeling
PCFGs can also be used for **language modeling**, if the sentence is unambiguous then $P(S)=P(T)$ and of not then $P(S)$ is the sum of the probabilities of all the possible parses for the sentence.  $$P(S)=\sum_{Ts.t.S=\textbf{yield}(T)}P(T,S)=\sum_{Ts.t.S=\textbf{yield}(T)}P(T)$$We can also get a probability for a **substring** of a sentence...

[[Syntax and Parsing]]
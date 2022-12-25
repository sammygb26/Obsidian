# LL(1) Predictive Parsing
We have seen in [[Parsing Context Free Languages]] a way to parse any language called **CYK** algorithm that runs in $O(n^3)$ time but this isn't good enough for many applications like very long documents. We would like something that would run in $O(n)$ time (single pass). We will say a language is made our of a list of tokens (terminals). We will to ensure we only take $O(1)$ time for each token. So we want to process a single token at a time. 

We will use the below language for our examples
![[Pasted image 20220210131807.png]]

## Predictive Parsing
The idea here is we our start symbol is $stmt$ we want a **leftmost derivation** of our program starting we will expand the leftmost terminal at each step. If the token starts at say $begin$ we want the maximum amount of information from this. We know our left most is $begin$ then this must come from a $begin-stmt$ we get a *prediction* for the remaining statement. In this case we predict we must have a following $stmt-list$ followed by $end$.
![[Pasted image 20220210131924.png]]
We have been able to tell all this derivation from the token we started with $begin$ and the token we must start from $stmt$. If we always know what to do from these two bit of information the current token and the symbol we are in. Then we have an LL(1) language.

**LL(1)** -> The correct production to apply is determined by jus two pieces of information, the current token and the nonterminal being expanded. For **LL(1)** grammars this is always true.

In our example if we have $stmt-list$ as the nonterminal being expanded. No matter what token we are given then our next production is unknown. As we don't know what rule to pick from without looking ahead. We can alter our rules to make our grammar **LL(1)** by changing statement list to always produce a statement followed by a statement tail.  

![[Pasted image 20220210132733.png]]

So if our statement has $if$ as the next token. We would get

![[Pasted image 20220210132901.png]]

So so far we will have

![[Pasted image 20220210132958.png]]

## Parse Table
Take the simple grammar which is **LL(1)** that is just a bracket sequence
![[Pasted image 20220210133033.png]]
This means we can draw a 2-d **parse table** telling us what rule to apply in any situation. This if for any terminal given we are expanding any non terminal (terminals column, nonterminal rows)
![[Pasted image 20220210133258.png]]
We also add the $ symbol to mean we are ending a sequence and all remaining non-terminals must add $\epsilon$ the blank entries are values are ones that will never happen in a grammatically correct. We will suppose we have been given this parse table and we will show how it is used for parsing.

#### Example
Take the input "(())" we will use a **stack** that keeps track of the predicted form for the remaining input.
![[Pasted image 20220210133731.png]]
We start with our next symbol being $($ with our state being $S$. This will give us the rule $S\implies TS$ to we push $S$ then $T$ to the stack. Then we do the same for $T\implies (S)$ making our stack $(S)S$. Once we get the open bracket we then check that  it matches what we have next in the tree. We can then continue like this. If we match a rile to $\epsilon$ we would just pop of the stack and add nothing. Then when we have no more input left we just use the $ symbol and see what it matches to. We then end and the stack must be empty.

## LL(1) Algorithm
![[Pasted image 20220210134648.png]]
So we initialize the stack to our starting nonterminal. We pop terminals or nonterminal of either matching them to the string and moving our position along by one r we match a rule to the current input value. If there is no rule we return an error. If we can't match we return an error. Then if we don't end on $ we return an error.

## More Parse Table
![[Pasted image 20220210135133.png]]
If we have popped the symbol $X$ of and are matching $a$. Then the blue parts means $a$ can be derived from within the symbol $X$ then $a$ can be part of $X$ in the red cases we reduce these values meaning $a$ isn't in $X$.

## Extra
**LL(1)** is an example of a *top-down* parser as it starts with the root and down to the terminals. **CYK** is a *bottom-up* as it start with terminals and builds up to a start node. **LL(1)** runs in $\Theta(n)$ time as it take a small amount of time for each symbol (limited number of times around the loop). For large-scale languages may want more flexibility so $LR(1)$ is used.

In the **real-world** parsers aren't implemented by hand. Instead we write a CFG then run a parser generator which create a parser automatically (typically by constructing a parsing table).

## Pipeline
This is a small part of language processing as a whole below is an idea of the whole pipeline
![[Pasted image 20220210140218.png]]
This is for natural languages
![[Pasted image 20220210140244.png]]

[[LL(1) Predictive Parsing Questions]]
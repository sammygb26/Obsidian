# Parsing Context Free Languages
Here we want to construct a syntax tree given a raw string input. We will look at the **Cocke-Younger-Kasami** algorithm (a dynamic algorithm), which works for any context free grammar. This works on CFGs in **Chomsky Normal Form** (but any grammar can be converted into this). It will take time $\Theta(n^3)$.  We will also look at computer parsing algorithm that run faster.

## Chomsky Normal Form
A CFG we define the rules to go form some non-terminal to a sequence of nonterminal and terminals. In **Chomsky Normal Form** we restrict this such that every nonterminal can either go to a terminal or two nonterminal.
$$
X\to YZ
$$
$$
X\to +
$$
An example is below

![[Pasted image 20220207132132.png]]

So either goes to a single terminal or a non-terminal. We can't have the rule $AP\to A$ as it wouldn't be in CNF.

## Parsing
If we want to parse a input we could start by adding markers to the string so we can more easily talk about substrings

![[Pasted image 20220207132412.png]]

We want to know how this phrase can come from the start point NP. We want to know which substrings can be derived form which substrings (do allows DP approach). We can store all these entries in a 2D array indexed by $i$ and $j$ for $i$ and $j$ indexing a substring $i:j$. We will start from the single substrings and work up to longer ones eventually working our way up to the total string. We can for these entries start with the simples ones (single words that must go to one) and work our way up to get more and more complicated ones. For each cell it must be made out of at most two nonterminal and this limits the number of options we have to look at. 

![[Pasted image 20220207133445.png]]

We start with each diagonal entry then we go up the column in turn we note the diagonal must come from a single nonterminal that allows the exact word. We then also look at the exact splits for each column entry. Then we see if that combination in the grammar that can be made from the possible values for the two split phrases. This is a **recognizer** which just says if our string is part of the language. We also want a **parser** which gives us the syntax tree. We can just add in some tracers to help us later, giving us a syntax tree (or more than one).

## Runtime
We can see from the three for loops running at most $n$ times then for each check we look all rules $m$ rules so it will be $\Theta(n^3)$ or $\Theta(n^3m)$. If we allow for example three splitting we have to look at all combinations of 3 parts but this adds another layer of looking giving us $\Theta(n^4)$. This is why we use CNF.

## Converting to Chomsky Normal Form
Any grammar can be converted to CNF if we don't allow the empty string. What we do is we convert any rule form $X\to ABCD$ with a new rule $X\to AY$, $Y\to BZ$ and $Z\to CD$. This gives the following steps

1.  Apply the above splitting trick to enforce every rules only goes to two smaller ones.
2. Find all non-terminals where we can derive an empty string these are called **nullable** terminals
3. Delete all $\epsilon$ productions but if there is a compound leading to it we add more options removing parts that will reduce to $\epsilon$ $T\to \epsilon|R$ so $TT$ becomes $TT|T
4. Then we remove **unit productions**. For this for every terminal we add a non-terminal to generate this terminal.

This will now be in **Chomsky Normal Form**. This conversion has to be done once per grammar we can convert a syntax tree from this back to original grammar. We could get a grammar that is at most $O(m^2)$.

[[Parsing Context Free Languages Questions]]
What is the CYK algorithm? #flashcard #IADS #ParsingContextFreeLanguages
	The Cocke-Younger-Kasami algorithm is a dynamic algorithm which for any context free grammar. The condition is it must be in Chomsky Normal Form. But any grammar can be converted into this taking $\Theta(n^3)$ time.

---
What is Chomsky Normal Form? #flashcard #IADS #ParsingContextFreeLanguages
	In a regular CDF we define rules to go from terminals to nonterminal. In CNF we restrict this such that a non-terminal can either go to a terminal or two nonterminal.

---
How can markers help us describe subsentences? #flashcard #IADS #ParsingContextFreeLanguages
	If we have a sentence we can give every work (terminal) a number in sequence. Then to refer to a subsequence we say $i:j$ to mean the sequence starting a $i$ and ending at $j$ where $i>j$.

---
What data structure does CYK use to store its computational workings broadly? #flashcard #IADS #ParsingContextFreeLanguages
	CYK uses a 2D array $tabel$ where each cell $tabel_{i,j}$ where $i>j$ stores a list of possible non-terminals that could expand to that substring.

How does CYK work? #flashcard #IADS #ParsingContextFreeLanguages
	We build up a 2D array of possible interpretations for each subphrase (blank if no interpretation). Then for single terminals we can add all the possible non-terminals that correspond to them. For anything else we consider each possible split and if any of the pairs of non-terminals can be produced by a rule we add the non-terminal originator in the rule to our new cell. By the end the cell $0:n$ will contain all possible starting interpretations for the phrase. We can then backtrack using the rules to find the exact tree.

---
What is the runtime for CYK? #flashcard #IADS #ParsingContextFreeLanguages
	There are many looks running $n$ times then also for $m$ rules in $G$. Hence it takes $\theta(n^3)$ or $\theta(n^3m)$.

---
What are the steps to converting to CNF? #flashcard #IADS #ParsingContextFreeLanguages
	It can be fairly simple all we do for any rule $X\to ABCD$ is we add $X\to AY$ then $Y\to BCD$ and so on. We can apply this until we have all rules to less than 3 non-terminals. Then we remove any sequence $A\to B$ making $A$ and $B$ the same. We then need to find all non-terminals where we can derive an empty string *nullable terminals*. We add $\epsilon$ to these meaning no output. Then for any production say $T\to\epsilon|R$ we can making $X\to TT$ into $X\to TT|T$ and remove epsilon. This conversion takes $O(m^2)$ time.

---

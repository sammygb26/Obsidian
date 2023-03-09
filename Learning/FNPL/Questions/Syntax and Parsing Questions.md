How is parsing syntax tree different from parsing morphology? #flashcard #FNLP #SyntaxParsing
	Often in language there are **long range** dependencies where words form can depend on words arbitrarily far away. But this generally doesn't happen with morphology.

---
What are phrase categories? #flashcard #FNLP #SyntaxParsing 
	Phrase categories are given by their **substitutability**. That is two phrases are in the same category if they can be substituted to every situation the other makes sense grammatically.

---
What are constituency tests? #flashcard #FNLP #SyntaxParsing 
	Constituency tests are used to find phrase categories and test is two phrases are in the same category.

---
What is the coordination constituency test? #flashcard #FNLP #SyntaxParsing
	Here if we can combine two phrases with a conjunction they are in the same category.

---
What is the clefting constituency test? #flashcard #FNLP #SyntaxParsing
	We use the template "___ is/are who/what/where/when/why/how __ ". Then we take our two supposed sentences and flip their order placing the template in between. 

---
What  are theories of syntax? #flashcard #FNLP #SyntaxParsing 
	These theories of how sentences are made. These describe how the phrases should be broken up and labeles applied. These should describe which sentences are well-formed (grammatical) and which are not.

---
What are the two theories of syntax we will look at in the course? #flashcard #FNLP #SyntaxParsing 
	The two theories are **constituency (aka phrase) structures** and **Dependency structures**.

---
What are constituent trees? #flashcard #FNLP #SyntaxParsing 
	This is a structure given by the constituency syntax theory. We form a tree where the nodes are labeles and the leaves are words. For example we might have noun phrases and word phrases.

---
In a constituent tree what is the first layer made out of after the words? #flashcard #FNLP #SyntaxParsing 
	This layer is made out of POS tags. These POS tags can be through of as emitting words. After this point phrases are made out of these simpler parts.

---
How does a constituency tree always state? #flashcard #FNLP #SyntaxParsing 
	A constituency tree always starts with a start tag $S$.

---
What is a context free grammar? #flashcard #FNLP #SyntaxParsing 
	A context free grammar is formed over a set $V$ of non-terminals (all of which must be expanded to have a grammatical sentence), then $\Sigma$ a set of terminal nodes. We then have a set f rule $X\to Y_1\dots Y_n$ where $X$ is a non-terminal and $Y_i\in V\cup\Sigma$.

---
What is structural ambiguity in syntax trees? #flashcard #FNLP #SyntaxParsing 
	Structural ambiguity comes from multiple trees giving the same output sentence. These syntax interpretations come down to the sentence having different meanings.

---
What are two common causes of structural ambiguity in syntax trees? #flashcard #FNLP #SyntaxParsing 
	Two common causes of structural ambiguity in syntax trees are **attachment ambiguity** and **POS ambiguity**.

---
Give an example of attachment ambiguity in a sentence? #flashcard #FNLP #SyntaxParsing 
	A classic example if "I saw a girl with a telescope" you can either be using a telescope or she can have a telescope.

---
What are context free grammars used? #flashcard #FNLP #SyntaxParsing 
	Context free grammar allow small parts of a sentence to be parsed on their own. By ignoring the global context we are able to build up to that global context in an efficient way.

---
Given a sentence and a CFG what are the two main problems? #flashcard #FNLP #SyntaxParsing 
	The two main problems will be the **recognition problem** (is a sentence in the language) and the **parsing problem** (what is the most plausible derivation tree for a sentence).

---
What properties do we want in a good syntax parser? #flashcard #FNLP #SyntaxParsing 
	We want the parser to be **correct** and find any possible derivation of a sentence. We also want it to be **efficient** and no exploits the combinatorial number of possible interpretations.

---
What are the different kind of directionality in syntax parsers? #flashcard #FNLP #SyntaxParsing 
	We can have **top-down** that start with the $S$ tag and attempt to grow out to the provided sentence. **Bottom-up** that start with the individual words and build up the the $S$ tag. Then **mixed** which use some combination of the two.

---
If we are using a top down parser what does our problem become? #flashcard #FNLP #SyntaxParsing 
	A tow down-search can be through of as performing a search through the space of possible sentences. It is attempting to find a path to our sentence. Because of this we can use search strategies like BFS, DFS, Greedy search and A* variants.

---
What is the CYK algorithm? #flashcard #FNLP #SyntaxParsing 
	This is a **bottom up** parsing algorithm that exploits the properties of the CFG to achieve a polynomial time exploration algorithm.

---
What is Chomsky Normal Form? #flashcard #FNLP #SyntaxParsing 
	Chomsky Normal Form is a form of any CFG where there are only two kinds of rules. There are **preterminal rules** (emissions) and **binary inner rules**. The emissions take the form $V\to\Sigma$ while the binary rules are of the form $X\to YZ$.

---
How can a CFG be converted to CNF? #flashcard #FNLP #SyntaxParsing 
	A CFG can be converted to CNF by 1) removing $\epsilon$ emissions. 2) Removing unary rules $C\to C_1$ 3) Binarization on any n-ary rules.

---
How can binarization be performed? #flashcard #FNLP #SyntaxParsing 
	Binarization can be performed by converting a big rule with intermediate non-terminals. These give the previously spun off parts of the phrase. From this the rules give the remaining nodes required.

---
What is binarization also called in the context of PCFGs? #flashcard #FNLP #SyntaxParsing 
	In the context of PCFGs binarization is called **lossless Markovization**.

---
What is the parsing task mathematically? #flashcard #FNLP #SyntaxParsing 
	In the **parsing** task we are given $G=(V,\Sigma, R,S)$ and a sentence $\mathbf w=(w_1,w_2,\dots,w_n)$ our goal is to produce a parse tree for $\mathbf w$.

---
How does span notation split up words? #flashcard #FNLP #SyntaxParsing 
	Span notation give a way to label a substring of a word. For example 0:1 is the first word 0:2 the first and the second. 3:6 would be the 4th to the 6th word.

---
If we find all possible ways to parse a string what tells us if it belongs to a language? #flashcard #FNLP #SyntaxParsing 
	This string only belongs to our language if on of the parses for the whole sentence is rooted in the $S$ tag.

---
How does CYK parse one word? #flashcard #FNLP #SyntaxParsing 
	CYK parses one word via by looking at the Preterminal rules. We can apply these rules and then recursively apply **unary rules**.

---
How does CYK binary rules? #flashcard #FNLP #SyntaxParsing 
	CYK does this by looking for any pair of subtrees (this is given by a span and a mid in said span). We want these two substring to parse to two non-terminals which we have a rule for. For any possible parse we record which mid lead to that parse.

---
What is the idea of signatures in CYK? #flashcard #FNLP #SyntaxParsing 
	The idea is once we have found what nodes a substring can be parsed to we know all we need to about said node. We can build up a trellis of these signature optionally storing the midpoint to allow backtracking later.

---
Broadly how does the CYK algorithm work? #flashcard #FNLP #SyntaxParsing 
	In CYK we start with the smallest substrings. Then We build up to a one deeper layer with two long substrings. At each level for every rule we check every splitting of the subtree. Any possibilities for a given span we add to its signature. This allows the next layer to be calculated and so on until we reach the full string and either get $S$ or not.

---
What is the unary rule problem in CYK? #flashcard #FNLP #SyntaxParsing 
	The issue is there is we need to apply unary rules over and over again as the application of one could allow another. To get around this we can perform **unary closure** and add in any unary rules that are implied. This ensures all possible interpretations given unary rules are found after only 1 iteration.

---
What is the ambiguity problem when parsing with CYK? #flashcard #FNLP #SyntaxParsing 
	The ambiguity problem is CYK gives you the possible parses but doesn't tell you which one to chooses and there may be exponentially many.

---
How should PCFGs help with ambiguity? #flashcard #FNLP #SyntaxParsing 
	Context Free Grammars can have ambiguity when parsing. But PCFGs give probabilities for each rule being applied. This way for each tree we can ger a probability that tree is correct.

---
For the PCFG probabilities what are the properties that must hold? #flashcard #FNLP #SyntaxParsing 
	The value of the probability must be between 0 and 1. Then the sum of the probability of all rule sleaving a state $X$ must be 1.

---
What is a problem with using PCFGs to give a distribution over possible trees for a sentence? #flashcard #FNLP #SyntaxParsing 
	A problem with this is PCFGs only give emission probabilities for given states. But for entire trees the probability may be less that 1. Luckily with MLE these are always proper.

---
How can we define a distribution of all derivations of a sentence? #flashcard #FNLP #SyntaxParsing 
	The distributions overall possible sentences are given as for $G(x)$ (all derivations of $x$) we defined $P(T)$ for $T\in x$.

---
Given a distribution P(T) for derivations of sentences in G(x) how is the best parse found? #flashcard #FNLP #SyntaxParsing 
	The best parse is found via $$\underset{T\in G(x)}{\arg\max}\space P(t)$$

---
How is maximum likelihood estimation performed for PCFGs given a treebank? #flashcard #FNLP #SyntaxParsing 
	Here we use the function $$p(X\to\alpha)=\frac{C(X\to \alpha)}{C(X)}$$where $C(X\to\alpha)$ is the number of times a rule is used in the corpus and $C(X)$ is the number of time a non-terminal is seen in the corpus.

---
What is a treebank? #flashcard #FNLP #SyntaxParsing 
	A treebank is a collection of possible trees for some CFG. We can use these predefined trees to give us a PCFG to generate them.

---
What are some peculiarities with Penn treebank?  #flashcard #FNLP #SyntaxParsing 
	Penn treebank has fine grained POS tags and Flat NPs.

---
How does CYK change majorly when we parse probabilistically? #flashcard #FNLP #SyntaxParsing 
	When we parse probabilistically we store for each span not just if a node was reached but instead the best probability path for each node.

---
What is the problem with unary rules in PCFGs? #flashcard #FNLP #SyntaxParsing 
	The problem with unary rules it that applying basic transitivity closure least to probabilistic value that break the PCFG. But this doesn't matter for CYK.

---
How can the best tree be recovered after performing CYK with a PCFG? #flashcard #FNLP #SyntaxParsing 
	In this case the signature for each span include the probabilities for each one and a back pointer to the best case. We simply follow the best back pointers.

---

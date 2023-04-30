What is constituency? #flashcard #FNLP #CFGs 
	**Constituency** at its most basic level is the idea that sentences are made our of parts which can be rearranged and transposed for parts in the same group. A **constituency group**! For example Noun Phrases, Verb phases. The phrases can move to different places withing a sentence construction but the **parts** cannot.

---
What does it mean for a constituent to dominate another in a constituency tree?  #flashcard #FNLP #CFGs 
	A constituent dominates another in the tree when it is an ancestor of a node. We have **immediate domination** when a node is a parent of another node.

---
What parts define a CFG mathematically? #flashcard #FNLP #CFGs 
	Mathematically a CFG is defined by $N$ - a set of **non-terminal symbols**, $\Sigma$ a set of **terminal symbols**, $R$ - a set of rules of the form $A\to \beta$ where $A$ is a non-terminals and $\beta$ is a sequence of terminals and non-terminals. $S$ - the start symbol.

---
When are sentences said to be grammatical and ungrammatical with respect to a CFG? #flashcard #FNLP #CFGs 
	If a sentence can be derived from the start symbols then it is said to be **grammatical** (or within the language defined by the CFG). If a sentence cannot be derived from the start symbols it is **ungrammatical**.

---
What is the declarative sentence level construction? #flashcard #FNLP #CFGs 
 The **declarative** sentence level construction states something about the world. For example "I have not slept in a while". The start rule that generates this is $S\to NP\space VP$ and so it is saying something about the noun phrase. "The biggest grape opens the bridge" (doesn't make sense but is grammatical).

---
What is the imperative sentence level construction? #flashcard #FNLP #CFGs 
	The **imperative** sentence level construction defines a sentence like "Open the door". It is given by the rule $S\to VP$ and is basically used as a command.

---
What are the possibilities for a determiner in noun phrases? #flashcard #FNLP #CFGs 
	Determiners modify the remaining *nominal*. For example "a, the, these, some, any" but there can also be more complicated possessive determiners $NP's$ of the form "Greg's", the bridge's" and so on. They can even be nested.

---
What is the nominal in constituent syntax? #flashcard #FNLP #CFGs 
	This is basically the Noun Phrase without the determiner. Once we have this we can apply many more complicated nominal rules to modify the main head noun in the noun phrase.

---
What is agreement? #flashcard #FNLP #CFGs 
	This is the phenomena comes in many flavors, where noun phrases have to conform to a form based on their subject, or determiners are restricted based on the type of head noun they modify (3sg or plural). Basically words are further constrained by rules which aren't easily captured by CFGs without exploding the number of nodes.

---
What is the main problem agreement causes when it comes to CFG construction? #flashcard #FNLP #CFGs 
	CFGs can only capture restriction on lower level dynamics through new non-terminals (constituent). The problem is agreement causes there to be many subclasses of agreements for all the different words a phrase must agree with. This can explode the size of the grammar making it harder to compute with.

---
What is verb phrase subcategorization? #flashcard #FNLP #CFGs 
	These are rules that designate the kinds of compliments a main verb in a verb phrase can take. For example you would say "I want a seat" and "I found a seat" but despite th fact you say "I want to fly" you wouldn't say "I found to fly". The compliment the verb takes is restricted. This isn't just an isolated rule often 100 or more categories can be made.

---
What are auxiliary verbs? #flashcard #FNLP #CFGs 
	There are verbs which further contextualize a following verb. For example providing timing , possibility or opinion information. "I could have been a vegetable", "I will see the plant", "Oh, it might have been prevented...".

---
What is coordination? #flashcard #FNLP #CFGs 
	Coordination is the general rule that allows non-terminals to be combined together. In general the rule is $$X\to X\text{ and }X$$Where $X$ stands for any non-terminal. This is an example of a **metarule**.

---
How can an implicit grammar be defined for a treebank? #flashcard #FNLP #CFGs 
	An implicit grammar can be defined by observing the rules used throughout the treebank. For example observing that some $S\to NP\space VP$ tells you that this is a rule. This can give many long rules depending on the guidance and way a treebank was constructed.

---

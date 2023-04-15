There are two main problems with **PCFGs**

1. **Poor independence assumptions** - The CFG rules impose an independence assumption on the probabilities which lead to poor modeling of structural dependences.
2. **Lack of lexical conditioning** - CFG doesn't incorporate facts about specific words so there are issues with subcategorization and ambiguities.

### Independence Assumptions Miss Structural Dependencies Between Rules
In a CFG the expansion of a non-terminal is independent of the context, other nearby terminals in the parse tree. For example $NP$ subjects are more likely to be pronouns and $NP$ objects are more likely to be non-pronounal. But this information isn't incorporated into our calculations.

![[Pasted image 20230410173652.png]]

There is no way to represent this in the PCFG formalism. **Parent annotation** can be used to allow modeling of this.

### Lack of Sensitivity to Lexical Dependencies
Lexical information is only used to generate POS tags but this information is useful elsewhere in the tree for example resolving $PP$ attachment ambiguities. For example

![[Pasted image 20230410174118.png]]

The second parse makes no sense but there is nothing in the grammar to allow differentiation based on the lower words. The different is $VP$ attachment vs $NP$ attachment (incorrect). Two sets of rules are switched out in the two cases: $$VP\to VBD\space NP\space PP$$or the incorrect $$VP\to VBD\space NP\hspace{64pt}NP\to NP\space PP$$but the second one is generally more likely than the other and so it will always give a tree with lower probability all other things being equal. So we either misclassify one set of sentences or misclassify another set. The ambiguity can be addressed if our grammar can represent **lexical dependency**. This problem also leads to **coordination ambiguities**

![[Pasted image 20230410175211.png]]


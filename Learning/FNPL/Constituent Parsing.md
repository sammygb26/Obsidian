## Parser Evaluation
There are two kinds of evaluation **intrinsic evaluation** and **extrinsic evaluation**. *Intrinsic* can be **automatic** (evaluated against test data) or **manual** performed according to human judgement. Then **extrinsic evaluation** scores by comparing how well a system using the model perform some task.

### Standard evaluation setting in parsing
When **Automatic intrinsic evaluation** is used we train against gold standard provided by linguists. We train into the sets 

1. **Training set** - set we train the model on
2. **Development set** - used for tuning the model (initial experiments)
3. **Test set** - final experiments to compare against previous work.

### Automatic evaluation of constituent parsers
These are the different ways to compare different parses for a sentence.

1. **Exact match** - percentage of tree predicted correctly. This way is poor sentences are very large and so to optimize this it is best to ignore them.
2. **Bracket score** - scores how well individual phrases are identified
3. **Crossing brackets** - percentage of phrase boundaries crossing
4. **Dependency metrics** - scores dependency structure corresponding to the constituent tree

##### Bracket score
This is the most standard score. It regards a tree as a collection of brackets $[\min,\max, C]$. The set of brackets predicted by the parser is compared against the set of brackets in the tree annotated by a linguist. With this we can then calculated precision, recall and FI. For example the **bracketing notation** might work as follows. This sentence:

![[Pasted image 20230309123121.png]]

Would be parsed as:

![[Pasted image 20230309123131.png]]

##### Bracket Scores
Precision recall and F1 can be found as

![[Pasted image 20230309123202.png]]

## Treebank PCFG
The way our grammar is made is by directly producing rules from TreeBank for example

![[Pasted image 20230309123426.png]]

This gets around 72% FI. There are many problems with this. They don't encode lexical preferences and they do not encode the structural properties (long distance dependencies) beyond single rules.

##### Context-free constraint
Since we are using a context free grammar we have a independence assumption based on only the node above. But these are too strong.

![[Pasted image 20230309123905.png]]

For example subject and object NP are statistically very different.

![[Pasted image 20230309123932.png]]

We can modify the grammar by using **grandparent annotation**.

![[Pasted image 20230309124001.png]]

We can also add the underlying word in the text.

![[Pasted image 20230309124034.png]]

## PCFG Extension
There are different approaches to enriching the grammar: **Structural annotation** and **lexicalization**.

### Vertical Markovization
Here past ancestors in the tree not just the parents are used to give probabilities.

![[Pasted image 20230309124443.png]]

##### Close Attachment
If we compare 2 configuration 

![[Pasted image 20230309124537.png]]

We will have close attachment a long attachment. One of these may a-priori be more likely. And so we can add a preference for close attachment. But PCFGs can't do this as each subtree has the same rules.

![[Pasted image 20230309124812.png]]

Both these tree would get the same score.

##### PCFG Weakness: Close attachment

...

### Evaluation

![[Pasted image 20230309124928.png]]

### Horizontal Markovization
Previously with binarization we split up n-ary rules as follows

![[Pasted image 20230309125229.png]]

The record in the tag can be through of as the horizontal history. Hence instead we add only a few words as follows

![[Pasted image 20230309125315.png]]

By decreasing the horizontal memory we can get better memory and reduce symbol count.

![[Pasted image 20230309125403.png]]

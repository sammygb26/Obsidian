This is a corpus where every sentence is annotated with a syntax tree. An example from the **Brown** and **ATIS** portions of the Penn Treebank is given below.

![[Pasted image 20230408211048.png]]
LISP-Style parenthesized notation is extremely common. (b) parses to the following tree

![[Pasted image 20230408211225.png]]

Penn Treebank is relatively flat and so there are many very long rules. These can be hard to deal with and so modifications are often used.

### Searching Treebanks
It is often important to search through treebanks to look for specific phrase types. Various tools have been developed like **Tgrep** and **TGrep2**. We will look at some ways of doing things from TGrep2. A patters consists of a specification of a node, possibly followed by links to other nodes. For example $NP$ returns all subtrees in a corpus whose root is $NP$. Nodes can be specified by a name, a regular expression inside slashes or a disjunction of these. For example (NN or NNS) using Penn Treebank notation can be given by

![[Pasted image 20230408214240.png]]

The power comes we we specify information about links. With < meaning **immediately dominates** with many more versions

![[Pasted image 20230408214357.png]]

### Heads and Head Finding
The idea of a head is a word that represents some constituent. For example N heads NP and V heads VP. This word is *grammatically the mode important*. These words are passed up and so we can get a structure as

![[Pasted image 20230408215047.png]]

This is closely related to [[Heads Dependency Parsing]]. The rules is defined as selecting one right hand side daughter.

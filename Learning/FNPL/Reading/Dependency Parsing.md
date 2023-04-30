**Dependency grammars** describe the structure of a sentence completely in terms of directed binary relations between *words*. For example

![[Pasted image 20230430113011.png]]

The arcs move from **heads** to **dependents**. In the above case it is a **type dependency structure** since the arcs are labeled. A **root** word is also marked as the head of the entire sentence.

We can also look at a *dependency analysis* compared to a corresponding phrase-structure analysis.

![[Pasted image 20230430113151.png]]

Phrasal constituent nodes are removed. This is useful since useful information encoded in the *head-dependent* relationships is directly available instead of being burred in the constituent tree. For example the object arguments to prefer are connected directly to it and the modifiers to the *flight* are also connected directly to it.

This also helps with languages with **free-word order** as dependencies  don't have fixed orders and can be applied even to different constituent orders. By contrast phrase-structure grammars require us to define more rules for each possible ordering.

## Dependency Relations
These are inspired by or at least carry on from **grammatical relations**. The arguments to the relation are the **head** and the **dependent**. The head works as a central organizing word while the dependent(s) acts as a modifier to the head. We classify beyond the fact there is a relation with the particular **grammatical function** the relation specifies.

> subject, direct object, indirect object etc

These relations are *more important* in languages with more flexible word order as the roles constituents play is not clear from the rules applied. So the rules act to help clarify which parts of the sentence play what role.

**Universal Dependencies** is a project to combine common relations found in the different taxonomies that have been constructed. There are 37 dependency relations.

![[Pasted image 20230430115210.png]]

In general there are **two sets** of relations. 1) **Clausal Relations** think subject, object, these are generally like arguments to a verb phrase and give the roles objects play with relation to that word. 2) **Modifier Relations** which give all the different ways words can be modifier (clarified specified).

#### Dependency Formalisms
A dependency structure can be represented as a directed graph $G=(V,A)$ consisting of a set of **vertices** $V$ and a set of arcs $A$. The *vertices* are the word (but this could also include grammar or morphemes for morphologically complicated languages). The *arcs* will also define the *grammatical function relationships*.

There are different restrictions on this graph, generally it must be connected and have a single root node. A **dependency tree** is a directed graph with the constraints

1) There is a single designated root node that has no incoming arcs
2) With the exception of the root node, each vertex has exactly one incoming arc
3) There is unique path from the root node to each vertex in $V$

This ensures every words has **a single head**, the structure is **connected** and there is a single root node.

#### Projectivity
This is an additional constraint on the structure of the dependency graph. An arc from a head to a dependent is **projective** if there is a path from the head to every vertex between the dependent and the head. Then a dependency tree is projective is all arcs in the tree are projective. Here is an example of a **non-projective** tree

![[Pasted image 20230430121105.png]]

Note the arc from **flight to was** is not projective since there is no path from flight to this or morning. For this to happen an arc must come through the non-projective arc. So another definition is a projective tree can be drawn with no crossing edges.

There are two issues that come from **projectivity**.

1) Most dependency treebanks are constructed by using head-finding rules which *always generated projective trees* and so will always be incorrect when it comes to constructions like the one above.
2) It is more computationally easy to generate projective trees, methods that are limited to projective only can have better computational characteristics but more flexible approaches are required to be correct.

#### Dependency Treebanks
These play a critical role allowing the evaluating and training of parsers. They are generating made by hand by labeling a corpus. they can also be made by correcting automatic parsers. The **universal dependencies project** is the largest community with almost 200 dependency treebanks in more than 100 languages.

## Transition-Based Dependency Parsing
**Transition-based** parsing is a way to get the dependency parse for a sentence. It is based on *shift-reduce* parsing which was developed to analyze programming languages. The architecture has a **stack** whose words we build arc on, a **buffer** of tokens to be parsed and a predictor called the **oracle** which tells us what operation to takes.

![[Pasted image 20230430123930.png]]

This goes through the items right to left shifting items from the buffer onto the stack. Then top two elements of the stack are examined to allow the *oracle* to make a decision on which **transition** to apply. There comprise intuitive actions we would take to construct a tree.

- Assign the current word as the head of a previous word
- Assign some previous word as the head of the current word
- Postpone dealing with the current word for later

This gives the different operations

1) $LeftArc$ - Assert a head-dependent relation between the first and second elements on the stack, then pop the second element.
2) $RightArc$ - Assert a head-dependent relation between the second and first elements on the stack, then pop the first element.
3) $Shift$ - remove the word from the front of the buffer and push it onto the stack

The way this works our is to apply an ark with a word $w$ as a dependent means it's head is set, the word is removed from the stack and cannot have any new relations added. This means all its dependents must already be assigned. 

Arcs can only be made between the top two elements of the stack and therefore we cannot have a non-projective parse.

The $LeftArc$ and $RightArc$ operations are sometimes called **reduce**operations due to the connection to *shift-reduce* parsing. The set of operations above is called **arc standard**.

We can represent the state of the parse with a **configuration**, this is made out of the current **stack** of words being parsed, **buffer** of remaining words and set of **relations**. The initial state has all the words in the buffer, the stack only containing the *root* node and an empty set of relations. When the algorithm progresses we hope to make a journey through this configuration space by making **operations** (predicted by the oracle) ending in a configuration with an empty stack, empty buffer and set of relations containing the correct parse.

![[Pasted image 20230430125435.png]]

This takes **linear** time be we are relying on the **oracle** being 100% correct and therefore this is a **greedy approach**. There many be multiple paths leading to the same parse and multiple possible parses.

We may also want to add in *dependency relations* and this will make the job of the oracle more difficult as there are more options in its classification task.

#### Creating an Oracle
We will train the oracle by **supervised machine learning**. This takes in the current **configuration** and gives back the next action. But we only have our *dependency treebank* and don't have a sequence of configuration -> action states.

**Generating Training Data** - The key idea is to train the oracle in the context of our reference parse. We can apply deterministic rules to always give correct actions in the different situations. This can be used to train giving gold labeles as we parse and then not used for testing / evaluation. The rules can be supersized formally as

1) $LeftArc(r):\textbf{ if }(S_1\space r\space S_2)\in R_p$
2) $RightArc(r) :\textbf{ if } (S_2\space r\space R_p)\textbf{ and }\forall r',w. ((S_1\space r'\space w)\in R_p)\implies (S_1\space r'\space w)\in R_c$
3) Otherwise $Shift$.

Here $R_p$ is the reference parse relations then $R_c$ is the current reference parse and $S$ is the stack.

If the tree is projective we can always apply $LeftArc$ without blocking any possible missed relations.  Assuming the parse is correct so far then all relations applying will have already been added before the **head** of the **dependent** was added. This isn't the case with $RightArc$ as there can be dependents which haven't been added to the stack yet. So if any relations to them exist we wait until we are sure we can make the arc. 

#### A feature-based classifier
This will give a basic approach. We can use a [[Hidden Markov and Maximum Entropy Models]] (second) to give the correct parse. For this we need **features** which we will train the model on. For this we can use **feature templates** to extract features automatically from the training set. For example.

![[Pasted image 20230430135803.png]]


When as we train we will run into **configurations** like for example.

![[Pasted image 20230430135844.png]]

Given the next correct parse is $Shift$ we can generate the following features.

![[Pasted image 20230430135907.png]]

#### A Neural Classifier
A simple approach here is to **encode** the entire sentence into a representation. Then concatenate this with a representation of the top two elements of the stack and first element of the buffer. This can pass through a *feedforward NN* and a SoftMax to give a distribution over the possible commands. Then we can use a cross-entropy loss to train with the target distribution being a one-hot encoding of our correct operation.

![[Pasted image 20230430140345.png]]

#### Advanced Methods in Transition-Based Parsing

**Alternate Transition Systems** - The **arc eager** transition system is an alternative to **arc** standard that allow rightward arcs to be made far sooner and so leads to a more natural process for building the dependency parse. The basic idea augments the rules to be 

1) $LeftArc$ - Assert a head-dependent relation between the word at the **front of the input buffer** to the word at the **top of the stack**; pop the stack
2) $RightArc$ - Assert a head-dependent relation between the word at the **top of the stack** and the word at the **front of the input buffer**; **shift** the word at the input buffer to the stack
3) $Shift$ - Remove the word from the front of the input buffer and push it onto the stack
4) $Reduce$: Pop the stack

The basic idea here is that words with right arcs have them added as they enter the stack instead of when the leave it. This leaving is given to the reduce operation. This allows words to have dependents added after their parent is defined.

One of the key things is that this method doesn't require a change to the main algorithm and in fact the operation set can be changed out and the algorithm will remain the same. There are many different operation sets some that allow **non-projective** parsing or assign semantic roles.

**Beam Search** - The standard dependency parse performs a **greedy search** but this means we cannot go back on any decision we make even if later information suggests a wrong decision was made.  A *beam search* allows us to keep multiple options options by performing a **breadth first search** but pruning low scoring nodes from the frontier to keep it always smaller than or equal to some **bream width**. A scoring is needed for each node and we can take the discriminator used to pick the next option that is $$\hat T(c)=\arg\max Score(t,c)$$to be the score. We can define the initial **config score** to be 0 then each operation we perform adds some score. $$ConfigScore(c_0)=0$$$$ConfigScore(c_i)=ConfigScore(c_{i-1})+Score(t_i,c_{i-1})$$Once we have found the top $b$ (for bream size) next paths we will always get rid of a parent (since its score is always lower than its children) hence the search always finds an end state eventually.

![[Pasted image 20230430151222.png]]

## Graph-Based Dependency Parsing
This is another family of dependency parsers which search the space of possible graphs. They can produce **non-projective** dependency parses and don't struggle with sentences where ethe head is far from dependents as *transition based parsers* do. 

The search through the space of graphs is performed with the help of **graph theory**. Formally given a sentence $S$ we are looking for the best dependency tree $\mathcal G_S$, which is the dependency parse that maximizes some score throughout the space of possible trees. $$\hat T(S)=\underset{t\in\mathcal G_S}{\arg\max}\space Score(t,S)$$We also make the assumption that this score can be **edge-factored** which means the score is a sum over all the edges of some score defined for them. $$Score(t,S)=\sum_{e\in t}Score(e)$$There are two problem a **graph-based** algorithm needs to solve

1) **Assign a score** to the edges
2) **Find the best parse tree** that maximizes the overall score

#### Parsing via finding the maximum spanning tree
The way this works is we start with a **fully-connected**, weighted directed graph $G$ for a sentence $S$. The vertices represent **all possible** head-dependent assignments with $Root$ also includes but with no incoming edges.  Finding the best dependency parse of $S$ is equivalent to finding the **maximum spanning tree** over $G$. This is just a subset of $G$ that is a tree and covers all vertices in $G$. Two intuitions are used to solve this problem

1) Every vertex has one incoming edge and so every *connected component* (every set of vertices that are linked by edges) will have one incoming edge.
2) The absolute value for the edges aren't critical. Since each node must have an edge into it changing the score of the incoming edge to a node by the same amount doesn't affect the *maximum spanning tree* as they must all include this factor.

To proceed the algorithm first **greedily** chooses all the highest scoring incoming edges. If this is a spanning tree we can stop here. It will be a **spanning tree** if there are no cycles and each node (accept root) has one edge entering. If the greedy search finds this then this is the best graph possible.

If we don't find a tree then the edges must contain some cycle. We want to switch on one of the incoming arcs to this cycle by doing so deactivating one of its cycle nodes (from the first assumption). But which one will be the best? We can use the *second assumption* here by subtracting the value of the greedy arc from all other arcs into a node. The value now gives how much worse than using the original switching on a given node would make the parse. This means that the value of all nodes tell us the **relative change** from the greedy search.

We now **collapse the cycles** creating a new node to represent them then assigning all incoming arcs to node in the cycle and adding all outgoing nodes to the same cycle. Now if we knew the **maximum spanning tree** on this graph it would tell us which alterations to make. For example for whichever edge into the collapse cycle we make we will remove some inner edge which is part of the cycle. 

The way we find the maximum spanning tree for this cycle is using the same algorithm and **recursion**. Even if by the greedy approach we never get a spanning tree we will eventual have one node and the root at which point we just pick the best arc into the combined node.

To reconstruct the graph we expand the node each time removing the inner edge which the incoming edge would conflict. So we remove the previously highlighted edge which points into the same node for which we are adding an edge. 

The algorithm is given here

![[Pasted image 20230430162717.png]]

with the parse for a simple sentence following these steps

![[Pasted image 20230430162740.png]]

This runs in time $O(mn)$ for $m$ edges and $n$ nodes. Of course the number of edges is $n^2$ and so we get $O(n^3)$. But there are more complicated versions which run in $O(m+n\log n)$ time.

#### A Feature-based algorithm for assigning scores
We need to assign score to each edge to give the overall score for a given tree since $$score(S,T)=\sum_{e\in T}score(S,e)$$In a feature based algorithm we compute ethe edge scores as a weighted sum of features extracted form it. That is $$score(S,e)=\sum_{i=1}^Nw_if_i(S,e)=\mathbf w\cdot\mathbf f$$We need to 

1) Identify **relevant features**, these can include wordforms, lemans, POS tags for head words and dependents. Corresponding features from contexts before and after and between the words. Word embeddings. The dependency relation itself. The direction of the relation (left or right). the distance from the head to the dependent.
2) **Learn the weights** - unlike previously we are not predicting to discriminate between classes instead we want to give high scores to the correct parse tree and lower scores to the incorrect parse tree. *Inference based-learning* is a popular way to perform this where we have random initial weights then for an incorrect parse we lower all the weights by some learning rate and for a correct parse we keep the weights the same.

#### A neural algorithm for assigning scores
The state of the art in graph-based parsing uses neural networks.  Instead of hand-designed features these run the sentence through an **encoder** and pass the **encoder representation** then the encoded representation of two words $w_i$ and $w_j$ are passed through a network which estimates the score of the edge $i\to j$. This is one possible option...

![[Pasted image 20230430165506.png]]

The sentence $X=x_1,...,x_n$ is run through an **encoder** which produces a **contextual embedding** representation $R=r_1,\dots,r_n$. The embedding for each token is passed through two separate FFNNs to produce a *head* and *dependent* embedding. that is $$h^{head}_i=FNN^{head}(r_i)\hspace{16pt}h_i^{dep}=FNN^{dep}(r_i)$$Now to calculate the score $i\to j$ we use a learned **biaffine scoring function** where $$Score(i\to j)=\text{Biaff}(h^{head}_i,h^{dep}_j)$$$$\text{Biaff}(\mathbf x,\mathbf y)=\mathbf x^T\mathbf U\mathbf y+\mathbf W(\mathbf x\oplus\mathbf y)+b$$Here $\mathbf U$, $\mathbf W$ and $b$ are *learned parameters* which allow the network to learn the multiplicative integrations between $\mathbf x$ and $\mathbf y$.

Then $Score(i\to j)$ is passed through a **SoftMax** to give a distribution for each token $j$ over potential heads $i$. That is $$p(i\to j)=\text{softmax}([Score(k\to j);\forall k\neq j, 1\le k\le n])$$This is then passed into the **maximum spanning tree algorithm** to find the best tree.

To add in different edge types generally the algorithm above is used to find the  best edges. Then a **label scorer** ranks all the different labels for the edges. 

## Evaluation
There are different metric we can use to evaluate just as when evaluating structure-based parsing. All these matric compare against some **gold labels**. **Exact match** only registers a correct parse if the parse if 100% correct. Generally this isn't fine grained enough and will overestimate how poorly our model is performing and wont discriminate models that make few errors almost all the time vs lost of error almost all the time.

**LAS** - Labeled attachment score is the percentage words that have the right head and correct label.

**UAS** - Unlabeled attachment score is the percentage of words that have the right head but doesn't care what the label was.

**LS** - Label accuracy is the percentage of words whose label was correct (*object, subject* etc).


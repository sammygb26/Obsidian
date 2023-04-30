This covers how we translate language into a meaning representing form such as **FOL**. There are different sources of meaning. 1) It can come from the conventional meaning associated with grammatical construction 2) It can come from knowledge about structure and discourse 3) The context the discourse is happening in. Here we will focus on **syntax-driven semantic analysis**. We will give meaning to sentences purely based on the grammar and lexicon. Our meaning will be *context-independent* and *free from inference*. Almost an unbiased interpretation of a sentence. This will give the *literal meaning* of the utterance.

## Syntax-Driven Semantic Analysis
We want to build the sentence's meaning up from its words as they are the minimum meaning unit in language. But the order and structure informs how we combine these meaning. Hence we can use a syntactic structure and the *components* and *relations* will inform how we compose the meaning. So first a **semantic analyzer** will be used to get the syntactic structure then we perform **semantic analysis** to get our meaning.

As an example we can take the sentence "Franco likes Frasca". "Franco" and "Frasca" will be resolved to consents then we can use the syntax tree to build up the full FOL statement.

![[Pasted image 20230425132127.png]]

We cannot define rules for every possible parse tree. Instead we define how the composition of the smaller tree's build up intermediate representation of the non-terminals. This way the structure describes the meaning and allow an infinite number of possible sentence constructions. The best place to define the composition rules is where the composition is defines, so with the non-terminal expansions or in general with the devices that generate the syntax representation. This is known as the **rule-to-rule hypothesis**.

## Semantic Augmentations to Syntactic Rules
We can begin by augmenting our CFG rules with **semantic attachments** these define how to construct the meaning of a constituent by the meaning of its constituent parts. Abstractly our rules becomes $$A\to\alpha_1\dots\alpha_n\hspace{32pt}\{f(\alpha_j.sem,\dots \alpha_k.sem)\}$$This states the meaning representation of $A$ ($A.sem$) can be constructed as a function of the meanings of the constituents of $A$. There are different ways to specify the function we use to get the semantics. We can use $\lambda$-notation to allow the meaning of verbs and phrase to be built up and added to over time. For example $S\to NP\space VP$ can have the semantics $\{VP.sem(NP.sem)\}$ this way we can have $$VP\to Verb\space\{Verb.sem\}$$$$Verb \to closed\space\{\lambda x.Closed(x)\}$$Then also $NP\to ProperNoun\space\{ProperNoun.sem\}$ and finally $ProperNoun\to Maharani\{Maharani\}$. This way we can resolve the meaning of $S$ to $$\lambda x.Closed(x)(Maharani)=Closed(Maharani)$$This is a simple rule and we would generally want to use **Davidsonian representations**.

#### Every x
When we use the word every we invoke $\forall$. Then the $x$ part will be the **restriction**. So "every restaurant" has a restaurant restriction! So every restaurant could be written as $$\forall x. Restaurant(x)$$But we want a formula that will compose with other constituents in a syntax parse. This only say everything is a restaurant! Instead what we want if for this statement to be just the **scope** for some other expression. Like saying "every restaurant is good". We can add in a dummy predicate to take the eventual property. Then we get $$\lambda Q.\forall x. Restaurant(x)\implies Q(x)$$Overall we can get a statements such as 

![[Pasted image 20230425164337.png]]

Which can allow us to build up the meaning of a simple utterance. In general the tools we can use are 

1. Associating complex, function-like $\lambda$ expressions with lexical items
2. Copying semantic values from children to parents in non-branching rules
3. Applying the semantics of one of the children of a rule to the semantics of the other children of the rule through $\lambda$-reduction.

## Quantifier Scope Ambiguity and Underspecification
Even if we can get a perfect syntactic reading of a sentence our parsing will not get rid of all ambiguity. For example "Every restaurant has a menu" this may have the meaning $$\forall x. Restaurant(x)\implies\exists y.(Menu(y)\land\exists e(Having(e)\land Haver(e,x)\land Had(e,y)))$$Meaning every restaurant has some possibly different menu. But an equally valid interpretation is $$\exists y. Menu(y)\land\forall x. Restaurant(x)\implies\exists e(Having(e)\land Haver(e,x)\land Had(e.y))$$Meaning every restaurant has the same menu. This problem is known as **quantifier scoping**. The different interpretations result from which of the quantified variables has the inner and outer scope. This comes in this context from the order in which the $\lambda$ expressions are reduced. To get around this limitation which locks us into one or the other representation we must have. 

1.  The ability to efficiently create *underspecified representation* that embody all possible readings without explicitly enumerating them
2. A means to generate, or extract, all of the possible readings from this representation
3. The ability to choose among the possible readings.

#### Store and Retrieve Approaches
In this approach we redefine what the semantic constituents are defined as. We ill keep the different parts of the expression separate, quantified. $$\exists e.Having(e)\land Haver(e,x)\land Had(e,y)$$$$\forall x.Restaurant(x)\implies Q(x)$$$$\exists x.Menu(x)\land Q(x)$$These different expressions all make up the parts of the different interpretations. But the two quantified statements define the $x$ and $y$ variable in the "has" semantics. It is this relation that we want to capture and nothing more. So in this **Cooper storage** method we keep a store of $\lambda$-expressions. There is a **meaning representation** for the node and an indexed list of quantified expressions. For example $$\exists e Having(e)\land Haver(e,s_1)\land Had(e,s_2)$$$$(\lambda Q.\forall x.Restaurant(x)\implies Q(x),1),$$$$(\lambda Q.\exists x. Menu(x)\land Q(x),2)$$The variables $s_1$ and $s_2$ are given by the 1st and 2nd store quantified statement respectively. To get a base level interpretation we pick one of the quantified statements and pass in the meaning statement. We do this in a particular order (once per statement). In the end after $\lambda$ reduction we get our meaning.

We also want to consider **how we got the store** that is via the syntax tree. That happens fairly simply, we can copy up the main meaning sentence as before either copying it up unchanged or in branching non-terminals applying some semantic rule and using $\lambda$ reduction to get a new expression. The quantified statements in one level are just copied up to the next level. When a quantified statement is created we abstract it behind some variable $s_x$ and put it in the store.

- A major problem with this method is it only works for quantified NPs but there are other statements for which scope can change the meaning. For example "Every restaurant did not close" does this mean "Every restaurant individually never closed" or "Not all the restaurants closed".
- This method also has no way to impose restrictions on the order of parts.

#### Constraint-Based Approaches
This approach instead of focusing on how to retrieve fully-formed representations. We can instead focus on just how to represent these  underspecified representations while adding additional constraints on top. Then any FOL statement we can make that satisfies the constraints is valid. Here we label holes in a given statement instead of $\lambda$ variables. Then in a fully-specified formula all holes must be filled with some label.

Then to add constraints to this we add **dominance constraints** between holes and labels. So $l\le h$ asserts that an expression containing the hole $h$ dominates the expression with label $l$. That is $h$ must ultimately have $l$ as a subexpression and not the other way around. Then we have $h_0$ be the whole for the entire expression. A description of "Every restaurant has a menu" would be.$$l_1:\forall x.Restaurant(x)\implies h_1$$$$l_2:\exists x.Menu(y)\land h_2$$$$l_3:\exists e. Having(e)\land Haver(e,x)\land Had(e,y)$$Now we need to add constraints. $h_0$ must dominate all. Then $l_3$ is outscope by all other labels. This gives$$l_1\le h_0,l_2\le h_0, l_3\le h_1, l_3\le h_2$$When we make an expression we just fill in the holes. this will create new holes and when they are all filled we will have a proper expression.

This approach works well since we are not tied down to any particular formula and the whole can be arbitrary pieces of FOL logic. Then we can give arbitrary constraints also making the approach flexible to incorporate lexical and world knowledge to reduce ambiguity.
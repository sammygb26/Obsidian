Semantics informs us about meaning. The reason we want **syntax trees** is to allow for a definite semantic mapping to words.

![[Pasted image 20230314121334.png]]

This gets are the goal of AI to *understand* what people mean when they talk.

### Literal Meaning
**Semantics** is concerned with how expression relate to 'the world'. This can include

1. **truth conditions and denotation** - literal meaning - with this kind of meaning a sentence is either true or false.1-15
2. **connotations** (other assertions - implied meaning - metaphors)

### Eliza
Joseph Weizenbaum wrote a program called Eliza in 1969 to demonstrate how easily people can be fooled into believing a machine have some deep understanding.

![[Pasted image 20230314121719.png]]

The idea here is to take key words and then match templates. A mode like **chatGPT** works in a similar way where we fill in structure. Only linguistic form is used and the relation between the signal (words) and the world isn't considered.

- Knowing something truly understand something is subject to philosophy. Instead in FNLP we test if things appear to understand.

### What is meaning? What is understanding?
These are deep philosophical questions. NLP usually takes a more **pragmatic view**, can the computer behave as through it understands (in order to do what we want)?

- Dialogue systems (e.g., Eliza)
- Machine translation
- Question answering

(coreference in assignment)

What issues will we face in building such systems

### A Concrete Goal
We would like to build a machine that answers questions in natural language, may have access to knowledge bases. May have access to vast quantities of English text. This is called **question answering**.

The **knowledge base** may be a database. Then we have to perform *context-to-text* generation. 

Anther option is having massive quantities of text. We don't return documents like Google but we instead return

### Semantics
TO build our QA system we will need to deal with issues in **Semantics** - meaning

Sentimental semantics: how words meaning combines. For example who did what to whom when how and why

![[Pasted image 20230314122724.png]]

Lexical semantics: the meanings of individual words deals with the meaning of individual words.

![[Pasted image 20230314122831.png]]

### Sentential Syntax
This captures if strings are valid grammatically and allows investigation of the classes of phrases, which can inform their meaning. It can generate an unbounded set of grammatical sentences (via finite lexicon, this is done via **recursion**) and can allow the induction of probabilistic grammars.

Sentential syntax reveals information about sentence meaning.

![[Pasted image 20230314123114.png]]

Decision about how to resolve syntactic ambiguity change the meaning of sentences as the syntax structure is changed. (Classic example "I saw a girl with a telescope").  Some syntactic ambiguities don't create ambiguities but most do. Resolving syntactic ambiguities does not resolve semantic ambiguities! It doesn't resolve

- *word sense* - what a word is meaning for example **bank** is sense ambiguous. "I went to the bank" has the same meaning no matter what bank refers to between river bank and bank building. We use common sense knowledge to disambiguate these but 
- **semantic scope** - for example "every man love a woman" does every man love the same woman or different women.
- **anaphoric expressions** - Here we need to resolve pronouns to previous sections.

This all means reasoning about **context** is important for the above.

## Compositionality
The idea here is the meaning of a phrase is a function of the meaning of its parts and how they are put together. We exploit compositionality to augment a grammar with a **Semantic component** which deterministically derives the **logical form** of a sentence from its syntax tree.

### Desiderata for (Literal) Semantic Representations
The semantic representation should be **unambiguous** - for example disambiguates between multiple meanings of sentences for example "I made her duck". We will ignore ambiguities as we have already went to the trouble of deriving the tree. We want is to support **automated inference** to allow it to be useful. We also want it to be **verifiable** allowing us to determine if the sentence is true with respect to a model of the world. These come to fit  both


### Logical vs. Commonsense Inference

![[Pasted image 20230318172043.png]]

**Someone** is a *logical constant* its meaning contributes to the logic of a sentence.

More complicated inference can occur. For example we entail Huston-based Lex Corp is an American company. 
![[Pasted image 20230318172128.png]]
The implication requires understanding the relationship between the words. The entailment depends on the words beneath. Using *something* for example relates to all things.

### Why FoL and not Propositional Logic
If we have sentences and how they would be parsed in propositional logic.

![[Pasted image 20230314124300.png]]

But this doesn't capture the internal structure of the proposition "Fred ate rice". We are unable to express important relationships between

![[Pasted image 20230314124405.png]]

So this lacks the inference power that other sentences require. There are many elements of language that only FoL can capture

![[Pasted image 20230314124428.png]]

From the syntax tree we build a template for a logical formula we then add in constraints on the words we have already build up. Finally this gives our FoL statement.

We can also capture **semantic scope ambiguities** this can be seen in v) where the two interpretations are conjoined. The conjunction is required event through the first parts is implied by the second part as later sentences can modify the statement and collapse it to the second option.

### Adding tense and modifiers Davidsonian Semantics
Here we introduce an event argument $e$ to action predicates is very useful. A time is also added $n$ (now).

![[Pasted image 20230318173324.png]]

That is there exists some event $e$ for which $fred$ ate $rice$ and this event was before $n$ now. When we add modifiers we can use conjugation. The event variable ties these modifiers together.

![[Pasted image 20230318173440.png]]

- An *adjunct* is a part of a statement this isn't required grammatically.

The event variables simplifies the formula. These events create a relationship. With $\land$ elimination these imply all the meaning we want. The elimination allows the meaning to be later split up.

## Compositionality
This is what allows us to work out the meaning of large sentences. What this means is that *"the meaning of a complex expression is a function of the meaning of its parts and of the rules by which they combine"*. The syntax rules give the rules for how the daughter sentences should be combined. This defines the semantics of how words relate to each other. This defines the **composition rules**. Then the **lexical rules** are given by associating each word. So the composition rules define how these lexical forms are combined to give our final sentence.


### What we are aiming for
![[Pasted image 20230314125125.png]]

Here we have a Verb Phrase but we want to fill it in with the arguments passed around. We need rules to allow us to find the augments.

### Lambda Calculus and Beta Reduction
This allows us to work with 'practically constructed' formulae. It is an extension of FoL.

- If $\psi$ is a well-formed FoL expression and $x$ is a variable, then $\lambda x\psi$ is a well-formed FoL expression. Its a **function** known as a $\lambda$-term

![[Pasted image 20230318175946.png]]

- $\lambda$-term has interesting semantic, but they also offer a way of substituting (free) variables in an FoL expression

This allows us to define lambda terms which define the substitution rules for our syntax. Adding the lambda term is called **Lambda abstraction** when the function is called its called **Beta reduction**.

As an example 

![[Pasted image 20230318180134.png]]

We can also perform higher type substitution variables. That is the variable can be a function.

![[Pasted image 20230318180308.png]]

We can do the same thing with out logical function for eats rice. We get

![[Pasted image 20230318180352.png]]

The arguments was a lambda term and so we get a lambda term out with $fred$ being passed in.

##### Example Composition for Fred ate rice
We pass up variables for unary rules. Then for VP phrases we need to decide what is the *functor* and what is the *argument*.
![[Pasted image 20230314125715.png]]

##### The Grammar that generates that tree
![[Pasted image 20230314125806.png]]

The **semantics** is a function. The order of the $\lambda$ terms matter. The outer ones are filled first.

In *blue* we define how semantics are built up to the mother nodes. So $VP.sem(NP.sem)$ means we pass the noun phrase semantics into the verb phrase semantics 

### Problematic
This doesn't work for quantified sentences. For example

![[Pasted image 20230319102457.png]]

But if we pass the every man statement into the ate rice statements as an argument we get an ill formed sentence.

![[Pasted image 20230319102640.png]]

Instead we can use a higher order function then pass the old functor in.

![[Pasted image 20230319102801.png]]

But then we must make all noun phrases functors and redefine $fred$ as $$fred := \lambda P.P(fred)$$
But this doesn't work for transitive verbs as the object can also be quantified.

![[Pasted image 20230319103248.png]]

Again to solve this we switch the functor and argument with a higher order functor.

![[Pasted image 20230319103500.png]]

The transitive verb places the old functor beyond the $\lambda z$ term giving a well formed sentence.

![[Pasted image 20230319103624.png]]

### Solution
The changes needed are given in purple.

![[Pasted image 20230319103655.png]]

With all the beta reductions applied we get a tree as:

![[Pasted image 20230319103742.png]]

### Semantic Scope
If we look at every man loves a woman

![[Pasted image 20230319104026.png]]

We get a single meaning that there is a woman for every man. But not there is a single woman all men love. There is only one syntax tree so where did this come form. This is an example of a semantic ambiguity that isn't a syntactic ambiguity.

### Scope
This comes down toe **scope**. In one interpretation *every* has scope over $a$ and in the other interpretation the scope is the other way around.

![[Pasted image 20230319104235.png]]

The scope of $a$ can be projected out of where it is placed in the parse tree.

We need our semantics to take into account this ambiguity. However we cannot just list the interpretation as the number of interpretations grows exponentially.

![[Pasted image 20230319104554.png]]

Here there are 18 different interpretations which are not logically the same.

But we don't worry about all the interpretations instead a shallower meaning can be used. This would be **semantic underspecification** (as opposed to enumeration which is exponential).

With this we build logical forms via a syntax that **underspecify** the relative semantic  scope of the quantifiers. This would be a partial description of FoL statements in this case.

Then when we interpret this LF we use surrounding sentences to disambiguate the meaning.

![[Pasted image 20230319105031.png]]

- Here it makes it clear "a computer" refers to a single computer making "a" outscore "every". 

### Semantic Underspecification
The LF constructed in the grammar will have FoL parts then constrains on how these statements are  combined. We can take the example of Every man loves a woman

![[Pasted image 20230319105414.png]]

The parts are the same but the relative placements is different. This can be visualized with a operation tree

![[Pasted image 20230319105946.png]]

In underspecified semantics the nodes are labeled then then we describe the aways they can be combined. If we ignore the existential quantification $\exists e$ and the now  statements $n\subseteq e$ we get

![[Pasted image 20230319110139.png]]

We don't define $h_5$ and $h_3$ but there are only a limited number of elements we can sub in their place and so a limited number of interpretations.

### Resolving Scope
There are some rules that ensures this. Each whole $h$s must equal a unique $l$ with no free variables. Given this there are only two solutions

![[Pasted image 20230319110502.png]]

[[Compositional Semantics Questions]]
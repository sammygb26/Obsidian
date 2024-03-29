 This is the problem of given a sentence identifying the different tokens in the sentence as a Part-of-Speech. For example:
 
![[Pasted image 20230228121233.png]]

The context can be somewhat hidden hence there is ambiguity in which tag we should give.

### Why do we care?
This gets us toward syntactic analysis (often used in later analysis). These are fast models but can still give useful information. So POS tags can also be used as features in classifiers. These illustrate the use of **hidden Markov models** we can be used in other tasks like sequence leveling. So these algorithms are general to other fields.

### Examples of other tagging tasks
**Named entity reignition** here we want to label words as belonging to **persons, organizations and locations**. These are useful for knowledge parsing.

![[Pasted image 20230228121624.png]]

This can be hard as names can be hierarchical and so tagging doesn't accomplish this naturally.

**Information field segmentation** Here given a type of text (classified advert, biography, entry), identity words belong to fields. So we fill in records given text.


![[Pasted image 20230228121838.png]]

### Sequence labelling: Key features
In all these tasks deciding the correct label depends on 

1. The **word** to be labeled, (NER) for example *Smith* is probably a parson, *chair* is probably a noun.
2. The **labels of surrounding words** - (NER) if following word is an organization (say *Corp*) then this word is more likely to be an organization too. (POS) if preceding word is a modal verb (say *will*) then this words is more likely to be a verb.

HMMs combine these sources of information *probabilistically*.

### Parts of Speech: reminder
**Open class words** (or content words)
	These are nouns, verbs, adjectives and adverbs. These mostly content-bearing: they refer to object, actions and features in the world.  This is a **open class** since there is no limit to what these words are then new ones are added all the time (**email**, **website**).

**Closed class words** (or function words)
	These are things like pronouns, determiners, propositions, connectives. These are a limited number of these and they are mostly functional: to tie concepts of a sequence together.

### How many parts of speech
Both linguistic and practical considerations are taken into account. This will give a different set of tags. For example should we distinguish between:

![[Pasted image 20230228122532.png]]

Commonly used tag-sets for English usually have 40-100 tags. For example Penn Treebank has 45 tags.

![[Pasted image 20230228122629.png]]

### Pos Tags in other languages
Morphologically rick languages often have compound words. But more morpho locally rich languages have equally rich tagging system given hundreds of thousands of tags.

![[Pasted image 20230228122808.png]]

Hence these techniques don't work for other languages in the same way.

### Why is POS tagging hard
Hardness comes from **ambiguity**. For example a words can be used in multiple POS tag classes.

![[Pasted image 20230228122850.png]]

Another examples is **time flies like an arrow**.

**Sparse data** is also a problem as many words haven't been seen before (at all, or in a context). Word-Tag pairs we have seen before can also be seen and so we may not know what action to take.

Many techniques are also English focused and so don't work well for morphologically rich languages and poor content languages (not so much in the way of large corpa)

### Relevant knowledge for POS tagging
Remember, we want a model that decides tags based on

![[Pasted image 20230228123145.png]]

But often clean rules may not apply well to messy colloquial language for example.

### A probabilistic model for tagging
To incorporate these sources of information, we imagine that the sentences we observe were generated probabilistically as follows. To generate a sequence of length $n$:

![[Pasted image 20230228123411.png]]

Here we are making an assumption that a) each tag depends on previous tags (we assume a bigram model) b) Words are independent given tags. So we **generate** from some start tag. Then a word is generated given a tag in the sequence. A word is generated based on a tag. These are strong *wrong* assumption made to allow the model to work. Also not we generally generate until we get stop tag.

Generally we don't use to generate data (as it doesn't work well) but in reverse this can be used to label sequences. We need **start tags** to allow the model to predict start word tags with the correct sequence.

### Probabilistic finite-state-machine
One way to view the mode: sentences are generated by walking through **states** in a graph.

![[Pasted image 20230228124105.png]]

Probs of moving from state $s$ is $s'$ is a **transition probability** $P(t_i=s'|t_{i-1}=s)$. For example given by a table like

![[Pasted image 20230228124154.png]]

Some feature are

![[Pasted image 20230228124217.png]]

We also require **emission probabilities** $P(w_i=w|t_i=s)$ as we need to generate words given the POS tag

![[Pasted image 20230228124322.png]]

This gives a table like

![[Pasted image 20230228124354.png]]

There will be many 0 probabilities for impossible combinations.

![[Pasted image 20230228124433.png]]

The labels in the rows would sum to 1.

### What can we do with this model?
If we know the transition ad output probabilities we can output the probabilities of a tagged sentence. That is given the sentence $S=w_1...w_n$ and the tags $T=t_1...t_n$. What is the probability that our probabilistic FSM would generate a sequence of words and tags we use

![[Pasted image 20230228124639.png]]

We could as the probability of

![[Pasted image 20230228124700.png]]

![[Pasted image 20230228124712.png]]

Then we can get the probabilities from the **corpus** as previously. 

### Tagging
We don't care about the probabilities but we want the tags. The **Hidden** part of the HMM. **Markov** coming from the independence assumption. With the FSM we want a sequence of states that would generate the words with the highest probability.

### Hidden Markov Model
A HMM is actual a general model for sequences Elements of a HMM are:

- A set of states (here tags)
- A set of output symbols (words)
- Initial state (beginning of sentences)
- State transition probabilities ($P(t_i|t_{i-1})$)
- Symbol emission probabilities ($P(w_i|t_i)$)

### Relationship to previous models
**N-gram model** - a model for sequences that also makes a Markov assumption but has no hidden variables.

**Naive bayes** - a model with hidden variables (the classes) but no sequential dependencies

**HMM** - a model for sequences with hidden variables

Like many other model the with hidden variables, we will use Bayes' Rule to help us infer the values of those variables. We usually assume hidden variables are observed during training - annotated data in the next class, we'll disuse what to do if we don't have training data.

### Formalizing the tagging problem
We want to find the best tag sequence $T$ for an untagged sentence $S$

![[Pasted image 20230228125413.png]]

We can then **decompose the model**

![[Pasted image 20230228125527.png]]

Then we search for the best tag sequence.  **Enumeration doesn't work** as we would have $c$ possible tags for each $n$ words given $c^n$ possible tag sequences. But we only need to keep the best for each tag in time as a lower one will never be chosen. The algorithm we will use will be the [[Viterbi Algorithm]].

[[Part-of-Speech Tagging Questions]]
Tutorial AT2.06

### Admin
Every week 3 lectures, then labs ever two weeks and tutorials every two weeks. Extra work to be done: reading (Speech and Language Processing), NLP techniques in Python. Weekly unassessed labs in python to help with concepts.

- Two **assignments** worth 25%, and an exam with 75%

### What is NLP
There are many different techniques that make up NLP and many tasks that need to be performed.  Some applications and technologies are given bellow:

![[Pasted image 20230117122427.png]]

In this course we will focus on core ideas, methods and technologies.

* Linguistic facts and issues
* Computational models and algorithms

More advanced methods and specific application areas covered in 4th/5th year courses. Classic methods at the start of this course, advanced state of that art more towards the end.

### Simple Example System
A computer provides information about train schedules:

![[Pasted image 20230117122851.png]]

What components would this system need and what problems might there be?

We need to ask what the system needs to know. There are levels of structure in languages. Humans fluently integrate all these levels of structure without caring about the level. Be we need computers to understand this too.

Levels:
- Syntax
- Parts of Speech
- Words
- Morphology
- Semantics
- Discourse

**Do we need to models all these levels in an application?** Lets look at an example
![[Pasted image 20230117123927.png]]

We might be given this and then questions like:

* Who bought a bridge?
	* Need named entry recognition, co-reference (pronoun) resolution
	* Need some inference as the fact of who bought it is never said 
	* ![[Pasted image 20230117124200.png]]
	* Even simple takes need lots of understanding
* Where will the bridge be re-built?
* How long will it take?


### Why is NLP hard?
![[Pasted image 20230117124234.png]]

##### Variability
He drew the house, he made a sketch of he house, he showed me his drawing of the house, he portrayed the house in his paintings, he drafted the house in his sketchbook.

There are many ways to say the same thing.

### Ambiguity
![[Pasted image 20230117124511.png]]

The same words can mean different things and there is an obvious use for us but the computer may not be able to understand that. **Ambiguity** also happens at many levels

![[Pasted image 20230117124632.png]]

The main way to deal with this is by using probabilistic techniques.

##### Syntactic Ambiguity
Take the phrase "I saw a girl with a telescope", one interpretation is the girl *has* the telescope or the telescope is being *used* to see. This comes down to the structure of what words relate to each other. In some canes there are many ambiguities

![[Pasted image 20230117125237.png]]

Here is an example of a large structure:

![[Pasted image 20230117125309.png]]

Syntax gleams meaning from the order of words. The reason we can't just rearrange a sentence is that is would change this syntax tree.

![[Pasted image 20230119121252.png]]

### Word Counts and Sparseness
We will look at frequencies of different words in a large corpus. Assume a "word" is a string of letters separated by spaces (simplification). Most frequent words (word types) in the English Europarl corpus:

![[Pasted image 20230119121627.png]]

Then also out of 93638 distinct word types, 36231 occur only once. For example

![[Pasted image 20230119121750.png]]

This may make it hard for our systems as many words are almost never used. If we look at the frequency of the $n$th ranked word we get (right zoomed in):

![[Pasted image 20230119121905.png]]

Another look makes it more clear when we use a logarithmic axis (also for other languages).

![[Pasted image 20230119122054.png]]

We see there is almost a linear relation between frequency and rate. This is known as **Zipf's law**.

#### Zipf's law
This summarizes the bahaviour above: $$f\times r\approx k$$For some $f$ frequency of a word, $r$ rank of a word and $k$ constant. This means regardless of how large our corpus is, there will be a lot of infrequent (and zero-frequency) words. This Infact holds for any level of linguistic structure (e.g. syntactic rules in a CFG).

This means we need to find clever ways to estimate probabilities for things we have rarely or never seen at training time.

### Robustness
This is often trickeries for NLP systems. We may train a part of speech tagger on WSJ. Which is a high quality but specific domain.

![[Pasted image 20230119122842.png]]

If we then apply this to social media it may be very hard. For example tagging

![[Pasted image 20230119122907.png]]

This has implications for fairness as it means language of certain types is overrepresented in the corpus and therefore our system works better with this kind of languages. So it may work well for whit middle aged and well educated people but may not work well for other communities.

**Relative grammaticality**: processing input of questionable grammar. For example people make grammatical errors of may not speak the language.

![[Pasted image 20230119123305.png]]

**Applications**: in practical situation there is often noise and the input is therefore ambiguous.

### Context dependence, Unknow Representation
This show the difficulty of correct interpretation is context-dependent and often requires world knowledge. Very difficult to capture this knowledge, since we don't even know how to represent the knowledge we have on its own. So we need to model context and work it into our NLP system.

### Language Diversity
We will focus on English however there are many others. The ones we build may not work well on other languages. For example there is a lot of **syntactic diversity**:

![[Pasted image 20230119123626.png]]

Or the **number of cases** for example nous are unmarked but this is different in other languages.

![[Pasted image 20230119123722.png]]

Freedom in word order and morphology are inter-related. The more freedom in the word order means les information is conveyed by word positions, more information should be included in "tokens", and this also gives a richer morphology. For example i in Russian words can be marked and then the order changes:

![[Pasted image 20230119123943.png]]

### Competence view on language
A **formal language (set) theory** may be the tool we use to model a language.

- **A language** is a set of word-sequences 
- **A sentence** is a sequence of words in the language
- **A grammar** is a formal device defining the language
- **Grammaticality** is a set of membership tests
- **Analyzing an utterance** is assigning the correct structure.

But this view is insufficient for NLP. It can be hard to bridge the gap between these abstract sets and reality for example to add in context and allow parsing based on a model of what's going on. This system may find it hard to parse uncertainty.

### Manifestations of Uncertainty
Most challenges we discussed can be regarded as manifestations of uncertainty.

![[Pasted image 20230119124400.png]]

Hence **probability** should be used to model it.

##### Not everyone agrees
![[Pasted image 20230119124453.png]]

##### Checking Probability
It has been showed every with simple 'ngram' models sentences being highly grammatical makes the far more likely.

### Dealing with uncertainty / ambiguity
With non-probabilistic methods (FSMs for morphology, CKY parse for syntax) we can return **all possible analyses**. Probabilistic models instead gives the **best possible analysis**.

##### Statistical NLP
Like most other areas of AI, NLP is dominated by statistical methods. These are typically more robust than earlier rule-based methods. Statistics / probabilities are **learned from data**. This usually requires **lots of data** about any phenomenon.

### Sketch of probabilistic model
**Functions**: Inputs e.g. set of words + context / utterances, Outputs e.g. set of POS-tags / syntactic analyzes.

**Example**: part of Speech (PoS) tagging:

![[Pasted image 20230119125307.png]]

**Model**: A probability function over the input0output pairs $$P:\text{Inputs $\times$ Outputs}\to[0,1]$$

Then given this $P$ we suppose $o_1,...o_n$ are possible outputs for input $i$. Then *how would we select the preferred output $o^\star$ for input $i$?* This is done by selecting $o^\star=\arg\max_{o\in\{o_1,...o_n\}}P(\langle i,o\rangle)$. We would need to perform more tasks to construct this model we do this as:

![[Pasted image 20230119125628.png]]

[[FNLP Introduction Questions]]
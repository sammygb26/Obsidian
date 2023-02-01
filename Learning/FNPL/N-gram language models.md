We need corpus data all the time to evaluate performance. For some tasks frequencies alone can work quite well We will consider **sentence probabilities** how likely a sentence is in a language. We will look at why they are useful and how we might compute them.

### Intuitive Interpretation
"Probability of a sentence" - how likely it is to occur in natural language. We will consider English's.

![[Pasted image 20230126171126.png]]

For example the first sentence is more grammatical and therefore more likely. In the second example the sentences mean different things and each one is more likely. In this example the semantics may educe the likelihood. This is real as English's speakers agree on probability.

### Language models in NLP
We can never know the true probability of an arbitrary sentence. But we can defined a **language model** that will give us good approximations. Like all models language models will be good at capturing some things and less good for together. 

- We might want different models for different tasks

We will look at **N-gram models**.

##### Spelling Correction
Sentence probabilities can help us decide selling. For example we may have the misspelled text "no much effort". The word is a correctly spelled one but the sentence is still wrong. We want to look at different examples that may be what we want

![[Pasted image 20230126171653.png]]

The **language model** takes our *error model*'s different values and give you the correct one. In this case the best case is "not much effort". We combine the likelihood of the error with the likelihood of the sentence to get the overall likelihood of a sentence.

##### Automatic Speech Recognition
This is another example where we want to disambiguate some heard sentence. An **acoustic model** decodes the sound into possible sentences.

![[Pasted image 20230126172006.png]]

Then our language model gives us the best guess "She studies morphosyntax". Again this may require general knowledge to do properly.

##### Translation
![[Pasted image 20230126172220.png]]

Again here a **translation model** gives results and we use a language model to get a best guess.

### LMs for prediction
LMs can be sed for **prediction** as well as correction. Predictive text correction / completion on mobile phones are used here (error model includes model of keyboard interaction and predicts as you are typing).

In this case, LM may be defied over sequence of characters instead of a sequence of words. We will have LMs are the character and word level (looking at other words and context).

### Estimative Probabilities
We want to know the probability of a word in a sequence $\vec w=w_1...w_n$ occurring in English. We assume we have some **training data** (large corpus of general English text). We can use this data to **estimate** the probability of a sequence of words.

### Probability theory vs estimation
In simple examples we can know the true examples. But in a corpus we can't calculate the true probability and we don't know the true counts.  In reality we make observations of some hidden true corpus, **evidence**. 

![[Pasted image 20230126173331.png]]

We need estimation theory for this. We assume the data (relative words and proportions) are **representative** of the true language. We are estimating the **latent variable** of the proportion of red and blue values. But if we miss any values this simple  solution can becomes hard.

Infact machine learning is quite bad an unawareness and they perform badly in scenarios where some new space is found. Probability theory assumes we know the state space but we don't care about the overall space. We simple graft spaces together. But we **assume we know the hypothesis space**.

### Notation
$P(x)$ will be taken to mean $P(X=x)$. We will also use $P(x)$ for the true probability, $\hat P(x)$ as the *estimated* probability. Then $P_E(x)$ for the estimated probability using a particular estimation method $E$.

### Example estimation: M&M colors
We may ask, what is the proportion of each color M&M? In 48 packages we have 

![[Pasted image 20230126173957.png]]

To estimate the probability from this data we use **relative frequency estimation**.

## Relative Frequency Estimation
We take the proportion of some color over the total. This is given as $$P_{RF}(x)=\frac{C(x)}{N}$$ where $C(x)$ is the count of $x$ in a large dataset, and $N=\sum_{x'}C(x')$ is the total number of items in the dataset. This is also called a **maximal likelihood estimate**, both are equivalent. 

- A problem is zero count words. Especially with small Corpuses. Hence any sequence constraining some zero word is 0. But this isn't impossible its just low likelihood.

##### MLS for Sentences
We can apply MLE to estimate the probability of $\vec w$ as a sentence of English? That is the probability that some sentence $S$ has words $\vec w$. This may be given as $$P_{MLE}(S=\vec w)=\frac{C(\vec w)}{N}$$where $C(\vec w)$ is count of $\vec w$ in a large dataset, and $N$ is the total number of sentences in the data.

##### Sentence that never occurred
![[Pasted image 20230126174613.png]]

Both these sentence have count zero. The former is rare but more likely than the latter as the grammar makes sense. Hence they should not both be zero. IN many cases the corpus is too small for the combinatorial large number of letters.

Again it may also think things that have never occurred will never occur. But his is false in reality. 

![[Pasted image 20230126174826.png]]

These example may all never happen but shouldn't have likelyhood 0.

##### Sparse data
In fact, even things that occur once or twice in our training data are a problem. Here are words that all appear only once in Europarl:

![[Pasted image 20230126174941.png]]

All occurred once but they may not all have equal probability.

### Towards better LM probabilities
One way to try fix this problem is to estimate $P(\vec w)$ by combining the probabilities of smaller parts of the sentence which will occur more frequently. This is the intuition behind **N-gram language models**.

We want to estimate $P(S=w_1...w_m)$. This is really a joint probability over the words in $S$. $P(W_1=w_1,W_2=w_2,...W_4=w_4)$.  We can apply **bayes rule** to break this down.

![[Pasted image 20230126175403.png]]

This is always true. The probability of the sentence if the probability of each word give the previous sequence.

![[Pasted image 20230126175521.png]]

The problem is the conditional probability we get are still just hard to derive for MLE.

### Deriving an N-gram model
In a unigram word we make an independence assumption that all words are independent. As we move up to higher $n$ we assume less independence.

![[Pasted image 20230126175909.png]]

For an N-gram model we assume any word is conditionally independent of all words behind the last $n$ given the last $n$ (including the last word so would be $n-1$). Word selections are mode likely as we take less words in a row.

We have a tradeoff between the **problem of sparse data** and quality of our estimates.

### Trigram Independence Assumption
Put another way ,trigram model assume these are equal

![[Pasted image 20230126180239.png]]

This may not always be a good assumption.

### Estimating Trigram Conditional Probs
We still need to estimate the conditional probabilities. The probability of the third in the context of the previous two words. Using MLE we consider out all all cases where we saw before first word the other two quat proportion contained different words. The count can still be 0 for many values and so this isn't enough for sparse data! Smoothing can be used to overcome this.

![[Pasted image 20230126180623.png]]

More generally

![[Pasted image 20230126180635.png]]

![[Pasted image 20230126180652.png]]

In a **unigram** model we consider all words.

![[Pasted image 20230126180751.png]]

### Trigram model: Summary
To estimate $P(\hat w)$ we use chain rule and make an independence assumption

![[Pasted image 20230126180934.png]]

Where we estimate the probabilities to be

![[Pasted image 20230126181002.png]]

##### Practical Detail
Sentence boundaries can change the probability of different sentences. The above model doesn't capture this. A way around this is to treat the beginning and end of sentences are tokens.

**![[Pasted image 20230126181218.png]]**

We instead take

![[Pasted image 20230126181238.png]]

We add two tokens to deal with **trigram** models. We don't use punctuation as it is *ambiguous*. 

Negative log probs are used as floating point probs are hard to work with.

[[N-gram language models questions]]
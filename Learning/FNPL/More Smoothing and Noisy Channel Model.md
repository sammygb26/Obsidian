Again smoothing helps solve the problem of 0 counts in the training data.

### Problems with Good Turing
We don't know the vocabulary size. So how should we assign values when we don't know the number of words. We can use UNK for unknown as a word in our counts. For a bigram with will add two probabilities for each other word and UNK-UNK.

Good Turing doesn't allow "holes" in the counts $N_i>0\implies N_{i-1}>0$. But we can estimate this with linear regression. 

We also need values for high frequency items but that can be get using discounts.

### Another Problem
We assign the same probability to all unseen values. But we can separate them by if they contain likely bigrams or only unlikely bigrams for example.

![[Pasted image 20230131122259.png]]

These may not be seen but shouldn't get the same probability. There are two ways to deal with this **interpolation** and **backoff**.

### Interpolation
Here we **combine** higher and lower order N-gram models, since they have different strengths and weaknesses.

![[Pasted image 20230131122430.png]]

Then finally we take our final probability to be a weighted combination of the other models.

![[Pasted image 20230131122509.png]]

We must measure the lambda's sum to one as otherwise there won't be probabilities. But we may still want to vary how we combine the different models.

![[Pasted image 20230131122736.png]]

### Fitting Interpolation Parameters
In general this weighted distribution is called a **mixture model**. The lambdas are the **interpolation parameters** or **mixture weights**. The values of the lambdas are chosen based on testing on the development set.

### Katz Back-Off
This solves the problem in a similar way to **Good-Turing**. We discount the trigram probability estimates. This leaves space to add in the bigram model.

![[Pasted image 20230131123152.png]]

This is similar to Good-Turing discount but instead of distribution the mass uniformly over unseen items we use the backoff estimate.

![[Pasted image 20230131123325.png]]

When we have a zero count for the trigram we back-off and use the bigram model. Then from the bigram we may back off to a unigram. We can still use Good Turing on $P^*$ to make room for the bigram. Again we need back-off weights to ensure probabilities sum to 0.

### Do our smoothing methods work here?

![[Pasted image 20230131123852.png]]

The problem is **multi-word expressions**. The problem is we back of to a bigram and our bigram will be dominated by sequences like "you-see". To backing off will make our model keep repeating "you see".

Another example is York. So it comes up a lot of a context but often with New and so New York is overrepresented.

### Kneser-Ney Smoothing
This takes diversity of histories into account. We count the distinct histories

![[Pasted image 20230131124408.png]]

Then instead of using MLE with

![[Pasted image 20230131124431.png]]

In KN smoothing we replace raw count with count of histories

![[Pasted image 20230131124454.png]]

##### In Practice

### Word Similarity
We may have some words with $C(w_1)>>C(w_2)$ say

![[Pasted image 20230131124542.png]]

But these are similar things so their probabilities should inform each-other. But this doesn't happen with n-grams.

**Class-based models** is a way to deal with this were we define a class for a word.

![[Pasted image 20230131124656.png]]

A recent version is **distributed** language models

![[Pasted image 20230131124723.png]]

#### Distributed word representations
Each word represented as a high dimensional vector

![[Pasted image 20230131124805.png]]

Similar word are represented by similar vectors

![[Pasted image 20230131124827.png]]

The hypothesis is the distance after training between word vectors is a measure of the similarity of the words.

This is called **distributional** embeddings as we look around the word 

### Training the Model
We want to learn representations (**embeddings**) such that words that behave similarly are close together in high-dimensional space.

![[Pasted image 20230131124945.png]]

N-gram LM collect counts, maybe optimize parameters but this is quick. But in distributed LM learning the reorientation of each word can take a long time. But learned embedding capture both semantic and syntactic similarity. These methods are more secure.

(quine and whickenstien)

### Using the model
If we want to compute $

### Noisy Channel Model
We image that someone tries to communicate a sequence to us, but noise is introduced. We only see the output sequence.

![[Pasted image 20230131125353.png]]

![[Pasted image 20230131125416.png]]

##### Spelling Correction Example
$P(Y)$ will be the distribution over the words the user indented to give / type. Which is a language model. $P(X|Y)$ is a distribution escribing what user is **likely** to type given what they meant. Could incorporate information about common spelling errors, key positions, etc. This is called a **noise model**. $P(X)$ is the resulting distribution over what we actually get.

Mathematically what we want is $\arg\max_y P(y|x)$. What should $y$ be given what we got. We can rewrite given bayes as

![[Pasted image 20230131125925.png]]

##### Noisy Channel as Probabilistic Inference
To recover $y$ best we need a language model (different for different applications) and a noise model (depends on application). We train both on corpus data.


We can train $P(X|Y)$, but why can't we just train $P(Y|X)$. But our language model is much easier to train as we have much more training data for it.

![[Pasted image 20230131130144.png]]
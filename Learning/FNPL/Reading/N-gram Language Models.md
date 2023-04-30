**Language Models** allow s to assign probabilities to sentences. This can be useful and allows us to rank sentences possibilities by their likelihood. This can help resolve ambiguity in many areas. For example *speech recognition* or *translation* there may be many interpretations of an input selecting the most probably one will give the best results.

**N-grams** are sequences of $n$ words. For example a 2-gram (bigram) may have (I, was), (was, going), (going, to), (to, the), (the, shop). An **N-gram language model** assigns probabilities to each of these n-grams. So in the bigram case we have $p(w_2|w_1)$ which is the probability of the next word given the first.

## N-Grams
We might consider the probability of a given word given the previous words. For example $$P(the\mid\text{its water is so transparent that})$$We can estimates this with a large corpus by the counts of the sequence "its water is so transparent that the" compared to "its water is so transparent that". $$=\frac{C(\text{its water is so transparent that the})}{C(\text{its water is so transparent that})}$$The issue is for many sentences we would need a truly **titanic** corpus to get the counts required. To estimate the probability of an entire sentence this way we would have to calculate a massive denominator of all possible sentences of a given length. One way to simplify this is to decompose with the **chain rule**. $$P(w_{1:n})=P(w_1)P(w_{2}|w_1)\dots P(w_{n}\mid w_{1:n-1})$$This will be the same as $$=\prod_{k=1}^nP(w_k|w_{1:k-1})$$Now that we can break a joint probability distribution down into the conditionals this way we need to calculate the conditionals. But many context may have never arisen before with long sequences of preceding words. Instead we can **approximate** a conditional probability as the condition given the last few elements. If we make a **bigram** model this will be the last two words. So $$P(w_n\mid w_{1:n-1})\approx P(w_n\mid w_{n-1})$$This assumption that the probability on depends on a previous words is a **Markov assumption**. We are basically assuming we can ignore the past at some point. For an N-gram we make the assumption $$P(w_n\mid w_{1:n-1})\approx P(w_n\mid w_{n-N+1|n=1})$$The word sequence probability for a **bigram** is therefore $$P(w_{1:n})=\prod P(w_k\mid w_{k-1})$$So we can build a language model just estimating 2-grams (:$$P(w_n\mid w_{n-1})=\frac{C(w_{n-1}w_n)}{\sum_{w'}C(w_{n-1}w')}=\frac{C(w_{n-1}w_n)}{C(w_{n-1
})}$$We will generally also add the $<s>$ tags to indicate the start of a sentences and $</s>$ to indicate the end.

Generally the **relative frequency** is used to find the probabilities. This will be the count of the prefix plus the additional character divided by the count of the prefix. Hence why it is called *relative*. This maximizes the likelihood of the training data given the model.

##### Practical Issues
Generally **trigrams** or higher order n-grams are used. We need to add some padding at the beginning of a sentence for example adding $P(I\mid <s><s>)$ in the case of the first word for a trigram. Generally also **log probabilities** are used. This prevents the numbers for getting too small and us getting an arithmetic underflow.

## Evaluating Language Models
The best way to do this is to put the language model into an actual application and then measure how much this improves the application. This is called **extrinsic evaluation**. So for spelling detection what we measure is if the new LM improves spelling detection.

Instead of this extrinsic way we want a cheap quick way that measures the LM on its own. For this we can use **intrinsic evaluation**. For this we will test the model on a **test set** which is a portion of data it hasn't trained on. To compare two models we train them on the training data and test them on the test set. We say a model *fits the test set* more if it assigns a higher probability to the data. We want to ensures this test data is separate from training data to ensure we are measuring how well our model will perform on data it wasn't trained on like for example when it is actually used

We can also use a test set so much we train hyper parameters to fit it. For this reason hyperparameter training is done on a **dev set** and we only evaluate on the **test set** when there are no more adjustments to be made.

#### Perplexity
The *perplexity* is generally used instead of the raw probability of a sentences. This is the inverse probability normalized over the number of words. So $$\text{perplexity}(W)=P(w_1w_2\dots w_n)^{-\frac1n}$$With the chain rule this can become $$\text{perplexity}(W)=\sqrt[n]{\prod_{i=1}^N\frac1{P(w_i\mid w_{1:i-1})}}$$and simplifies even further with a n-gram. This measure is inverse so the higher the probability the lower the perplexity. A perplexity of $1$ is the minimum for a maximum probability of 1. When calculating this $</s>$  is used at the end of the sentence so we add 1 to the length and then use $<s>$ padding at the start.

This can also be through of as the **average weighted branching factor**.  We are taking an average through a multiplicative space hence why the root is used.

Different language models have different perplexities and so it can be used to compare them.

![[Pasted image 20230415112907.png]]

We must ensure the same training and vocabulary is used between the models otherwise we cannot be sure we are comparing the different architecture but the training data's coverage of the test set. Then an improvement here may not always give an improvement in **extrinsic** performance.

## Sampling Sentences from a language model
This is one of the ways we can visualize the kind of knowledge a model embodies. We a choosing words according to their likelihood here. We are more likely in this scenario to pick sentences the model things are likely rather than not likely. For a unigram model each word will take up a portion of probability space. To sample a word we pick a uniform number between 0 and 1. Then we select the word that lies in that area.
![[Pasted image 20230415113517.png]]

## Generalization and Zeros
As we increase $N$ the N-gram will perform better on the corpus. For example 

![[Pasted image 20230415113711.png]]

We see the larger the N-grams used the better the model performs. But by the fourth N-gram sentences are being taken directly from Shakespeare's works. The dataset isn't too large and so by the 4th n-gram we have a sparsity problem and must memorize the data. We can do the same things with another dataset for example WSJ

![[Pasted image 20230415114050.png]]

We can see that the corpus we use highly affects what language our model things is likely. The corpus we use highly affects the eventual distribution of our data. This can include the type of language the model is modeling be it questions or legal documents as well as the dialect.

Even with the correct corpus we still have the problem of **sparsity**. Where some valid n-grams will just no occur in the language.  There is a combinatorial large number of n-grams for a given n-gram length and so we will always miss out. Any sentence with any unseen n-grams will have probability 0 and so we can't give a perplexity for it.

#### Unknown Words
We can also ask the question what is to be done with unknown words. One option is to disallow unknown words and use a **closed vocabulary**. Usually we have to deal with these **out of vocabulary** words. One way to do this is to add a pseudo-word called $<UNK>$.

One way to get probabilities for this tag is to use a fixed vocabulary then any word in training that isn't contained we convert to UNK. We then estimate as if UNK was a word. We could also replace all words seen only 1s for example with UNK. One thing to note is a LM get get low perplexity with a high number of UNK tags. So LMs should only be compared with the same vocabulary.

## Smoothing
We still have a problem of zero counts as known words may occur in a scenario we haven't seen in training. Instead we can move probability mas from seen n-gram to unseen ones. This is called **smoothing** or *discounting*.

#### Laplace Smoothing
Here we just add 1 to all the counts as if we had seen everything once twice etc.$$P(w_i)=\frac{c_i}{N}\hspace{16pt}\to\hspace{16pt}P_{\text{Laplace}}(w_i)=\frac{c_i+1}{N+V}$$We can also think of this as making an **adjusted count** $c^*$ which will make it easier to compare to MLE. After normalizing this count with $N$ we want the whole thing to be $\frac{c_i+1}{N+V}$. So we can make it $$c^*=\frac{(c_i+1)N}{N+V}$$Our bigrams may then look like

![[Pasted image 20230415134216.png]]

We can look at the ratio of the old probs to the new ones.

![[Pasted image 20230415134426.png]]

We see that many probs have been changed massively. We are moving a lot of mass to 0s and so the probabilities change a lot.

#### Add-k smoothing (lidstone)
Here we add a fractional amount for example $0.05$ to every count. For example $$P^*_{\text{Add-}k}(w_n\mid w_{n-1})=\frac{C(w_{n-1}w_n)+k}{C(w_{n-1})+kV}$$$k$ is a hyperparameter and so will be tuned on a **devset**. Even with this we have just scaled back the problem and have scaled up the old problem by doing it.

#### Backoff and Interpolation
Instead of adding counts to unseen say tri-grams we could instead use the knowledge encode by a bigram-model which may include the value. We can use **less context** but this is still better than treating the value as UNK. There are two ways to integrate data from smaller models 1) **Backoff** and 2) **interpolation**.

##### Linear Interpolation
This is the simples approach. For $k$ different $n$-gram models we have $k$ parameters $\lambda_1\dots\lambda_k$ which all sum to 1. This way we can have our probability as a weighted sum of ngrams at different levels.

![[Pasted image 20230415135313.png]]

Another way this can be done it to compute $\lambda$ weights conditioned on the context. This way we if one context has particularly accurate counts it will get a better scores.

![[Pasted image 20230415135505.png]]

In both cases we learn the lambdas from a **held-out** dataset. We can fix the probabilities then calculate optimal $\lambda$ values. Then to the reverse making use of th **Expectation Maximization**. 

##### Katz Backoff
We have to estimate the probability for an $n$-gram by backing of to first a $n-1$-gram and so on. We need a **discount factor** for each backoff so that when we do move to a "zero" count replacing it with a non-zero value doesn't cause the total probability to be greater than 1. This is defined as

![[Pasted image 20230415140643.png]]

Katz backoff is combined with a smoothing method called **Good-Turing**.

##### Good Turing
The basic idea here (and with many other discounting smoothing techniques) is to use the count of things you've seen once to estimate the count for things you've bever seen. The algorithm is based on $N_c$ which will be the number of n-grams occurring $c$ times. Formally defined as $$N_c=\sum_{x\in V}\mathbb 1_{count(x)=c}$$We are estimating $N_0$ with $N_1$ so the GT algorithm replaces the count $c$ with a new count based on the count in $c+1$. So we get $$c^*=(c+1)\frac{N_{c+1}}{N_c}$$here for the $N_c$ n-grams occurring times each occurs $c$ times. This means the total occurrences in that class will be $cN_c$ or $c$ times for each class. We can then calculate the probability for some element in $N_c$ being found according to GT to be $$P^*_{GT}(x)=\frac{(c+1)N_{c+1}}{N_cN}$$
##### Kneser-Ney Smoothing
This has its roots in a discounting method called **absolute discounting**. If we look at some counts from GT we can see the motivation.

![[Pasted image 20230417172349.png]]

We see that apart from the low counts we can approximate the change just by subtracting 0.75 from the counts. In *absolute smoothing* this is what we do and we take away a constant $D$ from each count and then pick a coefficient $\alpha$ such that all the probabilities sum up.

![[Pasted image 20230417172531.png]]

This is still a **back-off** model.

**Kneser-Ney** - Here the issue is **multi-word-expressions**. There are words that are very common  together but no so much apart. If we have some word following a context we haven't seen before then if that word is mostly seen in a multi word expression we should probably discount its probability. We divide the number of context a word occurs in by the total number of contexts.

![[Pasted image 20230417173529.png]]

### Class Based N-grams
The basic idea here is if words are similar in meaning can we draw on the common situations those words appear in? For example the word Salmon and Trout. Say one is rare in our corpus but we know they are both fish. Perhaps is reasonable to say "I caught a trout" if we see many "I caught a salmon". The simples way to do this is with **IBM clustering** which is a type of **hard clustering**. Basically we treat the sentence as a sequence of classes and a word only exists in one class. We then predict the word's frequency based on the probability of that words class given the previous word and the probability of the word given its class. So $$P(w_i\mid w_{i-1})\approx P(c_i \mid c_{i-1})P(w_i\mid c_i)$$Where for a corpus with labeled classes and words we can estimate $$P(w\mid c)=\frac{C(w)}{C(c)}\hspace{64pt}P(c_i\mid c_{i-1})=\frac{C(c_{i-1}c_i)}{\sum_c C(c_{i-1}c)}$$For this type of clustering we would build the class by hand for a given domain. Generally a better way to do this would be with **distributional semantic** which is how modern NLP systems work.


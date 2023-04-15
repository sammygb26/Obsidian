This will allow us to move from *sparse* vector representations to **embeddings** which are dense have 50-1000 parameters rather than tens of thousands. There generally work better possible due to reduced overfitting and an increased ability to capture synonymy. One way is the **skip-grams with negative sampling** also called **SGNS**. This is part of a software package called **word2vec** and so if often referred to as word2vec. These are **static embeddings** and are always the same unlike **contextual embeddings**.

The key idea is to instead treat this problem as a classification task and educe a vector representation to do this. That is we train a classifier to predict if a word should occur based on a given context. The weights learned by the model will be the vector embedding of our words. We use any content as implicitly supervised training data. For each word we get a context from surrounding words and train our representation. The true missing word is the **gold label**. This is often said to be a form of **self-supervision**. 

### The Classifier
We will pick a **context window** say two words on either side. Then we will predict our word in this case *apricot* based on the other words

![[Pasted image 20230411210236.png]]

We will train our classifier such that, given a tuple $(w,c)$ of a target word $w$ paired with candidate context word $c$ will return the probability that $c$ is a real context word. $$P(+\mid w, c)\hspace{64pt}P(-\mid w, c)=1-P(+\mid w, c)$$As in [[Pointwise Mutual Information]] and [[Cosine for Measuring Similarity]] we can take the probability $P(+\mid w, c)$ to be heigh when $w$ and $c$ are similar. We can use the **dot product** for this (cosine is only a normalized dot product). We can then take the **sigmoid** function and compute $$P(+\mid w, c)=\sigma(\mathbf c\cdot\mathbf w)=\frac1{1+\exp(-\mathbf c\cdot \mathbf w)}$$This will make our negative probability $$P(-\mid w, c)=1-P(+\mid w, c)=\frac1{1+\exp(\mathbf c\cdot\mathbf w)}$$The **Skipgram** makes the assumption that all context words are independent and so $$P(+\mid w, c_{1:L})=\prod_{i=1}^L\sigma(\mathbf c_i\cdot\mathbf w)$$$$\log P(+\mid w, c_{1:L})=\sum_{i=1}^L\log\sigma(\mathbf c_i\cdot\mathbf w)$$
**Skipgram** - Skip-gram train a probabilistic classifier, that given a test target word $w$ and its context window of $L$ words $c_{1:L}$ classifies this word based on how similar the context vectors and target vector are. The parameters learned will be $\theta$ as in

![[Pasted image 20230411212157.png]]

### Learning skip-gram embeddings
The basic idea is to initialize two matrices with $|V|$ vectors each to random values. Then we slowly shift the embedding of each word $w$ to be more like the embeddings of words that they occur nearby. We will walk through different target words and contexts in our corpus while training the classifier. For example 

![[Pasted image 20230411212539.png]]

The target work is "apricot" and the contexts words surround in in a $\pm2$  window. We can then generate $+$ and $-$ example as

![[Pasted image 20230411212753.png]]

For **SGNS** we have more negative samples than positive example the number will be set with a parameter $k$. So $k$ negatives for each positive. For this we have a window of random words $c_{neg}$ from the lexicon which are only constrained to not be the target word. Above we have $k=2$. The random choice is generally don via a weighed unigram probability $$p_\alpha(c)=p(c)^\alpha$$generally with $\alpha=0.75$. This just heightens how much rare words are used as negatives. We want to 

- Maximize the similarity of the target word to context words pairs for positive examples
- Minimize the similarity of the negative pairs

We will make a loss to be minimize which will accomplish this. This will be $$L_{CE}=-\log\left[P(+\mid w,c_{pos}\prod_{i=1}^kP(-\mid w,c_{neg_i})\right]$$$$=-\left[\log\sigma(c_{pos}\cdot w)+\sum_{i=1}^k\log\sigma(-c_{neg_i}\cdot w)\right]$$from the definition of $P(+\mid w, c)$. We need a gradient of this to perform **stochastic gradient descent**.

![[Pasted image 20230411220341.png]]

The derivatives will be 
![[Pasted image 20230411220425.png]]
Which will make the SGD updates
![[Pasted image 20230411220526.png]]
To make the updates we randomly initialize $W$ and $C$ matrices and then walk through the training corpus using gradient descent to move $W$ and $C$ as to minimize the loss. Generally $L$ is turned on a dev-set for best results.

### Other Kinds of Static embeddings
There are other kinds of embeddings **fasttext** addresses the problem of unknown words in word2vec. It also deals with scarcity in morphologically rich texts using sub-word models. Here words are represented by sub-words with special boundary symbols $<$ and $>$ added to each word. For example with $n=3$ for where we have

![[Pasted image 20230411221222.png]]

The embedding is learned for each constituent n-gram and the word is a sum of the embeddings for its constituent n-grams.
NNs take in vectors, so we need to **vectorize** our data for the NNs to interact with. We turn a sentence into a sequence of vectors. When we define an embedding we have a matrix the height of our vocabulary and width of our embedding space. 

![[Pasted image 20230403115021.png]]

There are different ways to do this.

##### One Hot
Here each word is given a column and each word just has one number set to 1 and the rest to 0. The 1 is in the column for that word. But this doesn't capture **similarity** and is **memory intensive**.

##### Latent Semantic Analysis
Here we have a context ($L$ sized window around the word) we then make a word's embedding as a count for each word through the corpus. We then approximate this matrix with $SVD$. Two matrices and a correlation matrix. (Word vectors and context vectors). The $d$ dimension is the size of these matrices which we control (not vocabulary or corpus size). We can then compute a truncated version of this. But NNs are more computationally available.

This is more general than just context instead it allows documents to be related to words and so describe their meaning.

### Prediction-based (neural) methods
Here from a word we define a probability distribution over words after and before. We shift this through the corpus predicting words. This si called **Mikolov's Skipgram** but there are variations. This can also predict in reverse for a different model.

We use our **central** and **context** matrices (both of height of the context size). We then want to combine these to get our probabilities. For example $$P(o|c)=\frac{\exp(u_o^Tv_c)}{\sum_{w\in V}\exp(u_w^Tv_c)}$$We don't use cosine as it is hard to optimize with NN backprop. Exponentiating and normalizing gives us a probability distribution. We are **soft-maxing** over the dot product between the vectors. 

![[Pasted image 20230405115606.png]]

For a context likelihood we compute dot products for each context word with the central word. This assumes all words are independent given the central word. In log space this loss will become

$$J(\theta)=-\frac1T\log L(\theta)=-\frac1T\sum_{t=1}^T\sum_\underset{j\neq0}{-m\le j\le m}\log p(w_{t+j}\mid w_t,\theta)$$

This is trained in the same way as [[Text Classification  - Logistic Regression]]. In practice we optimize one word at a time so we don't need all data in memory. So we use a **batch** based back prob progression.

### Optimizing the model
Our loss for a single word say *cute* and *cat* will be

![[Pasted image 20230405120245.png]]

This basically comes out to make. Closer words have larger dot products and since we are overall taking the $-\log$ of this we will make vectors in the same context closer and other further away.

A problem with this is there are many words in the vocabulary and so it is expensive to compute the denominator. To get bast this we use a random sample of the vocabulary.

### Relation to LSA
We can show that optimizing the Skipgram objective with negative sampling modification we are approximating the truncated SVD.

![[Pasted image 20230405120757.png]]

### Classification
![[Pasted image 20230405120827.png]]

##### Logistic Classifier
We convert a sequence of words to a embedding. So we have $h$ feature vectors for each word. For each class we have a vector for example.  We then dot product with the vectors add on a bias and then apply SoftMax to get a probability distribution.

![[Pasted image 20230405121014.png]]

##### NN Classifier
Here we don't have a vector for each class defined. Instead we define a NN. This produced features for which we apply a linear layer as before. In this sense when we train the system to predict words we are making the vector representation of words we produce similar to the vector representation of the class.

A well trained classifier will align these vector representation of the documents. In general this means further away from 0 the confidence will get more likely.

### Neural Models for Text Classification
We have covered the output of the NN but how does the vector work. One option s to sum vector together.

![[Pasted image 20230405122734.png]]

We may calculate these with Word2Vec model or something then we add it all together but this is almost not a NN. A problem is this adds the same weight to informative and non-informative words. Another way is to introduce a weight which increases word strength based on how informative the word is. we will take the inverse document frequency.

![[Pasted image 20230405122829.png]]

One way to do this is with **term-frequency** and **inverse-document frequency**. So we scale up frequent words but reduce word weighting if they are frequent in the corpus. The IDF looks like $$\log\frac{|D|}{|\{d\in D: w\in D\}|}$$then TF would just be the number of times the word occurs in the document.

[[Neural Embeddings Questions]]
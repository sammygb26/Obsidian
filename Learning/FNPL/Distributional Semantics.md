Again we will look at questions answering. If we have a question "What is a good way to remove wine stains?". The text available may be "Salt is a great way to eliminate wine stains." But the words used are not the same. So "remove" is replaced by "eliminate" and "good" with "great". We need a notion of **similarity** and **gradation** to cover these meanings.

### Thesaurus
This is one way to get a list of words meaning the same thing. It doesn't exist for all languages and even if we do have one many words and phrases will be missing. We would want the similarity automatically.

### Meaning from Context

![[Pasted image 20230403095419.png]]

### Distributional Hypothesis
Perhaps we can infer meaning just by looking at the contexts a word occurs in and maybe the meaning IS the context a word occurs in (Wittgenstein!). Either way similar context lead to similar meanings. This is called the **distributional hypothesis**.

- **Distribution** : a polysemous word - Can mean probability distribution but in linguistics it is the set of context a particular item has.

## Basic Idea
Represent each word $w_i$ as a vector of its contexts. Distributional semantic model also called **vector-space models**. Each dimension is a context work; = 1 if it co-occurs with $w_i$ otherwise 0. This is like a word association matric. Generally these will be very sparse with a lot of 0s!

![[Pasted image 20230403100429.png]]

We should ask what defines context? and so what we should consider co-occurrence. 

- **First-order co-occurrence** (syntagmatic association) - Nearby each other
- **Second-order co-occurrence** (paradigmatic association) Have similar neighbors

##### Defining the context
We usually ignore **stopwords** (function words and other very frequent low information words). Both lar (100 words) and small contexts (5 words) are possible. You can consider relation other than cooccurrence in sequence for example dependency relation from parser for example words in the syntax structure that are connect directly - but not in space.

- Large context defocus and we may look at context. Then small context could get finer details like POS tags.

All of these are used to define *semantic similarity*.

### How to weight the context words
Binary indicators are not very informative with more frequency cooccurrences mattering more. Ut is frequency good enough - frequent words are expected to have higher cooccurrence than chance.

### Collocations
The idea behind collocations allows us to how often some context includes a word $w$. We ask what **collocations** include $w$.

### Mutual Information
**Pointwise mutual information** is one way to capture this. We divide the probability of them occurring together $P(x,y)$ with them occurring independently $p(x)p(y)$. $$PMI(x,y)=\log_2\frac{p(x,y)}{p(x)p(y)}$$But this is still sensitive to chance occurrence of infrequent words. 

![[Pasted image 20230403103456.png]]

Mathematical reason:

Individual probabilities are low when when elements are infrequent. The relative different compared to the joint destitution makes the numbers so high.

### Alterative to PMI for finding collocations
There are a **lot** of way of measuring statistical (in)dependence.

- Student t-test
- Persons $\mathcal X^2$ statistic
- Dice coefficient
- likelihood ratio
- Lin association measure
- and more!

Improvements to PMI are possible with smoothing weighting, discarding negative elements and so on.

### How to measure similarity
So we have context vector for two words $\vec v$ and $\vec w$ but how do we find their similarity.

##### Vector Space Representation
In 2-dim space $cat$ and $dog$ will be closer than $computer$ for example. So for example Euclidian distance could be used to measure similarity. But it doesn't work well in high dimensions.

Another way s to take a dot product. But this depends on the norm a lot. But more frequent words will swamp out important words as they contribute much more to words.

### Normalized dot Product
Some vector are longer than others (have higher values). I vector is context word counts, these will be *frequent* words. If vector PMI values these are likely to be *infrequent words*. We divide by the length **normalizing**. Now out measure will be the $\cos$ between the two vectors.

### Other Similarity Measures
There are also alternative

- Jaccard measure
- Dice measure
- Jenson-Shannon divergence
- etc

These work better or worse in different contexts.

## Evaluation
Extrinsic may involve IR (information retrieval), QA automated essay marking etc. But this is hard and may require many benchmarks to truly show a methos is better or worse Intrinsic is often a comparison to psycholinguistic data. Relatedness judgements and word associations

### Relatedness Judgements
Here participants are asked on a scale of 1-10 how related are the following concepts


But this can be quite poorly defined and the wording of the task can change the results massively. Plus there is a lot of difference despite humans all talking the same.

Language is also learned through interaction and not just expose (poverty of stimulus argument). Learning about this is a good use for relatedness judgements as they change over time.

### Word Associations
Here participants see or hear a word and say the first word that comes to mind. Data collected form lost of people provide probabilities of each answer. This still may not capture what understanding would be


### Comparing to human data
Human judgments provide a ranked list of related words/ association for each word $w$. Computer system provide a ranked list of most similar words $w$. Compute the Spearman rank correlation between the lists (how well to do the rankings match and then we report on differences).

## Learning a more compact space
So far, our vectors have length $V$, the size of the vocabulary. But we may not need all these dimensions. Or learn to map a high dimensional space to a lower dimensional space may capture similarity in a more natural way.

### Latent Semantic Analysis (LSA)
The idea is to take a large matrix and decompose it into **word vectors** and **context vector**. Rank center matrix which will be a diagonal matrix. These are also called word and context *embeddings*. These can be obtained via SVD and get the same values in the closest possible way (Frobenius norm).

![[Pasted image 20230403112344.png]]

The idea is this will work as well if not better than the original space. Smoothing may also be applied automatically as detailed small counts are lost.

This is hard however as the matrix is massive and standard methods don't work.

### Neural Network Methods
More recently NNs have been used for dimensionality reduction. We train a NN to predict context words based on input word. We use hidden layers as the input word's vector representation. Some forms are closely related to LSA (they are connected Levy and Goldberg, 2014) but more scalable. These embeddings are often used to initialize NNs and used for supervised embeddings of words.

##### In Practice
Very hot topic in NLP. Embeddings seem to capture both syntactic and semantic information. So,  used for language modeling and to replace words as observations in parsing and there models. They can provide a kind of similarity based smoothing.

## Compositionality
One definition of collocation: **non-composition** phrases. So more than one word contributes to the meaning and so does context

![[Pasted image 20230403113617.png]]

We want to compute compositionality in vector space.

We might apply operations such as vector addition tensor product nonlinear combination etc.

[[Distributional Semantics Questions]]
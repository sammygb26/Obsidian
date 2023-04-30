What is a distribution in linguistics?  #flashcard #FNLP #VectorSemantics
	A distribution of a word is the neighborhood or grammatical environments that word is found in.

---
What is the distributional hypothesis?  #flashcard #FNLP #VectorSemantics
	This is the idea that a words **distribution** context and grammatical environment its found in give a word its meaning.

---
Why is it useful to represent words as embeddings?  #flashcard #FNLP #LexicalSemanticsQuestions 
	Representing words as embeddings allows the many dimensions of the embedding can combine to encode the different ways a word can be similar and different from other words. But having a unified meaning allows many simple operations to be used to query the representations. For example querying the connotations of a given word or asking what a word is related to.

---
What is a term-term and term-document matrix when applied to capturing the distribution of a word?  #flashcard #FNLP #LexicalSemanticsQuestions 
	Here we are trying to capture the meaning of words by the context they appear in. A term-term matrix compares how often words appear in the context of other words (cake and butter vs cake and traffic). A term-document matrix counts a words occurrence in different documents. This allows the vector representations of documents to be word occurrence vectors and the representations of words to be document occurrence vectors.

---
How can documents be compared with a term-document matrix?  #flashcard #FNLP #LexicalSemanticsQuestions 
	Here the columns give how many times a word occurs in a given document. If word occurrence describe a document the $\cos$ between two document vectors can be seen as a measure of the similarity between two documents.

---
When comparing the similarity of vectors why is cos better that the dot between the two vectors?  #flashcard #FNLP #LexicalSemanticsQuestions 
	The problem is dot is increased by the size of the vector. So it will be higher for words which occur more or documents with more words in them. But we would prefer is the similarity found was independent of the overall frequency and so we normalize by the size of the two vectors. This gives us the cos between them.

---
What is TF in TF-IDF?  #flashcard #FNLP #LexicalSemanticsQuestions 
	TF is **term frequency**, the most simple version of this is $$\text{tf}_{t,d}=\text{count}(t,d)$$but generally we we consider 100 times as many occurrences to not count 100 time as much as 1 occurrence or 10 times as much at 10 occurrences. So a log scale is used with +1 to make sure we don't take log(0) $$\text{tf}_{t,d}=\log_{10}(\text{count}(t,d))$$

---
What is TF-IDF?  #flashcard #FNLP #LexicalSemanticsQuestions 
	TF-IDF is a way of constructing a term-document matrix. TF is **term frequency** and emphasizes the importance of how often terms occur together. Then IDF is **inverse document frequency** and discounts terms which occur often in all documents.

---
What is IDF in TF-IDF?  #flashcard #FNLP #LexicalSemanticsQuestions 
		This is **inverse document frequency** it is equal to $$\text{idf}_t=\log_{10}\left(\frac N{\text{df}_t}\right)$$where $\text{df}_t$ is the document frequency or number of documents $t$ occurs in and $N$ is the number of documents.

---
How is the term-document matrix constructed in TF-IDF?  #flashcard #FNLP #LexicalSemanticsQuestions 
	We find the **term frequency** for each word and document. Then each row for a term $t$ is multiplied by the inverse document frequency. For the matrix $W$ we get $$w_{t,d}=\text{tf}_{t,d}\times\text{idf}_t$$

---
What is the formula for PMI?  #flashcard #FNLP #LexicalSemanticsQuestions 
	The **pointwise mutual information** is a measure of how much more often then we expect terms occur together. It is $$I(x,y)=\log_2\frac{P(x,y)}{P(x)P(y)}$$

---
What is PPMI (with problems and solutions)?  #flashcard #FNLP #LexicalSemanticsQuestions 
	PPMI is **Positive Pointwise Mutual Information** equal to $$PPMI_{ij}=\max\left(\log_2\frac{p_{ij}}{p_{i*}p_{*j}},0\right)=\max\left(\log_2\frac{P(w,c)}{P(w)P(c)},0\right)$$Some problems with this are if two terms are low frequency and they co-occur their PPMI will be eradiated. To fix this context term can be raised to some power $\alpha=0.75$ usually. So $P(c)$ is replaced with $P_\alpha(C)=\frac{C(c)^\alpha}{\sum_{c'}C(c')}$. Where $C(c)$ is the number of times $c$ occurs for every word. This basically acts to smooth and bring up the low $P(C)$ values.

---
What are the uses of PPMI and TF-IDF? #flashcard #FNLP #LexicalSemanticsQuestions 
	Both create matrices to allow for a distributional representation of word (and documents in the case of TF-IDF). But PPMI can be used to create term-term matrices while TF-IDF can be used to create term-document matrices.

---
How is the document vector calculated given a TF-IDF matrix? #flashcard #FNLP #LexicalSemanticsQuestions 
	This is a vector that describe a document it is the centroid of all the word vectors in that document. It will be $$d=\frac{w_1+w_2+\dots+w_k}k$$This can them be used to calculate the similarity of two documents with the cosine between the two vectors.

---
What is the difference between term-term matrix word embeddings and those created by word2vec? #flashcard #FNLP #LexicalSemanticsQuestions 
	Word2Vec creates **dense** embeddings that are 50-1000 parameter's instead of the 10,000s of word in term-term or term-document matrices.

---
In Word2Vec (Skipgram model) what are we training? #flashcard #FNLP #LexicalSemanticsQuestions 
	In general we perform **gradient descent** on our parameters $\theta$ these will be half the word embeddings $w_i$ and half the context embeddings $c_i$.

---
What is the classifier in Word2Vec? #flashcard #FNLP #LexicalSemanticsQuestions 
	In word2Vec the classifier is a Mikolov Skipgram we define the probability that a word $c$ is a real context work by $$P(+\mid w,c)=\sigma(\mathbf c\cdot \mathbf w)$$where $\mathbf c$ is the context embedding for the word $c$ and $\mathbf w$ is the word embedding for the word $w$. The negative probability likewise is $$P(-\mid w, c)=\sigma(-\mathbf c\cdot \mathbf w)$$

---
what is the independence relation between the Word2Vec  probability of some entire context? #flashcard #FNLP #LexicalSemanticsQuestions 
	This will be the positive probability of each context word given the center word. That is $$P(+\mid w,c_{1:L})=\prod_{i=1}^L\sigma(\mathbf c_i\cdot\mathbf w)$$

---
How are positive and negative example sampled in word2Vec? #flashcard #FNLP #LexicalSemanticsQuestions 
	For a word in the text the positive samples make up a window around the word for example $\pm2$. Then we choose $k$ negative examples for each positive example. The negative example are *noise words* which are just randomly sampled words from the lexicon that don't appear in the context window. These are generally chosen with their unigram probability $p(c)$ but often $p_\alpha(c)$ is used with $\alpha=0.75$.

---
What is the loss trained for Word2Vec? #flashcard #FNLP #LexicalSemanticsQuestions 
	This is $$L_{CE}=-\log\left[P(+\mid w,c_{pos})\prod_{i=1}^kP(-\mid w,c_{neg_i})\right]$$for each example in the context window.

---
What are vector space models? #flashcard #FNLP #LexicalSemanticsQuestions 
	Vector space models represent the meaning of a word as some vector.

---
